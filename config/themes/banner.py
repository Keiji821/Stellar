import os
import platform
import datetime
import time
import requests
import psutil
import shutil
import subprocess
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
        boot_time = psutil.boot_time()
        uptime = datetime.datetime.fromtimestamp(boot_time)
        ta_str = str(datetime.datetime.now() - uptime).split('.')[0]
    except Exception:
        ta_str = "No disponible"

    cpu_info = {
        'marca': platform.processor() or "N/A",
        'nucleos': "N/A",
        'hilos': "N/A",
        'uso': "N/A"
    }
    
    try:
        cpu_info.update({
            'nucleos': psutil.cpu_count(logical=False),
            'hilos': psutil.cpu_count(logical=True),
            'uso': f"{psutil.cpu_percent(interval=0.1)}%"
        })
    except Exception:
        pass

    vm = psutil.virtual_memory()
    du = psutil.disk_usage(os.path.expanduser("~"))

    ip_info = {'ipv4': "No disponible", 'ipv6': "No disponible"}
    try:
        ip_info['ipv4'] = requests.get("https://api.ipify.org", timeout=2).text
        ip_info['ipv6'] = requests.get("https://api64.ipify.org", timeout=2).text
    except Exception:
        pass

    try:
        bateria = psutil.sensors_battery()
        battery_info = f"{bateria.percent}% ({'⚡' if bateria.power_plugged else '🔋'})" if bateria else "N/A"
    except Exception:
        battery_info = "N/A"

    return {
        "Usuario": usuario,
        "Fecha": now.strftime("%d/%m/%Y"),
        "Hora": now.strftime("%H:%M:%S"),
        "OS": f"Termux {platform.machine()}",
        "Kernel": platform.release(),
        "Tiempo actividad": ta_str,
        "Shell": os.path.basename(os.getenv("SHELL", "bash")),
        "Terminal": os.getenv("TERM", "unknown"),
        "CPU": f"{cpu_info['marca']} ({cpu_info['nucleos']}C/{cpu_info['hilos']}T)",
        "Uso CPU": cpu_info['uso'],
        "Memoria": f"{vm.percent}% [{vm.used//(1024**2)}MB/{vm.total//(1024**2)}MB]",
        "Almacenamiento": f"{du.percent}% [{du.used//(1024**3)}GB/{du.total//(1024**3)}GB]",
        "IP": f"IPv4: {ip_info['ipv4']}\nIPv6: {ip_info['ipv6']}",
        "Batería": battery_info
    }

def render_bar(pct, width, fill="█", empty="░"):
    try:
        filled = int(pct * width / 100)
        return fill * filled + empty * (width - filled)
    except Exception:
        return ""

def crear_panel(info, panel_width):
    t = Table.grid(expand=False)
    t.add_column(style="#F2C1D7", justify="right", no_wrap=True)
    t.add_column(style="#B39AB6")
    
    emojis = {
        "Usuario": "👤", "Fecha": "📅", "Hora": "⏰", 
        "OS": "💻", "Kernel": "🧩", "Tiempo actividad": "⏳",
        "Shell": "🐚", "Terminal": "🖥️", "CPU": "🧠",
        "Uso CPU": "📈", "Memoria": "💾", 
        "Almacenamiento": "💽", "IP": "🌐", "Batería": "🔋"
    }

    for key in ["Usuario", "Fecha", "Hora", "OS", "Kernel",
                "Tiempo actividad", "Shell", "Terminal", 
                "CPU", "Uso CPU"]:
        t.add_row(f"{emojis.get(key, ' ')} {key}:", info[key])
    
    metricas = [
        ("Memoria", info["Memoria"].split()[0], "#FFB85C"),
        ("Almacenamiento", info["Almacenamiento"].split()[0], "#00FF7F")
    ]
    
    for nombre, valor, color in metricas:
        bar_w = max(min(panel_width - 20, 40), 10)
        try:
            bar = render_bar(float(valor.strip('%')), bar_w)
            t.add_row(f"{emojis[nombre]} {nombre}:", f"[{color}]{bar}[/{color}] {valor}")
        except Exception:
            t.add_row(f"{emojis[nombre]} {nombre}:", valor)

    t.add_row(f"{emojis['IP']} IP:", info["IP"])
    t.add_row(f"{emojis['Batería']} Batería:", info["Batería"])

    return Panel(
        t,
        title="📊 Sistema Info",
        border_style="#FF69B4",
        padding=(1,2),
        expand=False,
        width=panel_width
    )

if __name__ == "__main__":
    info = obtener_info()
    cols = shutil.get_terminal_size().columns
    banner_width = max(len(line) for line in banner.splitlines())
    info_width = cols - banner_width - 4
    panel = crear_panel(info, info_width)
    console.print(Columns([text_banner, panel], expand=False, equal=False))
    console.print("\n")