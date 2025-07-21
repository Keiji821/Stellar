from rich.console import Console
import os
from os import system
from rich.table import Table
from rich.panel import Panel
import requests

console = Console()

# Sistema

response = requests.get(f'https://api.ipapi.is/?ip=')
data = response.json()

ip = str(data.get("ip"))

is_tor = str(data.get("is_tor"))
if is_tor == "True":
    is_tor = "Activado"
if is_tor == "False":
    is_tor = "Desactivado"  

is_proxy = str(data.get("is_proxy"))
if is_proxy == "True":
    is_proxy = "Activado"
if is_proxy == "False":
    is_proxy = "Desactivado"

is_vpn = str(data.get("is_vpn"))
if is_vpn == "True":
    is_vpn = "Activado"
if is_vpn == "False":
    is_vpn = "Desactivado"

network = str(data.get("company", {}).get("network"))

route = str(data.get("asn", {}).get("route"))

with open("user.txt", encoding="utf-8") as f:
    user = f.read().strip()

with open("password.txt", encoding="utf-8") as f:
    password = f.read().strip()

with open("login_method.txt", encoding="utf-8") as f:
    login_method = f.read().strip()

# Ruta

os.chdir(os.path.expanduser("~/Stellar/config/themes"))

# Temas

with open("banner.txt", encoding="utf-8") as f:
    banner = f.read().strip()

with open("banner_color.txt", encoding="utf-8") as f:
    banner_color = f.read().strip()

if banner_color=="":
    banner_color = "no"

banner_color_tr = {
    'no': 'No configurado',
    'black': 'Negro',
    'red': 'Rojo',
    'green': 'Verde',
    'yellow': 'Amarillo',
    'blue': 'Azul',
    'magenta': 'Magenta',
    'cyan': 'Cian',
    'white': 'Blanco',
    'bold black': 'Negro intenso',
    'bold red': 'Rojo intenso',
    'bold green': 'Verde intenso',
    'bold yellow': 'Amarillo intenso',
    'bold blue': 'Azul intenso',
    'bold magenta': 'Magenta intenso',
    'bold cyan': 'Cian intenso',
    'bold white': 'Blanco intenso',
    'bright_black': 'Negro brillante',
    'bright_red': 'Rojo brillante',
    'bright_green': 'Verde brillante',
    'bright_yellow': 'Amarillo brillante',
    'bright_blue': 'Azul brillante',
    'bright_magenta': 'Magenta brillante',
    'bright_cyan': 'Cian brillante',
    'bright_white': 'Blanco brillante',
    'dark_red': 'Rojo oscuro',
    'dark_green': 'Verde oscuro',
    'dark_yellow': 'Amarillo oscuro',
    'dark_blue': 'Azul oscuro',
    'dark_magenta': 'Magenta oscuro',
    'dark_cyan': 'Cian oscuro',
    'grey0': 'Gris 0',
    'grey19': 'Gris 19',
    'grey30': 'Gris 30',
    'grey37': 'Gris 37',
    'grey46': 'Gris 46',
    'grey50': 'Gris 50',
    'grey54': 'Gris 54',
    'grey58': 'Gris 58',
    'grey62': 'Gris 62',
    'grey66': 'Gris 66',
    'grey70': 'Gris 70',
    'grey74': 'Gris 74',
    'grey78': 'Gris 78',
    'grey82': 'Gris 82',
    'grey85': 'Gris 85',
    'grey89': 'Gris 89',
    'grey93': 'Gris 93',
    'grey100': 'Gris 100',
    'orange1': 'Naranja 1',
    'orange3': 'Naranja 3',
    'orange4': 'Naranja 4'
}
color_banner = banner_color_tr.get(banner_color)

with open("banner_background.txt", encoding="utf-8") as f:
    banner_background = f.read().strip()
if banner_background=="no":
    banner_background = "No configurado"

with open("banner_background_color.txt", encoding="utf-8") as f:
    banner_background_color = f.read().strip()

if banner_background_color=="":
    banner_background_color = "no"

banner_background_color_tr = {
    'no': 'No configurado',
    'black': 'Negro',
    'red': 'Rojo',
    'green': 'Verde',
    'yellow': 'Amarillo',
    'blue': 'Azul',
    'magenta': 'Magenta',
    'cyan': 'Cian',
    'white': 'Blanco',
    'bold black': 'Negro intenso',
    'bold red': 'Rojo intenso',
    'bold green': 'Verde intenso',
    'bold yellow': 'Amarillo intenso',
    'bold blue': 'Azul intenso',
    'bold magenta': 'Magenta intenso',
    'bold cyan': 'Cian intenso',
    'bold white': 'Blanco intenso',
    'bright_black': 'Negro brillante',
    'bright_red': 'Rojo brillante',
    'bright_green': 'Verde brillante',
    'bright_yellow': 'Amarillo brillante',
    'bright_blue': 'Azul brillante',
    'bright_magenta': 'Magenta brillante',
    'bright_cyan': 'Cian brillante',
    'bright_white': 'Blanco brillante',
    'dark_red': 'Rojo oscuro',
    'dark_green': 'Verde oscuro',
    'dark_yellow': 'Amarillo oscuro',
    'dark_blue': 'Azul oscuro',
    'dark_magenta': 'Magenta oscuro',
    'dark_cyan': 'Cian oscuro',
    'grey0': 'Gris 0',
    'grey19': 'Gris 19',
    'grey30': 'Gris 30',
    'grey37': 'Gris 37',
    'grey46': 'Gris 46',
    'grey50': 'Gris 50',
    'grey54': 'Gris 54',
    'grey58': 'Gris 58',
    'grey62': 'Gris 62',
    'grey66': 'Gris 66',
    'grey70': 'Gris 70',
    'grey74': 'Gris 74',
    'grey78': 'Gris 78',
    'grey82': 'Gris 82',
    'grey85': 'Gris 85',
    'grey89': 'Gris 89',
    'grey93': 'Gris 93',
    'grey100': 'Gris 100',
    'orange1': 'Naranja 1',
    'orange3': 'Naranja 3',
    'orange4': 'Naranja 4'
}

color_background_banner = banner_background_color_tr.get(banner_background_color, banner_background_color)

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
table.add_row("Color del banner", color_banner)
table.add_row("Fondo del banner", banner_background)
table.add_row("Color del fondo del banner", color_background_banner)
table.add_row("")
table.add_row("Seguridad", style="bold green")
table.add_row("")
table.add_row("Método de verificación", login_method)
table.add_row("Contraseña", password)
table.add_row("")
table.add_row("Privacidad", style="bold green")
table.add_row("")
table.add_row("TOR", f"{is_tor} | del sistema")
table.add_row("VPN", f"{is_vpn} | del sistema")
table.add_row("PROXY", f"{is_proxy} | del sistema")
table.add_row("")
table.add_row("Red/Sistema", style="bold green")
table.add_row("")
table.add_row("Tú IP enmascarada", ip)
table.add_row("Red", network)
table.add_row("Ruta", route)

console.print(table, style="bright_white", justify="center")

# Banner

user_banner = Panel(
    banner,
    title="[bold green]Banner",
    title_align="center",
    border_style="bold white",
    style=banner_color,
    expand=False
)

if banner_background not in ("", "no", "No configurado"):
    console.print(user_banner, style=f"on {banner_background_color}", justify="center")
else:
    console.print(user_banner, justify="center")

console.print("")

