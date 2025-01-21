# Definir colores 

gris="${b}\033[1;30m"
blanco="\033[0m"
blanco2="$b\033[1;37m"
rojo="${b}\033[1;31m"
rojo2="${b}\033[31m"
azul="${b}\033[1;34m"
azul2="${b}\033[34m"
azul_agua="${b}\e[1;36m"
azul_agua2="${b}\e[36m"
verde="${b}\033[1;32m"
verde2="${b}\033[32m"
morado="$b\033[1;35m"
morado2="$b\033[35m"
amarillo="$b\033[1;33m"
amarillo2="$b\033[33m"
cyan="$b\033[38;2;23;147;209m"

# Configurar .bashrc a home

clear

cp ~/Stellar/config/.bash_profile ~/.
cp ~/Stellar/config/.bashrc ~/.

# Configurar archivos necesarios

cd
mkdir .configs_stellar
cd .configs_stellar
mkdir themes
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

response = requests.get('https://api.ipapi.is/?ip=')
data = response.json()

if data is not None:
    active = "[bold green]●[/bold green]"
    ip = data.get("ip")
if ip is None:
    ip = "El anonimizador no se ha iniciado"
    active = "[bold red]●[/bold red]"

console.print(
f"""[bold green]OS: [/bold green][bold white]{os_version}[/bold white]
[bold green]Sistema: [/bold green][bold white]{system_info}[/bold white]
[bold green]Fecha: [/bold green][bold white]{date_string}[/bold white]
[bold green]Hora: [/bold green][bold white]{hour_string}[/bold white]
[bold green]Tu IP tor: [/bold green][bold white]{active} {ip}[/bold white]""", justify="center")
console.print(" ")

if any(char.isalpha() for char in text_banner):
    f = Figlet(font=f"{font}")
    banner_text = f.renderText(text_banner)

if any(char.isalpha() for char in text_banner):
    terminal_width = os.get_terminal_size().columns
    centered_banner = "\n".join(
        line.center(terminal_width) for line in banner_text.splitlines()
)

if any(char.isalpha() for char in text_banner):
    process = subprocess.Popen(['lolcat'], stdin=subprocess.PIPE)
    process.communicate(input=centered_banner.encode())

console.print(text_banner, justify="center")

console.print(" ")
console.print("[underline][bold red]Stellar V1.0.0[/bold red][/underline]", justify="center")

console.print("""
[code][bold green]
Para ver comandos escriba [/bold green] [bold white]menu [/bold white][/code]

[code][bold green]Hecho por [/bold green] [bold white]Keiji821 [/bold white][/code]
""", justify="center")

os.system("""
cd
cd Stellar/config
git pull --force &>/dev/null &
cd
""")
EOF

echo Stellar > banner.txt
echo standard > banner_font.txt
echo Stellar > input.txt
cd

# Actualizar paquetes

printf "${amarillo}[${verde}+${amarillo}] ${blanco2} Iniciando instalación"
echo
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Actualizando paquetes"
 echo
 apt-get upgrade -y && apt-get update -y
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"

# Instalar dependencias bash necesarias

printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando python"
 echo
 apt-get install -y python 
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando tor"
 echo
 apt-get install -y tor
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando cloudflared"
 echo
 apt-get install -y cloudflared 
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando exiftool"
 echo
 apt-get install -y exiftool
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando nmap"
 echo
 apt-get install -y nmap
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando dnsutils"
 echo
 apt-get install -y dnsutils
 sleep 5

# Instalar dependencias python necesarias

echo
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
sleep 1
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install beautifulsoup4
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install bs4
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install pyfiglet
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install phonenumbers
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install psutil
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install PySocks
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install requests
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
echo
pip install rich
pip install "rich[jupyter]"
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
pip install lolcat
echo
clear
printf "${gris}[${verde}+${gris}]${blanco} Instalando paquetes python...$SECONDS\n"
pip install discord
echo
clear
printf "${gris}[${verde}✔${gris}]${blanco} Instalación completada.\n"
bash
reload
