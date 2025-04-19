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
            used = mem.used
            total = mem.total
            percent = mem.percent
            return f"{round(used/(1024**3),1)}GB/{round(total/(1024**3),1)}GB", used, total, percent
        except:
            return "N/A", 0, 0, 0

    def get_disk():
        try:
            disk = psutil.disk_usage('/data/data/com.termux/files/home')
            used = disk.used
            total = disk.total
            percent = disk.percent
            return f"{round(used/(1024**3),1)}GB/{round(total/(1024**3),1)}GB ({disk.percent}%)", used, total, percent
        except:
            return "N/A", 0, 0, 0

    try:
        response = requests.get('https://api.ipapi.is/?ip=', timeout=3)
        ip = response.json().get('ip', 'No disponible')
    except:
        ip = 'No disponible'

    mem_str, mem_used, mem_total, mem_percent = get_memory()
    disk_str, disk_used, disk_total, disk_percent = get_disk()

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
        "Almacenamiento": disk_str,
        "Tu IP Tor": ip,
        "mem_percent": mem_percent,
        "disk_percent": disk_percent
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

def create_colored_bar(percent):
    bar_length = 20
    filled_length = int(bar_length * percent // 100)
    empty_length = bar_length - filled_length
    bar = '█' * filled_length + '░' * empty_length

    if percent < 50:
        color = "green"
    elif percent < 80:
        color = "yellow"
    else:
        color = "red"

    return f"[{color}]{bar}[/] {percent}%"

def main():
    banner, color, background, background_color = display_banner()
    info = get_system_info()

    banner_style = Style(color=color, bold=True) if color else Style(bold=True)
    if background in ["si", "sí", "yes"]:
        banner_style += Style(bgcolor=background_color)

    left_panel = Text(banner, style=banner_style)
    right_panel = Text()
    blue = Style(color="blue", bold=True)
    white = Style(color="white", bold=True)
    magenta = Style(color="magenta", bold=True)
    label_padding = max(len(k) for k in info if not k.endswith('_percent')) + 2

    section_titles = {
        "Usuario": "[ Usuario ]",
        "OS": "[ Sistema ]",
        "Shell": "[ Entorno ]",
        "Memoria": "[ Recursos ]"
    }

    shown_sections = set()

    for key, value in info.items():
        if key in ['mem_percent', 'disk_percent']:
            continue

        section = section_titles.get(key, None)
        if section and section not in shown_sections:
            right_panel.append(f"\n{section}\n", style=magenta)
            shown_sections.add(section)

        label = f"{key.ljust(label_padding)}:"
        right_panel.append(label, style=blue)
        right_panel.append(f" {value}\n", style=white)

    right_panel.append(f"\n[ Uso de Recursos ]\n", style=magenta)
    right_panel.append(f"{'Memoria'.ljust(label_padding)}: {create_colored_bar(info['mem_percent'])}\n")
    right_panel.append(f"{'Almacenamiento'.ljust(label_padding)}: {create_colored_bar(info['disk_percent'])}\n")

    console.print(Columns([left_panel, right_panel], equal=False, expand=True))
    console.print("")
    console.print("")

if __name__ == "__main__":
    main()