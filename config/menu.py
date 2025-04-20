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

class StellarOS:
    def __init__(self):
        self.console = Console()
        self.themes = {
            "neon": {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_yellow","bg":"#0a0a1a"},
            "cyber": {"primary":"bright_green","secondary":"bright_blue","highlight":"bright_red","bg":"#0a1a0a"},
            "matrix": {"primary":"bright_white","secondary":"bright_green","highlight":"bright_cyan","bg":"black"},
            "shinkai": {"primary":"bright_cyan","secondary":"bright_blue","highlight":"bright_magenta","bg":"#101830"},
            "solar": {"primary":"#37474f","secondary":"#c62828","highlight":"#1a237e","bg":"#fff8e1"},
            "sunset": {"primary":"black","secondary":"dark_red","highlight":"white","bg":"#ffeb3b"},
            "frost": {"primary":"black","secondary":"cyan","highlight":"white","bg":"#e0f7fa"},
            "pastel": {"primary":"black","secondary":"magenta","highlight":"cyan","bg":"#f5e6e8"},
            "clean": {"primary":"black","secondary":"grey50","highlight":"dark_blue","bg":"#ffffff"},
            "midnight": {"primary":"bright_white","secondary":"bright_cyan","highlight":"bright_magenta","bg":"#001f3f"},
            "forest": {"primary":"green","secondary":"yellow","highlight":"white","bg":"#2f4f2f"},
            "aurora": {"primary":"bright_green","secondary":"bright_magenta","highlight":"cyan","bg":"#2b1f3b"},
            "dawn": {"primary":"bright_red","secondary":"yellow","highlight":"white","bg":"#0f1b1b"},
            "twilight": {"primary":"bright_cyan","secondary":"blue","highlight":"green","bg":"#1b2a3e"},
            "lava": {"primary":"bright_red","secondary":"yellow","highlight":"white","bg":"#2f0200"},
            "monokai": {"primary":"bright_yellow","secondary":"bright_magenta","highlight":"bright_green","bg":"#2d2a2e"},
            "dracula": {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_white","bg":"#282a36"},
            "ocean": {"primary":"bright_blue","secondary":"cyan","highlight":"white","bg":"#001f3f"},
            "vaporwave": {"primary":"bright_pink","secondary":"bright_blue","highlight":"bright_magenta","bg":"#2b0030"},
            "ember": {"primary":"bright_red","secondary":"bright_yellow","highlight":"bright_white","bg":"#3f0a0a"},
            "glacier": {"primary":"bright_cyan","secondary":"white","highlight":"white","bg":"#0a1e2a"},
            "daylight": {"primary":"#212121","secondary":"#616161","highlight":"#0d47a1","bg":"#f5f5f5"},
            "sage": {"primary":"white","secondary":"dark_green","highlight":"green","bg":"#dff0d8"},
            "retro": {"primary":"white","secondary":"bright_yellow","highlight":"bright_red","bg":"#333300"},
            "lunar": {"primary":"bright_white","secondary":"bright_blue","highlight":"bright_magenta","bg":"#102030"},
            "gold": {"primary":"black","secondary":"gold3","highlight":"white","bg":"#ffda44"},
            "storm": {"primary":"bright_white","secondary":"cyan","highlight":"blue","bg":"#0c1e3b"},
            "ink": {"primary":"white","secondary":"grey70","highlight":"grey30","bg":"#e6e6e6"},
            "highcontrast": {"primary":"black","secondary":"white","highlight":"red","bg":"#ffffff"},
            "deepspace": {"primary":"bright_white","secondary":"cyan","highlight":"yellow","bg":"#000033"},
            "crystal": {"primary":"bright_white","secondary":"bright_cyan","highlight":"bright_blue","bg":"#003366"},
            "crimson": {"primary":"white","secondary":"red","highlight":"cyan","bg":"#300000"},
            "hacker": {"primary":"bright_green","secondary":"black","highlight":"bright_red","bg":"#001100"}
        }
        self.menu_data = {
            "MAIN": [("intro", (
                "Stellar OS es un sistema operativo para Termux de fácil uso e instalación. "
                "Este menú presenta comandos preconfigurados listos para usar, enfocados en mejorar la apariencia de Termux "
                "y ofrecer utilidades opcionales para diferentes áreas."))],
            "SISTEMA": [("reload", "Recarga el banner"), ("clear", "Limpia la terminal"), 
                       ("bash", "Reinicia terminal"), ("ui", "Personalizar interfaz"), 
                       ("uninstall", "Desinstalar sistema"), ("update", "Actualizar desde GitHub")],
            "UTILIDADES": [("ia", "Asistente IA GPT-4"), ("ia-image", "Generador de imágenes"), 
                          ("traductor", "Traductor multidioma"), ("myip", "Muestra tu IP pública")],
            "OSINT": [("ipinfo", "Info de direcciones IP"), ("phoneinfo", "Búsqueda de teléfonos"), 
                     ("urlinfo", "Analiza URLs"), ("metadatainfo", "Extrae metadatos"), 
                     ("emailsearch", "Busca emails"), ("userfinder", "Rastrea usuarios")],
            "OSINT-DISCORD": [("userinfo", "Info de usuarios Discord"), ("serverinfo", "Info de servidores"), 
                             ("searchinvites", "Busca invitaciones"), ("inviteinfo", "Analiza enlaces")],
            "PENTESTING": [("ddos", "Ataque DDOS controlado")]
        }
        self.categories = list(self.menu_data.keys())
        self.cat_index = 0
        self.theme_cycle = cycle(self.themes.keys())
        self.current_theme = next(self.theme_cycle)
        self.version = "v2.4.2"
        self.worm_colors = ["red", "magenta", "yellow", "green", "cyan", "blue"]
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
        text = Text(justify="center")
        text.append("\n\nSTELLAR OS", style=f"bold {theme['secondary']} blink")
        text.append(f" [{self.version}]\n", style=f"bold {theme['highlight']}")
        
        # Sección de creadores mejorada
        creators = Text("\nCreadores:\n\n", style=f"bold {theme['primary']} underline", justify="center")
        creators.append("Keiji821 (Programador Principal)\n", style=f"bold {theme['highlight']}")
        creators.append("Galera (Diseñadora de Interfaces)\n\n", style=f"bold {theme['highlight']}")
        
        text.append(creators)
        return Panel(
            Align.center(text, vertical="middle"),
            border_style=self.worm_colors[self.worm_pos % len(self.worm_colors)],
            box=DOUBLE,
            style=Style(bgcolor=theme['bg']),
            padding=(2, 4)
        )

    def create_table(self):
        theme = self.themes[self.current_theme]
        cat = self.categories[self.cat_index]
        if cat == 'MAIN':
            intro = self.menu_data['MAIN'][0][1]
            intro_panel = Panel(
                Align.left(intro, vertical="top"),
                title='INTRODUCCIÓN', title_align='center',
                border_style=theme['highlight'], box=ROUNDED,
                style=Style(bgcolor=theme['bg']), padding=(2, 3))
            cats_text = Text()
            for i, name in enumerate(self.categories):
                if name == 'MAIN':
                    continue
                color = self.worm_colors[(self.worm_pos + i) % len(self.worm_colors)]
                cats_text.append(f"{name}\n", style=f"bold {color} underline")
            cat_panel = Panel(
                Align.left(cats_text, vertical="top"),
                title='Categorías', title_align='center',
                border_style=self.worm_colors[(self.worm_pos + 2) % len(self.worm_colors)],
                box=ROUNDED, style=Style(bgcolor=theme['bg']), padding=(1, 3))
            layout = Layout()
            layout.split_column(Layout(intro_panel, ratio=2), Layout(cat_panel))
            return layout
        table = Table.grid(padding=(0, 2))
        table.add_column(style=f"bold {theme['highlight']}", width=22)
        table.add_column(style=theme['primary'])
        table.add_row(Panel.fit(f"[bold]{cat}[/]", border_style=theme['secondary'], box=ROUNDED), "")
        for cmd, desc in self.menu_data[cat]:
            table.add_row(f"[{theme['highlight']}]› {cmd}", f"[{theme['primary']}] {desc}")
        return Panel(
            table,
            box=ROUNDED,
            border_style=self.worm_colors[(self.worm_pos + 4) % len(self.worm_colors)],
            style=Style(bgcolor=theme['bg']), padding=(1, 2))

    def tips_panel(self):
        theme = self.themes[self.current_theme]
        tips = Text(style=theme['primary'])
        tips.append("\nNAVEGACIÓN RÁPIDA\n\n", style=f"bold {theme['highlight']} underline")
        tips.append(" [W] Subir categoría\n", style=f"bold {theme['secondary']}")
        tips.append(" [S] Bajar categoría\n", style=f"bold {theme['secondary']}")
        tips.append(" [T] Cambiar tema visual\n", style=f"bold {theme['secondary']}")
        tips.append(" [Q] Salir del sistema\n", style=f"bold {theme['secondary']}")
        return Panel(
            Align.center(tips, vertical="middle"),
            box=ROUNDED,
            border_style=self.worm_colors[(self.worm_pos + 6) % len(self.worm_colors)],
            style=Style(bgcolor=theme['bg']),
            padding=(2, 4)
        )

    def loading_animation(self):
        theme = self.themes[self.current_theme]
        for style in cycle([theme['highlight'], theme['secondary'], theme['primary']]):
            prog = Progress(
                SpinnerColumn(style=f"bold {style}"),
                BarColumn(style=f"bold {style}"),
                TextColumn("{task.percentage:>3.0f}%", style=f"bold {style}"),
                console=self.console, 
                transient=True
            )
            task = prog.add_task("[bold] INICIANDO SISTEMA...", total=100)
            with prog:
                for _ in range(100):
                    time.sleep(0.01)
                    prog.update(task, advance=1)
            break

    def render(self):
        self.worm_pos = (self.worm_pos + 1) % len(self.worm_colors)
        layout = Layout()
        layout.split_column(
            Layout(self.animated_banner(), size=12),
            Layout(self.create_table(), ratio=2),
            Layout(self.tips_panel(), size=8)
        )
        return layout

    def main(self):
        self.loading_animation()
        with Live(auto_refresh=False, screen=True, console=self.console) as live:
            while True:
                live.update(self.render(), refresh=True)
                key = self.get_key()
                if key == 'q':
                    break
                if key == 't':
                    self.current_theme = next(self.theme_cycle)
                if key == 'w':
                    self.cat_index = max(0, self.cat_index - 1)
                if key == 's':
                    self.cat_index = min(len(self.categories) - 1, self.cat_index + 1)
        self.console.print("\n[bold cyan]SALIENDO DEL SISTEMA...")

if __name__ == "__main__":
    StellarOS().main()