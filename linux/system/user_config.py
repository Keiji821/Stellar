from stellar_translate import translate
from rich.console import Console
from datetime import datetime
from rich.panel import Panel
from os import system
import subprocess
import yaml
import time
import os

console = Console()
    
def banner():
    try:
        ruta = os.path.expanduser("~/Stellar/configs")
        os.chdir(ruta)
        user = subprocess.Popen(['whoami'])
        if not user:
            user = translate(category="user-config", type="unknown_message")
        hour = datetime.now().strftime("%H:%M:%S")
        if not hour:
            hour = translate(category="user-config", type="unknown_message")
        time = datetime.now().strftime("%Y-%m-%d")
        if not time:
            time = translate(category="user-config", type="unknown_message")
        subprocess.Popen(['clear'])
        info_banner = Panel(f"[bold green]● [bold blue]{translate(category="user-config", type="hour_message")}:[/bold blue] {hour} [bold green]● [bold blue]{translate(category="user-config", type="time_message")}:[/bold blue] {time} ● [bold blue]{translate(category="user-config", type="user_message")}:[/bold blue] {user}", border_style="bold cyan")
        banner = Panel(f"""
        [bold blue][1][/bold blue] {translate(category="user-config", type="banner_config_message")}
        [bold blue][2][/bold blue] {translate(category="user-config", type="banner_color_config_message")}
        [bold blue][3][/bold blue] {translate(category="user-config", type="banner_background_config_message")}
        [bold blue][4][/bold blue] {translate(category="user-config", type="theme_config_message")}
        [bold blue][5][/bold blue] {translate(category="user-config", type="font_config_message")}
        [bold blue][6][/bold blue] {translate(category="user-config", type="user_config_message")}
        [bold blue][7][/bold blue] {translate(category="user-config", type="login_config_message")}
        [bold blue][8][/bold blue] {translate(category="user-config", type="lang_config_message")}
        
        [bold red][0] [code]{translate(category="user-config", type="exit_message")}[/code][/bold red]
        """, 
        title=f"[bold green]{translate(category="user-config", type="config_message")}[/bold green]", 
        subtitle=f"[bold red]{translate(category="user-config", type="subtitle_message")}[/bold red]", 
        border_style="bold cyan"
        )
        tips_banner = Panel(translate(category="user-config", type="tips_message"), border_style="bold cyan")
        console.print(info_banner)
        console.print(banner)
        console.print(tips_banner)
        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return
    
def config(option=None):
    try:
        if option == "1":
            subprocess.Popen(['clear'])
            time.sleep(1)
            ruta = os.path.expanduser("~/Stellar/configs")
            os.chdir(ruta)
            edit = subprocess.Popen(['nano', 'banner.stel'])
            edit.wait()
            time.sleep(1)
            console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
            time.sleep(2)
            banner()
            
        elif option == "2":
            subprocess.Popen(['clear'])
            time.sleep(1)
            console.print(f"[bold green][INFO][/bold green] {translate(category="user-config", type="banner_color_activate_message")}")
            color = console.input(f"[bold green]{translate(category="user-config", type="enter_message")} [/bold green]")
            os.system(f"cd ~/Stellar/configs && echo {color} > banner_color.stel")
            console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
            time.sleep(2)
            banner()
            
        elif option == "3":
            subprocess.Popen(['clear'])
            time.sleep(1)
            isbanner_background = console.input(f"[bold green]{translate(category="user-config", type="banner_background_activate_message")} [/bold green]")
            if isbanner_background == "y":
                os.system(f"cd ~/Stellar/configs && echo {isbanner_background} > banner_background.stel")
                console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                console.print()
                time.sleep(2)
                console.print(f"[bold cyan][INFO][/bold cyan] {translate(category="user-config", type="banner_background_color_activate_message")}")
                iscolor = console.input(f"[bold green]{translate(category="user-config", type="enter_message")} [/bold green]")
                if iscolor:
                    os.system(f"cd ~/Stellar/configs && echo {iscolor} > banner_background_color.stel")
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                else:
                    console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")    
                    time.sleep(2)
                    return
                
            elif isbanner_background == "n":
                os.system(f"cd ~/Stellar/configs && echo {isbanner_background} > banner_background.stel")
                console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                time.sleep(2)
                banner()
                return
                
            else:
                console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                time.sleep(2)
                return
        
        elif option == "4":
            subprocess.Popen(['clear'])
            time.sleep(1)
            themes = (
                "Stellar", "Horizon", "Everforest"
                )
            numbs = (
                "1", "2", "3"
                )
            list_themes = Panel(f"""
            
            [bold blue][1][/bold blue] Stellar
            [bold blue][2][/bold blue] Horizon
            [bold blue][3][/bold blue] Everforest
            
            [bold blue][0][/bold blue] [code][bold red]{translate(category="user-config", type="default_theme_message")}[/bold red][/code]
            
            """, title=translate(category="user-config", type="themes_title_message"), border_style="bold cyan")
            tips_banner = Panel(translate(category="user-config", type="tips_message"), border_style="bold cyan")
            console.print(list_themes)
            console.print(tips_banner)
            theme_type = console.input(f"[bold green]{translate(category="user-config", type="enter_message")} [/bold green]")
            if theme_type:
                if theme_type == "0":
                    os.system("rm -rf ~/.termux/colors.properties")
                    subprocess.Popen(["termux-reload-settings"])
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                elif theme_type == "Stellar" or theme_type == "1":
                    ruta = os.path.expanduser("~/Stellar/resources/themes")
                    os.chdir(ruta)
                    with open("stellar.stel", encoding="utf-8") as f:
                        theme = f.read().strip()
                    os.system(f"""
cat > ~/.termux/colors.properties << 'EOF'
{theme}
EOF
                    """)
                    subprocess.Popen(["termux-reload-settings"])
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                elif theme_type == "Horizon" or theme_type == "2":
                    ruta = os.path.expanduser("~/Stellar/resources/themes")
                    os.chdir(ruta)
                    with open("horizon.stel", encoding="utf-8") as f:
                        theme = f.read().strip()
                    os.system(f"""
cat > ~/.termux/colors.properties << 'EOF'
{theme}
EOF
                    """)
                    subprocess.Popen(["termux-reload-settings"])
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                elif theme_type == "Everforest" or theme_type == "3":
                    ruta = os.path.expanduser("~/Stellar/resources/themes")
                    os.chdir(ruta)
                    with open("everforest.stel", encoding="utf-8") as f:
                        theme = f.read().strip()
                    os.system(f"""
cat > ~/.termux/colors.properties << 'EOF'
{theme}
EOF
                    """)
                    subprocess.Popen(["termux-reload-settings"])
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                else:
                    console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                    time.sleep(2)
                    return
            else:
                console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                time.sleep(2)
                return
        
        elif option == "5":
            time.sleep(1)
            console.print(f"[bold cyan][INFO][/bold cyan] {translate(category="user-config", type="close_option_message")}")
            time.sleep(2)
            banner()            
            
        elif option == "6":
            time.sleep(1)
            console.print(f"[bold cyan][INFO][/bold cyan] {translate(category="user-config", type="close_option_message")}")
            time.sleep(2)
            banner()
            
        elif option == "7":
            time.sleep(1)
            console.print(f"[bold cyan][INFO][/bold cyan] {translate(category="user-config", type="close_option_message")}")
            time.sleep(2)
            banner()
        
        elif option == "8":
            subprocess.Popen(['clear'])
            time.sleep(1)
            langs = (
                "Español", "English", "Japanese", 
                "Chinese", "Portuguese", "Korean"
                )
            numbs = (
                "1", "2", "3", 
                "4", "5", "6"
                )
            list_fonts = Panel("""
            
            [bold blue][1][/bold blue] Español
            [bold blue][2][/bold blue] English
            [bold blue][3][/bold blue] Japanese
            [bold blue][4][/bold blue] Chinese
            [bold blue][5][/bold blue] Korean
            [bold blue][6][/bold blue] Portuguese
            
            """, title=translate(category="user-config", type="langs_title_message"), border_style="bold cyan")
            tips_banner = Panel(translate(category="user-config", type="tips_message"), border_style="bold cyan")
            console.print(list_fonts)
            console.print(tips_banner)
            lang_type = console.input(f"[bold green]{translate(category="user-config", type="enter_message")} [/bold green]")
            if lang_type:
                if lang_type == "Español" or lang_type == "1":
                    os.system("cd ~/Stellar/configs && echo spanish > selected_lang.txt")
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                    
                elif lang_type == "English" or lang_type == "2":
                    os.system(f"cd ~/Stellar/configs && echo english > selected_lang.txt")
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                 
                elif lang_type == "Japanese" or lang_type == "3":
                    os.system("cd ~/Stellar/configs && echo japanese > selected_lang.txt")
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                    
                elif lang_type == "Chinese" or lang_type == "4":
                    os.system("cd ~/Stellar/configs && echo chinese > selected_lang.txt")
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                    
                elif lang_type == "Korean" or lang_type == "5":
                    os.system("cd ~/Stellar/configs && echo korean > selected_lang.txt")
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                    
                elif lang_type == "Portuguese" or lang_type == "6":
                    os.system("cd ~/Stellar/configs && echo portuguese > selected_lang.txt")
                    console.print(f"[bold green][SUCCESS][/bold green] {translate(category="user-config", type="success_message")}")
                    time.sleep(2)
                    banner()
                    
                else:
                    time.sleep(2)
                    console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                    return
            
        else:
            time.sleep(2)
            return
        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
        return
    
def main():
    try:
        while True:
            banner()
            data = console.input(f"[bold green]➤  {translate(category="user-config", type="enter_message")} [/bold green]")
            
            if data == "1":
                config(option="1")
            
            elif data == "2":
                config(option="2")
            
            elif data == "3":
                config(option="3")
            
            elif data == "4":
                config(option="4")
            
            elif data == "5":
                config(option="5")
            
            elif data == "6":
                config(option="6")
            
            elif data == "7":
                config(option="7")
                
            elif data == "8":
                config(option="8")
            
            elif data == "0":
                console.print(f"[bold cyan][INFO][/bold cyan] {translate(category="user-config", type="leave_message")}")
                time.sleep(3)
                os.system("clear")
                os.system("python ~/Stellar/termux/system/banner.py")
                exit()
            
            else:
                console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="invalid_data_message")}")
                time.sleep(2)
                banner()
                continue
        
        console.print()
        console.print()
        
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category="user-config", type="error_message")} > {e}")
        return
    
main()