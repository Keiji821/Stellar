import requests
import random
import time
from bs4 import BeautifulSoup
import re
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from fake_useragent import UserAgent
import concurrent.futures
import json
from datetime import datetime

class InstagramScraper:
    def __init__(self):
        self.session = requests.Session()
        self.ua = UserAgent()
        self.timeout = 30
        self.max_retries = 3
        self.delay_range = (5, 12)
        self.console = Console()
        
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'x-ig-app-id': '936619743392459'
        }

        self.status = "Inicializado"
        self.logs = []
        self.stats = {
            'success': 0,
            'failed': 0,
            'total_requests': 0
        }

    def log_message(self, message, level="INFO"):
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.logs.append(log_entry)

        if level == "ERROR":
            self.console.print(log_entry, style="bold red")
        elif level == "WARNING":
            self.console.print(log_entry, style="bold yellow")
        elif level == "SUCCESS":
            self.console.print(log_entry, style="bold green")
        else:
            self.console.print(log_entry, style="bold cyan")

    def random_delay(self):
        delay_time = random.uniform(*self.delay_range)
        time.sleep(delay_time)

    def fetch_via_api(self, username):
        try:
            api_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
                'X-IG-App-ID': '936619743392459',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Origin': 'https://www.instagram.com',
                'Referer': f'https://www.instagram.com/{username}/',
                'Connection': 'keep-alive',
            }
            
            response = self.session.get(api_url, headers=headers, timeout=self.timeout)
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and 'user' in data['data']:
                    user_data = data['data']['user']
                    return {
                        'username': user_data['username'],
                        'full_name': user_data.get('full_name', ''),
                        'biography': user_data.get('biography', ''),
                        'followers': user_data['edge_followed_by']['count'],
                        'following': user_data['edge_follow']['count'],
                        'posts': user_data['edge_owner_to_timeline_media']['count'],
                        'profile_pic': user_data.get('profile_pic_url_hd', 'No disponible'),
                        'is_private': user_data['is_private'],
                        'is_verified': user_data.get('is_verified', False),
                        'url': f"https://www.instagram.com/{username}/",
                        'status': 'success',
                        'source': 'api'
                    }
            return None
        except Exception as e:
            self.log_message(f"Error en API: {str(e)}", "WARNING")
            return None

    def fetch_html(self, username):
        self.stats['total_requests'] += 1

        for attempt in range(1, self.max_retries + 1):
            try:
                self.status = f"Intento {attempt}/{self.max_retries}"
                self.log_message(f"Obteniendo perfil de @{username}")

                self.random_delay()

                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                headers = self.headers.copy()
                headers.update({
                    'User-Agent': user_agent,
                    'Referer': 'https://www.instagram.com/'
                })

                response = self.session.get(
                    f"https://www.instagram.com/{username}/",
                    headers=headers,
                    timeout=self.timeout,
                    allow_redirects=True
                )

                if response.status_code == 200:
                    self.log_message("Perfil obtenido correctamente", "SUCCESS")
                    return response.text
                elif response.status_code == 404:
                    self.log_message("Perfil no encontrado (404)", "ERROR")
                    return None
                elif response.status_code == 429:
                    self.log_message("Límite de tasa excedido, aumentando pausa", "WARNING")
                    self.delay_range = (self.delay_range[0] + 3, self.delay_range[1] + 8)
                    time.sleep(10)
                    continue
                elif response.status_code == 403:
                    self.log_message("Acceso prohibido (posible bloqueo)", "ERROR")
                    return None
                else:
                    self.log_message(f"Respuesta HTTP: {response.status_code}", "WARNING")
                    continue

            except requests.exceptions.Timeout:
                self.log_message("Tiempo de espera agotado", "ERROR")
            except requests.exceptions.TooManyRedirects:
                self.log_message("Demasiadas redirecciones", "ERROR")
            except requests.exceptions.RequestException as e:
                self.log_message(f"Error de conexión: {str(e)}", "ERROR")

        self.log_message(f"Fallo al obtener perfil después de {self.max_retries} intentos", "ERROR")
        self.stats['failed'] += 1
        return None

    def extract_shared_data(self, html):
        try:
            pattern = r'window\._sharedData\s*=\s*({.*?});'
            match = re.search(pattern, html, re.DOTALL)
            if match:
                json_str = match.group(1)
                return json.loads(json_str)
        except Exception as e:
            self.log_message(f"Error extrayendo sharedData: {str(e)}", "WARNING")
        return None

    def extract_profile_data(self, html, username):
        try:
            api_data = self.fetch_via_api(username)
            if api_data:
                return api_data

            soup = BeautifulSoup(html, 'html.parser')
            
            shared_data = self.extract_shared_data(html)
            if shared_data and 'entry_data' in shared_data:
                try:
                    user_data = shared_data['entry_data']['ProfilePage'][0]['graphql']['user']
                    return {
                        'username': user_data['username'],
                        'full_name': user_data.get('full_name', ''),
                        'biography': user_data.get('biography', ''),
                        'followers': user_data['edge_followed_by']['count'],
                        'following': user_data['edge_follow']['count'],
                        'posts': user_data['edge_owner_to_timeline_media']['count'],
                        'profile_pic': user_data.get('profile_pic_url_hd', 'No disponible'),
                        'is_private': user_data['is_private'],
                        'is_verified': user_data.get('is_verified', False),
                        'url': f"https://www.instagram.com/{username}/",
                        'status': 'success',
                        'source': 'shared_data'
                    }
                except (KeyError, IndexError) as e:
                    self.log_message(f"Error parsing sharedData: {str(e)}", "WARNING")
            
            meta_description = soup.find('meta', property='og:description')
            title = soup.find('title')
            meta_image = soup.find('meta', property='og:image')

            if not meta_description or not title:
                self.log_message("Datos críticos faltantes en el perfil", "WARNING")
                return None

            stats_patterns = [
                r'([\d,]+)\s*seguidores',
                r'([\d,]+)\s*seguidos',
                r'([\d,]+)\s*publicaciones'
            ]
            
            description_text = meta_description.get('content', '')
            followers = following = posts = 0
            
            followers_match = re.search(stats_patterns[0], description_text)
            if followers_match:
                followers = int(followers_match.group(1).replace(',', ''))
            
            following_match = re.search(stats_patterns[1], description_text)
            if following_match:
                following = int(following_match.group(1).replace(',', ''))
            
            posts_match = re.search(stats_patterns[2], description_text)
            if posts_match:
                posts = int(posts_match.group(1).replace(',', ''))
            
            full_name = ""
            name_element = soup.find('h1', string=re.compile(r'[^\s]'))
            if name_element:
                full_name = name_element.get_text().strip()
            else:
                title_text = title.get_text() if title else ""
                full_name = title_text.split('(')[0].replace('• Instagram', '').strip()
            
            if len(full_name) > 80:
                full_name = full_name[:77] + '...'

            bio_element = soup.find('meta', property='og:description')
            biography = bio_element.get('content', '').split('-')[0].strip() if bio_element else ''
            if len(biography) > 150:
                biography = biography[:147] + '...'

            is_private = 'Privado' in (title.get_text() if title else "") or 'Esta cuenta es privada' in html

            return {
                'username': username,
                'full_name': full_name,
                'biography': biography,
                'followers': followers,
                'following': following,
                'posts': posts,
                'profile_pic': meta_image.get('content', 'No disponible') if meta_image else 'No disponible',
                'is_private': is_private,
                'is_verified': False,
                'url': f"https://www.instagram.com/{username}/",
                'status': 'success',
                'source': 'html'
            }

        except Exception as e:
            self.log_message(f"Error al analizar perfil: {str(e)}", "ERROR")
            return None

    def get_profile(self, username):
        if not username:
            self.log_message("Nombre de usuario vacío", "ERROR")
            return {'status': 'error', 'message': 'Nombre de usuario vacío'}

        api_profile = self.fetch_via_api(username)
        if api_profile:
            self.stats['success'] += 1
            return api_profile

        html = self.fetch_html(username)
        if not html:
            return {'status': 'error', 'message': 'Error al obtener perfil'}

        profile = self.extract_profile_data(html, username)
        if not profile:
            return {'status': 'error', 'message': 'Error al analizar datos'}

        self.stats['success'] += 1
        return profile

    def scan_multiple(self, usernames):
        results = []

        with Progress(
            SpinnerColumn(spinner_name="dots"),
            TextColumn("[progress.description]{task.description}"),
            TimeElapsedColumn(),
            console=self.console
        ) as progress:

            task = progress.add_task("[cyan]Escaneando perfiles...", total=len(usernames))

            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                futures = {executor.submit(self.get_profile, username): username for username in usernames}

                for future in concurrent.futures.as_completed(futures):
                    username = futures[future]
                    try:
                        result = future.result()
                        results.append(result)
                    except Exception as e:
                        self.log_message(f"Error para @{username}: {str(e)}", "ERROR")
                    progress.update(task, advance=1)

        return results

def show_results(profile, console):
    if profile.get('status') != 'success':
        console.print(f"[bold red]Error: {profile.get('message', 'Error desconocido')}[/bold red]")
        return

    table = Table(
        title=f"[bold green]Información de Instagram: @{profile['username']}[/bold green]",
        show_header=True,
        header_style="bold magenta",
        box=None
    )
    
    table.add_column("Campo", style="cyan", width=20)
    table.add_column("Valor", style="white")

    fields = [
        ("Usuario", f"@{profile['username']}"),
        ("Nombre completo", profile['full_name']),
        ("Biografía", profile['biography']),
        ("Seguidores", f"{profile['followers']:,}"),
        ("Siguiendo", f"{profile['following']:,}"),
        ("Publicaciones", f"{profile['posts']:,}"),
        ("Privado", "Sí" if profile['is_private'] else "No"),
        ("Verificado", "Sí" if profile.get('is_verified', False) else "No"),
        ("Fuente", profile.get('source', 'desconocida')),
        ("Enlace", profile['url']),
        ("Foto de perfil", profile['profile_pic'][:60] + "..." if len(profile['profile_pic']) > 60 else profile['profile_pic'])
    ]

    for field, value in fields:
        table.add_row(field, value)

    console.print(table)

if __name__ == "__main__":
    console = Console()

    try:
        scraper = InstagramScraper()
        username = console.input("[bold green]Ingrese nombre de usuario de Instagram: [/bold green]").strip()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Buscando perfil...", total=None)
            profile = scraper.get_profile(username)
            progress.update(task, completed=1)

        console.print()
        show_results(profile, console)
        console.print()

        console.print("[bold yellow]Registro de ejecución:[/bold yellow]")
        for entry in scraper.logs:
            if "ERROR" in entry:
                console.print(entry, style="bold red")
            elif "WARNING" in entry:
                console.print(entry, style="bold yellow")
            elif "SUCCESS" in entry:
                console.print(entry, style="bold green")
            else:
                console.print(entry, style="bold cyan")

        console.print()
        console.print("[bold green]Estadísticas:[/bold green]")
        console.print(f"Perfiles exitosos: {scraper.stats['success']}")
        console.print(f"Perfiles fallidos: {scraper.stats['failed']}")
        console.print(f"Solicitudes totales: {scraper.stats['total_requests']}")

    except KeyboardInterrupt:
        console.print("\n[bold red]Operación cancelada por el usuario[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error crítico: {str(e)}[/bold red]")