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
from rich.text import Text
from rich.style import Style
from rich.progress import Spinner
from rich.columns import Columns

console = Console()

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
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%I:%M%p"),
        "os": f"Termux {platform.machine()}",
        "kernel": platform.release(),
        "uptime": get_uptime(),
        "packages": get_packages(),
        "shell": os.path.basename(os.getenv('SHELL', 'bash')),
        "terminal": os.getenv('TERM', 'unknown'),
        "cpu": platform.processor() or "N/A",
        "memory": get_memory(),
        "disk": get_disk(),
        "ip": ip
    }

def display_banner():
    with open("banner.txt", "r") as f:
        banner = f.read().strip()
    with open("banner_color.txt", "r") as f:
        color = f.read().strip()
    with open("banner_background.txt", "r") as f:
        background = f.read().strip().lower()

    f = Figlet(font="cosmic")
    console.print(f.renderText("Stellar"))
    
    spinner = Spinner("dots", text="Presiona [code][Enter][/code] para continuar", style="yellow")
    with console.status(spinner):
        input("")
    
    os.system("clear")
    return banner, color, background

def main():
    banner, color, background = display_banner()
    info = get_system_info()
    
    banner_style = Style(color=color)
    if background in ["si", "sí", "yes"]:
        banner_style += Style(bgcolor="default")
    
    left_panel = Text(banner, style=banner_style)
    
    right_panel = Text()
    right_panel.append("\n")
    right_panel.append(f"Fecha:       {info['date']}\n")
    right_panel.append(f"Hora:        {info['time']}\n")
    right_panel.append(f"OS:          {info['os']}\n")
    right_panel.append(f"Kernel:      {info['kernel']}\n")
    right_panel.append(f"Uptime:      {info['uptime']}\n")
    right_panel.append(f"Packages:    {info['packages']}\n")
    right_panel.append(f"Shell:       {info['shell']}\n")
    right_panel.append(f"Terminal:    {info['terminal']}\n")
    right_panel.append(f"CPU:         {info['cpu']}\n")
    right_panel.append(f"Memory:      {info['memory']}\n")
    right_panel.append(f"Storage:     {info['disk']}\n")
    right_panel.append(f"IP Tor:      {info['ip']}\n")
    
    console.print(Columns([left_panel, right_panel], equal=False, expand=True))
    os.system("cd ~/Stellar && git pull --force &>/dev/null &")

if __name__ == "__main__":
    main()
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
