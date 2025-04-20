import os
import platform
import datetime
import time
import requests
import psutil
import shutil
from rich.console import Console
from rich.text import Text
from rich.style import Style
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

console = Console()

themes_dir = os.path.expanduser("~/Stellar/config/themes")
system_dir = os.path.expanduser("~/Stellar/config/system")

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
        "Hora": now.strftime("%I:%M%p"),
        "OS": f"Termux {platform.machine()}",
        "Kernel": platform.release(),
        "TiempoActividad": ta_str,
        "Shell": os.path.basename(os.getenv("SHELL", "bash")),
        "Terminal": os.getenv("TERM", "unknown"),
        "Memoria": f"{vm.percent}% ({vm.used//(1024**2)}MB/{vm.total//(1024**2)}MB)",
        "Almacenamiento": f"{du.percent}% ({du.used//(1024**3)}GB/{du.total//(1024**3)}GB)",
        "IP": ip
    }

def render_bar(pct, width=20):
    filled = int(pct * width / 100)
    return f"█{'░'*(width-filled)} {pct}%"

def crear_panel(info, panel_width):
    t = Table.grid(expand=False)
    t.add_column(style="#F2C1D7", justify="right")
    t.add_column(style="#B39AB6")
    
    for key in ["Usuario", "Fecha", "Hora", "OS", "Kernel", "TiempoActividad", "Shell", "Terminal"]:
        t.add_row(f"{key}:", info[key])
    
    t.add_row("Memoria:", f"[#FFB85C]{render_bar(float(info['Memoria'].split('%')[0]))}[/]")
    t.add_row("Almacenamiento:", f"[#00FF7F]{render_bar(float(info['Almacenamiento'].split('%')[0]))}[/]")
    t.add_row("IP:", info["IP"])

    return Panel(
        t,
        title="Stellar System Info",
        border_style="#FF69B4",
        padding=(1,2),
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