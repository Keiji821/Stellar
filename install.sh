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


cat > banner.txt << 'EOF'
         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--'
EOF

echo bold green > banner_color.txt
echo No > banner_background.txt
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
