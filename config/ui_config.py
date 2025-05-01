from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from  import Table
import os
from os import system

console = Console()


os.system("clear")


banner = console.input("¿Desea configurar el contenido del banner? (y/n): ", style="bold green")
if banner=="y":
    console.print("Presione [code][Enter][/code] para configurar su banner", style="bold green")
    os.system("rm -rf banner.txt")
    os.system("cd && cd Stellar/config/themes && nano banner.txt")

banner_color = console.input("¿Desea configurar el color de su banner? (y/n): ", style="bold green")
if banner_color=="y"
    bcolor = console.input("¿Desea ver los colores disponibles? (y/n): ", style="bold green")
    if bcolor=="y":
        colors = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "bright_black", "bright_red", "bright_green", "bright_yellow", 
    "bright_blue", "bright_magenta", "bright_cyan", "bright_white",
    "dark_red", "dark_green", "dark_yellow", "dark_blue",
    "dark_magenta", "dark_cyan", "grey0", "grey19", "grey30",
    "grey37", "grey46", "grey50", "grey54", "grey58", "grey62",
    "grey66", "grey70", "grey74", "grey78", "grey82", "grey85",
    "grey89", "grey93", "grey100", "orange1", "orange3", "orange4"
]
    for color in colors:
       console.print(f"[{color}]{color}[/{color}]")

color_selection = console.input("Ingrese el color a configurar: ", style="bold green")
os.system(f"echo {color_selection} > banner_color.txt")


banner_background = console.input("¿Desea que su banner tenga un fondo de color? (y/n): ", style="bold green")
if banner_background=="y":
    os.system("echo Sí > banner_background.txt")
    banner_background_color = console.input("¿Desea agregar un color al fondo de su banner? (y/n): ", style="bold green")
    if banner_background_color=="y":
        for color in colors:
            console.print(f"[{color}]{color}[/{color}]")
    banner_background_color_selection = console.input("Ingrese el color a configurar: ", style="bold green")
    os.system(f"echo {banner_background_color_selection} > banner_background_color.txt")



console.print("")
console.print("[code]Configuraciónes aplicadas correctamente[/code]", style="bold green", justify="center")
console.print("""
Escriba el comando "bash" o "login" para aplicar los cambios correctamente""", justify="center")
console.print("")
