import os
import platform
import datetime
import time
import requests
import psutil
import shutil
import random
import subprocess
from rich.console import Console
from rich.text import Text
from rich.style import Style
from rich.table import Table
from rich.columns import Columns
from rich.panel import Panel

console = Console()

themes_dir = os.path.expanduser("~/Stellar/termux/lang_es/config/themes")
system_dir = os.path.expanduser("~/Stellar/termux/lang_es/config/system")

def generate_palette():
    def color_rgb():
        return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    return {
        'title': color_rgb(),
        'key': color_rgb(),
        'value': color_rgb(),
        'memory': color_rgb(),
        'disk': color_rgb(),
        'border': color_rgb(),
        'memory_bar': color_rgb(),
        'disk_bar': color_rgb(),
        'background': color_rgb()
    }

def rgb_style(color):
    return Style(color=f"rgb({color[0]},{color[1]},{color[2]})")

def read_file(path, default=""):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return default

def get_phone_model():
    try:
        model = subprocess.check_output(['getprop', 'ro.product.model']).decode().strip()
        return model if model else "Desconocido"
    except:
        return "Desconocido"

def process_style(string):
    parts = string.lower().split()
    bold = "bold" in parts
    color = next((p for p in parts if p != "bold"), None)
    return Style(color=color, bold=bold)

palette = generate_palette()
banner = read_file(f"{themes_dir}/banner.st")
col = read_file(f"{themes_dir}/banner_color.st", "#6E97B7")
bg = read_file(f"{themes_dir}/banner_background.st", "no")
bgcol = read_file(f"{themes_dir}/banner_background_color.st", "#4D8FAC")
user = read_file(f"{system_dir}/user.st", "Usuario")

style = process_style(col)
if bg.lower() in ("si", "sí", "yes"):
    style += Style(bgcolor=bgcol)
text_banner = Text(banner, style=style)

def get_info():
    now = datetime.datetime.now()
    vm = psutil.virtual_memory()
    du = psutil.disk_usage(os.path.expanduser("~"))

    ip_services = [
        "https://api.ipify.org",
        "https://ipinfo.io/ip",
        "https://ifconfig.me/ip",
        "https://ident.me"
    ]

    ip = "No disponible"
    for service in ip_services:
        try:
            response = requests.get(service, timeout=2)
            if response.status_code == 200:
                ip = response.text.strip()
                break
            elif response.status_code == 429:
                time.sleep(1)
                continue
        except (requests.RequestException, ConnectionError):
            continue

    return {
        "user": user,
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%I:%M %p"),
        "phone": get_phone_model(),
        "os": f"{platform.machine()}",
        "kernel": platform.release(),
        "shell": os.path.basename(os.getenv("SHELL", "bash")),
        "terminal": os.getenv("TERM", "desconocido"),
        "memory_percent": vm.percent,
        "memory_total": f"{vm.total//(1024**2):,} MB",
        "memory_used": f"{vm.used//(1024**2):,} MB",
        "disk_percent": du.percent,
        "disk_total": f"{du.total//(1024**3):,} GB",
        "disk_used": f"{du.used//(1024**3):,} GB",
        "ip": ip
    }

def create_bar(pct, color):
    bar_color = f"rgb({color[0]},{color[1]},{color[2]})"
    return f"[{bar_color}]{'█' * int(pct/5)}{'░' * (20 - int(pct/5))}[/] {pct}%"

def create_panel(info, panel_width=None):
    t = Table(show_header=False, show_lines=False,
              border_style=rgb_style(palette['border']),
              box=None, padding=(0,1,0,0))

    t.add_column(style=rgb_style(palette['key']), justify="right", min_width=12)
    t.add_column(style=rgb_style(palette['value']), justify="left", min_width=24)

    def format_row(icon, text, value):
        icon_part = Text(icon, style=Style(color="white", bold=True))
        text_part = Text(f" {text}", style=rgb_style(palette['key']))
        return icon_part + text_part, value

    t.add_row(*format_row("󰀄", "Usuario", info["user"]))
    t.add_row(*format_row("󰃭", "Fecha", info["date"]))
    t.add_row(*format_row("󰥔", "Hora", info["time"]))
    t.add_row(*format_row("󰄛", "Celular", info["phone"]))
    t.add_row(*format_row("󰌽", "OS", info["os"]))
    t.add_row(*format_row("󰘚", "Kernel", info["kernel"]))
    t.add_row(*format_row("󰆍", "Shell", info["shell"]))
    t.add_row(*format_row("󰇊", "Terminal", info["terminal"]))
    t.add_row(*format_row("󰍛", "Memoria",
              create_bar(info['memory_percent'], palette['memory_bar'])))
    t.add_row("", f"{info['memory_used']} / {info['memory_total']}")
    t.add_row(*format_row("󰋊", "Almacenamiento",
              create_bar(info['disk_percent'], palette['disk_bar'])))
    t.add_row("", f"{info['disk_used']} / {info['disk_total']}")
    t.add_row(*format_row("󰩠", "IP",
              Text(info["ip"], style=rgb_style(palette['border']))))

    colors_row = " ".join(f"[rgb({palette[c][0]},{palette[c][1]},{palette[c][2]})]▀▀▀[/]"
                     for c in ['key', 'value', 'memory', 'disk', 'border'])
    t.add_row(*format_row("󰝤", "Paleta", colors_row))

    return Panel(t, title=Text("󱓞 Información del Sistema", style=Style(color="white", bold=True)),
                border_style=rgb_style(palette['border']),
                padding=(1,2))

if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')

    info = get_info()
    terminal_cols = shutil.get_terminal_size().columns
    banner_width = max(len(line) for line in banner.splitlines()) if banner else 0

    min_panel_width = 54
    space_between = 4

    if terminal_cols >= (banner_width + min_panel_width + space_between):
        panel_width = terminal_cols - banner_width - space_between
        panel = create_panel(info, panel_width)
        content = Columns([text_banner, panel], expand=False, equal=False)
    else:
        panel = create_panel(info)
        content = Columns([text_banner, panel], expand=True, equal=False)

    console.print(content)
    console.print("\n" * 1)