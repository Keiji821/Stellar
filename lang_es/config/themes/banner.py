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
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich import box
from rich.layout import Layout
from rich.live import Live
from rich.progress import ProgressBar
from rich.rule import Rule

console = Console()

themes_dir = os.path.expanduser("~/Stellar/lang_es/config/themes")
system_dir = os.path.expanduser("~/Stellar/lang_es/config/system")

# Paleta de colores moderna y profesional
COLOR_PRIMARY = "#6A89CC"
COLOR_SECONDARY = "#B8E994"
COLOR_ACCENT = "#F8C291"
COLOR_SUCCESS = "#78E08F"
COLOR_ERROR = "#E55039"
COLOR_WARNING = "#FAD390"
COLOR_INFO = "#4FC1E9"
COLOR_HIGHLIGHT = "#FFFFFF"
COLOR_BG = "#1E272E"

# Generar paleta con colores armonizados
def generar_paleta():
    def color_rgb():
        return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    
    # Colores principales basados en la paleta profesional
    return {
        'titulo': (106, 137, 204),      # Azul primario
        'clave': (184, 233, 148),       # Verde secundario
        'valor': (248, 194, 145),       # Naranja acento
        'memoria': (79, 193, 233),      # Azul información
        'disco': (120, 224, 143),       # Verde éxito
        'borde': (245, 211, 144),       # Amarillo advertencia
        'fondo': (30, 39, 46)           # Fondo oscuro
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
col = leer_archivo(f"{themes_dir}/banner_color.txt", COLOR_PRIMARY)
bg = leer_archivo(f"{themes_dir}/banner_background.txt", "no")
bgcol = leer_archivo(f"{themes_dir}/banner_background_color.txt", COLOR_BG)
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

    # Obtener temperatura de la CPU si es posible
    temp = "N/A"
    try:
        if hasattr(psutil, "sensors_temperatures"):
            temps = psutil.sensors_temperatures()
            if 'cpu_thermal' in temps:
                temp = f"{temps['cpu_thermal'][0].current}°C"
            elif 'coretemp' in temps:
                temp = f"{temps['coretemp'][0].current}°C"
    except:
        pass

    # Obtener porcentaje de batería
    bateria = "N/A"
    try:
        bateria = f"{psutil.sensors_battery().percent}%"
    except:
        pass

    return {
        "Usuario": usuario,
        "Fecha": now.strftime("%Y-%m-%d"),
        "Hora": now.strftime("%I:%M %p"),
        "Celular": obtener_modelo_celular(),
        "OS": f"{platform.machine()}",
        "Kernel": platform.release(),
        "Shell": os.path.basename(os.getenv("SHELL", "bash")),
        "Terminal": os.getenv("TERM", "unknown"),
        "MemoriaPorcentaje": vm.percent,
        "MemoriaTotal": f"{vm.total//(1024**2):,} MB",
        "MemoriaUsada": f"{vm.used//(1024**2):,} MB",
        "DiscoPorcentaje": du.percent,
        "DiscoTotal": f"{du.total//(1024**3):,} GB",
        "DiscoUsado": f"{du.used//(1024**3):,} GB",
        "Temperatura": temp,
        "Batería": bateria,
        "IP": ip
    }

def render_bar(pct, color, width=20):
    filled = int(pct * width / 100)
    bar = "█" * filled + "░" * (width - filled)
    return Text(bar, style=Style(color=f"rgb({color[0]},{color[1]},{color[2]}"))

def crear_panel(info, panel_width=None):
    # Crear layout con dos columnas
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7)
    )
    
    # Header con título y hora
    fecha_hora = Text(f"{info['Fecha']} | {info['Hora']}", style="bold " + estilo_rgb(paleta['clave']).color)
    layout["header"].update(
        Panel(
            Text.assemble(
                ("STELLAR ", f"bold rgb({paleta['titulo'][0]},{paleta['titulo'][1]},{paleta['titulo'][2]})"),
                ("TERMINAL", "bold white")
            ),
            subtitle=fecha_hora,
            border_style=estilo_rgb(paleta['borde']),
            box=box.ROUNDED,
            padding=(0, 1)
    )
    
    # Crear tabla principal con información
    t = Table.grid(expand=True, padding=(0, 1))
    t.add_column(style=estilo_rgb(paleta['clave']), justify="left", min_width=14)
    t.add_column(style=estilo_rgb(paleta['valor']), justify="left", min_width=10)
    t.add_column(style=estilo_rgb(paleta['clave']), justify="left", min_width=14)
    t.add_column(style=estilo_rgb(paleta['valor']), justify="left", min_width=10)
    
    # Agregar información en dos columnas
    t.add_row("Usuario:", info['Usuario'], "Modelo:", info['Celular'])
    t.add_row("Sistema:", info['OS'], "Kernel:", info['Kernel'])
    t.add_row("Shell:", info['Shell'], "Terminal:", info['Terminal'])
    t.add_row("Batería:", info['Batería'], "Temperatura:", info['Temperatura'])
    t.add_row("", "", "", "")
    
    # Sección de memoria
    t.add_row(
        "Memoria:", 
        Text.assemble(
            (f"{info['MemoriaPorcentaje']}% ", estilo_rgb(paleta['memoria'])),
            f"({info['MemoriaUsada']}/{info['MemoriaTotal']})"
        ),
        "",
        ""
    )
    t.add_row(render_bar(info['MemoriaPorcentaje'], paleta['memoria'], 30), "", "", "")
    
    # Sección de almacenamiento
    t.add_row(
        "Almacenamiento:", 
        Text.assemble(
            (f"{info['DiscoPorcentaje']}% ", estilo_rgb(paleta['disco'])),
            f"({info['DiscoUsado']}/{info['DiscoTotal']})"
        ),
        "",
        ""
    )
    t.add_row(render_bar(info['DiscoPorcentaje'], paleta['disco'], 30), "", "", "")
    
    # Agregar tabla al layout principal
    layout["main"].update(
        Panel(
            t,
            box=box.SQUARE,
            border_style=estilo_rgb(paleta['borde']),
            padding=(1, 2)
    )
    
    # Footer con IP y decoración
    ip_text = Text(f"IP: {info['IP']}", style="bold " + estilo_rgb(paleta['borde']).color)
    layout["footer"].update(
        Columns([
            Panel(
                Text("CONECTADO", style="bold " + estilo_rgb(COLOR_SUCCESS).color),
                box=box.SQUARE,
                border_style=estilo_rgb(COLOR_SUCCESS)
            ),
            Panel(
                ip_text,
                box=box.SQUARE,
                border_style=estilo_rgb(paleta['borde']))
        ])
    )
    
    return layout

def crear_banner_panel():
    return Panel(
        text_banner,
        box=box.ROUNDED,
        border_style=style,
        padding=(1, 2),
        width=min(40, shutil.get_terminal_size().columns//2)
    )

if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')
    info = obtener_info()
    terminal_cols = shutil.get_terminal_size().columns
    
    # Crear layout principal
    main_layout = Layout(name="root")
    
    if terminal_cols > 100:
        # Pantalla grande: banner y panel lado a lado
        main_layout.split_row(
            Layout(name="banner", ratio=1),
            Layout(name="panel", ratio=2)
        )
        banner_panel = crear_banner_panel()
        main_layout["banner"].update(banner_panel)
        main_layout["panel"].update(crear_panel(info))
        console.print(main_layout)
    else:
        # Pantalla pequeña: banner arriba, panel abajo
        main_layout.split(
            Layout(name="banner", size=min(15, shutil.get_terminal_size().lines//3)),
            Layout(name="panel", ratio=1)
        )
        banner_panel = crear_banner_panel()
        main_layout["banner"].update(banner_panel)
        main_layout["panel"].update(crear_panel(info))
        console.print(main_layout)
    
    # Espacio adicional al final
    console.print("\n" * 2)