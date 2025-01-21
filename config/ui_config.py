from rich.console import Console
import time
import os
from os import system

console = Console()

try:
    console.print()
    
    main = console.input("[bold green]Elija el tipo de banner a agregar,[/bold green] [bold yellow][code]Ascii Art/Texto: ")

    if main == "Ascii Art":
        os.system("nano .configs_stellar/themes/banner.txt")


    if main == "Texto":
        console.print("[bold yellow]Establecer banner")
        banner = console.input("[bold green]> ")
        if banner == "":
            banner = "Stellar"
        console.print("")

    if main == "Texto":
        console.print("[bold yellow]Establecer fuente para el banner de texto.")
        banner_font = console.input("[bold green]> ")
        if banner_font == "":
            banner_font = "standard"
        console.print("")


    console.print("[bold yellow]Establezca el texto personalizado de la input")
    input_text = console.input("[bold green]> ")
    if input_text == "":
        input_text = "Stellar"
    console.print()


    console.print("[code][bold green]Configuración realizada con éxito, escriba bash para que los cambios surtan efecto", justify="center")
    console.print()

except Exception as e:
    print(f"[code][bold red]Error: {e}")
time.sleep(2)
os.system(f"""
cd
cd .configs_stellar
cd themes
echo {banner} > banner.txt
echo {banner_font} > banner_font.txt
echo {input_text} > input.txt
cd
""")