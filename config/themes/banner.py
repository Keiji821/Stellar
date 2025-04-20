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
col = leer_archivo(f"{themes_dir}/banner_color.txt", "#00FF00")
bg = leer_archivo(f"{themes_dir}/banner_background.txt", "no")
bgcol = leer_archivo(f"{themes_dir}/banner_background_color.txt", "#00BFFF")
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
        "Memoria %": vm.percent,
        "Memoria": f"{round(vm.used/2**30,1)}GB/{round(vm.total/2**30,1)}GB",
        "Almacenamiento %": du.percent,
        "Almacenamiento": f"{round(du.used/2**30,1)}GB/{round(du.total/2**30,1)}GB ({du.percent}%)",
        "IP": ip
    }

def render_bar(pct, width, fill="█", empty="░"):
    filled = int(pct * width / 100)
    return fill * filled + empty * (width - filled)

def crear_panel(info, panel_width):
    t = Table.grid(expand=False)
    t.add_column(style="#FFFF00", justify="right", no_wrap=True)
    t.add_column(style="#1E90FF")
    emojis = {
        "Usuario": "👤", "Fecha": "📅", "Hora": "⏰", "OS": "💻",
        "Kernel": "🧩", "Tiempo de actividad": "⏳", "Paquetes": "📦",
        "Shell": "🐚", "Terminal": "🖥️", "CPU": "🧠", "Memoria": "🧮",
        "Almacenamiento": "💾", "IP": "🌐"
    }
    for key in ["Usuario","Fecha","Hora","OS","Kernel","Tiempo de actividad","Paquetes","Shell","Terminal","CPU"]:
        t.add_row(f"{emojis[key]} {key}:", info[key])
    bar_w = max(min(panel_width - 20, 40), 10)
    mem_bar = render_bar(info["Memoria %"], bar_w)
    disk_bar = render_bar(info["Almacenamiento %"], bar_w)
    t.add_row(f"{emojis['Memoria']} Memoria:", f"[#FF1493]{mem_bar}[/#FF1493] {info['Memoria %']}%")
    t.add_row(f"{emojis['Almacenamiento']} Almacen.:", f"[#8000FF]{disk_bar}[/#8000FF] {info['Almacenamiento %']}%")
    t.add_row(f"{emojis['IP']} IP:", info["IP"])
    return Panel(t, title="Información del Sistema", border_style="#FFD700", padding=(1,2), expand=False, width=panel_width)

if __name__ == "__main__":
    info = obtener_info()
    cols = shutil.get_terminal_size().columns
    banner_width = max(len(line) for line in banner.splitlines())
    info_width = cols - banner_width - 2
    panel = crear_panel(info, info_width)
    console.print(Columns([text_banner, panel], expand=False))