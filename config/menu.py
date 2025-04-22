from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.markdown import Markdown 
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
    os.system('clear' if os.name == 'posix' else 'cls')

def show_page(page_num):
    page = pages[page_num]
    clear_screen()
    
    # Cabecera con número de página
    header = Text(f"{page_num + 1}/{len(pages)}", justify="right", style="dim")
    console.print(header)
    
    # Contenido principal
    content = Columns([
        Panel.fit(
            Markdown(page["content"]),
            style=page["color"],
            width=40,
            title=f"[bold]{page['title']}[/]",
            title_align="left"
        )
    ], align="center")
    
    console.print(content, justify="center")
    
    # Pie de página con controles
    footer = Text("← Anterior | → Siguiente | Q Salir", justify="center", style="dim")
    console.print("\n" + footer)

def main():
    fd = sys.stdin.fileno()
    old_attr = termios.tcgetattr(fd)
    new_attr = termios.tcgetattr(fd)
    new_attr[3] = new_attr[3] & ~termios.ICANON & ~termios.ECHO
    
    try:
        termios.tcsetattr(fd, termios.TCSANOW, new_attr)
        current_page = 0
        
        while True:
            show_page(current_page)
            char = sys.stdin.read(1)
            
            if char == '\x1b':  # Tecla de escape
                char += sys.stdin.read(2)  # Leer los siguientes 2 caracteres
                
            if char in ('\x1b[D', 'h'):  # Flecha izquierda
                current_page = max(0, current_page - 1)
            elif char in ('\x1b[C', 'l'):  # Flecha derecha
                current_page = min(len(pages) - 1, current_page + 1)
            elif char.lower() == 'q':
                break
                
    except KeyboardInterrupt:
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old_attr)
        clear_screen()
        console.print("[bold green]¡Hasta pronto![/]", justify="center")

if __name__ == "__main__":
    main()