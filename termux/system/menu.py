from stellar_translate import translate
from rich.console import Console
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
import os

console = Console()


def menu():
    try:
        os.chdir(os.path.expanduser("~/Stellar/configs"))
        with open("user.stel", encoding="utf-8") as f:
            user = f.read().strip()
        if not user:
            user = translate(category="user-config", type="unknown_message")
        hour = datetime.now().strftime("%H:%M:%S")
        if not hour:
            hour = translate(category="user-config", type="unknown_message")
        time = datetime.now().strftime("%Y-%m-%d")
        if not time:
            time = translate(category="user-config", type="unknown_message")    
        
        info_panel = Panel(f"[bold green]● [bold blue]{translate(category="user-config", type="hour_message")}:[/bold blue] {hour} [bold green]● [bold blue]{translate(category="user-config", type="time_message")}:[/bold blue] {time} ● [bold blue]{translate(category="user-config", type="user_message")}:[/bold blue] {user}", border_style="bold cyan")
        console.print(info_panel)
        
        menu_panel = Table(title=translate(category="menu", type="table_title_message"), title_justify="center", title_style="bold green")
        menu_panel.add_column(f"[bold green]{translate(category="menu", type="table_command_message")}", style="code", no_wrap=False)
        menu_panel.add_column(f"[bold green]{translate(category="menu", type="table_description_message")}", style="code", no_wrap=False)
        menu_panel.add_column(f"[bold green]{translate(category="menu", type="table_status_message")}", style="code", no_wrap=False)
        
        menu_panel.add_row(f"[code]{translate(category="menu", type="table_system_message")}", style="bold green")
        menu_panel.add_row("")
        menu_panel.add_row(f"• reload", translate(category="menu", type="reload_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row(f"• user-config", translate(category="menu", type="user-config_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row(f"• my", translate(category="menu", type="my_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row(f"• manager", translate(category="menu", type="manager_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row(f"• bash", translate(category="menu", type="bash_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row(f"• reset", translate(category="menu", type="reset_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row(f"• tor-enable", translate(category="menu", type="tor-enabale_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row(f"• tor-disable", translate(category="menu", type="tor-disable_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row(f"• banner-enable", translate(category="menu", type="banner-enable_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row(f"• banner-disable", translate(category="menu", type="banner-disable_message"), translate(category="menu", type="status_system_message"))
        menu_panel.add_row("")
        menu_panel.add_row(f"[code]{translate(category="menu", type="table_osint_message")}", style="bold green")
        menu_panel.add_row("")
        menu_panel.add_row(f"• ipinfo", translate(category="menu", type="ipinfo_message"), translate(category="menu", type="online_status_message")) 
        menu_panel.add_row(f"• urlinfo", translate(category="menu", type="urlinfo_message"), translate(category="menu", type="online_status_message"))
        menu_panel.add_row(f"• phoneinfo", translate(category="menu", type="phoneinfo_message"), translate(category="menu", type="online_status_message"))
        menu_panel.add_row(f"• metadatainfo", translate(category="menu", type="metadatainfo_message"), translate(category="menu", type="online_status_message"))
        
        console.print(menu_panel, style="bright_white", justify="center")
        
        tips_panel = Panel(translate(category="menu", type="tips_message"), border_style="bold cyan")
        console.print(tips_panel)
        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return
menu()