from rich.console import Console
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
import os, platform, psutil
from rich.text import Text
from os import system
import subprocess 
import requests

console = Console()

ruta = "~/Stellar/linux/lang_es/config/themes"

user = subprocess.getoutput(["hostname"]) or subprocess.getoutput(["whoami"]) 
shell = psutil.Process().parent().name() 
ram = psutil.virtual_memory()
processor = platform.machine()
disk = psutil.disk_usage(os.path.expanduser("~"))
hora = datetime.now().strftime("%H:%M:%S")
fecha = datetime.now().strftime("%Y-%m-%d")
os.chdir(os.path.expanduser(f"{ruta}"))

# Funciones

def http():
    try:
        response = requests.get("https://ipinfo.io/ip")
        ip = response.text
        if response.status_code != 200:
            response = requests.get("https://ident.me")
            ip = response.text
            if response.status_code != 200:
                response = requests.get("https://ifconfig.me/ip")
                ip = response.text
                if response.status_code != 200:
                    response = requests.get("https://api.ipify.org")
                    ip = response.text
        return ip
    except Exception as e:
        console.print(f"[bold red][STELLAR] [bold white]Ha ocurrido un error en Stellar, error: [bold red]{e}")
        return "[bold red] No disponible"

def create_bar(pct, color):
    try:
        bar_color = f"rgb({color[0]},{color[1]},{color[2]})"
        return f"[{bar_color}]{'█' * int(pct/5)}{'░' * (20 - int(pct/5))}[/] {pct}%"
    except Exception as e:
        console.print(f"[bold red][STELLAR] [bold white]Ha ocurrido un error en Stellar, error: [bold red]{e}")
ram_bar = create_bar(ram.percent, (100, 200, 100))
disk_bar = create_bar(disk.percent, (200, 150, 100))

# Principal

def main():
    with open("banner.st", encoding="utf-8") as f:
        banner = f.read().strip()
    with open("banner_color.st", encoding="utf-8") as f:
        banner_color = f.read().strip()
    with open("banner_background.st", encoding="utf-8") as f:
        banner_background = f.read().strip()
    with open("banner_background_color.st", encoding="utf-8") as f:
        banner_background_color = f.read().strip()
    try:
        ip = http()
        console.print(banner, style=f"{banner_color}")
        if banner_background == ("si", "sí"):
            bg_banner = Text(banner, style=Style(color=f"{banner_color}", bold=True, bgcolor=f"{banner_background_color}"))
            console.print(banner, style=f"{banner_color}")
        def banner():
            try:
                icon_user = "󰀄"
                icon_hora = "󰃭"
                icon_fecha = "󰥔"
                icon_ram = "󰍛"
                icon_disk = "󰋊"
                icon_cpu = "󰘚"
                icon_shell = "󰆍"
                icon_ip = "󰩠"
                table = Table(show_header=False, show_lines=False, box=None)
                table.add_column(style=Style(color="cyan"), justify="right")
                table.add_column(style=Style(color="white"), justify="left")

                table.add_row(f"{icon_user} Usuario", user)
                table.add_row(f"{icon_hora} Hora", str(hora))
                table.add_row(f"{icon_fecha} Fecha", str(fecha))
                table.add_row(f"{icon_shell} Shell", shell)
                table.add_row(f"{icon_cpu} Procesador", processor)
                table.add_row(f"{icon_ram} RAM:", ram_bar)
                table.add_row("", f"{ram.used//(1024**2):,} MB / {ram.total//(1024**2):,} MB")
                table.add_row(f"{icon_disk} Disco:", disk_bar)
                table.add_row("", f"{disk.used//(1024**3):,} GB / {disk.total//(1024**3):,} GB")
                table.add_row(f"{icon_ip} IP", str(ip))

                panel = Panel(table, title="Sistema", border_style="bold blue")
                console.print(panel)
            except Exception as e:
                console.print(f"[bold red][STELLAR] [bold white]Ha ocurrido un error en Stellar, error: [bold red]{e}")
        banner()
        console.print("\n")
        console.print("\n")
    except Exception as e:
        console.print(f"[bold red][STELLAR] [bold white]Ha ocurrido un error en Stellar, error: [bold red]{e}")
main()