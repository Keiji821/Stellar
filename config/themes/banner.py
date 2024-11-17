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
with open("banner_font.txt", "r") as f:
    font = f.read().strip()

f = Figlet(font="cosmic")
text = f.renderText("Stellar")
console.print(text)
spinner = Spinner("dots", text="Presiona [code][Enter][/code] para continuar", style="yellow")
with console.status(spinner):
    input("")

os.system("clear")

colores = random.choice(["red", "magenta", "yellow", "blue", "cyan"])

response = requests.get('https://ipapi.co//json/')
data = response.json()

if data is not None:
    active = "[bold green]●[/bold green]"
    ip = data.get("network")
    if ip is None:
        ip = "El anonimizador no se ha iniciado"
        active = "[bold red]●[/bold red]"
else:
    active = "[bold red]●[/bold red]"
    ip = "Error de red"

console.print(
f"""[bold green]OS: [/bold green][bold white]{os_version}[/bold white]
[bold green]Sistema: [/bold green][bold white]{system_info}[/bold white]
[bold green]Fecha: [/bold green][bold white]{date_string}[/bold white]
[bold green]Hora: [/bold green][bold white]{hour_string}[/bold white]
[bold green]Tu IP tor/cloudflared: [/bold green][bold white]{active} {ip}[/bold white]""", justify="center")

f = Figlet(font=f"{font}")
banner_text = f.renderText(text_banner)

terminal_width = os.get_terminal_size().columns

centered_banner = "\n".join(
    line.center(terminal_width) for line in banner_text.splitlines()
)

process = subprocess.Popen(['lolcat', '-f'], stdin=subprocess.PIPE)
process.communicate(input=centered_banner.encode())

console.print("[bold red]Stellar V1.0.0[/bold red]", justify="center")

console.print("""
[code][bold green]
Para ver comandos escriba [/bold green] [bold white]menu [/bold white][/code]

[code][bold green]Hecho por [/bold green] [bold white]Keiji821 [/bold white][/code]
""", justify="center")
