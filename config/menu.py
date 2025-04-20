from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from rich.live import Live
from rich.box import ROUNDED, DOUBLE
from rich.style import Style
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
        self.theme_names = cycle([
            "neon", "shinkai", "matrix", "cyber", "dracula"
        ])
        self.current_theme = next(self.theme_names)
        self.color_cycle = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        self.color_index = 0
        self.themes = {
            "neon": {"primary": "bright_magenta", "secondary": "bright_cyan", "highlight": "bright_yellow", "bg": "#0a0a1a"},
            "shinkai": {"primary": "bright_cyan", "secondary": "bright_blue", "highlight": "bright_magenta", "bg": "#101830"},
            "matrix": {"primary": "bright_white", "secondary": "bright_green", "highlight": "bright_cyan", "bg": "black"},
            "cyber": {"primary": "bright_green", "secondary": "bright_blue", "highlight": "bright_red", "bg": "#0a1a0a"},
            "dracula": {"primary": "bright_magenta", "secondary": "bright_cyan", "highlight": "bright_white", "bg": "#282a36"},
        }
        self.menu_data = {
            "MAIN": [("intro", "Bienvenido a Stellar OS, el sistema visual para Termux.")],
            "SISTEMA": [("reload", "Recarga el banner"), ("clear", "Limpia la terminal"),
                        ("bash", "Reinicia terminal"), ("ui", "Personalizar interfaz"),
                        ("uninstall", "Desinstalar sistema"), ("update", "Actualizar desde GitHub")],
            "UTILIDADES": [("ia", "Asistente IA GPT-4"), ("ia-image", "Generador de imágenes"),
                           ("traductor", "Traductor multidioma"), ("myip", "Muestra tu IP pública")],
            "OSINT": [("ipinfo", "Info de IPs"), ("phoneinfo", "Búsqueda de teléfonos"),
                      ("urlinfo", "Analiza URLs"), ("metadatainfo", "Extrae metadatos"),
                      ("emailsearch", "Busca emails"), ("userfinder", "Rastrea usuarios")],
            "OSINT-DISCORD": [("userinfo", "Info de usuarios Discord"), ("serverinfo", "Info de servidores"),
                              ("searchinvites", "Busca invitaciones"), ("inviteinfo", "Analiza enlaces")],
            "PENTESTING": [("ddos", "Ataque DDOS controlado")]
        }

    def get_key(self, timeout=0.01):
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