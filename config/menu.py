from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
import termios
import sys
import os

console = Console(highlight=False)

pages = [
    {
        "title": "Portada",
        "content": """
        [bold #DAA520]
          ___  _          _           _       
         / __|| |_   __ _| |_   ___  | |      
         \__ \|  _| / _` |  _| / _ \ | |      
         |___/ \__| \__,_|\__| \___/ |_|      
        [/]                                  
        [bold white]Una herramienta multifuncional[/]
        [italic #808080]Presiona → para comenzar[/]""",
        "color": "#DAA520"
    },
    {
        "title": "Sistema",
        "content": """
        [bold cyan]● reload[/]    - Reiniciar aplicación
        [bold cyan]● ui[/]       - Modo interfaz gráfica
        [bold cyan]● uninstall[/] - Desinstalar Stellar
        [bold cyan]● update[/]    - Actualizar versión
        [bold cyan]● bash[/]     - Terminal integrado""",
        "color": "cyan"
    },
    {
        "title": "Utilidades",
        "content": """
        [bold green]● ia[/]        - Asistente conversacional
        [bold green]● ia-image[/]  - Generador de imágenes IA
        [bold green]● traductor[/] - Traducción en tiempo real
        [bold green]● myip[/]      - Información IP pública""",
        "color": "green"
    },
    {
        "title": "OSINT",
        "content": """
        [bold magenta]● ipinfo[/]     - Geolocalización IP
        [bold magenta]● urlinfo[/]    - Analizar URL
        [bold magenta]● userfinder[/] - Buscar en redes
        [bold magenta]● phoneinfo[/]  - Información numérica
        [bold magenta]● emailsearch[/] - Búsqueda de emails""",
        "color": "magenta"
    },
    {
        "title": "Pentesting",
        "content": """
        [bold red]● ddos[/]      - Herramienta de stress
        [bold red]● portscan[/]  - Escáner de puertos
        [bold red]● vulnscan[/]  - Detectar vulnerabilidades
        [bold red]● wireshark[/] - Análisis de tráfico""",
        "color": "red"
    }
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_centered_panel(content, color, title):
    return Panel.fit(
        Text.from_markup(content.strip()),
        style=color,
        width=40,
        title=f"[bold]{title}[/]",
        title_align="left",
        padding=(1, 2)
    )

def show_page(page_num):
    page = pages[page_num]
    clear_screen()
    
    console.print(
        Text(f"{page_num + 1}/{len(pages)}", 
        justify="right", 
        style="dim")
    )
    
    console.print(
        Columns([get_centered_panel(page["content"], page["color"], page["title"])], 
        align="center"), 
        justify="center"
    )
    
    footer = Text("← Anterior | → Siguiente | Q Salir", justify="center", style="dim")
    console.print(f"\n{footer}")

def setup_terminal():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new)
    return old

def reset_terminal(old_settings):
    fd = sys.stdin.fileno()
    termios.tcsetattr(fd, termios.TCSANOW, old_settings)

def handle_navigation():
    current_page = 0
    while True:
        show_page(current_page)
        key = os.read(sys.stdin.fileno(), 3).decode()
        
        if key in ('\x1b[D', 'h'):
            current_page = max(0, current_page - 1)
        elif key in ('\x1b[C', 'l'):
            current_page = min(len(pages) - 1, current_page + 1)
        elif key.lower() in ('q', '\x03'):
            break

def main():
    original_settings = setup_terminal()
    try:
        handle_navigation()
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/]")
    finally:
        reset_terminal(original_settings)
        clear_screen()
        console.print("[bold green]¡Hasta pronto![/]", justify="center")

if __name__ == "__main__":
    main()