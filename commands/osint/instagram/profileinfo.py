import requests
import random
import time
from bs4 import BeautifulSoup
import re
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from fake_useragent import UserAgent
import concurrent.futures
import sys

class InstagramScraperPremium:
    def __init__(self):
        self.session = requests.Session()
        self.ua = UserAgent()
        self.timeout = 35
        self.max_retries = 4
        self.delay_range = (12, 25)
        self.console = Console()
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.9',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        }
        self.estado = "Inicializado"
        self.registro = []
        
    def _log(self, mensaje, nivel="Info"):
        log_entry = f"[{time.strftime('%H:%M:%S')}] [{nivel}] {mensaje}"
        self.registro.append(log_entry)
        if nivel == "Error":
            self.console.print(log_entry, style="bold red")
        elif nivel == "Advertencia":
            self.console.print(log_entry, style="bold yellow")
        else:
            self.console.print(log_entry, style="bold cyan")

    def _random_delay(self):
        delay = random.uniform(*self.delay_range)
        self._log(f"Esperando {delay:.2f} segundos...")
        time.sleep(delay)

    def _get_html(self, username):
        for intento in range(1, self.max_retries + 1):
            try:
                self.estado = f"Intento {intento}/{self.max_retries}"
                self._log(f"Obteniendo perfil de @{username}")
                
                self._random_delay()
                
                user_agent = self.ua.random
                self.headers['User-Agent'] = user_agent
                self._log(f"User-agent: {user_agent}")
                
                response = self.session.get(
                    f"https://www.instagram.com/{username}/",
                    headers=self.headers,
                    timeout=self.timeout
                )
                
                if response.status_code == 200:
                    self._log("Perfil obtenido con éxito", "Éxito")
                    return response.text
                elif response.status_code == 404:
                    self._log("Perfil no encontrado (404)", "Error")
                    return None
                else:
                    self._log(f"Respuesta HTTP: {response.status_code}", "Advertencia")
                    
            except requests.exceptions.Timeout:
                self._log("Tiempo de espera agotado", "Error")
            except requests.exceptions.TooManyRedirects:
                self._log("Demasiadas redirecciones", "Error")
            except requests.exceptions.RequestException as e:
                self._log(f"Error de conexión: {str(e)}", "Error")
                
        self._log(f"Fallo al obtener perfil después de {self.max_retries} intentos", "Error")
        return None

    def _parse_profile(self, html, username):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            
            meta_description = soup.find('meta', property='og:description')
            title = soup.find('title')
            meta_image = soup.find('meta', property='og:image')
            
            if not meta_description or not title:
                self._log("Datos críticos faltantes en el perfil", "Advertencia")
                return None
                
            stats_pattern = r'([\d,]+) seguidores, ([\d,]+) seguidos, ([\d,]+) publicaciones'
            stats_match = re.search(stats_pattern, meta_description['content'])
            
            full_name = title.text.split('(')[0].replace('• Instagram', '').strip()
            if len(full_name) > 80:
                full_name = full_name[:77] + '...'
                
            biography = meta_description['content'].split('-')[0].strip()
            if len(biography) > 150:
                biography = biography[:147] + '...'
            
            return {
                'username': username,
                'full_name': full_name,
                'biography': biography,
                'followers': int(stats_match.group(1).replace(',', '')) if stats_match else 0,
                'following': int(stats_match.group(2).replace(',', '')) if stats_match else 0,
                'posts': int(stats_match.group(3).replace(',', '')) if stats_match else 0,
                'profile_pic': meta_image['content'] if meta_image else 'N/A',
                'is_private': 'Privado' in title.text,
                'url': f"https://www.instagram.com/{username}/",
                'status': 'success'
            }
            
        except Exception as e:
            self._log(f"Error al analizar perfil: {str(e)}", "Error")
            return None

    def get_profile(self, username):
        if not username:
            self._log("Nombre de usuario vacío", "Error")
            return {'status': 'error', 'message': 'Nombre de usuario vacío'}
            
        html = self._get_html(username)
        if not html:
            return {'status': 'error', 'message': 'Error al obtener perfil'}
        
        perfil = self._parse_profile(html, username)
        if not perfil:
            return {'status': 'error', 'message': 'Error al analizar datos'}
            
        return perfil

    def batch_scrape(self, usernames):
        resultados = []
        with Progress(console=self.console) as progress:
            tarea = progress.add_task("[bold green]Escaneando perfiles...[/bold green]", total=len(usernames))
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                futuros = {executor.submit(self.get_profile, user): user for user in usernames}
                
                for futuro in concurrent.futures.as_completed(futuros):
                    usuario = futuros[futuro]
                    try:
                        resultado = futuro.result()
                        resultados.append(resultado)
                    except Exception as e:
                        self._log(f"Error para @{usuario}: {str(e)}", "Error")
                    progress.update(tarea, advance=1)
                    
        return resultados

def mostrar_resultados(perfil, consola):
    if perfil.get('status') != 'success':
        consola.print(f"[bold red]Error: {perfil.get('message', 'Error desconocido')}[/bold red]")
        return

    tabla = Table(
        title=f"[bold green]Información de @{perfil['username']}[/bold green]", 
        box=None,
        show_header=False,
        style="bold green"
    )
    tabla.add_column("Campo", style="bold cyan", width=20)
    tabla.add_column("Valor", style="bold white")

    campos = [
        ("Usuario", f"@{perfil['username']}"),
        ("Nombre completo", perfil['full_name']),
        ("Biografía", perfil['biography']),
        ("Seguidores", f"{perfil['followers']:,}"),
        ("Siguiendo", f"{perfil['following']:,}"),
        ("Publicaciones", f"{perfil['posts']:,}"),
        ("Privado", "Sí" if perfil['is_private'] else "No"),
        ("Enlace", perfil['url']),
        ("Foto de perfil", perfil['profile_pic'][:60] + "..." if len(perfil['profile_pic']) > 60 else perfil['profile_pic'])
    ]

    for campo, valor in campos:
        tabla.add_row(campo, valor)

    consola.print(tabla)

if __name__ == "__main__":
    consola = Console()
    
    try:
        scraper = InstagramScraperPremium()
        usuario = consola.input("[bold green]Ingrese nombre de usuario de Instagram: [/bold green]").strip()
        
        perfil = scraper.get_profile(usuario)
        mostrar_resultados(perfil, consola)
        
        consola.print("\n[bold yellow]Registro de ejecución:[/bold yellow]")
        for entrada in scraper.registro:
            if "Error" in entrada:
                consola.print(entrada, style="bold red")
            elif "Advertencia" in entrada:
                consola.print(entrada, style="bold yellow")
            else:
                consola.print(entrada, style="bold cyan")
                
        consola.print()
                
    except KeyboardInterrupt:
        consola.print("\n[bold red]Operación cancelada por el usuario[/bold red]")
        consola.print()
    except Exception as e:
        consola.print(f"[bold red]Error crítico: {str(e)}[/bold red]")
        consola.print()