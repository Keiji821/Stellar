
import datetime
import os
import platform
import time
import requests
import psutil
from rich.console import Console
from rich.text import Text
from rich.style import Style
from rich.columns import Columns
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, ProgressColumn
from rich.table import Table

console = Console()

os.chdir(os.path.expanduser("~/Stellar/config/system"))
with open("user.txt", "r") as f:
    user = f.read().strip().lower()
os.chdir(os.path.expanduser("~/Stellar/config/themes"))

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
            used_gb = round(mem.used / (1024 ** 3), 1)
            total_gb = round(mem.total / (1024 ** 3), 1)
            percent = round(mem.percent, 1)
            return f"{used_gb}GB/{total_gb}GB", percent
        except:
            return "N/A", 0

    def get_disk():
        try:
            disk = psutil.disk_usage('/data/data/com.termux/files/home')
            used_gb = round(disk.used / (1024 ** 3), 1)
            total_gb = round(disk.total / (1024 ** 3), 1)
            percent = round(disk.percent, 1)
            return f"{used_gb}GB/{total_gb}GB ({percent}%)", percent
        except:
            return "N/A", 0

    def get_cpu():
        try:
            output = os.popen("top -n 1 | grep 'CPU:'").read()
            percent = next((part for part in output.split() if '%' in part), None)
            return percent if percent else "N/A"
        except:
            return "N/A"

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
        "CPU": get_cpu(),
        "Memoria": mem_str,
        "Memoria %": mem_percent,
        "Almacenamiento": disk_str,
        "Almacenamiento %": disk_percent,
        "Tu IP Tor": ip
    }

def display_banner():
    with open("banner.txt", "r") as f:
        banner = f.read().strip()
    with open("banner_color.txt", "r") as f:
        color = f.read().strip().replace("bold ", "")
    with open("banner_background.txt", "r") as f:
        background = f.read().strip().lower()
    with open("banner_background_color.txt", "r") as f:
        background_color = f.read().strip().lower()
    os.system("clear")
    return banner, color, background, background_color

class ColorBarColumn(ProgressColumn):
    def render(self, task):
        percent = task.percentage
        if percent is None:
            return Text("N/A")
        if percent >= 70:
            color = "bright_red"
        elif percent >= 40:
            color = "bright_yellow"
        else:
            color = "bright_green"
        bar = BarColumn(bar_width=25, complete_style=color)
        return bar.render(task)

def main():
    banner, color, background, background_color = display_banner()
    info = get_system_info()

    banner_style = Style(color=color, bold=True) if color else Style(bold=True)
    if background in ["si", "sí", "yes"]:
        banner_style += Style(bgcolor=background_color)

    left_panel = Text(banner, style=banner_style)

    table = Table.grid(padding=(0, 1))
    table.add_column(justify="right", style="bright_magenta", no_wrap=True)
    table.add_column(style="bright_cyan", no_wrap=False)

    table.add_row("Usuario:", info["Usuario"])
    table.add_row("Fecha:", info["Fecha"])
    table.add_row("Hora:", info["Hora"])
    table.add_row("OS:", info["OS"])
    table.add_row("Kernel:", info["Kernel"])
    table.add_row("Tiempo de actividad:", info["Tiempo de actividad"])
    table.add_row("Paquetes:", info["Paquetes"])
    table.add_row("Shell:", info["Shell"])
    table.add_row("Terminal:", info["Terminal"])
    table.add_row("CPU:", info["CPU"])
    table.add_row("Memoria:", info["Memoria"])
    table.add_row("Almacenamiento:", info["Almacenamiento"])
    table.add_row("Tu IP Tor:", info["Tu IP Tor"])

    progress = Progress(
        TextColumn("Memoria:"),
        BarColumn(bar_width=25, complete_style="bright_green"),
        TextColumn(f"{info['Memoria %']}%"),
        TextColumn("  "),
        TextColumn("Almacenamiento:"),
        BarColumn(bar_width=25, complete_style="bright_blue"),
        TextColumn(f"{info['Almacenamiento %']}%"),
        expand=False,
    )

    progress.add_task("", total=100, completed=info["Memoria %"])
    progress.add_task("", total=100, completed=info["Almacenamiento %"])

    right_panel = Panel.fit(table, border_style="bright_white", title="Información del Sistema", title_align="left")

    console.print(Columns([left_panel, right_panel], equal=False, expand=True))
    console.print(progress)

if __name__ == "__main__":
    main()