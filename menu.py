from colorama import init, Fore, Back, Style
import pyfiglet
from tabulate import tabulate

init()

# Tabla de comandos principales
comandos_data = [
    headers=("Comandos principales", "Información"),
    ["reload", "Reinicia su sesión de termux."],
    ["Comandos de utilidades", "Información"],
    ["ia", "Chatbot de inteligencia artificial."],
    ["Comandos de osint", "Información"],
    ["ipinfo", "Obtiene la información de una ip."],
    ["phoneinfo", "Obtiene la información de un numero de teléfono."],
    ["urlinfo", "Obtiene información sobre una url."],
    ["metadatainfo", "Recupera los metadatos de una imagen, audio o video."],
]

print(Style.BRIGHT + Fore.CYAN + tabulate(comandos_data, headers=("⭐️ Comandos de Stellar"), tablefmt="fancy_grid"), Style.RESET_ALL)
