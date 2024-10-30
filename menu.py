from colorama import init, Fore, Back, Style
import pyfiglet
from tabulate import tabulate

init()

# Tabla de comandos principales
comandos_data = [
    ["reload", "Reinicia su sesión de termux."],
    ["ia", "Chatbot de inteligencia artificial."],
    ["ipinfo", "Obtiene la información de una ip."],
    ["phoneinfo", "Obtiene la información de un numero de teléfono."],
    ["urlinfo", "Obtiene información sobre una url."],
    ["metadatainfo", "Recupera los metadatos de una imagen, audio o video."],
]

print(Style.BRIGHT + Back.WHITE + Fore.BLACK + tabulate(comandos_data, headers=("⭐️ Comandos de Stellar", "Descripción"), tablefmt="fancy_grid"), Fore.RESET + Back.RESET)
