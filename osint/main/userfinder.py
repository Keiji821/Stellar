import requests
from time import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from bs4 import BeautifulSoup
import random

console = Console()

PLATAFORMAS = {
    "Twitter": {"url": "https://twitter.com/{}", "indicador": "This account doesn’t exist"},
    "Instagram": {"url": "https://instagram.com/{}", "indicador": "La página no está disponible"},
    "Facebook": {"url": "https://www.facebook.com/public/{}", "indicador": "No pudimos encontrar ningún resultado"},
    "Pinterest": {"url": "https://pinterest.com/{}", "indicador": "Lo sentimos, esta página no está disponible"},
    "YouTube": {"url": "https://www.youtube.com/@{}", "indicador": "Este canal no está disponible"},
    "TikTok": {"url": "https://www.tiktok.com/@{}", "indicador": "Couldn't find this account"}
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
]

def obtener_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

def extraer_info(respuesta):
    try:
        sopa = BeautifulSoup(respuesta.text, "html.parser")
        titulo = sopa.title.string if sopa.title else "No disponible"
        meta_desc = sopa.find("meta", {"name": "description"})
        descripcion = meta_desc["content"] if meta_desc else "Sin descripción"
        return titulo.strip(), descripcion.strip()
    except Exception:
        return "No disponible", "Sin descripción"

def buscar_usuario(plataforma, username):
    url = PLATAFORMAS[plataforma]["url"].format(username)
    try:
        respuesta = requests.get(url, headers=obtener_headers(), timeout=5)
        if respuesta.status_code == 200 and PLATAFORMAS[plataforma]["indicador"] not in respuesta.text:
            nombre, bio = extraer_info(respuesta)
            return True, url, nombre, bio
    except requests.RequestException:
        pass
    return False, url, None, None

def verificar_usuario(username):
    tabla = Table(title="Resultados de Búsqueda", show_header=True, header_style="bold blue")
    tabla.add_column("Plataforma", justify="left")
    tabla.add_column("Estado", justify="center")
    tabla.add_column("URL", justify="left")
    tabla.add_column("Nombre", justify="left")
    tabla.add_column("Descripción", justify="left")

    with Progress() as progreso:
        tarea = progreso.add_task("Buscando en redes sociales...", total=len(PLATAFORMAS))
        resultados = []
        
        with ThreadPoolExecutor() as executor:
            futuros = {executor.submit(buscar_usuario, plataforma, username): plataforma for plataforma in PLATAFORMAS}
            
            for futuro in as_completed(futuros):
                plataforma = futuros[futuro]
                encontrado, url, nombre, bio = futuro.result()
                estado = "[green]Encontrado[/green]" if encontrado else "[red]No encontrado[/red]"
                nombre = nombre if nombre else "Desconocido"
                bio = bio if bio else "Sin información"
                tabla.add_row(plataforma, estado, url, nombre, bio)
                progreso.advance(tarea)

    console.print(tabla)

if __name__ == "__main__":
    usuario = console.input("[bold green]Introduce el nombre de usuario: [/bold green]")
    inicio = time()
    verificar_usuario(usuario)
    fin = time()
    console.print(f"[bold yellow]Tiempo total de ejecución:[/bold yellow] {fin - inicio:.2f} segundos")