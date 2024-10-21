from colorama import init, Fore, Back, Style
import pyfiglet
from tabulate import tabulate

init()

menu_data = [
    ["reload", "RECARGAR BANNER"],
    ["ipinfo", "OSINT"],
    ["phoneinfo", "OSINT"],
    ["urlinfo", "OSINT"],
    ["ia", "IA"],
]

headers = ["Comando", "Descripción"]

print(Style.BRIGHT + Fore.RED + tabulate(menu_data, headers, tablefmt="fancy_grid"), Style.RESET_ALL)
