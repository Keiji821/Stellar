from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.box import HEAVY, ROUNDED
from rich.align import Align
from itertools import cycle
import time
import os

class StellarOS:
    def __init__(self):
        self.console = Console()
        self.themes = {
            "neon": {
                "primary": "bright_magenta",
                "secondary": "bright_cyan",
                "highlight": "bright_yellow",
                "bg": "black"
            },
            "cyber": {
                "primary": "bright_green",
                "secondary": "bright_blue",
                "highlight": "bright_red",
                "bg": "black"
            },
            "galaxy": {
                "primary": "bright_blue",
                "secondary": "bright_purple",
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
            (f" STELLAR OS ", f"bold {self.themes[self.current_theme]['secondary']}"),
            (f" [{self.version}]", "bold grey50")
        )
        return Panel(
            Align.center(text), 
            border_style=self.themes[self.current_theme]['secondary'], 
            padding=(1, 4), 
            box=HEAVY
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
            
            task = progress.add_task(f"[{style}]Cargando interfaz...", total=100)
            
            with progress:
                for _ in range(100):
                    time.sleep(0.01)
                    progress.update(task, advance=1)
                break

    def render_screen(self):
        layout = Layout()
        layout.split_column(
            Layout(self.animated_banner(), size=5),
            Layout(
                Panel(
                    self.create_table(), 
                    border_style=self.themes[self.current_theme]['secondary'], 
                    box=ROUNDED, 
                    padding=(1, 0)
                ), 
                ratio=2
            ),
            Layout(
                Panel(
                    f"[dim {self.themes[self.current_theme]['primary']}]Presiona 'q' para salir | 't' para cambiar tema[/]", 
                    border_style=self.themes[self.current_theme]['secondary']
                ), 
                size=3
            ),
        )
        return layout

    def border_animation(self):
        colors = [
            self.themes[self.current_theme]['highlight'],
            self.themes[self.current_theme]['secondary'],
            self.themes[self.current_theme]['primary'],
            "bright_white",
            "bright_yellow"
        ]
        
        while True:
            for color in colors:
                yield color

    def main(self):
        self.loading_animation()
        border_gen = self.border_animation()
        
        with Live(self.render_screen(), refresh_per_second=15, screen=True) as live:
            while True:
                try:
                    current_screen = self.render_screen()
                    current_screen.border_style = next(border_gen)
                    live.update(current_screen)
                    
                    key = self.console.input(f"[bold {self.themes[self.current_theme]['highlight']}]Presiona una tecla (q/t)[/] ").lower()
                    
                    if key == 'q':
                        self.console.print("\n[bold cyan]Hasta pronto...")
                        break
                    elif key == 't':
                        self.current_theme = next(self.theme_cycle)
                        border_gen = self.border_animation()
                    
                    time.sleep(0.1)
                    
                except KeyboardInterrupt:
                    self.console.print("\n[bold cyan]Hasta pronto...")
                    break

if __name__ == "__main__":
    stellar_os = StellarOS()
    stellar_os.main()