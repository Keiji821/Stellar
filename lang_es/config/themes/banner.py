import os
import platform
import datetime
import time
import requests
import psutil
import shutil
import random
import subprocess
from rich.console import Console
from rich.text import Text
from rich.style import Style
from rich.table import Table
from rich.columns import Columns

console = Console()

themes_dir = os.path.expanduser("~/Stellar/lang_es/config/themes")
system_dir = os.path.expanduser("~/Stellar/lang_es/config/system")

def generar_paleta():
    def color_rgb():
        return (random.randint(100, 255), (random.randint(100, 255)), (random.randint(100, 255)))
    return {
        'titulo': color_rgb(),
        'clave': color_rgb(),
        'valor': color_rgb(),
        'memoria': color_rgb(),
        'disco': color_rgb(),
        'borde': color_rgb()
    }

def estilo_rgb(color):
    return Style(color=f"rgb({color[0]},{color[1]},{color[2]})")

def leer_archivo(ruta, defecto=""):
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return defecto

def obtener_modelo_celular():
    try:
        modelo = subprocess.check_output(['getprop', 'ro.product.model']).decode().strip()
        return modelo if modelo else "Desconocido"
    except:
        return "Desconocido"

def procesar_estilo(cadena):
    partes = cadena.lower().split()
    bold = "bold" in partes
    color = next((p for p in partes if p != "bold"), None)
    return Style(color=color, bold=bold)

paleta = generar_paleta()
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
    vm = psutil.virtual_memory()
    du = psutil.disk_usage(os.path.expanduser("~"))

    ip_services = [
        "https://api.ipify.org",
        "https://ipinfo.io/ip",
        "https://ifconfig.me/ip",
        "https://ident.me"
    ]

    ip = "No disponible"
    for service in ip_services:
        try:
            response = requests.get(service, timeout=2)
            if response.status_code == 200:
                ip = response.text.strip()
                break
            elif response.status_code == 429:
                time.sleep(1)
                continue
        except (requests.RequestException, ConnectionError):
            continue

    return {
        "☕ Usuario": usuario,
        "📅 Fecha": now.strftime("%Y-%m-%d"),
        "🕛 Hora": now.strftime("%I:%M %p"),
        "🧸 Celular": obtener_modelo_celular(),
        "📦 OS": f"{platform.machine()}",
        "💿 Kernel": platform.release(),
        "🐚 Shell": os.path.basename(os.getenv("SHELL", "bash")),
        "📀 Terminal": os.getenv("TERM", "unknown"),
        "MemoriaPorcentaje": vm.percent,
        "MemoriaTotal": f"{vm.total//(1024**2):,} MB",
        "MemoriaUsada": f"{vm.used//(1024**2):,} MB",
        "DiscoPorcentaje": du.percent,
        "DiscoTotal": f"{du.total//(1024**3):,} GB",
        "DiscoUsado": f"{du.used//(1024**3):,} GB",
        "🔒 IP": ip
    }

def render_bar(pct, color, width=20):
    filled = int(pct * width / 100)
    return Text("█" * filled + "░" * (width - filled), style=estilo_rgb(color))

def crear_panel(info, panel_width=None):
    t = Table.grid(expand=False)
    t.add_column(style=estilo_rgb(paleta['clave']), justify="left", min_width=18)
    t.add_column(style=estilo_rgb(paleta['valor']), justify="left", min_width=30)

    t.add_row("", "")

    for key in ["☕ Usuario", "📅 Fecha", "🕛 Hora", "🧸 Celular", "📦 OS", "💿 Kernel", "🐚 Shell", "📀 Terminal"]:
        t.add_row(f"{key}: ", info[key])

    memoria_bar = render_bar(info['MemoriaPorcentaje'], paleta['memoria'])
    t.add_row("💽 Memoria:", memoria_bar)
    t.add_row("", f"{info['MemoriaUsada']} / {info['MemoriaTotal']}")

    disco_bar = render_bar(info['DiscoPorcentaje'], paleta['disco'])
    t.add_row("💾 Almacenamiento:", disco_bar)
    t.add_row("", f"{info['DiscoUsado']} / {info['DiscoTotal']}")

    t.add_row("🔒 IP:", Text(info["🔒 IP"], style=estilo_rgb(paleta['borde'])))
    return t

if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')

    info = obtener_info()
    terminal_cols = shutil.get_terminal_size().columns
    banner_width = max(len(line) for line in banner.splitlines()) if banner else 0

    min_panel_width = 54
    espacio_entre = 4

    if terminal_cols >= (banner_width + min_panel_width + espacio_entre):
        panel_width = terminal_cols - banner_width - espacio_entre
        panel = crear_panel(info, panel_width)
        contenido = Columns([text_banner, panel], expand=False)
    else:
        panel = crear_panel(info)
        contenido = Columns([text_banner, panel], expand=True)

    console.print(contenido)
    console.print("\n" * 3)