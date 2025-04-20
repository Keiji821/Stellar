from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.style import Style
from rich.box import ROUNDED, DOUBLE
from rich.live import Live
from rich.layout import Layout
import time
import itertools

console = Console()

menu_data = {
    "SISTEMA": [
        ("reload", "Recarga el banner"),
        ("clear", "Limpia la pantalla"),
        ("bash", "Reinicia la sesión"),
        ("ui", "Personalizar temas e interfaz"),
        ("uninstall", "Desinstala todo el sistema"),
        ("update", "Actualiza desde el repositorio de GitHub")
    ],
    "UTILIDADES": [
        ("ia", "Asistente IA con API integrada"),
        ("ia-image", "Generación de imágenes con IA"),
        ("traductor", "Traducción en tiempo real"),
        ("myip", "Muestra tu IP real e información completa")
    ],
    "OSINT": [
        ("ipinfo", "Análisis detallado de IP"),
        ("phoneinfo", "Info de números telefónicos"),
        ("urlinfo", "Escaneo de URLs y dominios"),
        ("metadatainfo", "Extracción de metadatos"),
        ("emailsearch", "Búsqueda de correos electrónicos"),
        ("userfinder", "Búsqueda de nombres de usuario")
    ],
    "OSINT - DISCORD": [
        ("userinfo", "Info sobre un ID de usuario"),
        ("serverinfo", "Info sobre un servidor"),
        ("searchinvites", "Busca invitaciones por palabras clave"),
        ("inviteinfo", "Info sobre enlaces de invitación")
    ],
    "PENTESTING": [
        ("ddos", "Ataque DDOS a una URL"),
        ("portscan", "Escaneo de puertos avanzado"),
        ("vulnscan", "Escaneo de vulnerabilidades")
    ],
    "ATAJOS": [
        ("CTRL+Z", "Detención segura de procesos"),
        ("CTRL+C", "Terminación forzada/Salir"),
        ("TAB", "Autocompletado de comandos")
    ]
}

class AnimatedBorder:
    def __init__(self):
        self.colors = ["bright_cyan", "cyan", "dark_cyan", "cyan", "bright_cyan"]
        self.cycle = itertools.cycle(self.colors)
    
    @property
    def current(self):
        return next(self.cycle)

def generate_layout(animated_border):
    # Banner animado
    banner_text = Text.from_markup(
        f"[{animated_border.current}]╭───────────────────────────────────────╮\n"
        f"│    [blink bold bright_white]STELLAR OS[/blink bold bright_white] [bright_black](v1.0.0)[/bright_black]    │\n"
        f"╰───────────────────────────────────────╯[/{animated_border.current}]"
    )
    
    banner = Panel(
        banner_text,
        subtitle="[bright_black]by Keiji821[/]",
        border_style=animated_border.current,
        style=Style(bold=True),
        box=ROUNDED
    )
    
    # Tabla principal con animación
    main_table = Table.grid(padding=(0, 3), expand=True)
    main_table.add_column(style="bold cyan", width=22)
    main_table.add_column(style="bright_white")
    
    for category, commands in menu_data.items():
        category_style = Style(color=animated_border.current, bold=True, blink=(category == "SISTEMA"))
        main_table.add_row(
            Panel.fit(
                f"[bold]{category}[/]",
                border_style=animated_border.current,
                style=category_style
            ),
            ""
        )
        
        for cmd, desc in commands:
            main_table.add_row(
                f"[bold green]› {cmd}[/]",
                f"[bright_white]{desc}[/]"
            )
        main_table.add_row("", "")
    
    # Panel de contenido con animación
    content = Panel.fit(
        main_table,
        border_style=animated_border.current,
        padding=(1, 4),
        box=DOUBLE
    )
    
    # Panel principal compuesto
    main_panel = Panel(
        content,
        title=f"[{animated_border.current}] STELLAR TERMINAL INTERFACE [/]",
        subtitle="[bright_black]Presiona CTRL+C para salir[/]",
        border_style=animated_border.current,
        style=Style(bold=True),
        box=ROUNDED,
        width=90
    )
    
    # Panel de ayuda animado
    help_panel = Panel.fit(
        "[bright_black]TAB:Autocompletado  ↑/↓:Navegar  ENTER:Ejecutar  CTRL+C:Salir[/]",
        border_style=Style(color="yellow", blink=True),
        style=Style(bold=True)
    )
    
    return banner, main_panel, help_panel

def display_menu():
    animated_border = AnimatedBorder()
    
    try:
        with Live(refresh_per_second=10, screen=True) as live:
            while True:
                banner, main_panel, help_panel = generate_layout(animated_border)
                
                layout = Layout()
                layout.split_column(
                    Layout(name="top", size=7),
                    Layout(name="main"),
                    Layout(name="bottom", size=3)
                )
                
                layout["top"].update(banner)
                layout["main"].update(main_panel)
                layout["bottom"].update(help_panel)
                
                live.update(layout)
                time.sleep(0.2)
                
    except KeyboardInterrupt:
        console.print("\n[bold red]Cerrando Stellar OS...[/]")
        for i in range(3, 0, -1):
            console.print(f"[bright_black]Saliendo en {i}...[/]")
            time.sleep(1)

if __name__ == "__main__":
    display_menu()