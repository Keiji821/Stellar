from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt
from rich.align import Align
from rich.box import HEAVY, ROUNDED
from itertools import cycle
import time
import os

console = Console()

themes = {
    "claro": {
        "primary": "bright_white",
        "secondary": "sky_blue1",
        "highlight": "bright_cyan",
        "bg": "grey93"
    },
    "oscuro": {
        "primary": "white",
        "secondary": "dark_violet",
        "highlight": "magenta",
        "bg": "grey11"
    }
}

menu_data = {
    "UTILIDADES": [
        ("ia", "Asistente de IA con GPT-4"),
        ("traductor", "Traductor en tiempo real"),
    ],
    "OSINT": [
        ("ipinfo", "Información IP"),
        ("emailsearch", "Buscar correos"),
    ],
    "SISTEMA": [
        ("clear", "Limpiar pantalla"),
        ("theme", "Cambiar tema"),
        ("exit", "Salir del sistema"),
    ]
}

theme_cycle = cycle(["oscuro", "claro"])
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