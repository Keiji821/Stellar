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
from rich.progress import Progress

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

def color_bar(percent):
    color = "bright_green"
    if percent >= 70:
        color = "bright_red"
    elif percent >= 40:
        color = "bright_yellow"
    filled = int(percent // 4)
    empty = 25 - filled
    bar = "[" + "=" * filled + " " * empty + f"] {percent:.1f}%"
    return f"[{color}]{bar}[/{color}]"

def main():
    banner, color, background, background_color = display_banner()
    info = get_system_info()

    banner_style = Style(color=color, bold=True) if color else Style(bold=True)
    if background in ["si", "sí", "yes"]:
        banner_style += Style(bgcolor=background_color)

    left_panel = Text(banner, style=banner_style)
    right_panel = Text("\n")
    label_style = Style(color="bright_magenta", bold=True)
    value_style = Style(color="bright_cyan", bold=True)
    title_style = Style(color="bright_magenta", bold=True)

    def section(title):
        right_panel.append(f"[ {title} ]\n", style=title_style)

    label_padding = max(len(k) for k in info if not k.endswith('%')) + 1

    section("Usuario")
    for key in ["Usuario", "Fecha", "Hora"]:
        label = f"{key.ljust(label_padding)}:"
        right_panel.append(label, style=label_style)
        right_panel.append(f" {info[key]}\n", style=value_style)

    section("Sistema")
    for key in ["OS", "Kernel", "Tiempo de actividad", "Paquetes"]:
        label = f"{key.ljust(label_padding)}:"
        right_panel.append(label, style=label_style)
        right_panel.append(f" {info[key]}\n", style=value_style)

    section("Entorno")
    for key in ["Shell", "Terminal", "CPU"]:
        label = f"{key.ljust(label_padding)}:"
        right_panel.append(label, style=label_style)
        right_panel.append(f" {info[key]}\n", style=value_style)

    section("Recursos")
    for key in ["Memoria", "Almacenamiento", "Tu IP Tor"]:
        label = f"{key.ljust(label_padding)}:"
        right_panel.append(label, style=label_style)
        right_panel.append(f" {info[key]}\n", style=value_style)

    section("Uso de Recursos")
    right_panel.append(f"Memoria       : {color_bar(info['Memoria %'])}\n")
    right_panel.append(f"Almacenamiento: {color_bar(info['Almacenamiento %'])}\n")

    console.print(Columns([left_panel, right_panel], equal=False, expand=True))
    console.print("")
    console.print("")

if __name__ == "__main__":
    main()