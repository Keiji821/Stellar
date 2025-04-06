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

clear

set_password() {
    while true; do
        printf "${gris}[INFO] ${blanco}Configure una contraseña para su Termux.\n"
        printf "${gris}[INFO] ${blanco}Ingrese su nueva contraseña: "
        read -s password
        printf "\n${gris}[INFO] ${blanco}Repita la contraseña: "
        read -s password_confirm
        printf "\n"

        if [[ -z "$password" ]]; then
            printf "${amarillo}[WARNING] ${blanco}La contraseña no puede estar vacía\n\n"
            continue
        fi

        if [[ "$password" != "$password_confirm" ]]; then
            printf "${amarillo}[WARNING] ${blanco}Las contraseñas no coinciden\n\n"
            continue
        fi

        (echo "$password"; echo "$password") | passwd >/dev/null 2>&1

        if [[ $? -eq 0 ]]; then
            printf "${verde}[SUCCESS] ${blanco}Contraseña configurada correctamente\n"
            break
        else
            printf "${rojo}[ERROR] ${blanco}Error al configurar la contraseña\n\n"
        fi
    done
}

set_password

cp ~/Stellar/config/.bash_profile ~/.
cp ~/Stellar/config/.bashrc ~/.

cd
mkdir .configs_stellar &>/dev/null
cd .configs_stellar
mkdir themes &>/dev/null
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
info_text.append(f"Fecha: {date_string}\n", style="bold cyan")
info_text.append(f"Hora: {hour_string}\n", style="bold cyan")
info_text.append(f"OS: Termux {platform.machine()}\n", style="bold cyan")
info_text.append(f"Kernel: {platform.release()}\n", style="bold cyan")
info_text.append(f"Tiempo de actividad: {get_uptime()}\n", style="bold cyan")
info_text.append(f"Paquetes: {get_packages()}\n", style="bold cyan")
info_text.append(f"Shell: {os.path.basename(os.getenv('SHELL', 'bash'))}\n", style="bold cyan")
info_text.append(f"Terminal: {os.getenv('TERM', 'unknown')}\n", style="bold cyan")
info_text.append(f"CPU: {platform.processor()}\n", style="bold cyan")
info_text.append(f"Memoria: {get_memory()}\n", style="bold cyan")
info_text.append(f"Almacenamiento: {get_disk()}\n", style="bold cyan")
info_text.append(f"Tu IP TOR: {ip}", style="bold cyan")

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

echo Stellar > banner.txt
echo bold green > banner_color.txt
echo Stellar > input.txt
cd

printf "${amarillo}[${verde}+${amarillo}] ${blanco2} Iniciando instalación"
echo
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Actualizando paquetes"
 echo
 apt-get upgrade -y && apt-get update -y
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"

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
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando termux-api"
 echo
 apt-get install -y termux-api
 sleep 5
printf "${verde}＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿${blanco}"
 echo
 printf "${gris}[${verde}+${gris}] ${blanco} Instalando dnsutils"
 echo
 apt-get install -y dnsutils
 sleep 5

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
