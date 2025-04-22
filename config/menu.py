from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
import termios
import sys
import os

console = Console(highlight=False, width=80)

pages = [
    {
        "title": "🚀 Stellar Toolbox",
        "content": """
        [b #8A2BE2]Herramienta multifuncional[/]
        
        [italic #A0A0A0]Navegación:
        ← → : Cambiar páginas
        Q   : Salir del programa[/]""",
        "color": "bold #8A2BE2",
        "icon": "🌌"
    },
    {
        "title": "⚙️ Sistema",
        "content": """
        [bold #20B2AA]• reload     Reiniciar aplicación
        • ui        Modo interfaz gráfica
        • uninstall Desinstalar herramienta
        • update    Actualizar versión
        • bash      Terminal integrado[/]""",
        "color": "#20B2AA",
        "icon": "⚙️"
    },
    {
        "title": "🔧 Utilidades",
        "content": """
        [bold #32CD32]• ia         Asistente conversacional
        • ia-image   Generador de imágenes IA
        • traductor  Traducción en tiempo real
        • myip       Información de red[/]""",
        "color": "#32CD32",
        "icon": "🔧"
    },
    {
        "title": "🕵️ OSINT",
        "content": """
        [bold #DA70D6]• ipinfo      Geolocalización IP
        • urlinfo     Analizador de URL
        • userfinder  Búsqueda en redes
        • phoneinfo   Información telefónica
        • emailsearch Búsqueda de emails
        • discord     Analizador de Discord[/]""",
        "color": "#DA70D6",
        "icon": "🕵️"
    },
    {
        "title": "🔒 Pentesting",
        "content": """
        [bold #FF4500]• ddos       Herramienta de stress
        • portscan   Escaneo de puertos
        • vulnscan   Detección de vulnerabilidades
        • wireshark  Análisis de tráfico[/]""",
        "color": "#FF4500",
        "icon": "🔒"
    }
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_panel(page):
    return Panel(
        Text.from_markup(page["content"].strip()),
        width=60,
        title=f"{page['icon']} {page['title']}",
        style=page["color"],
        border_style="#404040",
        padding=(1, 3),
        subtitle=f"Página {pages.index(page)+1}/{len(pages)}",
        subtitle_style="dim"
    )

def show_page(page_num):
    clear_screen()
    page = pages[page_num]
    
    console.print(
        Columns([create_panel(page)], 
        align="center", 
        expand=True
    ))
    
    footer = Text("← Anterior | → Siguiente | Q Salir", 
                 style="dim #808080", justify="center")
    console.print(f"\n{footer}", justify="center")

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
    finally:
        reset_terminal(original_settings)
        clear_screen()
        console.print("[bold #8A2BE2]¡Hasta pronto! 👋[/]", justify="center")

if __name__ == "__main__":
    main()