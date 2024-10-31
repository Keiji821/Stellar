from colorama import init, Fore, Back, Style

init()

print("")
print(Fore.WHITE + Back.GREEN + "Comandos de Stellar", Style.RESET_ALL)
print("")
print(Fore.GREEN + "  PRINCIPALES", Style.RESET_ALL)
print("   reload", Fore.YELLOW + ">", Style.RESET_ALL + "Reinicia su sesion de termux/bash.")

print("")
print(Fore.GREEN + "  UTILIDADES", Style.RESET_ALL)
print("   ia", Fore.YELLOW + ">", Style.RESET_ALL + "Un pequeño servicio de inteligencia artificial.")

print(Fore.GREEN + "  OSINT", Style.RESET_ALL)
print("   ipinfo", Fore.YELLOW + ">", Style.RESET_ALL + "Obtiene la información de una ip, ya sea IPV4 o IPV6.")
print("   phoneinfo", Fore.YELLOW + ">", Style.RESET_ALL + "Obtiene la información de un numero de teléfono.")
print("   urlinfo", Fore.YELLOW + ">", Style.RESET_ALL + "Obtiene información de una url o enlace sin necesidad de entrar.")
print("   metadatainfo", Fore.YELLOW + ">", Style.RESET_ALL + "Recupera los metadatos de una imagen, archivo o video.")