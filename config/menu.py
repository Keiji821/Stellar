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
import termios, tty, sys, select
import time

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
            {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_yellow","bg":"#0a0a1a"},
            {"primary":"bright_cyan","secondary":"bright_blue","highlight":"bright_magenta","bg":"#101830"},
            {"primary":"bright_white","secondary":"bright_green","highlight":"bright_cyan","bg":"black"},
            {"primary":"bright_green","secondary":"bright_blue","highlight":"bright_red","bg":"#0a1a0a"},
            {"primary":"bright_magenta","secondary":"bright_cyan","highlight":"bright_white","bg":"#282a36"}
        ])
        self.current_theme = next(self.theme_cycle)
        self.worm_colors = ["bright_red","bright_yellow","bright_green","bright_cyan","bright_blue","bright_magenta"]
        self.worm_index = 0
        self.menu_data = {
            "MAIN": [("intro","Bienvenido a Stellar OS, sistema visual de Termux.")],
            "SISTEMA": [("reload","Recarga el banner"),("clear","Limpia la terminal"),("bash","Reinicia terminal"),("ui","Personalizar interfaz"),("uninstall","Desinstalar sistema"),("update","Actualizar desde GitHub")],
            "UTILIDADES": [("ia","Asistente IA GPT-4"),("ia-image","Generador de imágenes"),("traductor","Traductor multidioma"),("myip","Muestra tu IP pública")],
            "OSINT": [("ipinfo","Info de IPs"),("phoneinfo","Búsqueda de teléfonos"),("urlinfo","Analiza URLs"),("metadatainfo","Extrae metadatos"),("emailsearch","Busca emails"),("userfinder","Rastrea usuarios")],
            "OSINT-DISCORD": [("userinfo","Info Discord"),("serverinfo","Info Servidores"),("searchinvites","Busca Invitaciones"),("inviteinfo","Analiza enlaces")],
            "PENTESTING": [("ddos","Ataque DDOS controlado")]
        }
        self.layout = Layout()
        self.last_update = time.time()
        self.worm_speed = 1.0
        self.current_color = self.worm_colors[self.worm_index]

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
        banner_table = Table.grid(padding=0, expand=True)
        banner_table.add_column(justify="center")
        
        # Titulo principal
        title = Text("STELLAR OS", style=f"bold {t['secondary']}", justify="center")
        version = Text(self.version, style=f"bold {t['highlight']}", justify="center")
        
        # Línea de creadores compacta
        creators = Table.grid(padding=0)
        creators.add_column(justify="center")
        creators.add_row(
            Text("CREADORES: ", style=f"bold {t['primary']}") 
            + Text("Keiji821 (Programador)", style=f"bold {t['highlight']}") 
            + Text(" | ", style=f"bold {t['primary']}") 
            + Text("Galera (Diseñadora)", style=f"bold {t['highlight']}")
        )
        
        banner_table.add_row(title)
        banner_table.add_row(version)
        banner_table.add_row(creators)
        
        return Panel(
            banner_table,
            box=DOUBLE,
            border_style=self.current_color,
            style=Style(bgcolor=t['bg']),
            padding=(0,0)
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
            border_style=self.current_color,
            style=Style(bgcolor=t['bg']),
            padding=(0,0)
        )

    def create_tips(self):
        t = self.current_theme
        tips = Table.grid(padding=0)
        tips.add_column(justify="center")
        tips.add_row("[W]Arriba   [S]Abajo   [T]Tema   [Q]Salir", style=f"bold {t['secondary']}")
        return Panel(
            tips,
            box=ROUNDED,
            border_style=self.current_color,
            style=Style(bgcolor=t['bg']),
            padding=(0,0)
        )

    def render(self):
        if time.time() - self.last_update > self.worm_speed:
            self.worm_index = (self.worm_index + 1) % len(self.worm_colors)
            self.current_color = self.worm_colors[self.worm_index]
            self.last_update = time.time()
        
        self.layout.split_column(
            Layout(self.create_banner(), ratio=4),
            Layout(self.create_menu(), ratio=10),
            Layout(self.create_tips(), ratio=1)
        )
        return self.layout

    def main(self):
        with Live(self.render(), refresh_per_second=20, screen=True, console=self.console, transient=False) as live:
            while True:
                live.update(self.render())
                key = self.get_key()
                if key == 'q': break
                if key == 't': 
                    self.current_theme = next(self.theme_cycle)
                if key == 'w': 
                    self.cat_index = max(0, self.cat_index-1)
                if key == 's': 
                    self.cat_index = min(len(self.categories)-1, self.cat_index+1)
        self.console.print("[bold cyan]SALIENDO...")

if __name__ == "__main__":
    StellarOS().main()