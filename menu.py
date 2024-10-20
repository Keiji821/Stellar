from colorama import init, Fore, Back, Style
import pyfiglet
from tabulate import tabulate

init()

menu_data = [
    ["ipinfo", "Osint"],
    ["phoneinfo", "Osint"],
    ["urlinfo", "Osint"],
]

headers = ["Comando", "Descripción"]

print(Fore.BLACK + Back.RED + tabulate(menu_data, headers, tablefmt="fancy_grid"), Style.RESET_ALL)
