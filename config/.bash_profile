cp ~/Stellar/config/.bashrc ~/.

cd
cd .configs_stellar
cd themes

cat <<EOF > banner.py
import datetime
import os
import platform
import time
import requests
import psutil
from pyfiglet import Figlet
from rich.console import Console
from rich.columns import Columns
from rich.text import Text
from rich.style import Style
from rich.progress import Spinner

console = Console()

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")
hour_string = now.strftime("%I:%M%p")

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            hours = int(uptime_seconds // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            return f"[white]{hours}h {int(minutes)}m[/white]"
    except:
        return "[white]N/A[/white]"

def get_packages():
    try:
        count = len([name for name in os.listdir('/data/data/com.termux/files/usr/var/lib/dpkg/info') if name.endswith('.list')])
        return f"[white]{count}[/white]"
    except:
        return "[white]N/A[/white]"

def get_memory():
    try:
        mem = psutil.virtual_memory()
        return f"[white]{round(mem.used/(1024**3),1)}GB/{round(mem.total/(1024**3),1)}GB[/white]"
    except:
        return "[white]N/A[/white]"

def get_disk():
    try:
        disk = psutil.disk_usage('/data/data/com.termux/files/home')
        return f"[white]{round(disk.used/(1024**3),1)}GB/{round(disk.total/(1024**3),1)}GB ({disk.percent}%)[/white]"
    except:
        return "[white]N/A[/white]"

with open("banner.txt", "r") as f:
    banner = f.read().strip()
with open("banner_color.txt", "r") as f:
    color = f.read().strip()
with open("banner_background.txt", "r") as f:
    background = f.read().strip().lower()

f = Figlet(font="cosmic")
text = f.renderText("Stellar")
console.print(text)

spinner = Spinner("dots", text="Presiona [code][Enter][/code] para continuar", style="yellow")
with console.status(spinner):
    input("")

os.system("clear")

response = requests.get('https://api.ipapi.is/?ip=')
data = response.json()
ip = data.get("ip", "El anonimizador no se ha iniciado")

info_text = Text()
info_text.append(f"Fecha: [white]{date_string}[/white]\n", style="bold cyan")
info_text.append(f"Hora: [white]{hour_string}[/white]\n", style="bold cyan")
info_text.append(f"OS: [white]Termux {platform.machine()}[/white]\n", style="bold cyan")
info_text.append(f"Kernel: [white]{platform.release()}[/white]\n", style="bold cyan")
info_text.append(f"Uptime: {get_uptime()}\n", style="bold cyan")
info_text.append(f"Packages: {get_packages()}\n", style="bold cyan")
info_text.append(f"Shell: [white]{os.path.basename(os.getenv('SHELL', 'bash'))}[/white]\n", style="bold cyan")
info_text.append(f"Terminal: [white]{os.getenv('TERM', 'unknown')}[/white]\n", style="bold cyan")
info_text.append(f"CPU: [white]{platform.processor()}[/white]\n", style="bold cyan")
info_text.append(f"Memory: {get_memory()}\n", style="bold cyan")
info_text.append(f"Storage: {get_disk()}\n", style="bold cyan")
info_text.append(f"Tu IP Tor: [white]{ip}[/white]\n", style="bold cyan")

color_banner = Text(banner, style=color)
if background in ["si", "sí"]:
    color_banner = Text(banner, style=Style(color=color, bgcolor="default"))

console.print(Columns([color_banner, info_text], equal=False, expand=True))

os.system("cd ~/Stellar && git pull --force &>/dev/null &")
EOF

cd

preexec() {
    printf "${gris}[INFO] ${blanco}Ejecutando comando: $1"
    echo

}

if [ -n "$BASH_VERSION" ]; then
    trap 'preexec "$BASH_COMMAND"' DEBUG
fi