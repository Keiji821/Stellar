from instaloader import Instaloader, Profile
from rich.console import Console
from rich.panel import Panel
import time
import random

console = Console()
L = Instaloader()

def get_profile_info(username):
    try:
        # Configuración para reducir detección
        L.context.sleep = True
        L.context.max_connection_attempts = 1
        L.context.request_timeout = 30
        
        # Retardo aleatorio
        time.sleep(random.uniform(3, 7))
        
        profile = Profile.from_username(L.context, username)
        
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
        console.print(f"[red]Error al obtener información:[/red]")
        console.print(f"Instagram ha bloqueado la solicitud. Intenta de nuevo más tarde.")
        console.print(f"Detalle técnico: {str(e)}")

def main():
    console.print("\n[bold green]Consulta de perfiles públicos de Instagram[/bold green]")
    
    while True:
        username = console.input("\n[bold green]Ingrese usuario (@nombre) o 'salir': [/bold green]")
        if username.lower() in ['exit', 'salir', 'q']:
            break
            
        get_profile_info(username.strip('@'))
        
        # Espera entre consultas
        time.sleep(random.uniform(5, 10))

if __name__ == "__main__":
    main()