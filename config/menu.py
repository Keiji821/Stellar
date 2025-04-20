from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.style import Style
from rich.box import ROUNDED, DOUBLE
from rich.live import Live
from rich.layout import Layout
from rich.animation import Animation
import time
import itertools

console = Console(record=True)

menu_data = {
    "SISTEMA": [
        ("reload", "Recarga el banner del sistema"),
        ("clear", "Limpia la terminal completamente"),
        ("bash", "Reinicia la sesión de terminal"),
        ("ui", "Personalizar tema e interfaz gráfica"),
        ("uninstall", "Desinstalar todo el sistema"),
        ("update", "Actualizar desde repositorio GitHub")
    ],
    "UTILIDADES": [
        ("ia", "Asistente de IA con GPT-4"),
        ("ia-image", "Generador de imágenes con DALL-E"),
        ("traductor", "Traductor en tiempo real multidioma"),
        ("myip", "Muestra tu IP pública y geolocalización")
    ],
    "OSINT": [
        ("ipinfo", "Información detallada de direcciones IP"),
        ("phoneinfo", "Búsqueda de números telefónicos"),
        ("urlinfo", "Analizador de URLs y dominios"),
        ("metadatainfo", "Extracción avanzada de metadatos"),
        ("emailsearch", "Búsqueda de correos electrónicos"),
        ("userfinder", "Rastreo de nombres de usuario")
    ],
    "DISCORD": [
        ("userinfo", "Obten información de usuarios"),
        ("serverinfo", "Analiza servidores de Discord"),
        ("searchinvites", "Busca invitaciones públicas"),
        ("inviteinfo", "Analiza enlaces de invitación")
    ],
    "PENTESTING": [
        ("ddos", "Ataque DDOS controlado"),
        ("portscan", "Escaneo avanzado de puertos"),
        ("vulnscan", "Detector de vulnerabilidades")
    ]
}

class TerminalAnimator:
    def __init__(self):
        self.colors = ["bright_cyan", "cyan", "blue", "bright_blue"]
        self.spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])
        self.border_cycle = itertools.cycle(self.colors)
    
    def get_spinner(self):
        return next(self.spinner)
    
    def get_border_color(self):
        return next(self.border_cycle)

def generate_frame(animator):
    border_color = animator.get_border_color()
    spinner = animator.get_spinner()
    
    banner = Panel(
        Text.from_markup(f"[bold {border_color}]╭───────────────────────────────────────╮\n"
                       f"│    [blink]STELLAR OS[/blink] [bright_black](v2.1.0)[/bright_black]    │\n"
                       f"╰───────────────────────────────────────╯"),
        subtitle=f"[bright_black]{spinner} by Keiji821 [/bright_black]",
        border_style=border_color,
        box=ROUNDED
    )
    
    main_table = Table.grid(padding=(0, 3), expand=True)
    main_table.add_column(style=f"bold {border_color}", width=24)
    main_table.add_column(style="bright_white")
    
    for category, commands in menu_data.items():
        main_table.add_row(
            Panel.fit(
                f"[bold]{category}[/]",
                border_style=border_color,
                style=Style(bold=True, blink=(category=="SISTEMA"))
            , "")
        
        for cmd, desc in commands:
            main_table.add_row(
                f"[bold green]› {cmd}[/]",
                f"[bright_white]{desc}[/]"
            )
        main_table.add_row("", "")
    
    content = Panel.fit(
        main_table,
        border_style=border_color,
        padding=(1, 4),
        box=DOUBLE
    )
    
    main_panel = Panel(
        content,
        title=f"[bold {border_color}] STELLAR TERMINAL v2 [/]",
        subtitle="[bright_black]Presiona CTRL+C para salir[/]",
        border_style=border_color,
        box=ROUNDED,
        width=92
    )
    
    help_panel = Panel.fit(
        "[bright_black]TAB:Autocompletar  ↑/↓:Navegar  ENTER:Ejecutar  CTRL+C:Salir[/]",
        border_style="yellow",
        style=Style(bold=True, blink=True)
    )
    
    layout = Layout()
    layout.split_column(
        Layout(banner, name="header", size=7),
        Layout(main_panel, name="main"),
        Layout(help_panel, name="footer", size=3)
    )
    
    return layout

def exit_animation():
    frames = [
        "[bold red]Cerrando Stellar OS...[/]",
        "[bold yellow]Finalizando procesos...[/]",
        "[bold green]Sistema detenido correctamente[/]"
    ]
    for frame in frames:
        console.print(frame)
        time.sleep(0.8)

def display_menu():
    animator = TerminalAnimator()
    try:
        with Live(refresh_per_second=12, screen=True) as live:
            while True:
                live.update(generate_frame(animator))
                time.sleep(0.15)
    except KeyboardInterrupt:
        exit_animation()

if __name__ == "__main__":
    display_menu()