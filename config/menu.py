from rich.console import Console
from rich.markdown import Markdown
from os import system
import termios
import sys
import os

console = Console()

fd = sys.stdin.fileno()
attr = termios.tcgetattr(fd)
termios.tcsetattr(fd, termios.TCSANOW, attr)

def page1():
    console.print("[code][bold green]Comandos de Stellar[/code][/bold green]", justify="center")
    console.print("[bold white]Pagina principal[/bold white]", justify="center")
    

while True:
    char = sys.stdin.read(1)
    if char == "1":
        

    elif char == "2":
        

    elif char == "3":
        

    elif char == "4":
        

    elif char == "5":
        

    elif char == "":
        break

termios.tcsetattr(fd, termios.TCSANOW, attr)

if __name__ == "__main__":
    main()