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
import random

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
        self.running_colors = cycle([
            "bright_red", "bright_magenta", "bright_cyan", 
            "bright_green", "bright_blue", "bright_yellow"
        ])
        self.step = 0

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
        banner = Text.assemble(
            (f" STELLAR OS ", f"bold {self.themes[self.current_theme]['secondary']} blink"),
            (f" [{self.version}]", "bold grey50")
        )
        credits = Text.assemble(
            ("Desarrollado por ", "bold grey37"),
            ("Keiji821", f"bold {self.themes[self.current_theme]['highlight']}"),
            (" (Programador)   ", "bold grey37"),
            ("Galera", f"bold {self.themes[self.current_theme]['secondary']}"),
            (" (Diseñadora)", "bold grey37")
        )

        return Panel(
            Align.center(Text.assemble(banner, "\n", credits)), 
            border_style=next(self.running_colors), 
            padding=(1, 4), 
            box=DOUBLE,
            style=Style(bgcolor=self.themes[self.current_theme]['bg'])
        )

    def loading_animation(self):
        spinner_styles = [
            f"bold {self.themes[self.current_theme]['highlight']}",
            f"bold {self.themes[self.current_theme]['secondary']}",
            f"bold {self.themes[self.current_theme]['primary']}"
        ]

        for style in cycle(spinner_styles):
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
                    time.sleep(0.01)
                    progress.update(task, advance=1)
                break

    def render_screen(self):
        layout = Layout()
        layout.split_column(
            Layout(self.animated_banner(), size=7),
            Layout(
                Panel(
                    self.create_table(), 
                    border_style=next(self.running_colors),
                    box=ROUNDED, 
                    padding=(1, 0),
                    style=Style(bgcolor=self.themes[self.current_theme]['bg'])
                ), 
                ratio=2
            ),
            Layout(
                Panel(
                    Align.center(
                        f"[blink bold {self.themes[self.current_theme]['highlight']}]Presiona 'q' para salir | 't' para cambiar tema\n[dim]Tips: CTRL + C para detener | CTRL + Z para suspender[/]"
                    ), 
                    border_style=next(self.running_colors),
                    style=Style(bgcolor=self.themes[self.current_theme]['bg'])
                ), 
                size=4
            ),
        )
        return layout

    def main(self):
        self.loading_animation()
        with Live(auto_refresh=True, screen=True, console=self.console) as live:
            while True:
                try:
                    live.update(self.render_screen(), refresh=True)
                    time.sleep(0.15)
                    self.step += 1
                except KeyboardInterrupt:
                    self.console.print("\n[bold cyan]SALIENDO DEL SISTEMA...")
                    return

if __name__ == "__main__":
    StellarOS().main()