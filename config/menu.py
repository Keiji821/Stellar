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

console = Console(record=True)

color_palette = ["#6e7f80", "#304451", "#708090", "#5d7261", "#536878"]

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
        ("ddos", "Ataque DDOS controlado")
    ]
}

class TerminalAnimator:
    def __init__(self):
        self.colors = itertools.cycle(color_palette)
        self.spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])

    def get_spinner(self):
        return next(self.spinner)

    def get_color(self):
        return next(self.colors)

def generate_frame(animator):
    color = animator.get_color()
    spinner = animator.get_spinner()

    banner_text = Text.from_markup(
        f"[bold {color}]╭──────────────────────────────────────────╮\n"
        f"│            [blink]STELLAR OS[/blink] [#999999](v2.1.0)            │\n"
        f"╰──────────────────────────────────────────╯"
    )

    banner_panel = Panel(
        banner_text,
        border_style=color,
        box=ROUNDED,
        subtitle=f"[#888888]{spinner} by Keiji821[/#888888]",
        width=60,
        padding=(0, 1),
    )

    table = Table.grid(padding=(0, 2), expand=True)
    table.add_column(style=f"bold {color}", width=24)
    table.add_column(style="white")

    for category, commands in menu_data.items():
        table.add_row(
            Panel.fit(
                f"[bold]{category}[/]",
                border_style=color,
                style=Style(bold=True, blink=(category == "SISTEMA")),
                box=ROUNDED,
            ),
            ""
        )
        for cmd, desc in commands:
            table.add_row(
                f"[bold green]› {cmd}[/]",
                f"[white]{desc}[/]"
            )
        table.add_row("", "")

    content = Panel.fit(
        table,
        border_style=color,
        padding=(1, 4),
        box=DOUBLE
    )

    main_panel = Panel(
        content,
        title=f"[bold {color}] STELLAR TERMINAL v2 [/]",
        subtitle="[bright_black]Presiona CTRL+C para salir[/]",
        border_style=color,
        box=ROUNDED,
        width=92
    )

    footer_panel = Panel.fit(
        "[bright_black]TAB:Autocompletar  ↑/↓:Navegar  ENTER:Ejecutar  CTRL+C:Salir[/]",
        border_style="yellow",
        style=Style(bold=True, blink=True)
    )

    layout = Layout()
    layout.split_column(
        Layout(banner_panel, name="header", size=7),
        Layout(main_panel, name="main"),
        Layout(footer_panel, name="footer", size=3)
    )

    return layout

def exit_animation():
    for frame in [
        "[bold red]Cerrando Stellar OS...[/]",
        "[bold yellow]Finalizando procesos...[/]",
        "[bold green]Sistema detenido correctamente[/]"
    ]:
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