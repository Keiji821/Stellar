from stellar_translate import translate
from rich.console import Console
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
import requests
import os

console = Console()


def configs():
    try:
        os.chdir(os.path.expanduser("~/Stellar/configs"))
        
        with open("user.stel", encoding="utf-8") as f:
            user = f.read().strip()
            
        with open("banner.stel", encoding="utf-8") as f:
            banner = f.read().strip()
            
        with open("banner_color.stel", encoding="utf-8") as f:
            banner_color = f.read().strip()
            
        with open("banner_background.stel", encoding="utf-8") as f:
            banner_background = f.read().strip()
            
        with open("banner_background_color.stel", encoding="utf-8") as f:
            banner_background_color = f.read().strip()

        with open("isbanner.stel", encoding="utf-8") as f:
            isbanner = f.read().strip()
            
        with open("login_method.stel", encoding="utf-8") as f:
            login_method = f.read().strip()
            
        with open("password.stel", encoding="utf-8") as f:
            password = f.read().strip()
            
        with open("selected_lang.txt", encoding="utf-8") as f:
            selected_lang = f.read().strip()
            
        
        return user, banner, banner_color, banner_background, banner_background_color, isbanner, selected_lang, password, login_method
        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='error_message')} > {e}")
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
        
        return message_ip, ip

    except requests.exceptions.RequestException as e:
        ip = translate(category="user-config", type="unknown_message")
        message_ip = translate(category="banner", type="not_internet_message")
        return ip, message_ip
    except requests.exceptions.ConnectionError:
        ip = translate(category="user-config", type="unknown_message")
        message_ip = translate(category="banner", type="not_internet_message")
        return ip, message_ip
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return


def user():
    try:
        user, banner, banner_color, banner_background, banner_background_color, isbanner, selected_lang, password, login_method = configs()
        message_ip, ip = http()
        
        if banner_background == "y" and "yes":
            is_banner_background = translate(category="user", type="background_banner_active_message")
        elif banner_background != "y" and "yes":
            is_banner_background = translate(category="user", type="background_banner_idle_message")
            
        if isbanner == "y" and "yes":
            is_banner = translate(category="user", type="isbanner_active_message")
        elif isbanner != "y" and "yes":
            is_banner = translate(category="user", type="isbanner_inactive_message")
        
        info_panel = Panel(f"""
        
        [code][bold green]{translate(category="user", type="preferences_message")}[/bold green][/code]
        
        [bold green]●[/bold green] [bold cyan]{translate(category="user-config", type="user_message")}:[/bold cyan] {user}
        [bold green]●[/bold green] [bold cyan]{translate(category="user", type="banner_color_message")}:[/bold cyan] [{banner_color}]{banner_color}[/{banner_color}]
        [bold green]●[/bold green] [bold cyan]{translate(category="user", type="banner_background_color_message")}:[/bold cyan] [{banner_background_color}]{banner_background_color}[/{banner_background_color}]
        [bold green]●[/bold green] [bold cyan]{translate(category="user", type="banner_background_message")}:[/bold cyan] {is_banner_background}
        [bold green]●[/bold green] [bold cyan]{translate(category="user", type="isbanner_message")}:[/bold cyan] {is_banner}
        
        [code][bold green]{translate(category="user", type="configurations_message")}[/bold green][/code]
        
        [bold green]●[/bold green] [bold cyan]{translate(category="user", type="login_method_message")}:[/bold cyan] {login_method}
        [bold green]●[/bold green] [bold cyan]{translate(category="user", type="password_message")}:[/bold cyan] {password}
        
        [code][bold green]{translate(category="user", type="red_message")}[/bold green][/code]
        
        [bold green]●[/bold green] [bold cyan]{translate(category="banner", type="ip_message")}:[/bold cyan] [italic]{ip}[/italic]
        [bold green]●[/bold green] [bold cyan]{translate(category="user", type="ip_type_message")}[/bold cyan] > {message_ip}
        
        
        
        """, title=f"[bold green]{translate(category="user", type="title_user_message")}[/bold green]", 
        subtitle=f"[bold red]{translate(category="user-config", type="subtitle_message")}[/bold red]", border_style="bold cyan")
        
        console.print(info_panel)
        
        if banner:
            if banner_background != "y" and "yes":
                default_banner = Panel(banner, border_style="bold cyan", subtitle=f"[bold cyan]{translate(category="user", type="banner_message")}[/bold cyan]")
                console.print(default_banner, style=f"{banner_color}")
            elif banner_background == "y" and "yes":
                background_banner = Panel(f"[{banner_color}][code][{banner_background_color}]{banner}[/]", border_style="bold cyan")
                console.print(background_banner)
        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='error_message')} > {e}")
        return
user()