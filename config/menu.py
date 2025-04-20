import sys
import termios
import tty
import select
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.box import ROUNDED, DOUBLE
from rich.align import Align
from rich.style import Style
from itertools import cycle
import time

class StellarOS:
    def __init__(self):
        self.console = Console(style=Style(bgcolor="black"))
        self.themes = {
            "neon": {
                "primary": "bright_magenta",
                "secondary": "bright_cyan",
                "highlight": "bright_yellow",
                "bg": "#0a0a1a"
            },
            "cyber": {
                "primary": "bright_green",
                "secondary": "bright_blue",
                "highlight": "bright_red",
                "bg": "#0a1a0a"
            },
            "matrix": {
                "primary": "bright_green",
                "secondary": "green",
                "highlight": "bright_white",
                "bg": "black"
            }
        }

        self.menu_data = {
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

        self.theme_cycle = cycle(self.themes.keys())
        self.current_theme = next(self.theme_cycle)
        self.version = "v2.3.0"

    def create_table(self):
        table = Table.grid(padding=(0, 2))
        table.add_column(style=f"bold {self.themes[self.current_theme]['highlight']}", width=24)
        table.add_column(style=self.themes[self.current_theme]['primary'])

        for category, items in self.menu_data.items():
            table.add_row(
                Panel.fit(f"[bold]{category}[/]", 
                         border_style=self.themes[self.current_theme]['secondary'], 
                         box=ROUNDED),
                ""
            )
            for cmd, desc in items:
                table.add_row(
                    f"[{self.themes[self.current_theme]['highlight']}]› {cmd}", 
                    f"[{self.themes[self.current_theme]['primary']}]{desc}"
                )
            table.add_row("", "")
        return table

    def animated_banner(self):
        text = Text.assemble(
            (f" STELLAR OS ", f"bold {self.themes[self.current_theme]['secondary']} blink"),
            (f" [{self.version}]", "bold grey50")
        )
        return Panel(
            Align.center(text), 
            border_style=self.themes[self.current_theme]['secondary'], 
            padding=(1, 4), 
            box=DOUBLE,
            style=Style(bgcolor=self.themes[self.current_theme]['bg'])
        )

    def loading_animation(self):
        colors = ["rgb(0,255,255)", "rgb(0,200,255)", "rgb(0,150,255)", "rgb(0,100,255)", "rgb(50,0,255)", "rgb(100,0,255)"]
        styles = cycle(colors)
        style = next(styles)

        progress = Progress(
            SpinnerColumn(style=style),
            BarColumn(bar_width=None, style=style),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%", style=style),
            console=self.console,
            transient=True,
        )
        task = progress.add_task(f"[{style}]INICIANDO INTERFAZ...", total=100)
        with progress:
            for _ in range(100):
                time.sleep(0.02)
                progress.update(task, advance=1)

    def render_screen(self):
        layout = Layout()
        layout.split_column(
            Layout(self.animated_banner(), size=5),
            Layout(
                Panel(
                    self.create_table(), 
                    border_style=self.themes[self.current_theme]['secondary'], 
                    box=ROUNDED, 
                    padding=(1, 0),
                    style=Style(bgcolor=self.themes[self.current_theme]['bg'])
                ), 
                ratio=2
            ),
            Layout(
                Panel(
                    f"[blink bold {self.themes[self.current_theme]['highlight']}]Presiona 'q' para salir | 't' para cambiar tema[/]", 
                    border_style=self.themes[self.current_theme]['secondary'],
                    style=Style(bgcolor=self.themes[self.current_theme]['bg'])
                ), 
                size=3
            ),
        )
        return layout

    def get_key_non_blocking(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            rlist, _, _ = select.select([fd], [], [], 0.1)
            if rlist:
                return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None

    def main(self):
        self.loading_animation()
        with Live(auto_refresh=False, screen=True) as live:
            while True:
                try:
                    layout = self.render_screen()
                    live.update(layout)
                    live.refresh()
                    key = self.get_key_non_blocking()
                    if key == "q":
                        self.console.print("\n[bold cyan]SALIENDO DEL SISTEMA...")
                        return
                    elif key == "t":
                        self.current_theme = next(self.theme_cycle)
                except KeyboardInterrupt:
                    self.console.print("\n[bold cyan]SALIENDO DEL SISTEMA...")
                    return

if __name__ == "__main__":
    StellarOS().main()