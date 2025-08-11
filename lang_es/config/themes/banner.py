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
from rich.panel import Panel

console = Console()

themes_dir = os.path.expanduser("~/Stellar/lang_es/config/themes")
system_dir = os.path.expanduser("~/Stellar/lang_es/config/system")

def generar_paleta():
    def color_rgb():
        return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    return {
        'titulo': color_rgb(),
        'clave': color_rgb(),
        'valor': color_rgb(),
        'memoria': color_rgb(),
        'disco': color_rgb(),
        'borde': color_rgb(),
        'barra_memoria': color_rgb(),
        'barra_disco': color_rgb(),
        'fondo': color_rgb()
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
        "usuario": usuario,
        "fecha": now.strftime("%Y-%m-%d"),
        "hora": now.strftime("%I:%M %p"),
        "celular": obtener_modelo_celular(),
        "os": f"{platform.machine()}",
        "kernel": platform.release(),
        "shell": os.path.basename(os.getenv("SHELL", "bash")),
        "terminal": os.getenv("TERM", "unknown"),
        "MemoriaPorcentaje": vm.percent,
        "MemoriaTotal": f"{vm.total//(1024**2):,} MB",
        "MemoriaUsada": f"{vm.used//(1024**2):,} MB",
        "DiscoPorcentaje": du.percent,
        "DiscoTotal": f"{du.total//(1024**3):,} GB",
        "DiscoUsado": f"{du.used//(1024**3):,} GB",
        "ip": ip
    }

def crear_barra(pct, color):
    bar_color = f"rgb({color[0]},{color[1]},{color[2]})"
    return f"[{bar_color}]{'█' * int(pct/5)}{'░' * (20 - int(pct/5))}[/] {pct}%"

def crear_panel(info, panel_width=None):
    t = Table(show_header=False, show_lines=False,
              border_style=estilo_rgb(paleta['borde']),
              box=None, padding=(0,1,0,0))

    t.add_column(style=estilo_rgb(paleta['clave']), justify="right", min_width=12)
    t.add_column(style=estilo_rgb(paleta['valor']), justify="left", min_width=24)

    def nf_row(icon, text, value):
        icon_part = Text(icon, style=Style(color="white", bold=True))
        text_part = Text(f" {text}", style=estilo_rgb(paleta['clave']))
        return icon_part + text_part, value

    t.add_row(*nf_row("󰀄", "Usuario", info["usuario"]))
    t.add_row(*nf_row("󰃭", "Fecha", info["fecha"]))
    t.add_row(*nf_row("󰥔", "Hora", info["hora"]))
    t.add_row(*nf_row("󰄛", "Celular", info["celular"]))
    t.add_row(*nf_row("󰌽", "OS", info["os"]))
    t.add_row(*nf_row("󰘚", "Kernel", info["kernel"]))
    t.add_row(*nf_row("󰆍", "Shell", info["shell"]))
    t.add_row(*nf_row("󰇊", "Terminal", info["terminal"]))
    t.add_row(*nf_row("󰍛", "Memoria",
              crear_barra(info['MemoriaPorcentaje'], paleta['barra_memoria'])))
    t.add_row("", f"{info['MemoriaUsada']} / {info['MemoriaTotal']}")
    t.add_row(*nf_row("󰋊", "Almacenamiento",
              crear_barra(info['DiscoPorcentaje'], paleta['barra_disco'])))
    t.add_row("", f"{info['DiscoUsado']} / {info['DiscoTotal']}")
    t.add_row(*nf_row("󰩠", "IP",
              Text(info["ip"], style=estilo_rgb(paleta['borde']))))


    colors_row = " ".join(f"[rgb({paleta[c][0]},{paleta[c][1]},{paleta[c][2]})]▀▀▀[/]"
                     for c in ['clave', 'valor', 'memoria', 'disco', 'borde'])
    t.add_row(*nf_row("󰝤", "Paleta", colors_row))

    return Panel(t, title=Text("󱓞 System Info", style=Style(color="white", bold=True)),
                border_style=estilo_rgb(paleta['borde']),
                padding=(1,2))

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
        contenido = Columns([text_banner, panel], expand=False, equal=False)
    else:
        panel = crear_panel(info)
        contenido = Columns([text_banner, panel], expand=True, equal=False)

    console.print(contenido)
    console.print("\n" * 1)