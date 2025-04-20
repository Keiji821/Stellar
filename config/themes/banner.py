import os
import platform
import datetime
import time
import requests
import psutil
from rich.console import Console, Group
from rich.text import Text
from rich.style import Style
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn

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
if bg.lower() in ("si","sí","yes"):
    style += Style(bgcolor=bgcol)
text_banner = Text(banner, style=style)

def obtener_info():
    ahora = datetime.datetime.now()
    try:
        ta = time.time() - psutil.boot_time()
        ta_str = f"{int(ta//3600)}h {int((ta%3600)//60)}m"
    except Exception:
        ta_str = "No disponible"
    vm = psutil.virtual_memory()
    du = psutil.disk_usage(os.path.expanduser("~"))
    try:
        ip = requests.get("https://api.ipify.org", timeout=2).text
    except Exception:
        ip = "No disponible"
    return {
        "Usuario": usuario,
        "Fecha": ahora.strftime("%Y-%m-%d"),
        "Hora": ahora.strftime("%I:%M%p"),
        "OS": f"Termux {platform.machine()}",
        "Kernel": platform.release(),
        "Tiempo de actividad": ta_str,
        "Paquetes": str(len([f for f in os.listdir('/data/data/com.termux/files/usr/var/lib/dpkg/info') if f.endswith('.list')])),
        "Shell": os.path.basename(os.getenv("SHELL","bash")),
        "Terminal": os.getenv("TERM","unknown"),
        "CPU": platform.processor() or "N/A",
        "Memoria": f"{round(vm.used/2**30,1)}GB/{round(vm.total/2**30,1)}GB",
        "Memoria %": vm.percent,
        "Almacenamiento": f"{round(du.used/2**30,1)}GB/{round(du.total/2**30,1)}GB ({du.percent}%)",
        "Almacenamiento %": du.percent,
        "IP": ip
    }

def crear_tabla(info):
    t = Table.grid(padding=(0,1))
    t.add_column(justify="right", style="bright_magenta", no_wrap=True)
    t.add_column(style="bright_cyan")
    for k in ["Usuario","Fecha","Hora","OS","Kernel","Tiempo de actividad","Paquetes","Shell","Terminal","CPU","Memoria","Almacenamiento","IP"]:
        t.add_row(f"{k}:", info[k])
    return t

def mostrar():
    info = obtener_info()
    tabla = crear_tabla(info)
    prog = Progress(
        TextColumn("Memoria:", style="bold"),
        BarColumn(bar_width=None, complete_style="bright_red"),
        TextColumn(f"{info['Memoria %']}%", style="bright_red"),
        TextColumn("  "),
        TextColumn("Almac:", style="bold"),
        BarColumn(bar_width=None, complete_style="bright_green"),
        TextColumn(f"{info['Almacenamiento %']}%", style="bright_green"),
        expand=True,
        console=console
    )
    prog.add_task("", total=100, completed=info["Memoria %"])
    prog.add_task("", total=100, completed=info["Almacenamiento %"])
    panel = Panel(
        Group(tabla, prog),
        title="Información del Sistema",
        border_style="bright_white",
        padding=(1,2)
    )
    console.print(Columns([text_banner, panel], expand=True))

if __name__ == "__main__":
    mostrar()