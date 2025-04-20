import os
import platform
import datetime
import time
import requests
import psutil
import shutil
import random
from rich.console import Console
from rich.text import Text
from rich.style import Style
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

console = Console()

themes_dir = os.path.expanduser("~/Stellar/config/themes")
system_dir = os.path.expanduser("~/Stellar/config/system")

color_palettes = [
    {'key': '#F2C1D7', 'value': '#B39AB6', 'mem': '#FFB85C', 'disk': '#00FF7F', 'border': '#FF69B4'},
    {'key': '#89CFF0', 'value': '#77DD77', 'mem': '#FF6961', 'disk': '#AEC6CF', 'border': '#B39EB5'},
    {'key': '#CF9FFF', 'value': '#FFB347', 'mem': '#B19CD9', 'disk': '#FF6961', 'border': '#779ECB'},
    {'key': '#98FB98', 'value': '#FFD700', 'mem': '#87CEEB', 'disk': '#FFB6C1', 'border': '#FFA07A'}
]

palette = random.choice(color_palettes)

def leer_archivo(ruta, defecto=""):
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return defecto

def procesar_estilo(cadena):
    partes = cadena.lower().split()
    bold = "bold" in partes
    color = next((p for p in partes if p != "bold"), None)
    return Style(color=color, bold=bold)

banner = leer_archivo(f"{themes_dir}/banner.txt")
col = leer_archivo(f"{themes_dir}/banner_color.txt", "#6E97B7")
bg = leer_archivo(f"{themes_dir}/banner_background.txt", "no")
bgcol = leer_archivo(f"{themes_dir}/banner_background_color.txt", "#4D8FAC")
usuario = leer_archivo(f"{system_dir}/user.txt", "Usuario")

style = procesar_estilo(col)
if bg.lower() in ("si", "sí", "yes"):
    style += Style(bgcolor=bgcol)
text_banner = Text(banner, style=style)

def obtener_info():
    now = datetime.datetime.now()
    try:
        ta = time.time() - psutil.boot_time()
        ta_str = f"{int(ta//3600)}h {int((ta%3600)//60)}m"
    except:
        ta_str = "No disponible"
    vm = psutil.virtual_memory()
    du = psutil.disk_usage(os.path.expanduser("~"))
    try:
        ip = requests.get("https://api.ipify.org", timeout=2).text
    except:
        ip = "No disponible"
    return {
        "Usuario": usuario,
        "Fecha": now.strftime("%Y-%m-%d"),
        "Hora": now.strftime("%I:%M %p"),
        "OS": f"Termux {platform.machine()}",
        "Kernel": platform.release(),
        "TiempoActividad": ta_str,
        "Shell": os.path.basename(os.getenv("SHELL", "bash")),
        "Terminal": os.getenv("TERM", "unknown"),
        "MemoriaPorcentaje": vm.percent,
        "MemoriaTotal": f"{vm.total//(1024**2)}MB",
        "MemoriaUsada": f"{vm.used//(1024**2)}MB",
        "DiscoPorcentaje": du.percent,
        "DiscoTotal": f"{du.total//(1024**3)}GB",
        "DiscoUsado": f"{du.used//(1024**3)}GB",
        "IP": ip
    }

def render_bar(pct, width=20):
    filled = int(pct * width / 100)
    return f"█{'░'*(width-filled)}"

def crear_panel(info, panel_width):
    t = Table.grid(expand=False)
    t.add_column(style=palette['key'], justify="right", min_width=18)
    t.add_column(style=palette['value'], min_width=28)
    
    for key in ["Usuario", "Fecha", "Hora", "OS", "Kernel", "TiempoActividad", "Shell", "Terminal"]:
        t.add_row(f"{key}: ", info[key])
    
    memoria_bar = f"[{palette['mem']}]{render_bar(info['MemoriaPorcentaje'])}[/] {info['MemoriaPorcentaje']}%"
    memoria_detalle = f"{info['MemoriaUsada']} / {info['MemoriaTotal']}"
    t.add_row("Memoria: ", f"{memoria_bar}\n{memoria_detalle}")
    
    disco_bar = f"[{palette['disk']}]{render_bar(info['DiscoPorcentaje'])}[/] {info['DiscoPorcentaje']}%"
    disco_detalle = f"{info['DiscoUsado']} / {info['DiscoTotal']}"
    t.add_row("Almacenamiento: ", f"{disco_bar}\n{disco_detalle}")
    
    t.add_row("IP: ", info["IP"])

    return Panel(
        t,
        title="[bold] Sistema Stellar [/]",
        border_style=palette['border'],
        padding=(1, 2),
        width=panel_width
    )

if __name__ == "__main__":
    info = obtener_info()
    cols = shutil.get_terminal_size().columns
    banner_width = max(len(line) for line in banner.splitlines())
    info_width = cols - banner_width - 4
    panel = crear_panel(info, info_width)
    console.print(Columns([text_banner, panel], expand=False))
    console.print("\n")