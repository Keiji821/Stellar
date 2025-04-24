import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def osint_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
        ),
        "Accept-Language": "es-ES,es;q=0.9"
    }

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        console.print(f"[bold red]Error {res.status_code}[/bold red]: No se pudo acceder al perfil.")
        return

    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.find("meta", property="og:title")
    description = soup.find("meta", property="og:description")
    image = soup.find("meta", property="og:image")

    if not title or not description or not image:
        console.print("[bold red]No se pudo extraer la información del perfil.[/bold red]")
        return

    title_parts = title["content"].split("(@")
    name = title_parts[0].strip() if len(title_parts) > 1 else ""
    username = title_parts[1].rstrip(")") if len(title_parts) > 1 else username

    bio_stats = description["content"].split(" • ")
    posts = bio_stats[0].split(" ")[0]
    followers = bio_stats[1].split(" ")[0]
    following = bio_stats[2].split(" ")[0]

    console.print(Panel.fit(f"[bold cyan]Perfil OSINT de Instagram: @{username}[/bold cyan]", border_style="bright_blue"))
    if name:
        console.print(f"[bold]Nombre:[/bold] {name}")
    console.print(f"[bold]Seguidores:[/bold] {followers}")
    console.print(f"[bold]Siguiendo:[/bold] {following}")
    console.print(f"[bold]Publicaciones:[/bold] {posts}")
    console.print(f"[bold]Foto de perfil:[/bold] {image['content']}")

if __name__ == "__main__":
    username = Prompt.ask("[bold green]Ingresa el nombre de usuario[/bold green]")
    osint_instagram(username)