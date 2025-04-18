import datetime
import os
import platform
import time
import requests
import psutil
from rich.console import Console
from rich.text import Text
from rich.style import Style
from rich.progress import Spinner
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
            return f"{round(mem.used/(1024**3),1)}GB/{round(mem.total/(1024**3),1)}GB"
        except:
            return "N/A"

    def get_disk():
        try:
            disk = psutil.disk_usage('/data/data/com.termux/files/home')
            return f"{round(disk.used/(1024**3),1)}GB/{round(disk.total/(1024**3),1)}GB ({disk.percent}%)"
        except:
            return "N/A"

    try:
        response = requests.get('https://api.ipapi.is/?ip=', timeout=3)
        ip = response.json().get('ip', 'No disponible')
    except:
        ip = 'No disponible'
        
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
        "Memoria": get_memory(),
        "Almacenamiento": get_disk(),
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

def main():
    banner, color, background, background_color = display_banner()
    info = get_system_info()

    banner_style = Style(color=color, bold=True) if color else Style(bold=True)
    if background in ["si", "sí", "yes"]:
        banner_style += Style(bgcolor=background_color)

    left_panel = Text(banner, style=banner_style)
    right_panel = Text("\n", style="bold")
    blue = Style(color="blue", bold=True)

    label_padding = max(len(k) for k in info) + 1

    for key, value in info.items():
        label = f"{key.ljust(label_padding)}:"
        right_panel.append(label, style=blue)
        right_panel.append(f" {value}\n")

    console.print(Columns([left_panel, right_panel], equal=False, expand=True))
    console.print("")
    console.print("")

if __name__ == "__main__":
    main()
