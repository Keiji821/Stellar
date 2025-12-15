import os
from os import system
import subprocess
import time
import shutil
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich.table import Table
from rich.box import HEAVY, DOUBLE, SQUARE
from rich.align import Align
from rich.style import Style
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()
STELLAR_DIR = Path("~/Stellar/termux/lang_es").expanduser()
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
COLOR_BORDER = "#4FC1E9"

SPINNER = "dots"
SPINNER_SPEED = 0.5

AVAILABLE_COLORS = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "bright_black", "bright_red", "bright_green", "bright_yellow", "bright_blue",
    "bright_magenta", "bright_cyan", "bright_white",
    "#6A89CC", "#B8E994", "#F8C291", "#78E08F", "#E55039", "#FAD390", "#4FC1E9", "#2C3A47",
    "#1E272E", "#FF5555", "#50FA7B", "#BD93F9", "#BF616A", "#A3BE8C", "#81A1C1", "#CC241D",
    "#98971A", "#458588", "#F7768E", "#9ECE6A", "#7AA2F7", "#E06C75", "#98C379", "#61AFEF",
    "#f92672", "#a6e22e", "#66d9ef", "#dc322f", "#859900", "#268bd2", "#D20F39", "#40A02B",
    "#1E66F5", "#FF3559", "#00FF9D", "#00A1FF", "#E67E80", "#A7C080", "#7FBBB3", "#F28FAD",
    "#ABE9B3", "#96CDFB", "#E95678", "#29D398", "#26BBD9", "#FF0000", "#00FF00", "#0000FF",
    "#00FF41", "#0080FF", "#00CC00", "#0088FF", "#FF0044"
]

TERMUX_THEMES = {
    "dracula": "background=#282a36\nforeground=#f8f8f2\ncolor0=#000000\ncolor1=#ff5555\ncolor2=#50fa7b\ncolor3=#f1fa8c\ncolor4=#bd93f9\ncolor5=#ff79c6\ncolor6=#8be9fd\ncolor7=#bbbbbb\ncolor8=#44475a\ncolor9=#ff5555\ncolor10=#50fa7b\ncolor11=#f1fa8c\ncolor12=#bd93f9\ncolor13=#ff79c6\ncolor14=#8be9fd\ncolor15=#ffffff\n",
    "nord": "background=#2E3440\nforeground=#D8DEE9\ncolor0=#3B4252\ncolor1=#BF616A\ncolor2=#A3BE8C\ncolor3=#EBCB8B\ncolor4=#81A1C1\ncolor5=#B48EAD\ncolor6=#88C0D0\ncolor7=#E5E9F0\ncolor8=#4C566A\ncolor9=#BF616A\ncolor10=#A3BE8C\ncolor11=#EBCB8B\ncolor12=#81A1C1\ncolor13=#B48EAD\ncolor14=#8FBCBB\ncolor15=#ECEFF4\n",
    "gruvbox": "background=#282828\nforeground=#ebdbb2\ncolor0=#282828\ncolor1=#cc241d\ncolor2=#98971a\ncolor3=#d79921\ncolor4=#458588\ncolor5=#b16286\ncolor6=#689d6a\ncolor7=#a89984\ncolor8=#928374\ncolor9=#fb4934\ncolor10=#b8bb26\ncolor11=#fabd2f\ncolor12=#83a598\ncolor13=#d3869b\ncolor14=#8ec07c\ncolor15=#ebdbb2\n",
    "tokyo_night": "background=#1a1b26\nforeground=#a9b1d6\ncolor0=#15161E\ncolor1=#f7768e\ncolor2=#9ece6a\ncolor3=#e0af68\ncolor4=#7aa2f7\ncolor5=#bb9af7\ncolor6=#7dcfff\ncolor7=#c0caf5\ncolor8=#414868\ncolor9=#f7768e\ncolor10=#9ece6a\ncolor11=#e0af68\ncolor12=#7aa2f7\ncolor13=#bb9af7\ncolor14=#7dcfff\ncolor15=#c0caf5\n",
    "one_dark": "background=#282c34\nforeground=#abb2bf\ncolor0=#282c34\ncolor1=#e06c75\ncolor2=#98c379\ncolor3=#e5c07b\ncolor4=#61afef\ncolor5=#c678dd\ncolor6=#56b6c2\ncolor7=#abb2bf\ncolor8=#545862\ncolor9=#e06c75\ncolor10=#98c379\ncolor11=#e5c07b\ncolor12=#61afef\ncolor13=#c678dd\ncolor14=#56b6c2\ncolor15=#c8ccd4\n",
    "monokai": "background=#272822\nforeground=#f8f8f2\ncolor0=#272822\ncolor1=#f92672\ncolor2=#a6e22e\ncolor3=#f4bf75\ncolor4=#66d9ef\ncolor5=#ae81ff\ncolor6=#a1efe4\ncolor7=#f8f8f2\ncolor8=#75715e\ncolor9=#f92672\ncolor10=#a6e22e\ncolor11=#f4bf75\ncolor12=#66d9ef\ncolor13=#ae81ff\ncolor14=#a1efe4\ncolor15=#f9f8f5\n",
    "solarized_dark": "background=#002b36\nforeground=#839496\ncolor0=#073642\ncolor1=#dc322f\ncolor2=#859900\ncolor3=#b58900\ncolor4=#268bd2\ncolor5=#d33682\ncolor6=#2aa198\ncolor7=#eee8d5\ncolor8=#586e75\ncolor9=#cb4b16\ncolor10=#586e75\ncolor11=#657b83\ncolor12=#839496\ncolor13=#6c71c4\ncolor14=#93a1a1\ncolor15=#fdf6e3\n",
    "catppuccin_latte": "background=#eff1f5\nforeground=#4c4f69\ncolor0=#dce0e8\ncolor1=#d20f39\ncolor2=#40a02b\ncolor3=#df8e1d\ncolor4=#1e66f5\ncolor5=#ea76cb\ncolor6=#179299\ncolor7=#acb0be\ncolor8=#bcc0cc\ncolor9=#d20f39\ncolor10=#40a02b\ncolor11=#df8e1d\ncolor12=#1e66f5\ncolor13=#ea76cb\ncolor14=#179299\ncolor15=#4c4f69\n",
    "cyberpunk_neon": "background=#000b1e\nforeground=#0abdc6\ncolor0=#000b1e\ncolor1=#ff3559\ncolor2=#00ff9d\ncolor3=#ffd300\ncolor4=#00a1ff\ncolor5=#b967ff\ncolor6=#00ffff\ncolor7=#a0a0a0\ncolor8=#303030\ncolor9=#ff3559\ncolor10=#00ff9d\ncolor11=#ffd300\ncolor12=#00a1ff\ncolor13=#b967ff\ncolor14=#00ffff\ncolor15=#ffffff\n",
    "everforest": "background=#2b3339\nforeground=#d3c6aa\ncolor0=#2b3339\ncolor1=#e67e80\ncolor2=#a7c080\ncolor3=#dbbc7f\ncolor4=#7fbbb3\ncolor5=#d699b6\ncolor6=#83c092\ncolor7=#d3c6aa\ncolor8=#505a60\ncolor9=#e67e80\ncolor10=#a7c080\ncolor11=#dbbc7f\ncolor12=#7fbbb3\ncolor13=#d699b6\ncolor14=#83c092\ncolor15=#e4e1cd\n",
    "material_ocean": "background=#0f111a\nforeground=#a6accd\ncolor0=#0f111a\ncolor1=#ff5370\ncolor2=#c3e88d\ncolor3=#ffcb6b\ncolor4=#82aaff\ncolor5=#c792ea\ncolor6=#89ddff\ncolor7=#a6accd\ncolor8=#3a3c4e\ncolor9=#ff5370\ncolor10=#c3e88d\ncolor11=#ffcb6b\ncolor12=#82aaff\ncolor13=#c792ea\ncolor14=#89ddff\ncolor15=#d0d0d0\n",
    "horizon": "background=#1c1e26\nforeground=#cbced0\ncolor0=#1c1e26\ncolor1=#e95678\ncolor2=#29d398\ncolor3=#fab795\ncolor4=#26bbd9\ncolor5=#ee64ac\ncolor6=#59e1e3\ncolor7=#cbced0\ncolor8=#6f6f70\ncolor9=#ec6a88\ncolor10=#3fdaa4\ncolor11=#fbc3a7\ncolor12=#3fc4de\ncolor13=#f075b5\ncolor14=#6be4e6\ncolor15=#d5d8da\n",
    "matrix": "background=#000000\nforeground=#00ff00\ncolor0=#000000\ncolor1=#ff0000\ncolor2=#00ff00\ncolor3=#ffff00\ncolor4=#0000ff\ncolor5=#ff00ff\ncolor6=#00ffff\ncolor7=#bbbbbb\ncolor8=#555555\ncolor9=#ff5555\ncolor10=#55ff55\ncolor11=#ffff55\ncolor12=#5555ff\ncolor13=#ff55ff\ncolor14=#55ffff\ncolor15=#ffffff\n",
    "hacker_purple": "background=#000000\nforeground=#00ff41\ncolor0=#000000\ncolor1=#ff0000\ncolor2=#00ff41\ncolor3=#ffff00\ncolor4=#0080ff\ncolor5=#ff00ff\ncolor6=#00ffff\ncolor7=#bbbbbb\ncolor8=#555555\ncolor9=#ff5555\ncolor10=#55ff55\ncolor11=#ffff55\ncolor12=#5555ff\ncolor13=#ff55ff\ncolor14=#55ffff\ncolor15=#ffffff\n",
    "cyberpunk_red": "background=#000000\nforeground=#ff0000\ncolor0=#000000\ncolor1=#ff0000\ncolor2=#00ff00\ncolor3=#ffff00\ncolor4=#0066ff\ncolor5=#ff00ff\ncolor6=#00ffff\ncolor7=#bbbbbb\ncolor8=#555555\ncolor9=#ff5555\ncolor10=#55ff55\ncolor11=#ffff55\ncolor12=#5555ff\ncolor13=#ff55ff\ncolor14=#55ffff\ncolor15=#ffffff\n",
    "hacker_retro": "background=#000000\nforeground=#00cc00\ncolor0=#000000\ncolor1=#ff0044\ncolor2=#00cc00\ncolor3=#ffff00\ncolor4=#0088ff\ncolor5=#ff00ff\ncolor6=#00ffff\ncolor7=#bbbbbb\ncolor8=#555555\ncolor9=#ff5555\ncolor10=#55ff55\ncolor11=#ffff55\ncolor12=#5555ff\ncolor13=#ff55ff\ncolor14=#55ffff\ncolor15=#ffffff\n"
}

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

    login_status = "✅ Activado" if LOGIN_METHOD_PATH.exists() and LOGIN_METHOD_PATH.read_text().strip().lower() == "termux-fingerprint" else "❌ Desactivado"
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

    current = LOGIN_METHOD_PATH.exists() and LOGIN_METHOD_PATH.read_text().strip().lower() == "termux-fingerprint"
    status = "DESACTIVAR" if current else "ACTIVAR"
    if Confirm.ask(f"[{COLOR_ACCENT}]» ¿{status} autenticación por huella?[/]", default=True):
        new_value = "no" if current else "termux-fingerprint"
        LOGIN_METHOD_PATH.write_text(new_value)
        display_success(f"Autenticación por huella [bold]{'activada' if new_value == 'termux-fingerprint' else 'desactivada'}[/]")
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

def configure_banner():
    while True:
        clear_screen()
        display_header("CONFIGURACIÓN DEL BANNER")
        options = [
            ("1", "Editar texto del banner"),
            ("2", "Cambiar color del banner"),
            ("3", "Cambiar color de fondo"),
            ("4", "Activar/Desactivar fondo"),
            ("5", "Vista previa del banner"),
            ("0", "[bold bright_red]Volver al menú principal[/]")
        ]
        menu_table = create_menu_table(options, width=60)
        console.print(Align.center(menu_table))
        option = Prompt.ask(f"\n[{COLOR_ACCENT}]» Seleccione una opción →[/]")
        if option == "1":
            edit_banner_text()
        elif option == "2":
            change_banner_color()
        elif option == "3":
            change_banner_background_color()
        elif option == "4":
            toggle_banner_background()
        elif option == "5":
            banner_preview()
        elif option == "0":
            break
        else:
            display_error("Opción inválida")
            time.sleep(1)

def configure_termux_theme():
    while True:
        clear_screen()
        display_header("CONFIGURAR EL TEMA DE TERMUX")
        options = [
            ("1", "Elegir tema predefinido"),
            ("2", "Crear tema personalizado"),
            ("3", "Mostrar tema actual"),
            ("0", "[bold bright_red]Volver al menú principal[/]")
        ]
        menu_table = create_menu_table(options, width=60)
        console.print(Align.center(menu_table))
        option = Prompt.ask(f"\n[{COLOR_ACCENT}]» Seleccione una opción →[/]")
        if option == "1":
            choose_default_theme()
        elif option == "2":
            create_custom_theme()
        elif option == "3":
            list_current_theme()
        elif option == "0":
            break
        else:
            display_error("Opción inválida")
            time.sleep(1)

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
            ("1", "Configuración del banner"),
            ("2", "Configurar el tema de termux"),
            ("3", "Configuración del sistema"),
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
            os.system("python themes/banner.py")
            break
        else:
            display_error("Opción inválida")
            time.sleep(1)

def edit_banner_text():
    clear_screen()
    display_header("EDITAR TEXTO DEL BANNER")
    display_subtitle("Usa nano para personalizar tu banner")
    path = THEMES_DIR / "banner.txt"
    if not path.exists():
        path.write_text("Stellar Terminal\nPersonaliza tu experiencia")
    subprocess.run(["nano", str(path)])
    display_success("Texto del banner editado correctamente")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def change_banner_color():
    clear_screen()
    display_header("CAMBIAR COLOR DEL BANNER")
    display_subtitle("Selecciona un color de la paleta")
    show_color_palette()
    while True:
        color = Prompt.ask(f"[{COLOR_ACCENT}]» Seleccione color para el banner →[/]").strip().lower()
        if is_valid_color(color):
            break
        display_error(f"Color '{color}' no válido. Intente nuevamente")
    (THEMES_DIR / "banner_color.txt").write_text(color)
    display_success(f"Color del banner actualizado: [{color}]{color}[/]")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def change_banner_background_color():
    clear_screen()
    display_header("CAMBIAR COLOR DE FONDO DEL BANNER")
    display_subtitle("Selecciona un color de fondo")
    show_color_palette()
    while True:
        color = Prompt.ask(f"[{COLOR_ACCENT}]» Seleccione color para el fondo →[/]").strip().lower()
        if is_valid_color(color):
            break
        display_error(f"Color '{color}' no válido. Intente nuevamente")
    (THEMES_DIR / "banner_background_color.txt").write_text(color)
    display_success(f"Color de fondo actualizado: [{color}]{color}[/]")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def toggle_banner_background():
    clear_screen()
    display_header("ACTIVAR/DESACTIVAR FONDO DEL BANNER")
    path = THEMES_DIR / "banner_background.txt"
    current_background = "no"
    if path.exists():
        current_background = path.read_text().strip()
    status = "DESACTIVADO" if current_background == "si" else "ACTIVADO"
    color_status = COLOR_SUCCESS if status == "ACTIVADO" else COLOR_WARNING
    if Confirm.ask(f"[{COLOR_ACCENT}]» ¿{status} fondo del banner?[/]", default=True):
        new_status = "no" if current_background == "si" else "si"
        path.write_text(new_status)
        display_success(f"Fondo del banner [bold {color_status}]{status}[/]")
    else:
        display_info("Operación cancelada")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def banner_preview():
    clear_screen()
    display_header("VISTA PREVIA DEL BANNER")
    path = THEMES_DIR / "banner.txt"
    color_path = THEMES_DIR / "banner_color.txt"
    background_path = THEMES_DIR / "banner_background.txt"
    background_color_path = THEMES_DIR / "banner_background_color.txt"
    if path.exists():
        banner = path.read_text()
        color = color_path.read_text().strip() if color_path.exists() else "bright_white"
        lines = banner.splitlines()
        max_width = max(len(line) for line in lines) if lines else 20
        panel_width = min(max_width + 8, 80)
        style = Style.parse(color) if is_valid_color(color) else Style.parse("bright_white")
        banner_text = Text(banner, style=style)
        background_style = ""
        background_enabled = background_path.exists() and background_path.read_text().strip() == "si"
        if background_enabled:
            background_color = background_color_path.read_text().strip() if background_color_path.exists() else "black"
            if is_valid_color(background_color):
                background_style = Style(bgcolor=background_color)
            else:
                background_style = Style(bgcolor="black")
        preview = Panel(
            Align.center(banner_text),
            title="[bold]VISTA PREVIA",
            border_style=style,
            box=DOUBLE,
            width=panel_width,
            padding=(1, 2),
            style=background_style or ""
        )
        console.print(Align.center(preview))
    else:
        display_warning("No se encontró archivo de banner")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def show_color_palette():
    table = Table.grid(padding=(0, 1), expand=True)
    current_row = []
    for i, color in enumerate(AVAILABLE_COLORS):
        if is_valid_color(color):
            sample = f"[on {color}]   [/] [bold]{color}[/]"
            cell = Panel(sample, width=22, box=SQUARE, border_style="dim")
            current_row.append(cell)
            if len(current_row) == 3 or i == len(AVAILABLE_COLORS) - 1:
                table.add_row(*current_row)
                current_row = []
    console.print(Align.center(table))
    console.print()

def choose_default_theme():
    clear_screen()
    display_header("SELECCIONAR TEMA PREDEFINIDO")
    display_subtitle("Elige un tema de la lista")
    show_themes()
    theme = Prompt.ask(f"\n[{COLOR_ACCENT}]» Elija un tema →[/]").strip()
    if theme in TERMUX_THEMES:
        TERMUX_COLORS_PATH.write_text(TERMUX_THEMES[theme])
        subprocess.run(["termux-reload-settings"])
        display_success(f"Tema [bold]{theme}[/] aplicado")
        display_loading("Aplicando configuración")
    else:
        display_error("Tema no válido")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def create_custom_theme():
    clear_screen()
    display_header("CREAR TEMA PERSONALIZADO")
    display_subtitle("Usa nano para crear tu propio tema")
    if not TERMUX_COLORS_PATH.exists():
        TERMUX_COLORS_PATH.write_text("# Personaliza tu tema\nbackground=#000000\nforeground=#FFFFFF\n")
    subprocess.run(["nano", str(TERMUX_COLORS_PATH)])
    subprocess.run(["termux-reload-settings"])
    display_success("Tema personalizado configurado")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def list_current_theme():
    clear_screen()
    display_header("TEMA ACTUAL TERMUX")
    if TERMUX_COLORS_PATH.exists():
        theme = TERMUX_COLORS_PATH.read_text()
        panel = Panel.fit(
            theme,
            title="[bold]COLORES ACTUALES",
            box=DOUBLE,
            border_style=COLOR_ACCENT,
            padding=(1, 4)
        )
        console.print(Align.center(panel))
    else:
        display_warning("No hay tema configurado")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def show_themes():
    table = Table.grid(padding=(1, 2), expand=True)
    table.add_column("Tema", style=COLOR_ACCENT + " bold", width=20)
    table.add_column("Muestra", style=COLOR_PRIMARY, width=40)
    theme_samples = {
        "dracula": "[#FF5555]█[/][#50FA7B]█[/][#BD93F9]█",
        "nord": "[#BF616A]█[/][#A3BE8C]█[/][#81A1C1]█",
        "gruvbox": "[#CC241D]█[/][#98971A]█[/][#458588]█",
        "tokyo_night": "[#F7768E]█[/][#9ECE6A]█[/][#7AA2F7]█",
        "one_dark": "[#E06C75]█[/][#98C379]█[/][#61AFEF]█",
        "monokai": "[#f92672]█[/][#a6e22e]█[/][#66d9ef]█",
        "solarized_dark": "[#dc322f]█[/][#859900]█[/][#268bd2]█",
        "catppuccin_latte": "[#D20F39]█[/][#40A02B]█[/][#1E66F5]█",
        "cyberpunk_neon": "[#FF3559]█[/][#00FF9D]█[/][#00A1FF]█",
        "everforest": "[#E67E80]█[/][#A7C080]█[/][#7FBBB3]█",
        "material_ocean": "[#F28FAD]█[/][#ABE9B3]█[/][#96CDFB]█",
        "horizon": "[#E95678]█[/][#29D398]█[/][#26BBD9]█",
        "matrix": "[#FF0000]█[/][#00FF00]█[/][#0000FF]█",
        "hacker_purple": "[#FF0000]█[/][#00FF41]█[/][#0080FF]█",
        "cyberpunk_red": "[#FF0000]█[/][#00FF00]█[/][#0066FF]█",
        "hacker_retro": "[#FF0044]█[/][#00CC00]█[/][#0088FF]█"
    }
    for theme, sample in theme_samples.items():
        table.add_row(f"[bold]{theme}[/]", sample)
    console.print(Align.center(table))

def modify_user():
    clear_screen()
    display_header("EDITAR USUARIO")
    user_path = SYSTEM_DIR / "user.txt"
    while True:
        new_user = Prompt.ask(f"[{COLOR_ACCENT}]» Ingrese nuevo nombre de usuario →[/]").strip()
        if new_user:
            user_path.write_text(new_user)
            display_success(f"Usuario [bold]{new_user}[/] configurado")
            break
        display_error("Nombre de usuario no válido")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def show_user():
    clear_screen()
    display_header("USUARIO ACTUAL")
    user_path = SYSTEM_DIR / "user.txt"
    if user_path.exists():
        user = user_path.read_text().strip()
        panel = Panel.fit(
            f"[bold {COLOR_ACCENT}]{user}[/]",
            title="[bold]USUARIO CONFIGURADO",
            box=DOUBLE,
            border_style=COLOR_SUCCESS,
            padding=(1, 4)
        )
        console.print(Align.center(panel))
    else:
        display_warning("No hay usuario configurado")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

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