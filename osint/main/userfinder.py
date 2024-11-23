import requests
from time import time
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

PLATFORMS = {
    "Twitter": {"url": "https://twitter.com/{}", "api": False},
    "Instagram": {"url": "https://instagram.com/{}", "api": False},
    "Facebook": {"url": "https://www.facebook.com/public/{}", "api": True},
    "Pinterest": {"url": "https://pinterest.com/{}", "api": False},
    "YouTube": {"url": "https://www.youtube.com/@{}", "api": False},
    "TikTok": {"url": "https://www.tiktok.com/@{}", "api": False}
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def facebook_api_search(username):
    try:
        url = f"https://www.facebook.com/public/{username}"
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200 and "Sorry, we couldn't find any results" not in response.text:
            return True, url
        else:
            return False, None
    except requests.RequestException:
        return False, None

def check_username(username):
    table = Table(title="Resultados de Búsqueda", show_header=True, header_style="bold blue")
    table.add_column("Plataforma", justify="left")
    table.add_column("Estado", justify="center")
    table.add_column("URL", justify="left")

    for platform in track(PLATFORMS, description="Buscando..."):
        if platform == "Facebook" and PLATFORMS[platform]["api"]:
            found, url = facebook_api_search(username)
        else:
            url = PLATFORMS[platform]["url"].format(username)
            try:
                response = requests.get(url, headers=HEADERS, timeout=5)
                found = response.status_code == 200
            except requests.RequestException:
                found = False
        
        if found:
            table.add_row(platform, f"[green]Encontrado[/green]", url)
        else:
            table.add_row(platform, f"[red]No encontrado[/red]", url)

    console.print(table)

if __name__ == "__main__":
    console.print("[bold cyan]Herramienta OSINT: Búsqueda de Nombre de Usuario[/bold cyan]")
    username = console.input("[bold green]Introduce el nombre de usuario: [/bold green]")
    start_time = time()
    check_username(username)
    end_time = time()
    elapsed_time = end_time - start_time
    console.print(f"[bold yellow]Tiempo total de ejecución:[/bold yellow] {elapsed_time:.2f} segundos")
