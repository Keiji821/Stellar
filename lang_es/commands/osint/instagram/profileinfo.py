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
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
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
            self.stats['total_requests'] += 1
            self.log_message(f"Intentando API para @{username}")
            
            api_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
            
            headers = {
                'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 146536611)',
                'X-IG-App-ID': '936619743392459',
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Origin': 'https://www.instagram.com',
                'Referer': f'https://www.instagram.com/{username}/',
                'Connection': 'keep-alive',
            }
            
            self.random_delay()
            response = self.session.get(api_url, headers=headers, timeout=self.timeout)
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and 'user' in data['data']:
                    user_data = data['data']['user']
                    self.log_message("Datos obtenidos via API correctamente", "SUCCESS")
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
                        'status': 'success'
                    }
            elif response.status_code == 404:
                self.log_message("Usuario no encontrado via API", "ERROR")
            else:
                self.log_message(f"Error API: {response.status_code}", "WARNING")
                
            return None
            
        except Exception as e:
            self.log_message(f"Error en API: {str(e)}", "WARNING")
            return None

    def get_profile(self, username):
        if not username:
            self.log_message("Nombre de usuario vacío", "ERROR")
            return {'status': 'error', 'message': 'Nombre de usuario vacío'}

        profile = self.fetch_via_api(username)
        if profile:
            self.stats['success'] += 1
            return profile

        self.stats['failed'] += 1
        return {'status': 'error', 'message': 'Error al obtener datos del perfil'}

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