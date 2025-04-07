from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import os
import sys

console = Console()

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_title():
    clear_screen()
    console.print(Panel.fit(" Configurador de Banner Stellar ", style="bold blue"))
    console.print()

def get_banner():
    show_title()
    banner_path = os.path.expanduser("~/.configs_stellar/themes/banner.txt")
    
    if os.path.exists(banner_path):
        os.remove(banner_path)
    
    console.print("[bold green]Pulse [bold yellow]Enter[/bold yellow] para crear su nuevo banner[/bold green]")
    input()
    
    os.system(f"touch {banner_path} && nano {banner_path}")
    
    if not os.path.exists(banner_path) or os.path.getsize(banner_path) == 0:
        console.print("[bold red]Error: No se creó el banner o está vacío[/bold red]")
        sys.exit(1)

def show_color_options():
    colors = {
        "Estándar": ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"],
        "Brillantes": ["bright_black", "bright_red", "bright_green", "bright_yellow", 
                      "bright_blue", "bright_magenta", "bright_cyan", "bright_white"],
        "Grises": ["grey0", "grey11", "grey30", "grey50", "grey70", "grey90", "grey93", "grey100"]
    }
    
    for category, color_list in colors.items():
        text = Text(f"\n{category}:\n", style="bold underline")
        for color in color_list:
            text.append(f"{color} ", style=color)
        console.print(text)

def set_banner_color():
    show_title()
    console.print("[bold green]Colores disponibles para el banner:[/bold green]")
    show_color_options()
    
    color = console.input("\n[bold green]Elija un color para su banner (ej: blue): [/bold green]")
    color_path = os.path.expanduser("~/.configs_stellar/themes/banner_color.txt")
    with open(color_path, 'w') as f:
        f.write(color)

def set_background():
    show_title()
    background = console.input("[bold green]¿Desea que el banner tenga fondo? (s/n): [/bold green]").lower()
    
    bg_path = os.path.expanduser("~/.configs_stellar/themes/banner_background.txt")
    with open(bg_path, 'w') as f:
        f.write("si" if background in ['s', 'si', 'sí'] else "no")
    
    if background in ['s', 'si', 'sí']:
        show_title()
        console.print("[bold green]Colores disponibles para el fondo:[/bold green]")
        show_color_options()
        
        bg_color = console.input("\n[bold green]Seleccione un color para el fondo: [/bold green]")
        bg_color_path = os.path.expanduser("~/.configs_stellar/themes/banner_background_color.txt")
        with open(bg_color_path, 'w') as f:
            f.write(bg_color)

def main():
    try:
        themes_dir = os.path.expanduser("~/.configs_stellar/themes")
        os.makedirs(themes_dir, exist_ok=True)
        os.chdir(themes_dir)
        
        get_banner()
        set_banner_color()
        set_background()
        
        show_title()
        console.print(Panel.fit(
            "[bold green]Configuración completada con éxito!\n\n"
            "Escriba [yellow]bash[/yellow] para aplicar los cambios",
            style="bold green"
        ))
        
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
        sys.exit(1)

if __name__ == "__main__":
    main()