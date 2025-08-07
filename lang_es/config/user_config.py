import os
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED, HEAVY, DOUBLE, SQUARE
from rich.align import Align
from rich.style import Style
from rich.live import Live
from rich.layout import Layout
from rich.progress import Progress, SpinnerColumn, TextColumn
from pathlib import Path
import shutil

# Configuración inicial
console = Console()
STELLAR_DIR = Path("~/Stellar/lang_es").expanduser()
THEMES_DIR = STELLAR_DIR / "config/themes"
SYSTEM_DIR = STELLAR_DIR / "config/system"
TERMUX_COLORS_PATH = Path("~/.termux/colors.properties").expanduser()
THEMES_DIR.mkdir(parents=True, exist_ok=True)
SYSTEM_DIR.mkdir(parents=True, exist_ok=True)

# Paleta de colores mejorada
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

# Nuevas constantes para animaciones
SPINNER = "dots"
SPINNER_SPEED = 0.5

def limpiar_pantalla():
    os.system("clear")

def mostrar_header(texto):
    ancho = min(shutil.get_terminal_size().columns - 4, 90)
    titulo = Text.assemble(
        ("★ ", "bold " + COLOR_ACCENT),
        (texto, "bold " + COLOR_HIGHLIGHT),
        (" ★", "bold " + COLOR_ACCENT)
    )
    panel = Panel(
        Align.center(titulo),
        style=f"bold white on {COLOR_BG}",
        padding=(0, 2),
        width=ancho,
        box=HEAVY,
        border_style=COLOR_BORDER
    )
    console.print(panel, justify="center")
    console.print()

def mostrar_subtitulo(texto):
    console.print(Align.center(Text(f"» {texto} «", style=COLOR_SECONDARY + " dim"), width=80))
    console.print()

def mostrar_error(mensaje):
    console.print(f"[{COLOR_ERROR}]✖ ERROR →[/] {mensaje}", justify="center")

def mostrar_exito(mensaje):
    console.print(f"[{COLOR_SUCCESS}]✓ ÉXITO →[/] {mensaje}", justify="center")

def mostrar_advertencia(mensaje):
    console.print(f"[{COLOR_WARNING}]⚠ ADVERTENCIA →[/] {mensaje}", justify="center")

def mostrar_informacion(mensaje):
    console.print(f"[{COLOR_INFO}]ℹ INFORMACIÓN →[/] {mensaje}", justify="center")

def mostrar_carga(mensaje):
    with Progress(
        SpinnerColumn(spinner_name=SPINNER, style=COLOR_ACCENT),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
        console=console
    ) as progress:
        progress.add_task(description=mensaje, total=None)
        time.sleep(SPINNER_SPEED)

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

def crear_tabla_menu(opciones, ancho=50):
    tabla = Table.grid(padding=(1, 4), expand=True)
    tabla.add_column(style=COLOR_ACCENT + " bold", width=10, justify="center")
    tabla.add_column(style=COLOR_PRIMARY, width=ancho-14)
    
    for opcion, descripcion in opciones:
        tabla.add_row(opcion, descripcion)
    
    return tabla

def crear_tabla_estado():
    tabla = Table(
        box=SQUARE,
        header_style=COLOR_ACCENT,
        border_style=COLOR_BORDER,
        expand=True
    )
    tabla.add_column("Configuración", style=COLOR_PRIMARY, width=25)
    tabla.add_column("Estado", style=COLOR_SECONDARY, width=25)
    return tabla

def editar_banner_texto():
    limpiar_pantalla()
    mostrar_header("EDITAR TEXTO DEL BANNER")
    mostrar_subtitulo("Usa nano para personalizar tu banner")
    
    path = THEMES_DIR / "banner.txt"
    if not path.exists():
        path.write_text("Stellar Terminal\nPersonaliza tu experiencia")
    
    subprocess.run(["nano", str(path)])
    mostrar_exito("Texto del banner editado correctamente")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def mostrar_paleta_colores():
    table = Table.grid(padding=(0, 1), expand=True)
    fila_actual = []
    
    for i, color in enumerate(COLORES_DISPONIBLES):
        if es_color_valido(color):
            muestra = f"[on {color}]   [/] [bold]{color}[/]"
            celda = Panel(muestra, width=22, box=SQUARE, border_style="dim")
            fila_actual.append(celda)
            
            if len(fila_actual) == 3 or i == len(COLORES_DISPONIBLES) - 1:
                table.add_row(*fila_actual)
                fila_actual = []
    
    console.print(Align.center(table))
    console.print()

def cambiar_color_banner():
    limpiar_pantalla()
    mostrar_header("CAMBIAR COLOR DEL BANNER")
    mostrar_subtitulo("Selecciona un color de la paleta")
    
    mostrar_paleta_colores()
    
    while True:
        color = Prompt.ask(f"[{COLOR_ACCENT}]» Seleccione color para el banner →[/]").strip().lower()
        if es_color_valido(color):
            break
        mostrar_error(f"Color '{color}' no válido. Intente nuevamente")
    
    (THEMES_DIR / "banner_color.txt").write_text(color)
    mostrar_exito(f"Color del banner actualizado: [{color}]{color}[/]")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def cambiar_color_fondo_banner():
    limpiar_pantalla()
    mostrar_header("CAMBIAR COLOR DE FONDO DEL BANNER")
    mostrar_subtitulo("Selecciona un color de fondo")
    
    mostrar_paleta_colores()
    
    while True:
        color = Prompt.ask(f"[{COLOR_ACCENT}]» Seleccione color para el fondo →[/]").strip().lower()
        if es_color_valido(color):
            break
        mostrar_error(f"Color '{color}' no válido. Intente nuevamente")
    
    (THEMES_DIR / "banner_background_color.txt").write_text(color)
    mostrar_exito(f"Color de fondo actualizado: [{color}]{color}[/]")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def toggle_fondo_banner():
    limpiar_pantalla()
    mostrar_header("ACTIVAR/DESACTIVAR FONDO DEL BANNER")
    
    path = THEMES_DIR / "banner_background.txt"
    fondo_actual = "no"
    if path.exists():
        fondo_actual = path.read_text().strip()
    
    estado = "ACTIVADO" if fondo_actual == "no" else "DESACTIVADO"
    color_estado = COLOR_SUCCESS if estado == "ACTIVADO" else COLOR_WARNING
    
    if Confirm.ask(f"[{COLOR_ACCENT}]» ¿{estado} fondo del banner?[/]", default=True):
        nuevo_estado = "si" if fondo_actual == "no" else "no"
        path.write_text(nuevo_estado)
        mostrar_exito(f"Fondo del banner [bold {color_estado}]{estado}[/]")
    else:
        mostrar_informacion("Operación cancelada")
    
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def banner_preview():
    limpiar_pantalla()
    mostrar_header("VISTA PREVIA DEL BANNER")
    
    path = THEMES_DIR / "banner.txt"
    color_path = THEMES_DIR / "banner_color.txt"
    fondo_path = THEMES_DIR / "banner_background.txt"
    fondo_color_path = THEMES_DIR / "banner_background_color.txt"
    
    if path.exists():
        banner = path.read_text()
        color = color_path.read_text().strip() if color_path.exists() else "bright_white"
        
        lineas = banner.splitlines()
        ancho_max = max(len(linea) for linea in lineas) if lineas else 20
        ancho_panel = min(ancho_max + 8, 80)
        
        estilo = Style.parse(color) if es_color_valido(color) else Style.parse("bright_white")
        
        texto_banner = Text(banner, style=estilo)
        
        estilo_fondo = None
        fondo_activado = fondo_path.exists() and fondo_path.read_text().strip() == "si"
        
        if fondo_activado:
            color_fondo = fondo_color_path.read_text().strip() if fondo_color_path.exists() else "black"
            if es_color_valido(color_fondo):
                estilo_fondo = Style(bgcolor=color_fondo)
            else:
                estilo_fondo = Style(bgcolor="black")
        
        preview = Panel(
            Align.center(texto_banner),
            title="[bold]VISTA PREVIA",
            border_style=estilo,
            box=DOUBLE,
            width=ancho_panel,
            padding=(1, 2),
            style=estilo_fondo
        )
        console.print(Align.center(preview))
    else:
        mostrar_advertencia("No se encontró archivo de banner")
    
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def configurar_banner():
    while True:
        limpiar_pantalla()
        mostrar_header("CONFIGURACIÓN DE BANNER")
        
        opciones = [
            ("1", "Editar texto del banner"),
            ("2", "Cambiar color del banner"),
            ("3", "Cambiar color de fondo"),
            ("4", "Activar/Desactivar fondo"),
            ("5", "Vista previa del banner"),
            ("0", "[bold bright_red]Volver al menú principal[/]")
        ]
        
        tabla_menu = crear_tabla_menu(opciones, ancho=60)
        console.print(Align.center(tabla_menu))
        
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]» Seleccione una opción →[/]")
        
        if opcion == "1": editar_banner_texto()
        elif opcion == "2": cambiar_color_banner()
        elif opcion == "3": cambiar_color_fondo_banner()
        elif opcion == "4": toggle_fondo_banner()
        elif opcion == "5": banner_preview()
        elif opcion == "0": break
        else: 
            mostrar_error("Opción inválida")
            time.sleep(1)

def mostrar_temas():
    tabla = Table.grid(padding=(1, 2), expand=True)
    tabla.add_column("Tema", style=COLOR_ACCENT + " bold", width=20)
    tabla.add_column("Muestra", style=COLOR_PRIMARY, width=40)
    
    temas_muestras = {
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
    
    for tema, muestra in temas_muestras.items():
        tabla.add_row(f"[bold]{tema}[/]", muestra)
    
    console.print(Align.center(tabla))

def elegir_tema_predeterminado():
    limpiar_pantalla()
    mostrar_header("SELECCIONAR TEMA PREDEFINIDO")
    mostrar_subtitulo("Elige un tema de la lista")
    
    mostrar_temas()
    
    tema = Prompt.ask(f"\n[{COLOR_ACCENT}]» Elija un tema →[/]")
    if tema in TERMUX_THEMES:
        TERMUX_COLORS_PATH.write_text(TERMUX_THEMES[tema])
        subprocess.run(["termux-reload-settings"])
        mostrar_exito(f"Tema [bold]{tema}[/] aplicado")
        mostrar_carga("Aplicando configuración")
    else:
        mostrar_error("Tema no válido")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def crear_tema_personalizado():
    limpiar_pantalla()
    mostrar_header("CREAR TEMA PERSONALIZADO")
    mostrar_subtitulo("Usa nano para crear tu propio tema")
    
    if not TERMUX_COLORS_PATH.exists():
        TERMUX_COLORS_PATH.write_text("# Personaliza tu tema\nbackground=#000000\nforeground=#FFFFFF\n")
    
    subprocess.run(["nano", str(TERMUX_COLORS_PATH)])
    subprocess.run(["termux-reload-settings"])
    mostrar_exito("Tema personalizado configurado")
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def listar_tema_actual():
    limpiar_pantalla()
    mostrar_header("TEMA ACTUAL TERMUX")
    
    if TERMUX_COLORS_PATH.exists():
        tema = TERMUX_COLORS_PATH.read_text()
        panel = Panel.fit(
            tema, 
            title="[bold]COLORES ACTUALES", 
            box=DOUBLE, 
            border_style=COLOR_ACCENT,
            padding=(1, 4)
        )
        console.print(Align.center(panel))
    else:
        mostrar_advertencia("No hay tema configurado")
    
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def configurar_tema_termux():
    while True:
        limpiar_pantalla()
        mostrar_header("CONFIGURAR TEMA TERMUX")
        
        opciones = [
            ("1", "Elegir tema predefinido"),
            ("2", "Crear tema personalizado"),
            ("3", "Mostrar tema actual"),
            ("0", "[bold bright_red]Volver al menú principal[/]")
        ]
        
        tabla_menu = crear_tabla_menu(opciones, ancho=60)
        console.print(Align.center(tabla_menu))
        
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]» Seleccione una opción →[/]")
        
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
        nuevo_usuario = Prompt.ask(f"[{COLOR_ACCENT}]» Ingrese nuevo nombre de usuario →[/]").strip()
        if nuevo_usuario:
            user_path.write_text(nuevo_usuario)
            mostrar_exito(f"Usuario [bold]{nuevo_usuario}[/] configurado")
            break
        mostrar_error("Nombre de usuario no válido")
    
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def mostrar_usuario():
    limpiar_pantalla()
    mostrar_header("USUARIO ACTUAL")
    user_path = SYSTEM_DIR / "user.txt"
    
    if user_path.exists():
        usuario = user_path.read_text().strip()
        panel = Panel.fit(
            f"[bold {COLOR_ACCENT}]{usuario}[/]", 
            title="USUARIO",
            box=DOUBLE,
            border_style=COLOR_ACCENT,
            width=30
        )
        console.print(Align.center(panel))
    else:
        mostrar_advertencia("Usuario no configurado")
    
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def configurar_usuario():
    while True:
        limpiar_pantalla()
        mostrar_header("CONFIGURACIÓN DE USUARIO")
        
        opciones = [
            ("1", "Editar usuario"),
            ("2", "Mostrar usuario actual"),
            ("0", "[bold bright_red]Volver al menú principal[/]")
        ]
        
        tabla_menu = crear_tabla_menu(opciones, ancho=60)
        console.print(Align.center(tabla_menu))
        
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]» Seleccione una opción →[/]")
        
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
        mostrar_carga("Configurando seguridad")
    else:
        mostrar_error("Termux-API no instalado")
        mostrar_informacion("Instale con: [bold]pkg install termux-api[/]")
    
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def desactivar_proteccion():
    limpiar_pantalla()
    mostrar_header("DESACTIVAR PROTECCIÓN")
    
    if Confirm.ask(f"[{COLOR_ACCENT}]» ¿Desactivar protección?[/]", default=False):
        metodo_path = SYSTEM_DIR / "login_method.txt"
        metodo_path.write_text("no")
        mostrar_exito("Protección desactivada")
    else:
        mostrar_informacion("Operación cancelada")
    
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def mostrar_metodo_actual():
    limpiar_pantalla()
    mostrar_header("MÉTODO DE AUTENTICACIÓN")
    metodo_path = SYSTEM_DIR / "login_method.txt"
    
    if metodo_path.exists():
        metodo = metodo_path.read_text().strip()
        if metodo == "termux-fingerprint":
            estado = "[bold bright_green]HUELLA ACTIVADA[/]"
            icono = "🔒"
        else:
            estado = "[bold bright_red]PROTECCIÓN DESACTIVADA[/]"
            icono = "🔓"
        panel = Panel.fit(
            f"{icono} {estado}", 
            width=30,
            box=DOUBLE,
            border_style=COLOR_ACCENT
        )
        console.print(Align.center(panel))
    else:
        mostrar_advertencia("No configurado")
    
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def configurar_autenticacion():
    while True:
        limpiar_pantalla()
        mostrar_header("CONFIGURACIÓN DE AUTENTICACIÓN")
        
        opciones = [
            ("1", "Activar huella digital"),
            ("2", "Desactivar protección"),
            ("3", "Mostrar método actual"),
            ("0", "[bold bright_red]Volver al menú principal[/]")
        ]
        
        tabla_menu = crear_tabla_menu(opciones, ancho=60)
        console.print(Align.center(tabla_menu))
        
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]» Seleccione una opción →[/]")
        
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
        console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")
        return
    
    metodo = metodo_path.read_text().strip()
    if metodo == "termux-fingerprint":
        console.print(f"\n[{COLOR_WARNING}]» Probando autenticación...[/]")
        try:
            subprocess.run(['termux-fingerprint'], check=True)
            mostrar_exito("Autenticación exitosa ✅")
        except:
            mostrar_error("Autenticación fallida ❌")
    else:
        mostrar_error("Método de huella no configurado")
        time.sleep(2)
    
    console.input(f"\n[{COLOR_INFO}]Pulsa Enter para continuar →[/]")

def mostrar_estado_actual():
    estado_tabla = crear_tabla_estado()
    
    # Usuario
    user_path = SYSTEM_DIR / "user.txt"
    if user_path.exists():
        usuario = user_path.read_text().strip()
        estado_tabla.add_row("Usuario", f"[bold]{usuario}[/]")
    else:
        estado_tabla.add_row("Usuario", "[bright_red]No configurado[/]")
    
    # Autenticación
    metodo_path = SYSTEM_DIR / "login_method.txt"
    if metodo_path.exists():
        metodo = metodo_path.read_text().strip()
        if metodo == "termux-fingerprint":
            estado = "[bright_green]Huella activada[/]"
        else:
            estado = "[bright_red]Desactivada[/]"
        estado_tabla.add_row("Autenticación", estado)
    else:
        estado_tabla.add_row("Autenticación", "[bright_red]No configurada[/]")
    
    # Banner
    banner_path = THEMES_DIR / "banner.txt"
    estado_tabla.add_row("Banner", "[bright_green]Configurado[/]" if banner_path.exists() else "[bright_red]No configurado[/]")
    
    # Fondo Banner
    fondo_path = THEMES_DIR / "banner_background.txt"
    fondo_estado = "[bright_green]Activado[/]" if fondo_path.exists() and fondo_path.read_text().strip() == "si" else "[bright_red]Desactivado[/]"
    estado_tabla.add_row("Fondo Banner", fondo_estado)
    
    # Tema Termux
    estado_tabla.add_row("Tema Termux", "[bright_green]Configurado[/]" if TERMUX_COLORS_PATH.exists() else "[bright_red]No configurado[/]")
    
    console.print(Align.center(estado_tabla, width=72))

def menu_principal():
    while True:
        limpiar_pantalla()
        mostrar_header("PANEL PRINCIPAL STELLAR")
        console.print(Align.center(Text("ESTADO DEL SISTEMA", style=COLOR_ACCENT), width=80))
        mostrar_estado_actual()
        console.print()
        
        opciones = [
            ("1", "Configurar banner"),
            ("2", "Configurar tema Termux"),
            ("3", "Configurar usuario"),
            ("4", "Configurar autenticación"),
            ("5", "[bold " + COLOR_WARNING + "]Probar autenticación[/]"),
            ("0", "[bold bright_red]Salir del sistema[/]")
        ]
        
        tabla_menu = crear_tabla_menu(opciones, ancho=60)
        console.print(Align.center(tabla_menu))
        opcion = Prompt.ask(f"\n[{COLOR_ACCENT}]» Seleccione opción →[/]")
        
        if opcion == "1": configurar_banner()
        elif opcion == "2": configurar_tema_termux()
        elif opcion == "3": configurar_usuario()
        elif opcion == "4": configurar_autenticacion()
        elif opcion == "5": probar_autenticacion()
        elif opcion == "0":
            limpiar_pantalla()
            console.print(Align.center(Panel.fit(
                "[bold bright_green]Saliendo del sistema Stellar...\n¡Hasta pronto! ✨", 
                box=ROUNDED,
                border_style="bright_green",
                width=50
            )))
            time.sleep(1.5)
            os.system("python ~/Stellar/config/themes/banner.py")
            exit(0)
        else: 
            mostrar_error("Opción inválida")
            time.sleep(1)

def inicio():
    limpiar_pantalla()
    mostrar_header("SISTEMA DE CONFIGURACIÓN STELLAR")
    mostrar_carga("Inicializando sistema")
    
    # Crear archivos esenciales si no existen
    user_path = SYSTEM_DIR / "user.txt"
    if not user_path.exists():
        user_path.write_text("Usuario Stellar")
    
    metodo_path = SYSTEM_DIR / "login_method.txt"
    if not metodo_path.exists():
        metodo_path.write_text("no")
    
    banner_path = THEMES_DIR / "banner.txt"
    if not banner_path.exists():
        banner_path.write_text("Stellar Terminal\nPersonaliza tu experiencia")
    
    menu_principal()

if __name__ == "__main__":
    inicio()