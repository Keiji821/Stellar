from instaloader import Instaloader, Profile, TwoFactorAuthRequiredException
from rich.console import Console
from rich.panel import Panel
import time
import random

def login_instagram(loader):
    console = Console()
    while True:
        try:
            username = console.input("[bold green]Tu usuario de Instagram: [/bold green]")
            password = console.input("[bold green]Contraseña: [/bold green]")
            try:
                loader.login(username, password)
                console.print("[green]Inicio de sesión exitoso[/green]")
                return True
            except TwoFactorAuthRequiredException:
                code = console.input("[bold green]Código 2FA: [/bold green]")
                loader.two_factor_login(code)
                console.print("[green]Verificación 2FA exitosa[/green]")
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
            f"Usuario: @{username}\n"
            f"Nombre: {profile.full_name}\n"
            f"Privado: {'Sí' if profile.is_private else 'No'}\n"
            f"Seguidores: {profile.followers:,}\n"
            f"Seguidos: {profile.followees:,}\n"
            f"Publicaciones: {profile.mediacount:,}\n"
            f"Biografía: {profile.biography}",
            title=f"Información de @{username}",
            border_style="blue"
        )
        console.print(info_panel)
    except Exception as e:
        console.print(f"Error: {str(e)}")

def main():
    console = Console()
    L = Instaloader()
    
    if console.input("\n[bold green]¿Iniciar sesión? (s/n): [/bold green]").lower() == 's':
        if not login_instagram(L):
            console.print("Continuando sin sesión")
    
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