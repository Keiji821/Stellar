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
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table

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
col = leer_archivo(f"{themes_dir}/banner_color.txt", "cyan")
bg = leer_archivo(f"{themes_dir}/banner_background.txt", "no")
bgcol = leer_archivo(f"{themes_dir}/banner_background_color.txt", "black")
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
        "Tiempo de actividad": ta_str,
        "Paquetes": str(len([f for f in os.listdir('/data/data/com.termux/files/usr/var/lib/dpkg/info') if f.endswith('.list')])),
        "Shell": os.path.basename(os.getenv("SHELL", "bash")),
        "Terminal": os.getenv("TERM", "unknown"),
        "CPU": platform.processor() or "N/A",
        "Memoria": f"{round(vm.used/2**30,1)}GB/{round(vm.total/2**30,1)}GB",
        "Memoria %": vm.percent,
        "Almacenamiento": f"{round(du.used/2**30,1)}GB/{round(du.total/2**30,1)}GB ({du.percent}%)",
        "Almacenamiento %": du.percent,
        "IP": ip
    }

def render_bar(pct, width):
    llenado = int(pct * width / 100)
    vacio = width - llenado
    return "[" + "█" * llenado + " " * vacio + "]"

def crear_panel(info):
    cols = shutil.get_terminal_size().columns
    bar_width = max(min(cols - 40, 40), 10)
    t = Table.grid(padding=(0, 1))
    t.add_column(justify="right", style="bright_magenta", no_wrap=True)
    t.add_column(style="bright_cyan", no_wrap=False)
    claves = ["Usuario", "Fecha", "Hora", "OS", "Kernel", "Tiempo de actividad", "Paquetes", "Shell", "Terminal", "CPU"]
    for k in claves:
        t.add_row(f"{k}:", info[k])
    barra_mem = render_bar(info["Memoria %"], bar_width)
    barra_disk = render_bar(info["Almacenamiento %"], bar_width)
    t.add_row("Memoria:", f"{barra_mem} {info['Memoria']}")
    t.add_row("Almacenamiento:", f"{barra_disk} {info['Almacenamiento']}")
    t.add_row("IP:", info["IP"])
    return Panel(t, title="Información del Sistema", border_style="bright_white", padding=(1, 2), expand=True)

if __name__ == "__main__":
    info = obtener_info()
    panel = crear_panel(info)
    console.print(Columns([text_banner, panel], expand=True))