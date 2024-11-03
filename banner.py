import datetime
import os
import platform
import requests
import random
from rich.console import Console
from rich.markdown import Markdown
from colorama import init, Fore, Back, Style

init()

os_version = os.sys.platform

system_info = platform.machine() + " - " + platform.processor()

# Mostrar fecha y hora

now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")
hour_string = now.strftime("%I:%M%p")

# Definir banners

imagen1 = """https://st5.depositphotos.com/81867662/67161/i/450/depositphotos_671612542-stock-photo-vector-illustration-woman-backpack.jpg"""

response = requests.get('https://api.waifu.im/search?included_tags=waifu')
data = response.json()

imágenes = random.choice([imagen1, data.get("url")])

os.system(f"jp2a --color {imágenes}")

print("")
MARKDOWN = """
# Stellar V1.0
"""
console = Console()
md = Markdown(MARKDOWN)
console.print(md)
print(Style.BRIGHT + Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "]" + Fore.RED + " Para ver comandos utilice: menu", Style.RESET_ALL)
print(Style.BRIGHT + Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "]" + Fore.RED + " Hora actual: " + hour_string + " │ Fecha: " + date_string + Style.RESET_ALL)
print("")
