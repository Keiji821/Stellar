from rich.console import Console
import time
import os
from os import system

console = Console()

try:
    console.print("[code][bold yellow]Establecer banner")
    banner = console.input()
    if banner == "":
        banner = "Stellar"
    time.sleep(5)
    console.print("")
    console.print("[code][bold yellow]Establecer fuente para el banner de texto, deje en blanco si no coloco un banner de texto.")
    banner_font = console.input()
    if banner_font == "":
        banner_font = "standard"
    time.sleep(5)
    console.print("")   
    console.print("[code][bold yellow]Establezca el texto personalizado de la input")
    input_text = console.input()
    if input_text == "":
        input_text = "Stellar"
    time.sleep(5)

    console.print("[code][bold green]Configuración realizada con éxito, escriba bash para que los cambios surtan efecto", justify="center")
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