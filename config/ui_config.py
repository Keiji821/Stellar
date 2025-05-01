from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import os
from os import system

console = Console()


os.system("clear")


def configbanner():
    banner = console.input("¿Desea configurar el contenido del banner? (Sí/No): ", style="bold green")
    if banner=="Sí":
        os.system("rm -rf banner.txt")
        os.system("cd && cd Stellar/config/themes && nano banner.txt")