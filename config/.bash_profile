cp ~/Stellar/config/.bashrc ~/.

cd
cd .configs_stellar
cd themes

cat <<EOF > banner.py
import datetime
import os
from os import system
import platform
import random
import time
import requests
import subprocess
from pyfiglet import Figlet
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Spinner
from rich.text import Text

console = Console()

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")
hour_string = now.strftime("%I:%M%p")

os_version = os.sys.platform
system_info = platform.machine() + " - " + platform.processor()

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

colores = random.choice(["red", "magenta", "yellow", "blue", "cyan"])

response = requests.get('https://api.ipapi.is/?ip=')
data = response.json()

if data is not None:
    active = "[bold green]●[/bold green]"
    ip = data.get("ip")
if ip is None:
    ip = "El anonimizador no se ha iniciado"
    active = "[bold red]●[/bold red]"

console.print("[bold green]OS[/bold green]", os_version, justify="left")
console.print("[bold green]Sistema[/bold green]", system_info, justify="left")
console.print(f"[code][{color}]{text_banner}[/code]", justify="center")
console.print("Hora", hour_string, justify="left")
console.print("Fecha", date_string, justify="left")

console.print("")
console.print("")
EOF

os.system("cd && cd Stellar && git pull --force &>/dev/null &")
cd

preexec() {
    printf "${gris}[INFO] ${verde}Ejecutando comando: ${blanco}$1"
    echo

}

if [ -n "$BASH_VERSION" ]; then
    trap 'preexec "$BASH_COMMAND"' DEBUG
fi