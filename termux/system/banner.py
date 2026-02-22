from stellar_translate import translate
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
import random

console = Console()

# Funciones

def data():
    try:
        os.chdir(os.path.expanduser("~/Stellar/configs"))
        with open("user.stel", encoding="utf-8") as f:
            user = f.read().strip()
        if not user:
            user = translate(category="banner", type="user_unknown_message")
        shell = os.path.basename(os.getenv("SHELL", "bash"))
        if not shell:
            shell = translate(category="banner", type="shell_unknown_message")
        ram = psutil.virtual_memory()
        processor = platform.machine()
        if not processor:
            processor = translate(category="banner", type="processor_unknown_message")
        system = platform.system()
        if not system:
            system = translate(category="banner", type="system_unknown_message")
        kernel = platform.release()
        if not kernel:
            kernel = translate(category="banner", type="kernel_unknown_message")
        version = platform.version()
        if not version:
            version = translate(category="banner", type="version_unknown_message")
        disk = psutil.disk_usage(os.path.expanduser("~"))
        device = subprocess.getoutput("getprop ro.product.model").strip() or "Desconocido"
        hora = datetime.now().strftime("%H:%M:%S")
        if not hora:
            hora = translate(category="banner", type="hour_unknown_message")
        fecha = datetime.now().strftime("%Y-%m-%d")
        if not fecha:
            fecha = translate(category="banner", type="time_unknown_message")
        return user, processor, system, shell, disk, ram, version, kernel, device, hora, fecha
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return

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
    
    except requests.exceptions.RequestException as e:
        ip = translate(category="user-config", type="unknown_message")
        return ip
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return


def create_bar(pct, color):
    try:
        bar_color = f"rgb({color[0]},{color[1]},{color[2]})"
        return f"[{bar_color}]{'█' * int(pct/5)}{'░' * (20 - int(pct/5))}[/] {pct}%"
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return
user, processor, system, shell, disk, ram, version, kernel, device, hora, fecha = data()
ram_bar = create_bar(ram.percent, (100, 200, 100))
disk_bar = create_bar(disk.percent, (200, 150, 100))

# Principal

def main():
    os.chdir(os.path.expanduser("~/Stellar/configs"))
    with open("banner.stel", encoding="utf-8") as f:
        banner = f.read().strip()
    with open("banner_color.stel", encoding="utf-8") as f:
        banner_color = f.read().strip()
    with open("banner_background.stel", encoding="utf-8") as f:
        banner_background = f.read().strip()
    with open("banner_background_color.stel", encoding="utf-8") as f:
        banner_background_color = f.read().strip()
    try:
        def get_type_ip():
            try:
                response = requests.get(f"https://api.ipapi.is/?ip=")
                data = response.json()
                is_tor = data.get("is_tor")
                is_vpn = data.get("is_vpn")
                is_proxy = data.get("is_proxy")
                if is_tor == True:
                    message_ip = translate(category="banner", type="tor_ip_message")
                elif is_tor == False:
                    if is_vpn == True:
                        message_ip = translate(category="banner", type="vpn_ip_message")
                    elif is_vpn == False:
                        if is_proxy == True:
                            message_ip = translate(category="banner", type="proxy_ip_message")
                        elif is_proxy == False:
                            message_ip = translate(category="banner", type="public_ip_message")
                else:
                    message_ip = translate(category="banner", type="ip_unknown2_message")
                return message_ip
                
            except requests.exceptions.ConnectionError:
                message_ip = translate(category="banner", type="not_internet_message")
                return message_ip
            except Exception as e:
                console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
                message_ip = translate(category="banner", type="ip_unknown_message")
                return message_ip
        ip = http()
        message_ip = get_type_ip()
        user, processor, system, shell, disk, ram, version, kernel, device, hora, fecha = data()
        
        if banner_background != "y" and "yes":
            console.print(banner, style=f"{banner_color}")
        elif banner_background == "y" and "yes":
            console.print(f"[{banner_color}][code][{banner_background_color}]{banner}[/]")
            
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
                icon_system = "󰌽"
                icon_kernel = "󰘚"
                icon_version = "󰇊"
                icon_palette = ""
                icon_device = ""
                colors_list1 = [
                    "#00FF00", "#32CD32", "#008000", "#90EE90", "#00FF7F",
                    "#FFFF00", "#FFD700", "#FFA500", "#FF8C00", "#FF6347",
                    "#0000FF", "#1E90FF", "#4169E1", "#00BFFF", "#87CEEB",
                    "#00FFFF", "#40E0D0", "#20B2AA", "#008B8B", "#5F9EA0",
                    "#FF1493", "#FF69B4", "#DB7093", "#C71585", "#FF00FF",
                    "#8B0000", "#B22222", "#DC143C", "#FF4500", "#800000",
                    "#9400D3", "#8A2BE2", "#4B0082", "#9932CC", "#BA55D3",
                    "#FFFFFF", "#D3D3D3", "#A9A9A9", "#696969", "#000000",
                    "#FFE4E1", "#FAF0E6", "#F5F5DC", "#F0FFF0", "#F0FFFF",
                    "#FFF0F5", "#FFFAFA", "#F8F8FF", "#F5FFFA", "#FDF5E6",
                    "#8B4513", "#D2691E", "#A0522D", "#CD853F", "#DEB887"
                    ]
                colors_list2 = [
                    "#FF6B6B", "#FF9F43", "#FFD93D", "#6BCF7F", "#4D96FF",
                    "#845EC2", "#D65DB1", "#FF5C8D", "#C34A36", "#FF8066",
                    "#00C9A7", "#00D2FC", "#4FFBDF", "#A162E8", "#FEFFAC",
                    "#5EFFB1", "#B465FF", "#FF8E8E", "#87FFAB", "#FFB8DE",
                    "#7045AF", "#2B7DE9", "#2CEAA3", "#FFD166", "#EF476F",
                    "#38B000", "#9B5DE5", "#F15BB5", "#00BBF9", "#00F5D4",
                    "#B5E48C", "#D9ED92", "#FFD6FF", "#E2C2FF", "#A9D6E5",
                    "#8AC926", "#1982C4", "#6A4C93", "#FF595E", "#FFCA3A",
                    "#8AC926", "#1982C4", "#6A4C93", "#FF595E", "#FFCA3A",
                    "#6A0572", "#AB83A1", "#3CBBB1", "#F0B67F", "#FE5F55"
                    ]
                colors1 = random.choice(colors_list1)
                colors2 = random.choice(colors_list2)

                table = Table(show_header=False, show_lines=False, box=None)
                table.add_column(style=Style(color=f"{colors2}"), justify="right")
                table.add_column(style=Style(color="bright_white"), justify="left")
                table.add_column(justify="left")

                table.add_row(f"{icon_user} {translate(category="banner", type="user_message")}", str(user))
                table.add_row(f"{icon_hora} {translate(category="banner", type="hour_message")}", str(hora))
                table.add_row(f"{icon_fecha} {translate(category="banner", type="time_message")}", str(fecha))
                table.add_row(f"{icon_shell} {translate(category="banner", type="shell_message")}", str(shell))
                table.add_row(f"{icon_device} {translate(category="banner", type="device_message")}", str(device))
                table.add_row(f"{icon_system} {translate(category="banner", type="system_message")}", str(system))
                table.add_row(f"{icon_kernel} {translate(category="banner", type="kernel_message")}", str(kernel))
                table.add_row(f"{icon_version} {translate(category="banner", type="version_message")}", str(version))
                table.add_row(f"{icon_cpu} {translate(category="banner", type="processor_message")}", str(processor))
                table.add_row(f"{icon_ram} {translate(category="banner", type="ram_message")}", ram_bar)
                table.add_row("", f"{ram.used//(1024**2):,} MB / {ram.total//(1024**2):,} MB")
                table.add_row(f"{icon_disk} {translate(category="banner", type="cpu_message")}", disk_bar)
                table.add_row("", f"{disk.used//(1024**3):,} GB / {disk.total//(1024**3):,} GB")
                table.add_row(f"{icon_ip} {translate(category="banner", type="ip_message")}", str(ip), message_ip)
                table.add_row(f"{icon_palette} {translate(category="banner", type="palette_colors_message")}", f"[{colors1}]▅▅▅▅ [{colors2}]▅▅▅▅ [{banner_color}]▅▅▅▅ [{banner_background_color}]▅▅▅▅") 
                panel = Panel(table, title=f"[bold white]{translate(category="banner", type="banner_title_message")}[/bold white]", border_style=f"{colors1}")
                console.print(panel)
            except Exception as e:
                console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
                return
        banner()
        console.print("\n")
        console.print("\n")
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return
main()