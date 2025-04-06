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
    printf "${gris}[INFO] ${blanco} Configure una contraseña para su termux."
    printf "\n${gris}[INFO] ${blanco}Ingrese su nueva contraseña: "
    read -s password
    printf "\n${gris}[INFO] ${blanco}Repita la contraseña: "
    read -s password_confirm
    printf "\n"

    if [[ "$password" != "$password_confirm" ]]; then
        printf "${amarillo}[WARNING] ${blanco}Las contraseñas no coinciden\n"
        return 1
    fi

    (echo "$password"; echo "$password") | passwd >/dev/null 2>&1

    if [[ $? -eq 0 ]]; then
        printf "${gris}[INFO] ${blanco}Contraseña configurada correctamente\n"
        return 0
    else
        printf "${rojo}[ERROR] ${blanco}Error al configurar la contraseña\n"
        return 1
    fi
}

set_password

cp ~/Stellar/config/.bash_profile ~/.
cp ~/Stellar/config/.bashrc ~/.

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
import time
import requests
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

response = requests.get('https://api.ipapi.is/?ip=')
data = response.json()

if data is not None:
    active = "[bold green]●[/bold green]"
    ip = data.get("ip")
if ip is None:
    ip = "El anonimizador no se ha iniciado"
    active = "[bold red]●[/bold red]"

console.print("[bold green]OS[/bold green]", os_version, justify="center")
console.print("[bold green]Sistema[/bold green]", system_info, justify="center")
console.print("[bold green]Hora[/bold green]", hour_string, justify="center")
console.print("[bold green]Fecha[/bold green]", date_string, justify="center")
console.print(f"[code][{color}]{text_banner}[/code]", justify="center")
console.print("")
console.print(f"[bold green]Tu IP Tor[/bold green] {active} {ip}", justify="center")


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
