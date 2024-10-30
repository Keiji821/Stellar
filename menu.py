from colorama import init, Fore, Back, Style
import pyfiglet
from tabulate import tabulate

init()

# Tabla de comandos principales
principales_data = [
    ["reload", "Reinicia su sesión de termux."],
]

print(Style.BRIGHT + Fore.CYAN + tabulate(principales_data, headers=("Comando principales", "Información"), tablefmt="fancy_grid"), Style.RESET_ALL)

# Tabla de comandos de utilidad
utilidades_data = [
    ["ia", "Chatbot de inteligencia artificial."],
]

print(Style.BRIGHT + Fore.CYAN + tabulate(utilidades_data, headers=("Comando de utilidades", "Información"), tablefmt="fancy_grid"), Style.RESET_ALL)

# Tabla de comandos osint
osint_data = [
    ["ipinfo", "Obtiene la información de una ip."],
    ["phoneinfo", "Obtiene la información de un numero de teléfono."],
    ["urlinfo", "Obtiene información sobre una url."],
    ["metadatainfo", "Recupera los metadatos de una imagen, audio o video."],
]

print(Style.BRIGHT + Fore.CYAN + tabulate(osint_data, headers=("Comandos osint", "Información"), tablefmt="fancy_grid"), Style.RESET_ALL)
