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
import sys, termios, tty, select, time

class StellarOS:
    def __init__(self):
        self.console = Console()
        self.themes = {
            "neon": {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_yellow","bg":"#0a0a1a"},
            "cyber": {"primary":"bright_green","secondary":"bright_blue","highlight":"bright_red","bg":"#0a1a0a"},
            "matrix": {"primary":"bright_white","secondary":"bright_green","highlight":"bright_cyan","bg":"black"},
            "shinkai": {"primary":"bright_cyan","secondary":"bright_blue","highlight":"bright_magenta","bg":"#101830"},
        }
        self.menu_data = {
            "MAIN": [("intro", "Stellar OS es un sistema operativo para Termux de fácil uso e instalación. Este menú presenta comandos preconfigurados listos para usar, enfocados en mejorar la apariencia de Termux y ofrecer utilidades opcionales para diferentes áreas.")],
            "SISTEMA": [("reload", "Recarga el banner"), ("clear", "Limpia la terminal"), ("bash", "Reinicia terminal"), ("ui", "Personalizar interfaz"), ("uninstall", "Desinstalar sistema"), ("update", "Actualizar desde GitHub")],
            "UTILIDADES": [("ia", "Asistente IA GPT-4"), ("ia-image", "Generador de imágenes"), ("traductor", "Traductor multidioma"), ("myip", "Muestra tu IP pública")],
            "OSINT": [("ipinfo", "Info de direcciones IP"), ("phoneinfo", "Búsqueda de teléfonos"), ("urlinfo", "Analiza URLs"), ("metadatainfo", "Extrae metadatos"), ("emailsearch", "Busca emails"), ("userfinder", "Rastrea usuarios")],
            "OSINT-DISCORD": [("userinfo", "Info de usuarios Discord"), ("serverinfo", "Info de servidores"), ("searchinvites", "Busca invitaciones"), ("inviteinfo", "Analiza enlaces")],
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
        text.append("\nSTELLAR OS", style=f"bold {theme['secondary']} blink")
        text.append(f" [{self.version}]\n", style=f"bold {theme['highlight']}")
        return Panel(
            Align.center(text, vertical="middle"),
            border_style=self.worm_colors[self.worm_pos % len(self.worm_colors)],
            box=DOUBLE,
            style=Style(bgcolor=theme['bg']),
            padding=(1, 4)
        )

    def creators_panel(self):
        theme = self.themes[self.current_theme]
        txt = Text(justify="center")
        txt.append("CREADORES\n\n", style=f"bold {theme['primary']} underline")
        txt.append("Keiji821 (Programador Principal)\n", style=f"bold {theme['highlight']}")
        txt.append("Galera (Diseñadora de Interfaces)\n", style=f"bold {theme['highlight']}")
        return Panel(
            Align.center(txt, vertical="middle"),
            border_style=theme['highlight'],
            box=ROUNDED,
            style=Style(bgcolor=theme['bg']),
            padding=(1, 4)
        )

    def create_table(self):
        theme = self.themes[self.current_theme]
        cat = self.categories[self.cat_index]
        if cat == 'MAIN':
            intro = self.menu_data['MAIN'][0][1]
            intro_panel = Panel(
                Align.center(intro, vertical="middle"),
                title='INTRODUCCIÓN',
                border_style=theme['highlight'],
                box=ROUNDED,
                style=Style(bgcolor=theme['bg']),
                padding=(2, 4)
            )
            return intro_panel

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
            style=Style(bgcolor=theme['bg']),
            padding=(1, 2)
        )

    def tips_panel(self):
        theme = self.themes[self.current_theme]
        tips = Text(justify="center")
        tips.append("NAVEGACIÓN RÁPIDA\n\n", style=f"bold {theme['highlight']} underline")
        tips.append("[W] Subir categoría   [S] Bajar categoría\n", style=f"bold {theme['secondary']}")
        tips.append("[T] Cambiar tema      [Q] Salir del sistema\n", style=f"bold {theme['secondary']}")
        return Panel(
            Align.center(tips, vertical="middle"),
            box=ROUNDED,
            border_style=self.worm_colors[(self.worm_pos + 6) % len(self.worm_colors)],
            style=Style(bgcolor=theme['bg']),
            padding=(1, 4)
        )

    def render(self):
        self.worm_pos = (self.worm_pos + 1) % len(self.worm_colors)
        layout = Layout()
        layout.split_column(
            Layout(self.animated_banner(), size=3),
            Layout(self.creators_panel(), size=5),
            Layout(self.create_table(), ratio=2),
            Layout(self.tips_panel(), size=6)
        )
        return layout

    def main(self):
        for style in cycle([self.themes[self.current_theme]['highlight'], self.themes[self.current_theme]['secondary'], self.themes[self.current_theme]['primary']]):
            prog = Progress(SpinnerColumn(style=f"bold {style}"), BarColumn(style=f"bold {style}"), TextColumn("{task.percentage:>3.0f}%", style=f"bold {style}"), console=self.console, transient=True)
            task = prog.add_task(" INICIANDO SISTEMA...", total=100)
            with prog:
                for _ in range(100): time.sleep(0.01); prog.update(task, advance=1)
            break
        with Live(auto_refresh=False, screen=True, console=self.console) as live:
            while True:
                live.update(self.render(), refresh=True)
                key = self.get_key()
                if key == 'q': break
                if key == 't': self.current_theme = next(self.theme_cycle)
                if key == 'w': self.cat_index = max(0, self.cat_index - 1)
                if key == 's': self.cat_index = min(len(self.categories) - 1, self.cat_index + 1)
        self.console.print("\n[bold cyan]SALIENDO DEL SISTEMA...")

if __name__ == "__main__":
    StellarOS().main()
