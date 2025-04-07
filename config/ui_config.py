from rich.console import Console
import time
import os
from os import system

console = Console()

try:
    os.system("cd .configs_stellar/themes")
    console.print()
    
    main = console.input("[bold green]Pulse [code][bold yellow]Enter[/bold yellow][/code] para agregar su banner: [/bold green]")

    if main == "":
        os.system("cd && rm -rf .configs_stellar/themes/banner.txt")
        os.system("cd && nano .configs_stellar/themes/banner.txt")

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
        os.system(f"echo {color} > banner_color.txt")

        input_background = console.input("[bold green]Desea que el banner tenga fondo? No/Sí: [bold green]")
        os.system(f"echo {input_background} > banner_background.txt") 

        with open("banner_background.txt", "r") as f:
            background = f.read().strip().lower()

        if background =="Sí":
            input_background_color_list = console.print("[bold green]Pulse [code][bold yellow]Enter[/bold yellow][/code] para ver colores disponibles para el fondo de su banner: [bold green]")
            console.print("""
[bold underline]Colores estándar:[/bold underline]
[black]black[/] [red]red[/] [green]green[/] [yellow]yellow[/] [blue]blue[/] [magenta]magenta[/] [cyan]cyan[/] [white]white[/]

[bold underline]Colores brillantes:[/bold underline]
[bright_black]bright_black[/] [bright_red]bright_red[/] [bright_green]bright_green[/] [bright_yellow]bright_yellow[/]
[bright_blue]bright_blue[/] [bright_magenta]bright_magenta[/] [bright_cyan]bright_cyan[/] [bright_white]bright_white[/]

[bold underline]Grises (greys):[/bold underline]
[grey0]grey0[/] [grey11]grey11[/] [grey30]grey30[/] [grey50]grey50[/] [grey70]grey70[/] [grey90]grey90[/] [grey93]grey93[/] [grey100]grey100[/]

[bold underline]Colores extendidos:[/bold underline]
[dark_red]dark_red[/] [firebrick]firebrick[/] [indian_red]indian_red[/] [light_salmon]light_salmon[/]
[dark_green]dark_green[/] [chartreuse]chartreuse[/] [sea_green]sea_green[/] [pale_green]pale_green[/]
[dark_blue]dark_blue[/] [navy_blue]navy_blue[/] [blue3]blue3[/] [royal_blue]royal_blue[/]
[sky_blue]sky_blue[/] [deep_sky_blue1]deep_sky_blue1[/] [dodger_blue2]dodger_blue2[/] [steel_blue]steel_blue[/]
[dark_cyan]dark_cyan[/] [turquoise]turquoise[/] [medium_turquoise]medium_turquoise[/] [aquamarine1]aquamarine1[/]
[purple]purple[/] [medium_purple]medium_purple[/] [dark_magenta]dark_magenta[/] [orchid]orchid[/]
[orange1]orange1[/] [gold1]gold1[/] [khaki1]khaki1[/] [light_goldenrod1]light_goldenrod1[/]
[slate_gray1]slate_gray1[/] [dark_slate_gray]dark_slate_gray[/]
""")
        background_color_set = console.input("[bold green]Seleccione un color: [bold green]")
        os.system(f"echo {background_color_set} > banner_background_color.txt") 
    
    console.print("")
    console.print("[code][bold green]Configuración realizada con éxito, escriba bash para que los cambios surtan efecto", justify="center")
    console.print()
    os.system("cd")

except Exception as e:
    print(f"[code][bold red]Error: {e}")