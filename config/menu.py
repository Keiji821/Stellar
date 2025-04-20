from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt
from rich.box import HEAVY, ROUNDED
from rich.align import Align
from itertools import cycle
import time
import os

console = Console()

themes = {
    "claro": {
        "primary": "bright_white",
        "secondary": "bright_blue",
        "highlight": "bright_cyan",
        "bg": "white"
    },
    "oscuro": {
        "primary": "white",
        "secondary": "bright_magenta",
        "highlight": "cyan",
        "bg": "black"
    },
    "makoto": {
        "primary": "bright_green",
        "secondary": "bright_blue",
        "highlight": "bright_cyan",
        "bg": "black"
    }
}

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

theme_cycle = cycle(["oscuro", "claro", "makoto"])
current_theme = next(theme_cycle)

def create_table(theme):
    table = Table.grid(padding=(0, 2))
    table.add_column(style=f"bold {themes[theme]['highlight']}", width=24)
    table.add_column(style=themes[theme]['primary'])
    for category, items in menu_data.items():
        table.add_row(
            Panel.fit(f"[bold]{category}[/]", border_style=themes[theme]['secondary'], box=ROUNDED),
            ""
        )
        for cmd, desc in items:
            table.add_row(f"[{themes[theme]['highlight']}]› {cmd}", f"[{themes[theme]['primary']}]{desc}")
        table.add_row("", "")
    return table

def animated_banner(theme):
    text = Text.assemble(
        (f" STELLAR OS ", f"bold {themes[theme]['secondary']}"),
        (" [v2.2.0]", "bold grey50")
    )
    return Panel(Align.center(text), border_style=themes[theme]['secondary'], padding=(1, 4), box=HEAVY)

def loading_animation(theme):
    progress = Progress(
        SpinnerColumn(),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
        transient=True,
    )
    task = progress.add_task("[bold]Cargando interfaz...", total=100)
    with progress:
        for _ in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)

def render_screen(theme):
    layout = Layout()
    layout.split_column(
        Layout(animated_banner(theme), size=5),
        Layout(Panel(create_table(theme), border_style=themes[theme]['secondary'], box=ROUNDED), ratio=2),
        Layout(Panel("[dim]Escribe un comando o CTRL+C para salir[/]", border_style="yellow"), size=3),
    )
    return layout

def run_command(command):
    if command == "clear":
        os.system("clear")
    elif command == "theme":
        global current_theme
        current_theme = next(theme_cycle)
    elif command == "exit":
        console.print("[bold red]Saliendo del sistema...")
        raise KeyboardInterrupt()
    else:
        console.print(f"[bold green]Ejecutando:[/] {command}")
        time.sleep(1)

def main():
    loading_animation(current_theme)
    with Live(render_screen(current_theme), refresh_per_second=10, screen=True) as live:
        while True:
            try:
                live.update(render_screen(current_theme))
                command = Prompt.ask("[bold cyan]› Ingresar comando[/]")
                run_command(command)
            except KeyboardInterrupt:
                console.print("\n[bold magenta]Hasta pronto...")
                break

if __name__ == "__main__":
    main()