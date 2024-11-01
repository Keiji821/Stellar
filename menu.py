from rich.console import Console
from rich.markdown import Markdown
from colorama import init, Fore, Back, Style

init()

print("")
MARKDOWN = """
# Comandos de Stellar
"""
console = Console()
md = Markdown(MARKDOWN)
console.print(md)
print("")
print(Style.BRIGHT + Fore.GREEN + "  PRINCIPALES", Style.RESET_ALL)
print("   reload", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + "Reinicia su sesion de termux/bash.")

print("")
print(Style.BRIGHT + Fore.GREEN + "  UTILIDADES", Style.RESET_ALL)
print("   ia", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + "Un pequeño servicio de inteligencia artificial.")

print("")
print(Style.BRIGHT + Fore.GREEN + "  OSINT", Style.RESET_ALL)
print("   ipinfo", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + "Obtiene la información de una ip, ya sea IPV4 o IPV6.")
print("   phoneinfo", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + "Obtiene la información de un numero de teléfono.")
print("   urlinfo", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + "Obtiene información de una url o enlace sin necesidad de entrar.")
print("   metadatainfo", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + "Recupera los metadatos de una imagen, archivo o video.")

print("")
print(Style.BRIGHT + Fore.WHITE + Back.GREEN + "CTRL + Z", Style.RESET_ALL + Fore.GREEN + " Esto detendrá cualquier comando o preceso existente.", Style.RESET_ALL)
print("")