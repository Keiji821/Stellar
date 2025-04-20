from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.style import Style
from rich.box import ROUNDED, DOUBLE
from itertools import cycle
import termios, tty, sys, select, time

class StellarOS:
    def __init__(self):
        self.console = Console()
        self.version = "v2.4.2"
        self.categories = [
            "MAIN", "SISTEMA", "UTILIDADES", "OSINT",
            "OSINT-DISCORD", "PENTESTING"
        ]
        self.cat_index = 0
        self.theme_cycle = cycle([
            {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_yellow","bg":"#0a0a1a"},  # neon
            {"primary":"bright_cyan","secondary":"bright_blue","highlight":"bright_magenta","bg":"#101830"},  # shinkai
            {"primary":"bright_white","secondary":"bright_green","highlight":"bright_cyan","bg":"black"},  # matrix
            {"primary":"bright_green","secondary":"bright_blue","highlight":"bright_red","bg":"#0a1a0a"},  # cyber
            {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_white","bg":"#282a36"}   # dracula
        ])
        self.current_theme = next(self.theme_cycle)
        self.worm_colors = ["red","yellow","green","cyan","blue","magenta"]
        self.worm_index = 0
        self.menu_data = {
            "MAIN": [("intro","Bienvenido a Stellar OS, sistema visual de Termux.")],
            "SISTEMA": [("reload","Recarga el banner"),("clear","Limpia la terminal"),("bash","Reinicia terminal"),("ui","Personalizar interfaz"),("uninstall","Desinstalar sistema"),("update","Actualizar desde GitHub")],
            "UTILIDADES": [("ia","Asistente IA GPT-4"),("ia-image","Generador de imágenes"),("traductor","Traductor multidioma"),("myip","Muestra tu IP pública")],
            "OSINT": [("ipinfo","Info de IPs"),("phoneinfo","Búsqueda de teléfonos"),("urlinfo","Analiza URLs"),("metadatainfo","Extrae metadatos"),("emailsearch","Busca emails"),("userfinder","Rastrea usuarios")],
            "OSINT-DISCORD": [("userinfo","Info Discord"),("serverinfo","Info Servidores"),("searchinvites","Busca Invitaciones"),("inviteinfo","Analiza enlaces")],
            "PENTESTING": [("ddos","Ataque DDOS controlado")]
        }

    def get_key(self, timeout=0.005):
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

    def create_banner(self):
        t = self.current_theme
        text = Text(justify="center")
        text.append("STELLAR OS\n", style=f"bold {t['secondary']} blink")
        text.append(f"{self.version}\n", style=f"bold {t['highlight']}")
        # Creadores
        text.append("\nCREADORES\n", style=f"bold {t['primary']} underline")
        text.append("Keiji821 (Programador)\n", style=f"bold {t['highlight']}")
        text.append("Galera (Diseñadora)\n", style=f"bold {t['highlight']}")
        return Panel(
            Align.center(text, vertical="middle"),
            box=DOUBLE,
            border_style=self.worm_colors[self.worm_index % len(self.worm_colors)],
            style=Style(bgcolor=t['bg']),
            padding=(1,2)
        )

    def create_menu(self):
        t = self.current_theme
        cat = self.categories[self.cat_index]
        table = Table.grid(padding=(0,1))
        table.add_column(style=f"bold {t['highlight']}", width=20)
        table.add_column(style=t['primary'])
        table.add_row(Panel.fit(f"[bold]{cat}[/]", box=ROUNDED, border_style=t['secondary']), "")
        for cmd, desc in self.menu_data[cat]:
            table.add_row(f"[{t['highlight']}]› {cmd}", f"[{t['primary']}] {desc}")
        return Panel(
            table,
            box=ROUNDED,
            border_style=self.worm_colors[(self.worm_index+2) % len(self.worm_colors)],
            style=Style(bgcolor=t['bg']),
            padding=(1,2)
        )

    def create_tips(self):
        t = self.current_theme
        tips = Text(justify="center")
        tips.append("NAVEGACIÓN RÁPIDA\n", style=f"bold {t['highlight']} underline")
        tips.append("[W] Arriba   [S] Abajo   [T] Tema   [Q] Salir", style=f"bold {t['secondary']}")
        return Panel(
            Align.center(tips),
            box=ROUNDED,
            border_style=self.worm_colors[(self.worm_index+4) % len(self.worm_colors)],
            style=Style(bgcolor=t['bg']),
            padding=(1,2)
        )

    def render(self):
        self.worm_index += 1
        layout = Layout()
        layout.split_column(
            Layout(self.create_banner(), ratio=3),
            Layout(self.create_menu(), ratio=5),
            Layout(self.create_tips(), ratio=2)
        )
        return layout

    def main(self):
        with Live(self.render(), refresh_per_second=120, screen=True, console=self.console) as live:
            while True:
                time.sleep(0.008)
                live.update(self.render())
                key = self.get_key()
                if key == 'q': break
                if key == 't': self.current_theme = next(self.theme_cycle)
                if key == 'w': self.cat_index = max(0, self.cat_index-1)
                if key == 's': self.cat_index = min(len(self.categories)-1, self.cat_index+1)
        self.console.print("[bold cyan]SALIENDO...")

if __name__ == "__main__":
    StellarOS().main()
