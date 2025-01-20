import rich.console 
import time
import os
from os import system

console = Console()


console.print("[code][bold green]Establecer banner", s)
banner = input()
console.print("[code][bold green]Establecer fuente para el banner de texto, deje en blanco si no coloco un banner de texto.")






os.system(f"""
cd
cd .configs_stellar
cd themes
echo {banner} > banner.txt
""")