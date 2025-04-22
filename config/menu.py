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

def main():
    console.print("[code][bold green]Comandos de Stellar[/code][/bold green]", justify="center")
    console.print("[bold white]Pagina principal[/bold white]", justify="center")
    
def page1():
    console.print("[code][bold cyan]Sistema[/code][/bold cyan]")

def page2():
    console.print("[code][bold cyan]Utilidades[/code][/bold cyan]")

def page3():
    console.print("[code][bold cyan]Osint[/code][/bold cyan]")

def page4():
    console.print("[code][bold cyan]Osint - Discod[/code][/bold cyan]")

def page5():
    console.print("[code][bold cyan]Pentesting[/code][/bold cyan]")


while True:
    char = sys.stdin.read(1)
    if char == "1":
        page1()
    elif char == "2":
        page2()
    elif char == "3": 
        page3()       
    elif char == "4":  
        page4()     
    elif char == "5":  
        page5()        
    elif char == "x":
        break

termios.tcsetattr(fd, termios.TCSANOW, attr)

if __name__ == "__main__":
    main()