from instaloader import Instaloader, Profile, TwoFactorAuthRequiredException
from rich.console import Console
from rich.panel import Panel
import time
import random
import getpass

def login_instagram(loader):
    console = Console()
    while True:
        try:
            username = console.input("[bold cyan]Tu usuario de Instagram: [/bold cyan]")
            password = getpass.getpass("[bold cyan]Contraseña: [/bold cyan]")
            try:
                loader.login(username, password)
                console.print("[green]✓ Inicio de sesión exitoso[/green]")
                return True
            except TwoFactorAuthRequiredException:
                code = console.input("[bold yellow]Código 2FA: [/bold yellow]")
                loader.two_factor_login(code)
                console.print("[green]✓ Verificación 2FA exitosa[/green]")
                return True
            except Exception:
                return False
        except KeyboardInterrupt:
            return False

def get_profile_info(loader, username):
    console = Console()
    try:
        delay = random.uniform(2, 5)
        time.sleep(delay)
        profile = Profile.from_username(loader.context, username)
        info_panel = Panel.fit(
            f"[bold]👤 Usuario:[/bold] @{username}\n"
            f"[bold]📛 Nombre:[/bold] {profile.full_name}\n"
            f"[bold]🔒 Privado:[/bold] {'Sí' if profile.is_private else 'No'}\n"
            f"[bold]❤️ Seguidores:[/bold] {profile.followers:,}\n"
            f"[bold]👥 Seguidos:[/bold] {profile.followees:,}\n"
            f"[bold]📸 Publicaciones:[/bold] {profile.mediacount:,}\n"
            f"[bold]📝 Biografía:[/bold] {profile.biography}",
            title=f"[bold green]🔍 Información de @{username}[/bold green]",
            border_style="blue"
        )
        console.print(info_panel)
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")

def main():
    console = Console()
    L = Instaloader()
    
    if console.input("\n[bold]¿Iniciar sesión? (s/n): [/bold]").lower() == 's':
        if not login_instagram(L):
            console.print("[yellow]Continuando sin sesión[/yellow]")
    
    while True:
        try:
            target_user = console.input("\n[bold green]Usuario a consultar (o 'salir'): [/bold green]")
            if target_user.lower() in ['exit', 'salir', 'q']:
                break
            get_profile_info(L, target_user)
        except KeyboardInterrupt:
            continue
        except Exception:
            continue

if __name__ == "__main__":
    main()