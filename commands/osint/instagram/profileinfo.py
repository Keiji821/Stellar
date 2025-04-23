from instaloader import Instaloader, Profile
from rich.console import Console
from rich.panel import Panel

L = Instaloader()
console = Console()

usuario = console.input("[bold green]Ingrese usuario de Instagram: ")
console.print()

try:
    profile = Profile.from_username(L.context, usuario)
    
    info_panel = Panel.fit(
        f"[bold]Usuario:[/bold] {usuario}\n"
        f"[bold]Nombre:[/bold] {profile.full_name}\n"
        f"[bold]Seguidores:[/bold] {profile.followers:,}\n"
        f"[bold]Seguidos:[/bold] {profile.followees:,}\n"
        f"[bold]Publicaciones:[/bold] {profile.mediacount:,}\n"
        f"[bold]Biografía:[/bold] {profile.biography}",
        title="[bold green]Información del Perfil[/bold green]",
        border_style="blue"
    )
    
    console.print(info_panel)
    
except Exception as e:
    console.print(f"[bold red]Error:[/bold red] {str(e)}")