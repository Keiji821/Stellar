from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
import os
import sys
import configparser

console = Console()
CONFIG_PATH = os.path.expanduser("~/Stellar/config/themes/colors.properties")

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_header(title):
    clear_screen()
    console.print(Panel.fit(f" {title} ", style="bold blue"))
    console.print()

def init_config():
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'w') as f:
            f.write("[Colors]\n")

def update_config(section, key, value):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    
    if not config.has_section(section):
        config.add_section(section)
    
    config.set(section, key, value)
    
    with open(CONFIG_PATH, 'w') as f:
        config.write(f)

def show_color_palette():
    color_table = Table(show_header=False, box=None)
    color_table.add_column(width=25)
    color_table.add_column()
    
    colors = {
        "Basic": ["black", "red", "green", "yellow", 
                 "blue", "magenta", "cyan", "white"],
        "Bright": ["bright_black", "bright_red", "bright_green", 
                  "bright_yellow", "bright_blue", "bright_magenta", 
                  "bright_cyan", "bright_white"],
        "RGB": [f"rgb({r},{g},{b})" for r in [0,128,255] 
               for g in [0,128,255] for b in [0,128,255]]
    }
    
    for category, colors in colors.items():
        color_row = Text(f"\n{category}:\n", style="bold underline")
        for color in colors:
            color_row.append(f" {color} ", style=color)
        color_table.add_row("", color_row)
    
    console.print(color_table)

def configure_element(element_name, config_key):
    show_header(f"Configurar {element_name}")
    console.print(f"[bold green]Seleccione color para {element_name}:[/]")
    show_color_palette()
    
    color = console.input(f"\n[bold green]Color ({element_name}): [/]")
    update_config('Colors', config_key, color)
    
    if console.input("[bold green]¿Agregar fondo? (s/n): [/]").lower() in ['s', 'si']:
        bg_color = console.input("[bold green]Color de fondo: [/]")
        update_config('Colors', f"{config_key}_bg", bg_color)

def create_banner():
    banner_path = os.path.expanduser("~/Stellar/config/themes/banner.txt")
    
    if os.path.exists(banner_path):
        os.remove(banner_path)
    
    console.print("[bold green]Presione Enter para editar el banner[/]")
    input()
    
    os.system(f"nano {banner_path}")
    
    if not os.path.exists(banner_path):
        console.print("[bold red]Error: No se creó el banner[/]")
        sys.exit(1)

def main_menu():
    init_config()
    menu_options = {
        "1": ("Banner Principal", "banner"),
        "2": ("Texto de Estado", "status_text"),
        "3": ("Barras de Progreso", "progress_bars"),
        "4": ("Fondo Global", "background"),
        "5": ("Salir", None)
    }
    
    while True:
        show_header("Menú de Personalización")
        table = Table(box=None)
        table.add_column("[bold cyan]Opción[/]", width=10)
        table.add_column("[bold cyan]Configuración[/]")
        
        for key, (name, _) in menu_options.items():
            table.add_row(f"[bold yellow]{key}[/]", name)
        
        console.print(table)
        choice = console.input("\n[bold green]Seleccione opción: [/]")
        
        if choice == "5":
            break
        elif choice in menu_options:
            if menu_options[choice][1]:
                configure_element(menu_options[choice][0], menu_options[choice][1])
        else:
            console.print("[bold red]Opción inválida![/]")

def main():
    try:
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        create_banner()
        main_menu()
        
        show_header("Configuración Completa")
        console.print(Panel.fit(
            "[bold green]¡Personalización guardada!\n\n"
            "Ejecute [yellow]stellar reload[/] para aplicar cambios",
            style="bold green"
        ))
        
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/]")
        sys.exit(1)

if __name__ == "__main__":
    main()