from rich.console import Console
import time
import os
from os import system

console = Console()

try:
    console.print()
    
    main = console.input("[bold green]Elija el tipo de banner a agregar[/bold green] [bold yellow][code]Ascii Art/Texto:[/code][/bold yellow] ")

    if main == "Ascii Art":
        os.system("cd && nano .configs_stellar/themes/banner.txt")

    if main == "Texto":
        console.print("[bold yellow]Establecer banner")
        banner = console.input("[bold green]> ")
        if banner == "":
            banner = "Stellar"
        os.system("""
cd 
cd .configs_stellar/themes
echo {banner} > banner.txt
cd""")
        console.print("")

    if main == "Texto":
        console.print("[bold yellow]Establecer fuente para el banner de texto.")
        banner_font = console.input("[bold green]> ")
        if banner_font == "":
            banner_font = "standard"
        os.system("""
cd 
cd .configs_stellar/themes
echo {banner_font} > banner_font.txt
cd""")
        console.print("")

    console.print("[bold yellow]Establezca el texto personalizado de la input")
    input_text = console.input("[bold green]> ")
    if input_text == "":
        input_text = "By Keiji for you ❤️"
    os.system("""
cd 
cd .configs_stellar/themes
echo {input_text} > input.txt
cd""")
    console.print()

    console.print("[code][bold green]Configuración realizada con éxito, escriba bash para que los cambios surtan efecto", justify="center")
    console.print()

except Exception as e:
    print(f"[code][bold red]Error: {e}")