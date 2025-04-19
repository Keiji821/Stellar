import datetime
import os
import platform
import time
import requests
import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.progress import Progress, BarColumn, TextColumn

console = Console()

os.chdir(os.path.expanduser("~/Stellar/config/system"))
with open("user.txt", "r") as f:
    user = f.read().strip().lower()

def get_system_info():
    now = datetime.datetime.now()

    def get_uptime():
        try:
            uptime_seconds = time.time() - psutil.boot_time()
            hours, remainder = divmod(uptime_seconds, 3600)
            minutes = int(remainder // 60)
            return f"{int(hours)}h {minutes}m"
        except:
            return "N/A"

    def get_packages():
        try:
            return str(len([name for name in os.listdir('/data/data/com.termux/files/usr/var/lib/dpkg/info')
                            if name.endswith('.list')]))
        except:
            return "N/A"

    def get_memory():
        try:
            mem = psutil.virtual_memory()
            used = mem.used / (1024**3)
            total = mem.total / (1024**3)
            percent = mem.percent
            return f"{round(used, 1)}GB/{round(total, 1)}GB", percent
        except:
            return "N/A", 0

    def get_disk():
        try:
            disk = psutil.disk_usage('/data/data/com.termux/files/home')
            used = disk.used / (1024**3)
            total = disk.total / (1024**3)
            percent = disk.percent
            return f"{round(used,1)}GB/{round(total,1)}GB ({percent}%)", percent
        except:
            return "N/A", 0

    try:
        response = requests.get('https://api.ipapi.is/?ip=', timeout=3)
        ip = response.json().get('ip', 'No disponible')
    except:
        ip = 'No disponible'

    mem_str, mem_percent = get_memory()
    disk_str, disk_percent = get_disk()

    return {
        "Usuario": user,
        "Fecha": now.strftime("%Y-%m-%d"),
        "Hora": now.strftime("%I:%M%p"),
        "OS": f"Termux {platform.machine()}",
        "Kernel": platform.release(),
        "Tiempo de actividad": get_uptime(),
        "Paquetes": get_packages(),
        "Shell": os.path.basename(os.getenv('SHELL', 'bash')),
        "Terminal": os.getenv('TERM', 'unknown'),
        "CPU": platform.processor() or "N/A",
        "Memoria": mem_str,
        "Memoria %": mem_percent,
        "Almacenamiento": disk_str,
        "Almacenamiento %": disk_percent,
        "Tu IP Tor": ip
    }

def main():
    info = get_system_info()

    table = Table.grid(padding=(0, 1))
    table.add_column(justify="right", style="bright_magenta", no_wrap=True)
    table.add_column(style="bright_cyan", no_wrap=False)

    for key in ["Usuario", "Fecha", "Hora", "OS", "Kernel", "Tiempo de actividad", "Paquetes",
                "Shell", "Terminal", "CPU", "Memoria", "Almacenamiento", "Tu IP Tor"]:
        table.add_row(f"{key}:", info[key])

    progress = Progress(
        TextColumn("Memoria:"),
        BarColumn(bar_width=None, complete_style="bright_red"),
        TextColumn(f"{info['Memoria %']}%"),
        TextColumn("  "),
        TextColumn("Almacenamiento:"),
        BarColumn(bar_width=None, complete_style="bright_green"),
        TextColumn(f"{info['Almacenamiento %']}%"),
        expand=True,
        console=console
    )

    progress.add_task("", total=100, completed=info["Memoria %"])
    progress.add_task("", total=100, completed=info["Almacenamiento %"])

    panel = Panel.fit(table, border_style="bright_white", title="Información del Sistema", title_align="left")

    console.print(Columns([panel], expand=True))
    console.print(progress)

if __name__ == "__main__":
    main()