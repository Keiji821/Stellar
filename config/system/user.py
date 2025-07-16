from rich.console import Console
import os
from os import system
from rich.table import Table
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

with open("banner_color.txt", encoding="utf-8") as f:
    banner_color = f.read().strip()

if banner_color=="":
    banner_color = "no"

banner_color_tr = {
'no': 'No configurado',
'bold green': 'Verde intenso',
'bold yellow': 'Amarillo intenso',
'bold white': 'Blanco intenso',
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
'bold green': 'Verde intenso',
'bold yellow': 'Amarillo intenso',
'bold white': 'Blanco intenso',
}
color_background_banner = banner_background_color_tr.get(banner_background_color)

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
table.add_row("Red" network)
table.add_row("Ruta" ruta)


console.print(table, style="bright_white", justify="center")
console.print("")

