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
col = leer_archivo(f"{themes_dir}/banner_color.txt", "#91ee98")
bg = leer_archivo(f"{themes_dir}/banner_background.txt", "no")
bgcol = leer_archivo(f"{themes_dir}/banner_background_color.txt", "#a6c8d8")
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

def crear_panel(info):
    cols = shutil.get_terminal_size().columns
    bar_w = max(min(cols - 35, 40), 10)
    t = Table.grid(expand=False)
    t.add_column(style="#e5e186", justify="right", no_wrap=True)
    t.add_column(style="#a6c8d8")
    emojis = {
        "Usuario": "👤", "Fecha": "📅", "Hora": "⏰", "OS": "💻",
        "Kernel": "🧩", "Tiempo de actividad": "⏳", "Paquetes": "📦",
        "Shell": "🐚", "Terminal": "🖥️", "CPU": "🧠", "Memoria": "🧮",
        "Almacenamiento": "💾", "IP": "🌐"
    }
    for key in ["Usuario","Fecha","Hora","OS","Kernel","Tiempo de actividad",
                "Paquetes","Shell","Terminal","CPU"]:
        t.add_row(f"{emojis[key]} {key}:", info[key])
    mem_bar = render_bar(info["Memoria %"], bar_w)
    disk_bar = render_bar(info["Almacenamiento %"], bar_w)
    t.add_row(f"{emojis['Memoria']} Memoria:", f"[#e57d7d]{mem_bar}[/#e57d7d] {info['Memoria %']}%")
    t.add_row(f"{emojis['Almacenamiento']} Almacen.:", f"[#8579ce]{disk_bar}[/#8579ce] {info['Almacenamiento %']}%")
    t.add_row(f"{emojis['IP']} IP:", info["IP"])
    return Panel(t, title="Información del Sistema", border_style="#fd9bca", padding=(1,2))

if __name__ == "__main__":
    info = obtener_info()
    panel = crear_panel(info)
    console.print(Columns([text_banner, panel], expand=True, equal=True, align="center"))