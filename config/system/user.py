from rich.console import Console
import os
from os import system
from rich.table import Table
import requests

console = Console()

# Sistema

response = requests.get(f'https://api.ipapi.is/?ip={IpQuery}')
ip = response.json()

with open("user.txt", encoding="utf-8") as f:
    user = f.read().strip()

with open("password.txt", encoding="utf-8") as f:
    password = f.read().strip()

with open("login_method.txt", encoding="utf-8") as f:
    login_method = f.read().strip()

# Ruta

os.chdir(os.path.expanduser("~/Stellar/config/themes"))

# Temas

with open("banner_color.txt", encoding="utf-8") as f:
    banner_color = f.read().strip()

with open("banner_background.txt", encoding="utf-8") as f:
    banner_background = f.read().strip()

with open("banner_background_color.txt", encoding="utf-8") as f:
    banner_background_color = f.read().strip()

# Perfíl 
            
console.print("")
table = Table(title="Perfil", title_justify="center", title_style="bold green")
table.add_column(f"[bold green] Información", style="code", no_wrap=False)
table.add_column("[bold green] Descripción", style="code")

table.add_row("General", style="bold green")
table.add_row("")
table.add_row("Usuario", user)
table.add_row("")
table.add_row("Preferencias", style="bold green")
table.add_row("")
table.add_row("Color del banner", banner_color)
table.add_row("Fondo del banner", banner_background)
table.add_row("Color del fondo del banner", banner_background_color)
table.add_row("")
table.add_row("Seguridad", style="bold green")
table.add_row("")
table.add_row("Método de verificación", login_method)
table.add_row("Contraseña", password)
table.add_row("")
table.add_row("Privacidad", style="bold green")
table.add_row("")
table.add_row("Tor", "Activado • del sistema")
table.add_row("")
table.add_row("Tu IP en el internet", ip)

console.print(table, style="bright_white", justify="center")
console.print("")

