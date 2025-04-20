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
            "matrix":    {"primary":"bright_white","secondary":"bright_green","highlight":"bright_cyan","bg":"black"},
            "shinkai":   {"primary":"bright_cyan","secondary":"bright_blue","highlight":"bright_magenta","bg":"#101830"},
            "solar":     {"primary":"black","secondary":"bright_yellow","highlight":"bright_red","bg":"#fff8e1"},
            "sunset":    {"primary":"black","secondary":"dark_red","highlight":"white","bg":"#ffeb3b"},
            "frost":     {"primary":"black","secondary":"cyan","highlight":"white","bg":"#e0f7fa"},
            "pastel":    {"primary":"black","secondary":"magenta","highlight":"cyan","bg":"#f5e6e8"},
            "clean":     {"primary":"black","secondary":"grey50","highlight":"dark_blue","bg":"#ffffff"},
            "midnight":  {"primary":"bright_blue","secondary":"bright_cyan","highlight":"bright_magenta","bg":"#001f3f"},
            "forest":    {"primary":"green","secondary":"yellow","highlight":"white","bg":"#2f4f2f"},
            "aurora":    {"primary":"bright_green","secondary":"bright_magenta","highlight":"cyan","bg":"#2b1f3b"},
            "dawn":      {"primary":"bright_red","secondary":"yellow","highlight":"white","bg":"#0f1b1b"},
            "twilight":  {"primary":"bright_cyan","secondary":"blue","highlight":"green","bg":"#1b2a3e"},
            "lava":      {"primary":"bright_red","secondary":"yellow","highlight":"white","bg":"#2f0200"},
            "monokai":   {"primary":"bright_yellow","secondary":"bright_magenta","highlight":"bright_green","bg":"#2d2a2e"},
            "dracula":   {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_white","bg":"#282a36"},
            "ocean":     {"primary":"bright_blue","secondary":"cyan","highlight":"white","bg":"#001f3f"},
            "vaporwave": {"primary":"bright_pink","secondary":"bright_blue","highlight":"bright_magenta","bg":"#2b0030"},
            "ember":     {"primary":"bright_red","secondary":"bright_yellow","highlight":"bright_white","bg":"#3f0a0a"},
            "glacier":   {"primary":"bright_cyan","secondary":"white","highlight":"white","bg":"#0a1e2a"},
            "daylight":  {"primary":"black","secondary":"grey70","highlight":"dark_blue","bg":"#f0f0f0"},
            "sage":      {"primary":"white","secondary":"dark_green","highlight":"green","bg":"#dff0d8"},
            "retro":     {"primary":"white","secondary":"bright_yellow","highlight":"bright_red","bg":"#333300"},
            "lunar":     {"primary":"bright_white","secondary":"bright_blue","highlight":"bright_magenta","bg":"#102030"},
            "gold":      {"primary":"black","secondary":"gold3","highlight":"white","bg":"#ffda44"},
            "storm":     {"primary":"bright_white","secondary":"cyan","highlight":"blue","bg":"#0c1e3b"},
            "ink":       {"primary":"white","secondary":"grey70","highlight":"grey30","bg":"#e6e6e6"}
        }
        self.menu_data = {
            "MAIN": [("intro",
                "Stellar OS es un sistema operativo para Termux de fácil uso e instalación. "
                "Este menú presenta comandos preconfigurados listos para usar, enfocados en mejorar la apariencia de Termux "
                "y ofrecer utilidades opcionales para diferentes áreas.")],
            "SISTEMA": [("reload","Recarga el banner"),("clear","Limpia la terminal"),
                        ("bash","Reinicia terminal"),("ui","Personalizar interfaz"),
                        ("uninstall","Desinstalar sistema"),("update","Actualizar desde GitHub")],
            "UTILIDADES":[("ia","Asistente IA GPT-4"),("ia-image","Generador de imágenes"),
                          ("traductor","Traductor multidioma"),("myip","Muestra tu IP pública")],
            "OSINT":[("ipinfo","Info de direcciones IP"),("phoneinfo","Búsqueda de teléfonos"),
                     ("urlinfo","Analiza URLs"),("metadatainfo","Extrae metadatos"),
                     ("emailsearch","Busca emails"),("userfinder","Rastrea usuarios")],
            "OSINT-DISCORD":[("userinfo","Info de usuarios Discord"),("serverinfo","Info de servidores"),
                             ("searchinvites","Busca invitaciones"),("inviteinfo","Analiza enlaces")],
            "PENTESTING":[("ddos","Ataque DDOS controlado")]
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
            r,_,_ = select.select([fd],[],[],timeout)
            if r: return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return None

    def animated_banner(self):
        t = self.themes[self.current_theme]
        text = Text.assemble(
            (" STELLAR OS ", f"bold {t['secondary']} blink"),
            (f" [{self.version}]\n", f"bold {t['highlight']}"),
            ("Creadores:\n", f"bold {t['primary']}"),
            ("  Keiji821 (Programador)\n", f"{t['highlight']}"),
            ("  Galera (Diseñadora)", f"{t['highlight']}")
        )
        panel = Panel(
            Align.center(text),
            border_style=self.worm_colors[self.worm_pos % len(self.worm_colors)],
            box=DOUBLE,
            style=Style(bgcolor=t['bg']),
            padding=(1,2)
        )
        return panel

    def create_table(self):
        t = self.themes[self.current_theme]
        cat = self.categories[self.cat_index]
        if cat == "MAIN":
            intro = self.menu_data["MAIN"][0][1]
            p1 = Panel(
                Align.left(intro),
                title="INTRODUCCIÓN", title_align="center",
                border_style=t["secondary"], box=ROUNDED,
                style=Style(bgcolor=t["bg"]), padding=(1,2)
            )
            cats = Text()
            for i,c in enumerate(self.categories):
                if c=="MAIN": continue
                color = self.worm_colors[(self.worm_pos + i) % len(self.worm_colors)]
                cats.append(f"{c}\n", style=f"underline bold {color}")
            p2 = Panel(
                Align.left(cats),
                title="Categorías", title_align="center",
                border_style=self.worm_colors[(self.worm_pos+2)%len(self.worm_colors)],
                box=ROUNDED, style=Style(bgcolor=t["bg"]), padding=(1,2)
            )
            # Devolver un Panel compuesto
            return Panel.fit(
                Align.center(Group(p1, p2)),
                box=ROUNDED, border_style=t["highlight"], style=Style(bgcolor=t["bg"])
            )

        table = Table.grid(padding=(0,2))
        table.add_column(style=f"bold {t['highlight']}", width=24)
        table.add_column(style=t["primary"])
        table.add_row(Panel.fit(f"[bold]{cat}[/]", border_style=t["secondary"], box=ROUNDED), "")
        for cmd,desc in self.menu_data[cat]:
            table.add_row(f"[{t['highlight']}]› {cmd}", f"[{t['primary']}] {desc}")
        panel = Panel(
            table, box=ROUNDED,
            border_style=self.worm_colors[(self.worm_pos+4)%len(self.worm_colors)],
            style=Style(bgcolor=t["bg"]), padding=(1,1)
        )
        return panel

    def tips_panel(self):
        t = self.themes[self.current_theme]
        text = Text.assemble(
            ("Tips Rápidos:\n", "bold underline"),
            (" w/s   ", "dim"), ("Subir/Bajar Categorías\n", ""),
            (" t     Cambiar tema\n", ""),
            (" q     Salir", "")
        )
        return Panel(
            text, box=ROUNDED,
            border_style=self.worm_colors[(self.worm_pos+6)%len(self.worm_colors)],
            style=Style(bgcolor=t["bg"]), padding=(1,1)
        )

    def loading_animation(self):
        t = self.themes[self.current_theme]
        for style in cycle([t["highlight"], t["secondary"], t["primary"]]):
            prog = Progress(
                SpinnerColumn(style=f"bold {style}"),
                BarColumn(style=f"bold {style}"),
                TextColumn("{task.percentage:>3.0f}%", style=f"bold {style}"),
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
            Layout(self.tips_panel(), size=4)
        )
        return layout

    def main(self):
        self.loading_animation()
        with Live(self.render(), console=self.console, auto_refresh=False, screen=True) as live:
            while True:
                live.update(self.render(), refresh=True)
                key = self.get_key()
                if   key == "q": break
                elif key == "t": self.current_theme = next(self.theme_cycle)
                elif key == "w": self.cat_index = (self.cat_index - 1) % len(self.categories)
                elif key == "s": self.cat_index = (self.cat_index + 1) % len(self.categories)
        self.console.print("\n[bold cyan]SALIENDO DEL SISTEMA...")

if __name__=="__main__":
    from rich.console import Group
    StellarOS().main()