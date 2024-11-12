from rich.console import Console
from rich.table import Table
from rich.progress import track
import os
from os import system

console = Console()

os.system("clear")

os.system("pkill tor &>/dev/null &")

os.system("pkill cloudflared &>/dev/null &")

os.system("sleep 5")

os.system("export ALL_PROXY=socks5h://localhost:9050")

os.system("tor &>/dev/null &")

os.system("sleep 5")

os.system("cloudflared --url Stellar &>/dev/null &")

os.system("sleep 5")

os.system("cd")

os.system("cd Stellar")

os.system("bash update.sh &>/dev/null &")

os.system("git pull --force")

os.system("cp ~/Stellar/configuración/.bash_profile ~/.")