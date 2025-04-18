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

cp ~/Stellar/config/.bash_profile ~/.
cp ~/Stellar/config/.bashrc ~/.

cd
mkdir .configs_stellar &>/dev/null
cd .configs_stellar
mkdir themes &>/dev/null
mkdir system &>/dev/null
cd themes

cat <<EOF > banner.py
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

with open("user.txt", "r") as f:
    user = f.read().strip().lower()

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
EOF


cat > banner.txt << 'EOF'
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠴⠒⠒⠒⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠁⠀⠀⣠⠖⠛⠛⠲⢤⠀⠀⠀⣰⠚⠛⢷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⣸⠃⠀⠀⢀⣀⠈⢧⣠⣤⣯⢠⣤⠘⣆⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⡇⠀⠀⠀⠻⠟⠠⣏⣀⣀⣨⡇⠉⢀⣿⠀⠀⠀
⠀⠀⠀⠀⢀⡟⠀⠀⠹⡄⠀⠀⠀⠀⠀⠉⠑⠚⠉⠀⣠⡞⢿⠀⠀⠀
⠀⠀⠀⢀⡼⠁⠀⠀⠀⠙⠳⢤⡄⠀⠀⠀⠀⠀⠀⠀⠁⠙⢦⠳⣄⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠤⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠙⡆
⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⡇
⠀⠀⣏⠀⠀⠀⠀⠲⣄⡀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⢸⠀⢀⡼⠁
⢀⡴⢿⠀⠀⠀⠀⠀⢸⠟⢦⡀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠘⠗⣿⠁⠀
⠸⣦⡘⣦⠀⠀⠀⠀⣸⣄⠀⡉⠓⠚⠀⠀⠀⠀⠀⠀⠀⠀⡴⢹⣦⡀
⠀⠀⠉⠛⠳⢤⣴⠾⠁⠈⠟⠉⣇⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⣠⠞⠁
⠀⠀⠀⠀⠀⠀⠙⢧⣀⠀⠀⣠⠏⠀⠀⢀⣀⣠⠴⠛⠓⠚⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠋⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢤⠀⠉⠁⠀⠠⠀⣐⠑⠬⢠⠀⠁⠀⠀⠂⠄⠄⡤⠀⡀⠀⠀
EOF

echo bold green > banner_color.txt
echo No > banner_background.txt
echo bright_white > banner_background_color.txt



user_config () {
read -p "Configure su nombre de usuario: " usuario

echo $usuario > user.txt
}

user_config()


cd

printf "${amarillo}[${verde}+${amarillo}]${blanco} Iniciando instalación\n"

apt-get update -y && apt-get upgrade -y &>/dev/null &

apt install python &>/dev/null &

apt install tor &>/dev/null &

apt install cloudflared &>/dev/null &

apt install exiftool &>/dev/null &

apt install nmap &>/dev/null &

apt install termux-api &>/dev/null &

apt install dnsutils &>/dev/null &

pip install beautifulsoup4 &>/dev/null &

pip install bs4 &>/dev/null &

pip install pyfiglet &>/dev/null &

pip install phonenumbers &>/dev/null &

pip install psutil &>/dev/null &

pip install PySocks &>/dev/null &

pip install requests &>/dev/null &

pip install rich &>/dev/null &

pip install "rich[jupyter]" &>/dev/null &

pip install lolcat &>/dev/null &

pip install discord &>/dev/null &