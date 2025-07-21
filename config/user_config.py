import os
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED, HEAVY, DOUBLE
from rich.align import Align
from rich.style import Style
from pathlib import Path

console = Console()
STELLAR_DIR = Path("~/Stellar").expanduser()
THEMES_DIR = STELLAR_DIR / "config/themes"
SYSTEM_DIR = STELLAR_DIR / "config/system"
TERMUX_COLORS_PATH = Path("~/.termux/colors.properties").expanduser()
THEMES_DIR.mkdir(parents=True, exist_ok=True)
SYSTEM_DIR.mkdir(parents=True, exist_ok=True)

COLOR_PRIMARY = "bold cyan"
COLOR_SECONDARY = "bold magenta"
COLOR_ACCENT = "bold yellow"
COLOR_SUCCESS = "bold green"
COLOR_ERROR = "bold red"
COLOR_WARNING = "bold yellow"
COLOR_INFO = "bold blue"
COLOR_HIGHLIGHT = "bold white on rgb(40,42,54)"

TERMUX_THEMES = {
    "dracula": """
background=#282A36
foreground=#F8F8F2
color0=#21222C
color1=#FF5555
color2=#50FA7B
color3=#F1FA8C
color4=#BD93F9
color5=#FF79C6
color6=#8BE9FD
color7=#BFBFBF
color8=#4D4D4D
color9=#FF6E67
color10=#5AF78E
color11=#F4F99D
color12=#CAA9FA
color13=#FF92D0
color14=#9AEDFE
color15=#E6E6E6
""",
    "nord": """
background=#2E3440
foreground=#D8DEE9
color0=#3B4252
color1=#BF616A
color2=#A3BE8C
color3=#EBCB8B
color4=#81A1C1
color5=#B48EAD
color6=#88C0D0
color7=#E5E9F0
color8=#4C566A
color9=#D08770
color10=#8FBCBB
color11=#ECEFF4
color12=#5E81AC
color13=#EBCB8B
color14=#B48EAD
color15=#FFFFFF
""",
    "gruvbox": """
background=#282828
foreground=#EBDBB2
color0=#1D2021
color1=#CC241D
color2=#98971A
color3=#D79921
color4=#458588
color5=#B16286
color6=#689D6A
color7=#A89984
color8=#928374
color9=#FB4934
color10=#B8BB26
color11=#FABD2F
color12=#83A598
color13=#D3869B
color14=#8EC07C
color15=#EBDBB2
""",
    "tokyo_night": """
background=#1A1B26
foreground=#A9B1D6
color0=#16161E
color1=#F7768E
color2=#9ECE6A
color3=#E0AF68
color4=#7AA2F7
color5=#BB9AF7
color6=#7DCFFF
color7=#C0CAF5
color8=#414868
color9=#FF7A93
color10=#B9F27C
color11=#FF9E64
color12=#7AA2F7
color13=#BB9AF7
color14=#0DB9D7
color15=#FFFFFF
""",
    "one_dark": """
background=#282C34
foreground=#ABB2BF
color0=#1E2127
color1=#E06C75
color2=#98C379
color3=#E5C07B
color4=#61AFEF
color5=#C678DD
color6=#56B6C2
color7=#DCDFE4
color8=#5C6370
color9=#BE5046
color10=#7ECA9C
color11=#D19A66
color12=#4FA6ED
color13=#BF68D9
color14=#48B0BD
color15=#FFFFFF
""",
    "monokai": """
background=#272822
foreground=#f8f8f2
cursor=#f8f8f2
color0=#272822
color1=#f92672
color2=#a6e22e
color3=#f4bf75
color4=#66d9ef
color5=#ae81ff
color6=#a1efe4
color7=#f8f8f2
color8=#75715e
color9=#f92672
color10=#a6e22e
color11=#f4bf75
color12=#66d9ef
color13=#ae81ff
color14=#a1efe4
color15=#f9f8f5
""",
    "solarized_dark": """
background=#002b36
foreground=#839496
cursor=#839496
color0=#073642
color1=#dc322f
color2=#859900
color3=#b58900
color4=#268bd2
color5=#d33682
color6=#2aa198
color7=#eee8d5
color8=#586e75
color9=#cb4b16
color10=#859900
color11=#b58900
color12=#268bd2
color13=#6c71c4
color14=#2aa198
color15=#fdf6e3
""",
    "catppuccin_latte": """
background=#EFF1F5
foreground=#4C4F69
cursor=#4C4F69
color0=#5C5F77
color1=#D20F39
color2=#40A02B
color3=#DF8E1D
color4=#1E66F5
color5=#EA76CB
color6=#179299
color7=#ACB0BE
color8=#6C6F85
color9=#D20F39
color10=#40A02B
color11=#DF8E1D
color12=#1E66F5
color13=#EA76CB
color14=#179299
color15=#BCC0CC
""",
    "cyberpunk_neon": """
background=#0C0C0C
foreground=#00FF9D
cursor=#00FF9D
color0=#000000
color1=#FF3559
color2=#00FF9D
color3=#FFD700
color4=#00A1FF
color5=#FF00AA
color6=#00FFFF
color7=#CCCCCC
color8=#333333
color9=#FF3559
color10=#00FF9D
color11=#FFD700
color12=#00A1FF
color13=#FF00AA
color14=#00FFFF
color15=#FFFFFF
""",
    "everforest": """
background=#2B3339
foreground=#D5C9AB
cursor=#D5C9AB
color0=#4B565C
color1=#E67E80
color2=#A7C080
color3=#DBBC7F
color4=#7FBBB3
color5=#D699B6
color6=#83C092
color7=#D5C9AB
color8=#4B565C
color9=#E67E80
color10=#A7C080
color11=#DBBC7F
color12=#7FBBB3
color13=#D699B6
color14=#83C092
color15=#DEE2D9
""",
    "material_ocean": """
background=#0F111A
foreground=#8F93A2
cursor=#8F93A2
color0=#1E1E2E
color1=#F28FAD
color2=#ABE9B3
color3=#FAE3B0
color4=#96CDFB
color5=#D5AEEA
color6=#89DCEB
color7=#BAC2DE
color8=#585B70
color9=#F28FAD
color10=#ABE9B3
color11=#FAE3B0
color12=#96CDFB
color13=#D5AEEA
color14=#89DCEB
color15=#A6ADC8
""",
    "horizon": """
background=#1C1E26
foreground=#CBCED0
cursor=#CBCED0
color0=#16161C
color1=#E95678
color2=#29D398
color3=#FAB795
color4=#26BBD9
color5=#EE64AC
color6=#59E1E3
color7=#CBCED0
color8=#3E4058
color9=#E95678
color10=#29D398
color11=#FAB795
color12=#26BBD9
color13=#EE64AC
color14=#59E1E3
color15=#E6E6E6
""",
    "matrix": """
background=#000000
foreground=#00FF00
cursor=#00FF00
color0=#000000
color1=#FF0000
color2=#00FF00
color3=#FFFF00
color4=#0000FF
color5=#FF00FF
color6=#00FFFF
color7=#BBBBBB
color8=#555555
color9=#FF5555
color10=#55FF55
color11=#FFFF55
color12=#5555FF
color13=#FF55FF
color14=#55FFFF
color15=#FFFFFF
""",
    "hacker_purple": """
background=#0D0208
foreground=#00FF41
cursor=#00FF41
color0=#0D0208
color1=#FF0000
color2=#00FF41
color3=#FFFF00
color4=#0080FF
color5=#FF00FF
color6=#00FFFF
color7=#C0C0C0
color8=#333333
color9=#FF3333
color10=#33FF33
color11=#FFFF33
color12=#3399FF
color13=#FF33FF
color14=#33FFFF
color15=#FFFFFF
""",
    "cyberpunk_red": """
background=#000000
foreground=#FF0000
cursor=#FF0000
color0=#000000
color1=#FF0000
color2=#00FF00
color3=#FF6600
color4=#0066FF
color5=#CC00FF
color6=#00FFFF
color7=#AAAAAA
color8=#333333
color9=#FF3333
color10=#33FF33
color11=#FF9933
color12=#3399FF
color13=#CC33FF
color14=#33FFFF
color15=#FFFFFF
""",
    "hacker_retro": """
background=#121212
foreground=#00FF00
cursor=#00FF00
color0=#121212
color1=#FF0044
color2=#00CC00
color3=#FFA800
color4=#0088FF
color5=#CC00CC
color6=#00CCCC
color7=#C0C0C0
color8=#333333
color9=#FF3366
color10=#33FF33
color11=#FFCC33
color12=#3399FF
color13=#CC33FF
color14=#33FFFF
color15=#FFFFFF
"""
}

COLORES_DISPONIBLES = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "bright_black", "bright_red", "bright_green", "bright_yellow", 
    "bright_blue", "bright_magenta", "bright_cyan", "bright_white",
    "dark_red", "dark_green", "dark_yellow", "dark_blue",
    "dark_magenta", "dark_cyan", "grey0", "grey19", "grey30",
    "grey37", "grey46", "grey50", "grey54", "grey58", "grey62",
    "grey66", "grey70", "grey74", "grey78", "grey82", "grey85",
    "grey89", "grey93", "grey100", "orange1", "orange3", "orange4"
]

def limpiar_pantalla():
    os.system("clear")

def mostrar_header(texto):
    ancho = 78
    panel = Panel(
        Align.center(Text(texto, style=Style.parse(COLOR_HIGHLIGHT))),
        style="bold bright_white on rgb(30,30,40)",
        padding=(1, 2),
        width=ancho,
        box=HEAVY
    )
    console.print(panel)
    console.print(Align.center(Text("ESTADO ACTUAL", style=COLOR_ACCENT), width=ancho))

def mostrar_error(mensaje):
    console.print(f"[bold bright_white on red] ERROR [/] [bold bright_red]→[/] {mensaje}")

def mostrar_exito(mensaje):
    console.print(f"[bold bright_white on green] ÉXITO [/] [bold bright_green]→[/] {mensaje}")

def mostrar_advertencia(mensaje):
    console.print(f"[bold bright_white on yellow] ADVERTENCIA [/] [bold bright_yellow]→[/] {mensaje}")

def mostrar_informacion(mensaje):
    console.print(f"[bold bright_white on blue] INFORMACIÓN [/] [bold bright_blue]→[/] {mensaje}")

def es_color_valido(color):
    try:
        Style.parse(color)
        return True
    except:
        return False

def verificar_termux_api():
    try:
        resultado = subprocess.run(['pkg', 'list-installed'], capture_output=True, text=True, check=True)
        return 'termux-api' in resultado.stdout
    except:
        return False

def editar_banner_texto():
    limpiar_pantalla()
    mostrar_header("EDITAR TEXTO DEL BANNER")
    path = THEMES_DIR / "banner.txt"
    subprocess.run(["nano", str(path)])
    mostrar_exito("Texto del banner editado correctamente")
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def cambiar_color_banner():
    limpiar_pantalla()
    mostrar_header("CAMBIAR COLOR DEL BANNER")
    
    table = Table.grid(padding=(0, 2))
    fila_actual = []
    for i, color in enumerate(COLORES_DISPONIBLES):
        if es_color_valido(color):
            muestra = f"[{color}]{color}[/]"
            fila_actual.append(muestra)
            if len(fila_actual) == 4 or i == len(COLORES_DISPONIBLES) - 1:
                table.add_row(*fila_actual)
                fila_actual = []
    
    console.print(table, justify="center")
    
    while True:
        color = Prompt.ask(f"\n[{COLOR_ACCENT}]Seleccione color para el banner →[/]").strip()
        if es_color_valido(color):
            break
        mostrar_error(f"Color '{color}' no válido. Intente nuevamente")
    
    (THEMES_DIR / "banner_color.txt").write_text(color)
    mostrar_exito(f"Color del banner actualizado: [{color}]{color}[/]")
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def banner_preview():
    limpiar_pantalla()
    mostrar_header("VISTA PREVIA DEL BANNER")
    path = THEMES_DIR / "banner.txt"
    color_path = THEMES_DIR / "banner_color.txt"
    
    if path.exists():
        banner = path.read_text()
        color = color_path.read_text().strip() if color_path.exists() else "bright_white"
        
        lineas = banner.splitlines()
        ancho_max = max(len(linea) for linea in lineas) if lineas else 20
        ancho_panel = min(ancho_max + 8, 80)
        
        estilo = Style.parse(color) if es_color_valido(color) else Style.parse("bright_white")
        
        if not es_color_valido(color):
            mostrar_advertencia(f"Color '{color}' no válido. Usando blanco brillante")
        
        texto_banner = Text(banner, style=estilo)
        
        preview = Panel(
            Align.center(texto_banner),
            title="[bold]VISTA PREVIA",
            border_style=estilo,
            box=DOUBLE,
            width=ancho_panel,
            padding=(1, 2)
        )
        console.print(Align.center(preview))
    else:
        mostrar_advertencia("No se encontró archivo de banner")
    
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def configurar_banner():
    while True:
        limpiar_pantalla()
        mostrar_header("CONFIGURACIÓN DE BANNER")
        
        menu = Table.grid(padding=(1, 4))
        menu.add_column("Opción", style=COLOR_ACCENT, justify="center")
        menu.add_column("Descripción", style=COLOR_PRIMARY)
        
        menu.add_row("1", "Editar texto del banner")
        menu.add_row("2", "Cambiar color del banner")
        menu.add_row("3", "Vista previa del banner")
        menu.add_row("0", "[bold bright_red]Volver al menú principal[/]")
        
        console.print(Align.center(menu))
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]Seleccione una opción →[/]")
        
        if opcion == "1": editar_banner_texto()
        elif opcion == "2": cambiar_color_banner()
        elif opcion == "3": banner_preview()
        elif opcion == "0": break
        else: 
            mostrar_error("Opción inválida")
            time.sleep(1)

def elegir_tema_predeterminado():
    limpiar_pantalla()
    mostrar_header("SELECCIONAR TEMA PREDEFINIDO")
    
    table = Table.grid(padding=(1, 3), expand=True)
    table.add_column("Tema", style=COLOR_ACCENT)
    table.add_column("Muestra", style=COLOR_PRIMARY)
    
    temas_muestras = {
        "dracula": "[#FF5555]█[/] [#50FA7B]█[/] [#BD93F9]█",
        "nord": "[#BF616A]█[/] [#A3BE8C]█[/] [#81A1C1]█",
        "gruvbox": "[#CC241D]█[/] [#98971A]█[/] [#458588]█",
        "tokyo_night": "[#F7768E]█[/] [#9ECE6A]█[/] [#7AA2F7]█",
        "one_dark": "[#E06C75]█[/] [#98C379]█[/] [#61AFEF]█",
        "monokai": "[#f92672]█[/] [#a6e22e]█[/] [#66d9ef]█",
        "solarized_dark": "[#dc322f]█[/] [#859900]█[/] [#268bd2]█",
        "catppuccin_latte": "[#D20F39]█[/] [#40A02B]█[/] [#1E66F5]█",
        "cyberpunk_neon": "[#FF3559]█[/] [#00FF9D]█[/] [#00A1FF]█",
        "everforest": "[#E67E80]█[/] [#A7C080]█[/] [#7FBBB3]█",
        "material_ocean": "[#F28FAD]█[/] [#ABE9B3]█[/] [#96CDFB]█",
        "horizon": "[#E95678]█[/] [#29D398]█[/] [#26BBD9]█",
        "matrix": "[#FF0000]█[/] [#00FF00]█[/] [#0000FF]█",
        "hacker_purple": "[#FF0000]█[/] [#00FF41]█[/] [#0080FF]█",
        "cyberpunk_red": "[#FF0000]█[/] [#00FF00]█[/] [#0066FF]█",
        "hacker_retro": "[#FF0044]█[/] [#00CC00]█[/] [#0088FF]█"
    }
    
    for tema, muestra in temas_muestras.items():
        table.add_row(f"[bold]{tema}[/]", muestra)
    
    console.print(Align.center(table))
    
    tema = Prompt.ask(f"\n[{COLOR_ACCENT}]Elija un tema →[/]")
    if tema in TERMUX_THEMES:
        TERMUX_COLORS_PATH.write_text(TERMUX_THEMES[tema])
        subprocess.run(["termux-reload-settings"])
        mostrar_exito(f"Tema [bold]{tema}[/] aplicado")
    else:
        mostrar_error("Tema no válido")
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def crear_tema_personalizado():
    limpiar_pantalla()
    mostrar_header("CREAR TEMA PERSONALIZADO")
    subprocess.run(["nano", str(TERMUX_COLORS_PATH)])
    subprocess.run(["termux-reload-settings"])
    mostrar_exito("Tema personalizado configurado")
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def listar_tema_actual():
    limpiar_pantalla()
    mostrar_header("TEMA ACTUAL TERMUX")
    if TERMUX_COLORS_PATH.exists():
        tema = TERMUX_COLORS_PATH.read_text()
        console.print(Panel.fit(tema, title="[bold]COLORES ACTUALES", box=DOUBLE, border_style=COLOR_ACCENT))
    else:
        mostrar_advertencia("No hay tema configurado")
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def configurar_tema_termux():
    while True:
        limpiar_pantalla()
        mostrar_header("CONFIGURAR TEMA TERMUX")
        
        menu = Table.grid(padding=(1, 4))
        menu.add_column("Opción", style=COLOR_ACCENT, justify="center")
        menu.add_column("Descripción", style=COLOR_PRIMARY)
        
        menu.add_row("1", "Elegir tema predefinido")
        menu.add_row("2", "Crear tema personalizado")
        menu.add_row("3", "Mostrar tema actual")
        menu.add_row("0", "[bold bright_red]Volver al menú principal[/]")
        
        console.print(Align.center(menu))
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]Seleccione una opción →[/]")
        
        if opcion == "1": elegir_tema_predeterminado()
        elif opcion == "2": crear_tema_personalizado()
        elif opcion == "3": listar_tema_actual()
        elif opcion == "0": break
        else: 
            mostrar_error("Opción inválida")
            time.sleep(1)

def editar_usuario():
    limpiar_pantalla()
    mostrar_header("EDITAR USUARIO")
    user_path = SYSTEM_DIR / "user.txt"
    
    while True:
        nuevo_usuario = Prompt.ask(f"[{COLOR_ACCENT}]Ingrese nuevo nombre de usuario →[/]").strip()
        if nuevo_usuario:
            user_path.write_text(nuevo_usuario)
            mostrar_exito(f"Usuario [bold]{nuevo_usuario}[/] configurado")
            break
        mostrar_error("Nombre de usuario no válido")
    
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def mostrar_usuario():
    limpiar_pantalla()
    mostrar_header("USUARIO ACTUAL")
    user_path = SYSTEM_DIR / "user.txt"
    
    if user_path.exists():
        usuario = user_path.read_text().strip()
        console.print(Panel.fit(
            f"[bold {COLOR_ACCENT}]{usuario}[/]", 
            title="USUARIO",
            box=DOUBLE,
            border_style=COLOR_ACCENT,
            width=30
        ))
    else:
        mostrar_advertencia("Usuario no configurado")
    
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def configurar_usuario():
    while True:
        limpiar_pantalla()
        mostrar_header("CONFIGURACIÓN DE USUARIO")
        
        menu = Table.grid(padding=(1, 4))
        menu.add_column("Opción", style=COLOR_ACCENT, justify="center")
        menu.add_column("Descripción", style=COLOR_PRIMARY)
        
        menu.add_row("1", "Editar usuario")
        menu.add_row("2", "Mostrar usuario actual")
        menu.add_row("0", "[bold bright_red]Volver al menú principal[/]")
        
        console.print(Align.center(menu))
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]Seleccione una opción →[/]")
        
        if opcion == "1": editar_usuario()
        elif opcion == "2": mostrar_usuario()
        elif opcion == "0": break
        else: 
            mostrar_error("Opción inválida")
            time.sleep(1)

def activar_huella():
    limpiar_pantalla()
    mostrar_header("ACTIVAR HUELLA DIGITAL")
    
    if verificar_termux_api():
        metodo_path = SYSTEM_DIR / "login_method.txt"
        metodo_path.write_text("termux-fingerprint")
        mostrar_exito("Autenticación por huella activada")
    else:
        mostrar_error("Termux-API no instalado")
        mostrar_informacion("Instale con: [bold]pkg install termux-api[/]")
    
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def desactivar_proteccion():
    limpiar_pantalla()
    mostrar_header("DESACTIVAR PROTECCIÓN")
    metodo_path = SYSTEM_DIR / "login_method.txt"
    metodo_path.write_text("no")
    mostrar_exito("Protección desactivada")
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def mostrar_metodo_actual():
    limpiar_pantalla()
    mostrar_header("MÉTODO DE AUTENTICACIÓN")
    metodo_path = SYSTEM_DIR / "login_method.txt"
    
    if metodo_path.exists():
        metodo = metodo_path.read_text().strip()
        if metodo == "termux-fingerprint":
            estado = "[bold bright_green on black] HUELLA ACTIVADA "
        else:
            estado = "[bold bright_red on black] PROTECCIÓN DESACTIVADA "
        console.print(Panel.fit(
            estado, 
            width=30,
            box=DOUBLE,
            border_style=COLOR_ACCENT
        ))
    else:
        mostrar_advertencia("No configurado")
    
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def configurar_autenticacion():
    while True:
        limpiar_pantalla()
        mostrar_header("CONFIGURACIÓN DE AUTENTICACIÓN")
        
        menu = Table.grid(padding=(1, 4))
        menu.add_column("Opción", style=COLOR_ACCENT, justify="center")
        menu.add_column("Descripción", style=COLOR_PRIMARY)
        
        menu.add_row("1", "Activar huella digital")
        menu.add_row("2", "Desactivar protección")
        menu.add_row("3", "Mostrar método actual")
        menu.add_row("0", "[bold bright_red]Volver al menú principal[/]")
        
        console.print(Align.center(menu))
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]Seleccione una opción →[/]")
        
        if opcion == "1": activar_huella()
        elif opcion == "2": desactivar_proteccion()
        elif opcion == "3": mostrar_metodo_actual()
        elif opcion == "0": break
        else: 
            mostrar_error("Opción inválida")
            time.sleep(1)

def probar_autenticacion():
    limpiar_pantalla()
    mostrar_header("PROBAR AUTENTICACIÓN")
    metodo_path = SYSTEM_DIR / "login_method.txt"
    
    if not metodo_path.exists():
        mostrar_error("Método no configurado")
        time.sleep(2)
        input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")
        return
    
    metodo = metodo_path.read_text().strip()
    if metodo == "termux-fingerprint":
        console.print(f"\n[{COLOR_WARNING}]Probando autenticación...[/]")
        try:
            subprocess.run(['termux-fingerprint'], check=True)
            mostrar_exito("Autenticación exitosa")
        except:
            mostrar_error("Autenticación fallida")
    else:
        mostrar_error("Método de huella no configurado")
        time.sleep(2)
    
    input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def mostrar_estado_actual():
    estado_tabla = Table(
        box=ROUNDED,
        header_style=COLOR_ACCENT,
        border_style=COLOR_SECONDARY
    )
    estado_tabla.add_column("Configuración", style=COLOR_PRIMARY)
    estado_tabla.add_column("Estado", style=COLOR_SECONDARY)
    
    user_path = SYSTEM_DIR / "user.txt"
    if user_path.exists():
        usuario = user_path.read_text().strip()
        estado_tabla.add_row("Usuario", f"[bold]{usuario}[/]")
    else:
        estado_tabla.add_row("Usuario", "[bright_red]No configurado[/]")
    
    metodo_path = SYSTEM_DIR / "login_method.txt"
    if metodo_path.exists():
        metodo = metodo_path.read_text().strip()
        estado = "[bright_green]Activada[/]" if metodo == "termux-fingerprint" else "[bright_red]Desactivada[/]"
        estado_tabla.add_row("Autenticación", estado)
    else:
        estado_tabla.add_row("Autenticación", "[bright_red]No configurada[/]")
    
    banner_path = THEMES_DIR / "banner.txt"
    estado_tabla.add_row("Banner", "[bright_green]Configurado[/]" if banner_path.exists() else "[bright_red]No configurado[/]")
    
    console.print(Align.center(estado_tabla, width=72))

def menu_principal():
    opciones_validas = [
        "1", "1.1", "1.2", "1.3", "2", "2.1", "2.2", "2.3",
        "3", "3.1", "3.2", "4", "4.1", "4.2", "4.3", "5", "0"
    ]
    
    while True:
        limpiar_pantalla()
        mostrar_header("PANEL PRINCIPAL STELLAR")
        mostrar_estado_actual()
        
        menu_tabla = Table(
            box=HEAVY,
            show_header=False,
            border_style=COLOR_SECONDARY,
            width=78
        )
        menu_tabla.add_column("Opción", style=COLOR_ACCENT, width=8)
        menu_tabla.add_column("Descripción", style=COLOR_PRIMARY)
        
        menu_tabla.add_row("1", "[bold]Configurar banner[/]")
        menu_tabla.add_row("1.1", "  Editar texto del banner")
        menu_tabla.add_row("1.2", "  Cambiar color del banner")
        menu_tabla.add_row("1.3", "  Vista previa del banner")
        menu_tabla.add_row("", "")
        menu_tabla.add_row("2", "[bold]Configurar tema Termux[/]")
        menu_tabla.add_row("2.1", "  Elegir tema predefinido")
        menu_tabla.add_row("2.2", "  Crear tema personalizado")
        menu_tabla.add_row("2.3", "  Mostrar tema actual")
        menu_tabla.add_row("", "")
        menu_tabla.add_row("3", "[bold]Configurar usuario[/]")
        menu_tabla.add_row("3.1", "  Editar usuario")
        menu_tabla.add_row("3.2", "  Mostrar usuario actual")
        menu_tabla.add_row("", "")
        menu_tabla.add_row("4", "[bold]Configurar autenticación[/]")
        menu_tabla.add_row("4.1", "  Activar huella")
        menu_tabla.add_row("4.2", "  Desactivar protección")
        menu_tabla.add_row("4.3", "  Mostrar método actual")
        menu_tabla.add_row("", "")
        menu_tabla.add_row("5", "[bold bright_yellow]Probar autenticación[/]")
        menu_tabla.add_row("0", "[bold bright_red]Salir del sistema[/]")
        
        console.print(Align.center(menu_tabla))
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]Seleccione opción →[/]")
        
        if opcion not in opciones_validas:
            mostrar_error("Opción inválida")
            time.sleep(1)
            continue
            
        if opcion == "1": configurar_banner()
        elif opcion == "1.1": editar_banner_texto()
        elif opcion == "1.2": cambiar_color_banner()
        elif opcion == "1.3": banner_preview()
        elif opcion == "2": configurar_tema_termux()
        elif opcion == "2.1": elegir_tema_predeterminado()
        elif opcion == "2.2": crear_tema_personalizado()
        elif opcion == "2.3": listar_tema_actual()
        elif opcion == "3": configurar_usuario()
        elif opcion == "3.1": editar_usuario()
        elif opcion == "3.2": mostrar_usuario()
        elif opcion == "4": configurar_autenticacion()
        elif opcion == "4.1": activar_huella()
        elif opcion == "4.2": desactivar_proteccion()
        elif opcion == "4.3": mostrar_metodo_actual()
        elif opcion == "5": probar_autenticacion()
        elif opcion == "0":
            limpiar_pantalla()
            console.print(Panel.fit(
                "[bold bright_green]Saliendo del sistema Stellar...", 
                box=HEAVY,
                border_style="bright_green"
            ))
            time.sleep(1)
            exit(0)

def inicio():
    limpiar_pantalla()
    mostrar_header("SISTEMA DE CONFIGURACIÓN STELLAR")
    
    user_path = SYSTEM_DIR / "user.txt"
    if not user_path.exists():
        mostrar_advertencia("Usuario no configurado")
        editar_usuario()
    
    metodo_path = SYSTEM_DIR / "login_method.txt"
    if not metodo_path.exists():
        mostrar_advertencia("Autenticación no configurada")
        activar_huella()
    
    time.sleep(1)
    menu_principal()

if __name__ == "__main__":
    inicio()