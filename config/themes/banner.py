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

def display_banner():
    os.chdir(os.path.expanduser("~/Stellar/config/system"))
    with open("banner.txt", "r") as f:
        banner = f.read().strip()
    with open("banner_color.txt", "r") as f:
        color = f.read().strip().replace("bold ", "")
    with open("banner_background.txt", "r") as f:
        bg = f.read().strip().lower()
    with open("banner_background_color.txt", "r") as f:
        bg_color = f.read().strip().lower()
    os.system("clear")
    style = Style(color=color, bold=True)
    if bg in ["si", "sí", "yes"]:
        style += Style(bgcolor=bg_color)
    return Text(banner, style=style)

def get_system_info():
    now = datetime.datetime.now()
    def get_uptime():
        try:
            up = time.time() - psutil.boot_time()
            h, r = divmod(up, 3600)
            m = int(r // 60)
            return f"{int(h)}h {m}m"
        except:
            return "N/A"
    def get_memory():
        m = psutil.virtual_memory()
        return f"{round(m.used / (1024 ** 3), 1)}GB/{round(m.total / (1024 ** 3), 1)}GB", m.percent
    def get_disk():
        d = psutil.disk_usage(os.path.expanduser("~"))
        return f"{round(d.used / (1024 ** 3), 1)}GB/{round(d.total / (1024 ** 3), 1)}GB ({d.percent}%)", d.percent
    def get_cpu():
        out = os.popen("top -n 1 | grep 'CPU:'").read().split()
        return next((p for p in out if p.endswith("%")), "N/A")
    try:
        ip = requests.get('https://api.ipify.org', timeout=2).text
    except:
        ip = "No disponible"

    mem_str, mem_pct = get_memory()
    disk_str, disk_pct = get_disk()
    return {
        "Usuario": user,
        "Fecha": now.strftime("%Y-%m-%d"),
        "Hora": now.strftime("%I:%M%p"),
        "OS": f"Termux {platform.machine()}",
        "Kernel": platform.release(),
        "Tiempo de actividad": get_uptime(),
        "Paquetes": str(len([f for f in os.listdir('/data/data/com.termux/files/usr/var/lib/dpkg/info') if f.endswith('.list')])),
        "Shell": os.path.basename(os.getenv("SHELL", "bash")),
        "Terminal": os.getenv("TERM", "unknown"),
        "CPU": get_cpu(),
        "Memoria": mem_str,
        "Memoria %": mem_pct,
        "Almacenamiento": disk_str,
        "Almacenamiento %": disk_pct,
        "Tu IP": ip
    }

def make_panel(info):
    table = Table.grid(padding=(0, 1))
    table.add_column(justify="right", style="bright_magenta", no_wrap=True)
    table.add_column(style="bright_cyan")
    for key in ["Usuario", "Fecha", "Hora", "OS", "Kernel", "Tiempo de actividad", "Paquetes", "Shell", "Terminal", "CPU", "Memoria", "Almacenamiento", "Tu IP"]:
        table.add_row(f"{key}:", info[key])

    progress = Progress(
        TextColumn("Memoria:"),
        BarColumn(bar_width=None, complete_style="bright_red"),
        TextColumn(f"{info['Memoria %']}%"),
        TextColumn("   "),
        TextColumn("Almacenamiento:"),
        BarColumn(bar_width=None, complete_style="bright_green"),
        TextColumn(f"{info['Almacenamiento %']}%"),
        expand=True,
        console=console
    )
    progress.add_task("", total=100, completed=info["Memoria %"])
    progress.add_task("", total=100, completed=info["Almacenamiento %"])

    panel = Panel.fit(
        table,
        title="Información del Sistema",
        border_style="bright_white",
        padding=(1, 2),
    )
    return panel, progress

def main():
    global user
    os.chdir(os.path.expanduser("~/Stellar/config/system"))
    user = open("user.txt").read().strip().lower()
    banner = display_banner()
    info = get_system_info()
    panel, progress = make_panel(info)
    console.print(Columns([banner, panel], expand=True))
    console.print(progress)

if __name__ == "__main__":
    main()