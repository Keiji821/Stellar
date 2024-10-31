from colorama import init, Fore, Back, Style

init()

print("")
print(Style.BRIGHT + Fore.WHITE + Back.GREEN + "Comandos de Stellar", Style.RESET_ALL)
print("")
print(Style.BRIGHT + Fore.GREEN + "  PRINCIPALES", Style.RESET_ALL)
print(Style.BRIGHT + "   reload", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + Style.BRIGHT + "Reinicia su sesion de termux/bash.")

print("")
print(Style.BRIGHT + Fore.GREEN + "  UTILIDADES", Style.RESET_ALL)
print(Style.BRIGHT + "   ia", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + Style.BRIGHT + "Un pequeño servicio de inteligencia artificial.")

print(Fore.GREEN + "  OSINT", Style.RESET_ALL)
print(Style.BRIGHT + "   ipinfo", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + Style.BRIGHT + "Obtiene la información de una ip, ya sea IPV4 o IPV6.")
print(Style.BRIGHT + "   phoneinfo", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + Style.BRIGHT + "Obtiene la información de un numero de teléfono.")
print(Style.BRIGHT + "   urlinfo", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + Style.BRIGHT + "Obtiene información de una url o enlace sin necesidad de entrar.")
print(Style.BRIGHT + "   metadatainfo", Style.BRIGHT + Fore.YELLOW + ">", Style.RESET_ALL + Style.BRIGHT + "Recupera los metadatos de una imagen, archivo o video.")