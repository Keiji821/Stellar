import requests
import re
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def osint_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "es-ES,es;q=0.9"
    }

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        console.print(f"[bold red]Error {res.status_code}[/bold red]: No se pudo acceder al perfil.")
        return

    match = re.search(r'{"biography":.*?,"blocked_by_viewer"', res.text)
    if not match:
        console.print("[bold red]No se pudo extraer la información del perfil.[/bold red]")
        return

    json_raw = match.group(0)
    json_raw = json_raw.replace('false', 'False').replace('true', 'True').replace('null', 'None')

    try:
        data = eval(json_raw)
        console.print(Panel.fit(f"[bold cyan]Perfil OSINT de Instagram: @{username}[/bold cyan]", border_style="bright_blue"))
        console.print(f"[bold]Nombre:[/bold] {data.get('full_name')}")
        console.print(f"[bold]Biografía:[/bold] {data.get('biography')}")
        console.print(f"[bold]Seguidores:[/bold] {data['edge_followed_by']['count']}")
        console.print(f"[bold]Siguiendo:[/bold] {data['edge_follow']['count']}")
        console.print(f"[bold]Publicaciones:[/bold] {data['edge_owner_to_timeline_media']['count']}")
        console.print(f"[bold]Privado:[/bold] {'Sí' if data['is_private'] else 'No'}")
        console.print(f"[bold]Verificado:[/bold] {'Sí' if data['is_verified'] else 'No'}")
        console.print(f"[bold]Foto de perfil:[/bold] {data['profile_pic_url_hd']}")
    except Exception as e:
        console.print(f"[bold red]Error procesando datos:[/bold red] {e}")

if __name__ == "__main__":
    username = Prompt.ask("[bold green]Ingresa el nombre de usuario[/bold green]")
    osint_instagram(username)