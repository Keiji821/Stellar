cp ~/Stellar/config/.bashrc ~/.

cd
cd .configs_stellar
cd themes

cat <<EOF > banner.py
import datetime
import os
from os import system
import platform
import time
import requests
from pyfiglet import Figlet
from rich.console import Console
from rich.columns import Columns
from rich.markdown import Markdown
from rich.progress import Spinner
from rich.panel import Panel
from rich.text import Text

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
            return f"{hours}h {minutes}m"
    except:
        return "N/A"

def get_packages():
    try:
        return len([name for name in os.listdir('/data/data/com.termux/files/usr/var/lib/dpkg/info') if name.endswith('.list')])
    except:
        return 0

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

with open("banner.txt", "r") as f:
    text_banner = f.read().strip()
with open("banner_color.txt", "r") as f:
    color = f.read().strip()

f = Figlet(font="cosmic")
text = f.renderText("Stellar")
console.print(text)
spinner = Spinner("dots", text="Presiona [code][Enter][/code] para continuar", style="yellow")
with console.status(spinner):
    input("")

os.system("clear")

response = requests.get('https://api.ipapi.is/?ip=')
data = response.json()

if data is not None:
    ip = data.get("ip")
if ip is None:
    ip = "El anonimizador no se ha iniciado"


info_text = Text()
info_text.append(f"{os.getlogin()}@termux\n")
info_text.append(f"[bold green]OS[/bold green]: Termux {platform.machine()}\n")
info_text.append(f"[bold green]Kernel[/bold green]: {platform.release()}\n")
info_text.append(f"Uptime: {get_uptime()}\n")
info_text.append(f"[bold green]Packages[/bold green]: {get_packages()}\n")
info_text.append(f"[bold green]Shell[/bold green]: {os.path.basename(os.getenv('SHELL', 'bash'))}\n")
info_text.append(f"[bold green]Terminal[/bold green]: {os.getenv('TERM', 'unknown')}\n")
info_text.append(f"[bold green]CPU[/bold green]: {platform.processor()}\n")
info_text.append(f"[bold green]Memoria[/bold green]: {get_memory()}\n")
info_text.append(f"[bold green]Almacenamiento[/bold green]: {get_disk()}\n")
info_text.append(f"[bold green]Tu IP TOR[/bold green]: {ip}")

console.print(Columns([f"[code]{text_banner}[/code]", Panel(info_text)], equal=False, expand=True))

console.print("")
console.print("")
console.print("")
os.system("""
cd
cd Stellar
git pull --force &>/dev/null &
cd
""")
EOF

cd

apreexec() {
    printf "${gris}[INFO] ${blanco}Ejecutando comando: $1"
    echo

}

if [ -n "$BASH_VERSION" ]; then
    trap 'preexec "$BASH_COMMAND"' DEBUG
fi