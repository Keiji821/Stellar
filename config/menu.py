from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.style import Style
from rich.box import ROUNDED, DOUBLE
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from itertools import cycle
import sys
import termios
import tty
import select
import time
import random

class StellarOS:
    def __init__(self):
        self.console = Console()
        self.themes = {
            "neon":      {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_yellow","bg":"#0a0a1a"},
            "cyber":     {"primary":"bright_green","secondary":"bright_blue","highlight":"bright_red","bg":"#0a1a0a"},
            "matrix":    {"primary":"bright_green","secondary":"green","highlight":"bright_white","bg":"black"},
            "shinkai":   {"primary":"bright_cyan","secondary":"bright_blue","highlight":"bright_magenta","bg":"#101830"},
            "solar":     {"primary":"yellow","secondary":"bright_red","highlight":"bright_white","bg":"#1f1f1f"},
            "sunset":    {"primary":"black","secondary":"dark_red","highlight":"white","bg":"#ffeb3b"},
            "frost":     {"primary":"black","secondary":"blue","highlight":"white","bg":"#e0f7fa"},
            "pastel":    {"primary":"black","secondary":"magenta","highlight":"cyan","bg":"#f5e6e8"},
            "clean":     {"primary":"black","secondary":"grey50","highlight":"dark_blue","bg":"#ffffff"},
            "midnight":  {"primary":"white","secondary":"bright_blue","highlight":"bright_magenta","bg":"#001f3f"},
            "forest":    {"primary":"white","secondary":"green","highlight":"bright_green","bg":"#013220"},
            "aurora":    {"primary":"bright_green","secondary":"bright_magenta","highlight":"cyan","bg":"#2b1f3b"},
            "dawn":      {"primary":"bright_red","secondary":"yellow","highlight":"white","bg":"#0f1b1b"},
            "twilight":  {"primary":"bright_cyan","secondary":"blue","highlight":"green","bg":"#1b2a3e"},
            "lava":      {"primary":"bright_red","secondary":"yellow","highlight":"white","bg":"#2f0200"},
            "monokai":   {"primary":"bright_yellow","secondary":"bright_magenta","highlight":"bright_green","bg":"#2d2a2e"},
            "dracula":   {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_white","bg":"#282a36"},
            "ocean":     {"primary":"bright_blue","secondary":"cyan","highlight":"white","bg":"#001f3f"},
            "vaporwave": {"primary":"bright_pink","secondary":"bright_blue","highlight":"bright_magenta","bg":"#2b0030"}
        }
        self.menu_data = {
            "MAIN": [
                ("intro",(
                    "Stellar OS es un sistema operativo para Termux de fácil uso e instalación. "
                    "Este menú presenta comandos preconfigurados listos para usar, enfocados en mejorar la apariencia de Termux "
                    "y ofrecer utilidades opcionales para diferentes áreas."))
            ],
            "SISTEMA": [
                ("reload",    "Recarga el banner"),
                ("clear",     "Limpia la terminal"),
                ("bash",      "Reinicia terminal"),
                ("ui",        "Personalizar interfaz"),
                ("uninstall", "Desinstalar sistema"),
                ("update",    "Actualizar desde GitHub")
            ],
            "UTILIDADES": [
                ("ia",        "Asistente IA GPT-4"),
                ("ia-image",  "Generador de imágenes"),
                ("traductor", "Traductor multidioma"),
                ("myip",      "Muestra tu IP pública")
            ],
            "OSINT": [
                ("ipinfo",      "Info de direcciones IP"),
                ("phoneinfo",   "Búsqueda de teléfonos"),
                ("urlinfo",     "Analiza URLs"),
                ("metadatainfo","Extrae metadatos"),
                ("emailsearch", "Busca emails"),
                ("userfinder",  "Rastrea usuarios")
            ],
            "OSINT-DISCORD": [
                ("userinfo",    "Info de usuarios Discord"),
                ("serverinfo",  "Info de servidores"),
                ("searchinvites","Busca invitaciones"),
                ("inviteinfo",  "Analiza enlaces")
            ],
            "PENTESTING": [
                ("ddos", "Ataque DDOS controlado")
            ],
        }
        self.categories = list(self.menu_data.keys())
        self.cat_index = 0
        self.theme_cycle = cycle(self.themes.keys())
        self.current_theme = next(self.theme_cycle)
        self.version = "v2.3.0"
        self.worm_colors = ["red","magenta","yellow","green","cyan","blue"]
        self.worm_pos = 0

    def get_key(self, timeout=0.1):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            r, _, _ = select.select([fd], [], [], timeout)
            if r:
                return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return None

    def animated_banner(self):
        theme = self.themes[self.current_theme]
        header = Text.assemble(
            (" STELLAR OS ", f"bold {theme['secondary']} blink"),
            (f" [{self.version}]\n", "bold grey50")
        )
        sep = Text("─" * 38 + "\n", style="dim")
        authors = Text.assemble(
            ("Keiji821 (Programador)\n", f"bold {theme['highlight']}"),
            ("Galera (Diseñadora)\n",       f"bold {theme['secondary']}")
        )
        return Panel(
            Align.center(Text.assemble(header, sep, authors)),
            border_style=self.worm_colors[self.worm_pos % len(self.worm_colors)],
            box=DOUBLE,
            padding=(1,2),
            style=Style(bgcolor=theme['bg'])
        )

    def create_table(self):
        theme = self.themes[self.current_theme]
        cat = self.categories[self.cat_index]
        if cat == "MAIN":
            intro = self.menu_data['MAIN'][0][1]
            cats = "\n".join([f"[underline]{c}[/]" for c in self.categories if c != 'MAIN'])
            content = f"{intro}\n\n{cats}"
            return Panel(
                Align.left(content),
                title="MAIN", title_align="center",
                border_style=theme['secondary'], box=ROUNDED,
                padding=(1,2), style=Style(bgcolor=theme['bg'])
            )
        table = Table.grid(padding=(0,2))
        table.add_column(style=f"bold {theme['highlight']}", width=20)
        table.add_column(style=theme['primary'])
        table.add_row(Panel.fit(f"[bold]{cat}[/]", border_style=theme['secondary'], box=ROUNDED), "")
        for cmd, desc in self.menu_data[cat]:
            table.add_row(f"[{theme['highlight']}]› {cmd}", f"[{theme['primary']}] {desc}")
        return Panel(
            table,
            border_style=self.worm_colors[(self.worm_pos+2) % len(self.worm_colors)],
            box=ROUNDED, padding=(1,1), style=Style(bgcolor=theme['bg'])
        )

    def tips_panel(self):
        theme = self.themes[self.current_theme]
        tips = "[bold]Tips Rápidos:[/bold]  [dim]w/s[/dim] ↑/↓ Categorías  |  [dim]t[/dim] Cambiar tema  |  [dim]q[/dim] Salir"
        return Panel(
            tips,
            border_style=self.worm_colors[(self.worm_pos+4) % len(self.worm_colors)],
            box=ROUNDED, style=Style(bgcolor=theme['bg'])
        )

    def loading_animation(self):
        theme = self.themes[self.current_theme]
        styles = [f"bold {theme['highlight']}", f"bold {theme['secondary']}", f"bold {theme['primary']}" ]
        for style in cycle(styles):
            prog = Progress(
                SpinnerColumn(style=style), BarColumn(bar_width=None, style=style),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%", style=style),
                console=self.console, transient=True
            )
            task = prog.add_task("INICIANDO...", total=100)
            with prog:
                for _ in range(100):
                    time.sleep(0.01)
                    prog.update(task, advance=1)
            break

    def render(self):
        self.worm_pos = (self.worm_pos + 1) % len(self.worm_colors)
        layout = Layout()
        layout.split_column(
            Layout(self.animated_banner(), size=7),
            Layout(self.create_table(), ratio=2),
            Layout(self.tips_panel(), size=3)
        )
        return layout

    def main(self):
        self.loading_animation()
        with Live(screen=True, auto_refresh=False, console=self.console) as live:
            while True:
                live.update(self.render(), refresh=True)
                key = self.get_key()
                if key == 'q': break
                if key == 't': self.current_theme = next(self.theme_cycle)
                if key == 'w': self.cat_index = (self.cat_index - 1) % len(self.categories)
                if key == 's': self.cat_index = (self.cat_index + 1) % len(self.categories)
        self.console.print("\n[bold cyan]SALIENDO DEL SISTEMA...")

if __name__ == "__main__":
    StellarOS().main()
