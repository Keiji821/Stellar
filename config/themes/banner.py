import os
import platform
import datetime
import time
import requests
import psutil
from rich.console import Console
from rich.text import Text
from rich.style import Style
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn

console = Console()

themes_dir = os.path.expanduser("~/Stellar/config/themes")
system_dir = os.path.expanduser("~/Stellar/config/system")

def leer_archivo(ruta_archivo, valor_por_defecto=""):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read().strip()
    except FileNotFoundError:
        return valor_por_defecto

def procesar_estilo(cadena_estilo):
    partes = cadena_estilo.lower().split()
    es_bold = 'bold' in partes
    color = next((parte for parte in partes if parte != 'bold'), None)
    return Style(color=color, bold=es_bold)

banner = leer_archivo(os.path.join(themes_dir, "banner.txt"))
cadena_estilo = leer_archivo(os.path.join(themes_dir, "banner_color.txt"), "cyan")
banner_background = leer_archivo(os.path.join(themes_dir, "banner_background.txt"), "no")
banner_background_color = leer_archivo(os.path.join(themes_dir, "banner_background_color.txt"), "black")
usuario = leer_archivo(os.path.join(system_dir, "user.txt"), "Usuario")

style = procesar_estilo(cadena_estilo)
if banner_background.lower() in ["si", "sí", "yes"]:
    style += Style(bgcolor=banner_background_color)
text_banner = Text(banner, style=style)

def obtener_informacion_sistema():
    ahora = datetime.datetime.now()
    
    try:
        tiempo_actividad = time.time() - psutil.boot_time()
        tiempo_actividad_str = f"{int(tiempo_actividad // 3600)}h {int((tiempo_actividad % 3600) // 60)}m"
    except (PermissionError, psutil.Error) as e:
        tiempo_actividad_str = "No disponible"
    
    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage(os.path.expanduser("~"))
    try:
        ip = requests.get("https://api.ipify.org", timeout=2).text
    except requests.RequestException:
        ip = "No disponible"
    
    return {
        "Usuario": usuario,
        "Fecha": ahora.strftime("%Y-%m-%d"),
        "Hora": ahora.strftime("%I:%M%p"),
        "OS": f"Termux {platform.machine()}",
        "Kernel": platform.release(),
        "Tiempo de actividad": tiempo_actividad_str,
        "Paquetes": str(len([f for f in os.listdir('/data/data/com.termux/files/usr/var/lib/dpkg/info') if f.endswith(".list")])),
        "Shell": os.path.basename(os.getenv("SHELL", "bash")),
        "Terminal": os.getenv("TERM", "unknown"),
        "CPU": platform.processor() or "N/A",
        "Memoria": f"{round(memoria.used / 2**30, 1)}GB/{round(memoria.total / 2**30, 1)}GB",
        "Memoria %": memoria.percent,
        "Almacenamiento": f"{round(disco.used / 2**30, 1)}GB/{round(disco.total / 2**30, 1)}GB ({disco.percent}%)",
        "Almacenamiento %": disco.percent,
        "IP": ip
    }

def crear_panel_informacion(info):
    tabla = Table.grid(padding=(0, 1))
    tabla.add_column(justify="right", style="bright_magenta", no_wrap=True)
    tabla.add_column(style="bright_cyan")
    for clave in ["Usuario", "Fecha", "Hora", "OS", "Kernel", "Tiempo de actividad", "Paquetes", "Shell", "Terminal", "CPU", "Memoria", "Almacenamiento", "IP"]:
        tabla.add_row(f"{clave}:", info[clave])

    panel = Panel.fit(tabla, title="Información del Sistema", border_style="bright_white", padding=(1, 2))
    return panel

def mostrar_barras_progreso(info):
    with Progress(
        TextColumn("Memoria:"),
        BarColumn(bar_width=None, complete_style="bright_red"),
        TextColumn(f"{info['Memoria %']}%", style="bright_red"),
        TextColumn(" "),
        TextColumn("Almacenamiento:"),
        BarColumn(bar_width=None, complete_style="bright_green"),
        TextColumn(f"{info['Almacenamiento %']}%", style="bright_green"),
        expand=True,
        console=console
    ) as progreso:
        progreso.add_task("", total=100, completed=info["Memoria %"])
        progreso.add_task("", total=100, completed=info["Almacenamiento %"])

def mostrar_informacion():
    informacion = obtener_informacion_sistema()
    panel_informacion = crear_panel_informacion(informacion)
    panel_informacion_con_barras = Panel(
        Columns([panel_informacion, Text("  ")], expand=True),
        title="Sistema Detalles",
        border_style="bright_yellow",
        padding=(1, 2)
    )
    console.print(Columns([text_banner, panel_informacion_con_barras], expand=True))
    mostrar_barras_progreso(informacion)

if __name__ == "__main__":
    mostrar_informacion()