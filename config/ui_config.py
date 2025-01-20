import rich.console 
import time
import os
from os import system

console = Console()


console.print("[code][bold green]Establecer banner", justify="center")
banner = input()

console.print("[code][bold green]Establecer fuente para el banner de texto, deje en blanco si no coloco un banner de texto.", justify="center")
banner_font = input()
if banner_font == "":
    banner_font = "standard"

console.print("[code][bold green]Establezca el texto personalizado de la input", justify="center")
input_text = input()

os.system(f"""
cd
cd .configs_stellar
cd themes
echo {banner} > banner.txt
echo {banner_font} > banner_font.txt
echo {input_text} > input.txt
cd
""")