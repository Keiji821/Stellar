from rich.console import Console
import time
import os
from os import system

console = Console()

try:
    console.print()
    
    main = console.input("[bold green]Pulse [code][bold yellow]Enter[/bold yellow][/code] para agregar su banner: [/bold green]")

    if main == "":
        os.system("cd && nano .configs_stellar/themes/banner.txt")
        os.system("cd && rm -rf .configs_stellar/themes/banner.txt")

        color_menu = console.input("[bold green]Pulse [code][bold yellow]Enter[/bold yellow][/code] para ver colores disponibles: [bold green]")

        console.print("""[bold green]
> bold green = verde brilloso
> bold red = rojo brilloso
> bold cyan = cyan brilloso
> bold magenta = magenta brilloso
> bold yellow = amarillo brilloso
> bold white = Blanco brilloso
> bold blue = Azul brilloso
[bold green]""")

        color = console.input("[bold green]Elija un color para su banner: [bold green]")
        os.system(f"""
cd 
cd .configs_stellar/themes
echo {color} > banner_color.txt
cd""")

        input_text = console.input("[bold green]Ingrese un texto para la input: [bold green]")
        os.system(f"""
cd 
cd .configs_stellar/themes
echo {input_text} > input.txt
cd""")
    
    console.print("")
    console.print("[code][bold green]Configuración realizada con éxito, escriba bash para que los cambios surtan efecto", justify="center")
    console.print()

except Exception as e:
    print(f"[code][bold red]Error: {e}")