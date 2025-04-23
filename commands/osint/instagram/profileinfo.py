from instaloader import Instaloader, Profile
from rich.console import Console
from rich.panel import Panel
import time
import random
import requests

console = Console()
L = Instaloader()

L.context.sleep = True
L.context.max_connection_attempts = 2
L.context.request_timeout = 45
L.context.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except:
        return False

def get_profile_info(username):
    try:
        if not check_internet():
            console.print("Error: No hay conexión a internet")
            return

        delay = random.uniform(5, 15)
        time.sleep(delay)

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
        console.print(f"Error: {str(e)}")

def main():
    console.print("CONSULTOR DE PERFILES DE INSTAGRAM")

    while True:
        try:
            username = input("\nIngrese usuario (sin @) o 'salir': ").strip()
            
            if username.lower() in ['exit', 'salir', 'q']:
                console.print("Saliendo del programa...")
                break
                
            if not username:
                console.print("Error: Debes ingresar un nombre de usuario")
                continue

            get_profile_info(username)

            if random.random() < 0.3:
                wait_time = random.uniform(20, 40)
                time.sleep(wait_time)
            else:
                time.sleep(random.uniform(8, 15))

        except KeyboardInterrupt:
            console.print("\nOperación cancelada")
            continue

if __name__ == "__main__":
    main()