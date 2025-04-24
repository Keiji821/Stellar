import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import json

console = Console()

def osint_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari/537.36"
        )
    }

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        console.print(f"[bold red]Error {res.status_code}[/bold red]: No se pudo acceder al perfil.")
        return

    soup = BeautifulSoup(res.text, "html.parser")
    json_data = None

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            if data.get("@type") == "Person":
                json_data = data
                break
        except:
            continue

    if not json_data:
        console.print("[bold red]No se pudo extraer la información del perfil.[/bold red]")
        return

    name = json_data.get("name", "")
    description = json_data.get("description", "")
    profile_url = json_data.get("image", "")

    console.print(Panel.fit(f"[bold cyan]Perfil OSINT de Instagram: @{username}[/bold cyan]", border_style="bright_blue"))

    if name:
        console.print(f"[bold]Nombre:[/bold] {name}")
    console.print(f"[bold]Biografía:[/bold] {description}")
    if profile_url:
        console.print(f"[bold]Foto de perfil:[/bold] {profile_url}")

    try:
        shared_data = None
        for script in soup.find_all("script", type="text/javascript"):
            if script.string and 'window._sharedData' in script.string:
                shared_data = script.string.split(" = ", 1)[1].rstrip(";")
                break

        if shared_data:
            data = json.loads(shared_data)
            user = data['entry_data']['ProfilePage'][0]['graphql']['user']
            console.print(f"[bold]Seguidores:[/bold] {user['edge_followed_by']['count']}")
            console.print(f"[bold]Siguiendo:[/bold] {user['edge_follow']['count']}")
            console.print(f"[bold]Publicaciones:[/bold] {user['edge_owner_to_timeline_media']['count']}")
            console.print(f"[bold]Privado:[/bold] {'Sí' if user['is_private'] else 'No'}")
            console.print(f"[bold]Verificado:[/bold] {'Sí' if user['is_verified'] else 'No'}")
    except Exception as e:
        console.print(f"[bold red]Error extra:[/bold red] {e}")

if __name__ == "__main__":
    username = Prompt.ask("[bold green]Ingresa el nombre de usuario[/bold green]")
    osint_instagram(username)
