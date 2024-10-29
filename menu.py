from colorama import init, Fore, Back, Style
import pyfiglet
from tabulate import tabulate

init()

principales_data = [
    ["reload", "Reinicia su sesión de termux."],
]

headers = ["Comando", "Descripción"]

# Tabla de comandos principales
print(Style.BRIGHT + Fore.RED + tabulate(principales_data, headers=("Comando", "Información"), tablefmt="fancy_grid"), Style.RESET_ALL)

utilidades_data = [
    ["ia", "Chatbot de inteligencia artificial."],
]

Tabla de comandos de utilidad
print(Style.BRIGHT + Fore.RED + tabulate(utiliades_data, headers=("Comando", "Información"), tablefmt="fancy_grid"), Style.RESET_ALL)

osint_data = [
    ["ipinfo", "Obtiene la información de una ip."],
    ["phoneinfo", "Obtiene la información de un numero de teléfono."],
    ["urlinfo", "Obtiene información sobre una url."],
    ["metadatainfo", "Recupera los metadatos de una imagen, audio o video."],
]

Tabla de comandos osint
print(Style.BRIGHT + Fore.RED + tabulate(osint_data, headers=("Comando", "Información"), tablefmt="fancy_grid"), Style.RESET_ALL)
