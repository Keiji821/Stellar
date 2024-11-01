import datetime
import os
import platform
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

os.system("""

cd

jp2a --color Stellar/imagenes/anti-spiral1.jpg

""")

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
os.system('''

termux-toast -c green -b black "Bienvenido"

''')
