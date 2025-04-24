import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def osint_instagram(username):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "x-ig-app-id": "936619743392459"
    }

    try:
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            console.print(f"[bold red]Error {res.status_code}[/bold red]: No se pudo acceder al perfil.")
            return

        data = res.json()
        user = data.get("data", {}).get("user", {})

        if not user:
            console.print("[bold red]No se pudo extraer la información del perfil.[/bold red]")
            return

        console.print(Panel.fit(f"[bold cyan]Perfil OSINT de Instagram: @{username}[/bold cyan]", border_style="bright_blue"))
        console.print(f"[bold]Nombre completo:[/bold] {user.get('full_name', 'N/A')}")
        console.print(f"[bold]Biografía:[/bold] {user.get('biography', 'N/A')}")
        console.print(f"[bold]Seguidores:[/bold] {user.get('edge_followed_by', {}).get('count', 'N/A')}")
        console.print(f"[bold]Siguiendo:[/bold] {user.get('edge_follow', {}).get('count', 'N/A')}")
        console.print(f"[bold]Publicaciones:[/bold] {user.get('edge_owner_to_timeline_media', {}).get('count', 'N/A')}")
        console.print(f"[bold]Privado:[/bold] {'Sí' if user.get('is_private') else 'No'}")
        console.print(f"[bold]Verificado:[/bold] {'Sí' if user.get('is_verified') else 'No'}")
        console.print(f"[bold]Foto de perfil:[/bold] {user.get('profile_pic_url_hd', 'N/A')}")

    except Exception as e:
        console.print(f"[bold red]Error al procesar los datos:[/bold red] {e}")

if __name__ == "__main__":
    username = Prompt.ask("[bold green]Ingresa el nombre de usuario[/bold green]")
    osint_instagram(username)