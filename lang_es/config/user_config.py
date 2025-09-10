import os
import subprocess
import time
import shutil
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED, HEAVY, DOUBLE, SQUARE
from rich.align import Align
from rich.style import Style
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()
STELLAR_DIR = Path("~/Stellar/lang_es").expanduser()
THEMES_DIR = STELLAR_DIR / "config/themes"
SYSTEM_DIR = STELLAR_DIR / "config/system"
TERMUX_COLORS_PATH = Path("~/.termux/colors.properties").expanduser()
LOGIN_METHOD_PATH = SYSTEM_DIR / "login_method.txt"
THEMES_DIR.mkdir(parents=True, exist_ok=True)
SYSTEM_DIR.mkdir(parents=True, exist_ok=True)

COLOR_PRIMARY = "bold #6A89CC"
COLOR_SECONDARY = "bold #B8E994"
COLOR_ACCENT = "bold #F8C291"
COLOR_SUCCESS = "bold #78E08F"
COLOR_ERROR = "bold #E55039"
COLOR_WARNING = "bold #FAD390"
COLOR_INFO = "bold #4FC1E9"
COLOR_HIGHLIGHT = "bold #FFFFFF on #2C3A47"
COLOR_BG = "#1E272E"
COLOR_PANEL = "#2C3A47"
COLOR_BORDER = "#4FC1E9"

SPINNER = "dots"
SPINNER_SPEED = 0.5

AVAILABLE_COLORS = [...]  # (igual que antes)
TERMUX_THEMES = {...}  # (igual que antes)

def clear_screen():
    os.system("clear")

def display_header(text):
    width = min(shutil.get_terminal_size().columns - 4, 90)
    title = Text.assemble(
        ("★ ", "bold " + COLOR_ACCENT),
        (text, "bold " + COLOR_HIGHLIGHT),
        (" ★", "bold " + COLOR_ACCENT)
    )
    panel = Panel(
        Align.center(title),
        style=f"bold white on {COLOR_BG}",
        padding=(0, 2),
        width=width,
        box=HEAVY,
        border_style=COLOR_BORDER
    )
    console.print(panel, justify="center")
    console.print()

def display_subtitle(text):
    console.print(Align.center(Text(f"» {text} «", style=COLOR_SECONDARY + " dim"), width=80))
    console.print()

def display_error(message):
    console.print(f"[{COLOR_ERROR}]✖ ERROR →[/] {message}", justify="center")

def display_success(message):
    console.print(f"[{COLOR_SUCCESS}]✓ ÉXITO →[/] {message}", justify="center")

def display_warning(message):
    console.print(f"[{COLOR_WARNING}]⚠ ADVERTENCIA →[/] {message}", justify="center")

def display_info(message):
    console.print(f"[{COLOR_INFO}]ℹ INFORMACIÓN →[/] {message}", justify="center")

def display_loading(message):
    with Progress(
        SpinnerColumn(spinner_name=SPINNER, style=COLOR_ACCENT),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
        console=console
    ) as progress:
        progress.add_task(description=message, total=None)
        time.sleep(SPINNER_SPEED)

def is_valid_color(color):
    try:
        Style.parse(color)
        return True
    except Exception:
        return False

def check_termux_api():
    try:
        result = subprocess.run(['pkg', 'list-installed'], capture_output=True, text=True, check=True)
        return 'termux-api' in result.stdout
    except Exception:
        return False

def create_menu_table(options, width=50):
    table = Table.grid(padding=(1, 4), expand=True)
    table.add_column(style=COLOR_ACCENT + " bold", width=10, justify="center")
    table.add_column(style=COLOR_PRIMARY, width=width-14)
    for option, description in options:
        table.add_row(option, description)
    return table

def create_status_table():
    table = Table(
        box=SQUARE,
        header_style=COLOR_ACCENT,
        border_style=COLOR_BORDER,
        expand=True
    )
    table.add_column("Configuración", style=COLOR_PRIMARY, width=25)
    table.add_column("Estado", style=COLOR_SECONDARY, width=25)
    return table

def show_status():
    status_table = create_status_table()

    banner_path = THEMES_DIR / "banner.txt"
    banner_status = "✅ Configurado" if banner_path.exists() else "❌ No configurado"
    status_table.add_row("Banner", banner_status)

    background_path = THEMES_DIR / "banner_background.txt"
    background_enabled = background_path.exists() and background_path.read_text().strip() == "si"
    background_status = "✅ Activado" if background_enabled else "❌ Desactivado"
    status_table.add_row("Fondo de banner", background_status)

    termux_status = "✅ Configurado" if TERMUX_COLORS_PATH.exists() else "❌ No configurado"
    status_table.add_row("Tema Termux", termux_status)

    user_path = SYSTEM_DIR / "user.txt"
    user_status = "✅ Configurado" if user_path.exists() else "❌ No configurado"
    if user_path.exists():
        user_status += f" ({user_path.read_text().strip()})"
    status_table.add_row("Usuario", user_status)

    login_status = "✅ Activado" if LOGIN_METHOD_PATH.exists() and LOGIN_METHOD_PATH.read_text().strip().lower() == "si" else "❌ Desactivado"
    status_table.add_row("Huella digital", login_status)

    termux_api_status = "✅ Instalado" if check_termux_api() else "❌ No instalado"
    status_table.add_row("Termux API", termux_api_status)

    console.print(Align.center(status_table))
    console.print()

def toggle_fingerprint_login():
    clear_screen()
    display_header("ACTIVAR/DESACTIVAR AUTENTICACIÓN POR HUELLA")
    if not check_termux_api():
        display_error("Termux API no está instalada. Instálala con: pkg install termux-api")
        console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")
        return

    current = LOGIN_METHOD_PATH.exists() and LOGIN_METHOD_PATH.read_text().strip().lower() == "si"
    status = "DESACTIVAR" if current else "ACTIVAR"
    if Confirm.ask(f"[{COLOR_ACCENT}]» ¿{status} autenticación por huella?[/]", default=True):
        new_value = "no" if current else "si"
        LOGIN_METHOD_PATH.write_text(new_value)
        display_success(f"Autenticación por huella [bold]{'activada' if new_value == 'si' else 'desactivada'}[/]")
    else:
        display_info("Operación cancelada")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def test_fingerprint_auth():
    clear_screen()
    display_header("PROBAR AUTENTICACIÓN POR HUELLA")
    if not check_termux_api():
        display_error("Termux API no está instalada.")
        console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")
        return

    display_info("Coloca tu dedo en el sensor...")
    result = subprocess.run(["termux-fingerprint"], capture_output=True, text=True)
    if result.returncode == 0 and "AUTH_RESULT_SUCCESS" in result.stdout:
        display_success("Autenticación exitosa ✅")
    else:
        display_error("Autenticación fallida ❌")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def configure_system():
    while True:
        clear_screen()
        display_header("CONFIGURACIÓN DEL SISTEMA")
        options = [
            ("1", "Editar nombre de usuario"),
            ("2", "Mostrar usuario actual"),
            ("3", "Activar/Desactivar huella digital"),
            ("4", "Probar autenticación por huella"),
            ("0", "[bold bright_red]Volver al menú principal[/]")
        ]
        menu_table = create_menu_table(options, width=60)
        console.print(Align.center(menu_table))
        option = Prompt.ask(f"\n[{COLOR_ACCENT}]» Seleccione una opción →[/]")
        if option == "1":
            modify_user()
        elif option == "2":
            show_user()
        elif option == "3":
            toggle_fingerprint_login()
        elif option == "4":
            test_fingerprint_auth()
        elif option == "0":
            break
        else:
            display_error("Opción inválida")
            time.sleep(1)

def main_menu():
    while True:
        clear_screen()
        display_header("STELLAR")
        show_status()
        options = [
            ("1", "Configuración de Banner"),
            ("2", "Configurar Tema Termux"),
            ("3", "Configuración del Sistema"),
            ("0", "[bold bright_red]Salir[/]")
        ]
        menu_table = create_menu_table(options, width=60)
        console.print(Align.center(menu_table))
        option = Prompt.ask(f"\n[{COLOR_ACCENT}]» Seleccione una opción →[/]")
        if option == "1":
            configure_banner()
        elif option == "2":
            configure_termux_theme()
        elif option == "3":
            configure_system()
        elif option == "0":
            clear_screen()
            display_header("¡HASTA PRONTO!")
            display_subtitle("Gracias por usar Stellar")
            time.sleep(2)
            break
        else:
            display_error("Opción inválida")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clear_screen()
        display_header("PROGRAMA INTERRUMPIDO")
        display_warning("El programa fue interrumpido por el usuario")
    except Exception as e:
        clear_screen()
        display_header("ERROR INESPERADO")
        display_error(f"Ocurrió un error: {str(e)}")
        console.input(f"\n[{COLOR_INFO}]Pulsa Enter para salir →[/]")
