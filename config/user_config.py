import os
import subprocess
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich.table import Table
from rich.box import ROUNDED, SQUARE
from rich import print as rprint
from pathlib import Path

console = Console()

STELLAR_DIR = Path("~/Stellar").expanduser()
THEMES_DIR = STELLAR_DIR / "config/themes"
SYSTEM_DIR = STELLAR_DIR / "config/system"
TERMUX_COLORS_PATH = Path("~/.termux/colors.properties").expanduser()

THEMES_DIR.mkdir(parents=True, exist_ok=True)
SYSTEM_DIR.mkdir(parents=True, exist_ok=True)

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

def mostrar_error(mensaje):
    console.print(f"✖ [bold red]{mensaje}[/bold red]")

def mostrar_exito(mensaje):
    console.print(f"✓ [bold green]{mensaje}[/bold green]")

def mostrar_advertencia(mensaje):
    console.print(f"⚠ [bold yellow]{mensaje}[/bold yellow]")

def mostrar_informacion(mensaje):
    console.print(f"→ [bold cyan]{mensaje}[/bold cyan]")

def mostrar_titulo(mensaje):
    console.print(Panel.fit(
        mensaje,
        style="bold white on rgb(50,57,150)",
        padding=(1, 2),
        subtitle="[yellow]Sistema de Configuración Stellar[/yellow]"
    ))

def verificar_termux_api():
    try:
        resultado = subprocess.run(
            ['pkg', 'list-installed'], 
            capture_output=True, 
            text=True, 
            check=True
        )
        return 'termux-api' in resultado.stdout
    except:
        return False

def configurar_banner():
    mostrar_titulo("Configuración de Banner")
    
    if Confirm.ask("¿Configurar contenido del banner?"):
        banner_path = THEMES_DIR / "banner.txt"
        subprocess.run(["nano", str(banner_path)])
        mostrar_exito("Contenido del banner configurado")
    
    if Confirm.ask("¿Configurar color del banner?"):
        console.print("\n[bold magenta]Colores disponibles:[/bold magenta]")
        
        for i in range(0, len(COLORES_DISPONIBLES), 4):
            fila = COLORES_DISPONIBLES[i:i+4]
            linea = ""
            for color in fila:
                linea += f"[{color}]{color.ljust(15)}[/{color}]"
            console.print(linea)
        
        color = Prompt.ask("\nSeleccione color para el banner", choices=COLORES_DISPONIBLES)
        (THEMES_DIR / "banner_color.txt").write_text(color)
        mostrar_exito(f"Color del banner configurado: {color}")
    
    if Confirm.ask("¿Agregar fondo al banner?"):
        (THEMES_DIR / "banner_background.txt").write_text("si")
        
        console.print("\n[bold magenta]Colores disponibles para fondo:[/bold magenta]")
        for i in range(0, len(COLORES_DISPONIBLES), 4):
            fila = COLORES_DISPONIBLES[i:i+4]
            linea = ""
            for color in fila:
                linea += f"[{color}]{color.ljust(15)}[/{color}]"
            console.print(linea)
        
        bg_color = Prompt.ask("\nSeleccione color para fondo", choices=COLORES_DISPONIBLES)
        (THEMES_DIR / "banner_background_color.txt").write_text(bg_color)
        mostrar_exito(f"Color de fondo configurado: {bg_color}")
    else:
        (THEMES_DIR / "banner_background.txt").write_text("no")
        mostrar_informacion("Fondo del banner desactivado")

def mostrar_previa_tema(tema, contenido):
    colores = {}
    for linea in contenido.strip().split('\n'):
        if '=' in linea:
            clave, valor = linea.split('=', 1)
            colores[clave] = valor
    
    tabla = Table(show_header=False, box=SQUARE, padding=(0, 1))
    tabla.add_column("Propiedad", style="bold cyan", width=15)
    tabla.add_column("Valor", width=20)
    tabla.add_column("Muestra", width=10)
    
    propiedades = ['background', 'foreground', 'color0', 'color1', 'color2', 'color3', 'color4']
    
    for prop in propiedades:
        if prop in colores:
            valor = colores[prop]
            muestra = Text("  " * 4, style=f"on {valor}")
            tabla.add_row(prop, valor, muestra)
    
    console.print(Panel(
        tabla,
        title=f"[bold]{tema.upper()}[/bold]",
        border_style="bright_magenta",
        padding=(1, 2)
    ))

def configurar_tema_termux():
    mostrar_titulo("Configuración de Tema para Termux")
    
    if not Confirm.ask("¿Configurar tema para Termux?"):
        mostrar_informacion("Configuración cancelada")
        return
    
    console.print("\n[bold magenta]Temas disponibles:[/bold magenta]")
    
    temas_tabla = Table(
        box=SQUARE,
        header_style="bold cyan",
        title_style="bold yellow",
        expand=True
    )
    temas_tabla.add_column("Nombre", style="bold magenta", width=20)
    temas_tabla.add_column("Preview", width=50)
    
    for nombre, contenido in TERMUX_THEMES.items():
        lineas = contenido.strip().split('\n')
        preview = Text()
        for i in range(min(5, len(lineas))):
            if '=' in lineas[i]:
                _, valor = lineas[i].split('=', 1)
                preview.append(f"{valor} ", style=f"on {valor}" if "background" not in lineas[i] else f"on {valor}")
        temas_tabla.add_row(nombre, preview)
    
    console.print(temas_tabla)
    
    console.print("\n[bold green]Opciones:[/bold green]")
    console.print(" [bold cyan]s[/bold cyan] - Seleccionar tema predefinido")
    console.print(" [bold cyan]c[/bold cyan] - Crear tema personalizado")
    
    opcion = Prompt.ask("\nSeleccione opción", choices=["s", "c"])
    
    if opcion == "s":
        tema = Prompt.ask("Ingrese nombre del tema", choices=list(TERMUX_THEMES.keys()))
        TERMUX_COLORS_PATH.write_text(TERMUX_THEMES[tema])
        mostrar_exito(f"Tema {tema} aplicado")
        mostrar_informacion("Reinicie Termux para ver cambios")
    else:
        mostrar_informacion("Abriendo editor para tema personalizado")
        subprocess.run(["nano", str(TERMUX_COLORS_PATH)])
        mostrar_exito("Tema personalizado configurado")

def configurar_usuario():
    mostrar_titulo("Configuración de Usuario")
    user_path = SYSTEM_DIR / "user.txt"
    
    if user_path.exists():
        usuario_actual = user_path.read_text().strip()
        if usuario_actual == "Stellar":
            mostrar_error("Usuario no configurado")
        else:
            console.print(f"Usuario actual: [bold magenta]{usuario_actual}[/bold magenta]")
            if not Confirm.ask("¿Cambiar usuario?"):
                mostrar_informacion("Usuario no modificado")
                return
    
    while True:
        nuevo_usuario = Prompt.ask("Ingrese nuevo nombre de usuario").strip()
        if nuevo_usuario:
            user_path.write_text(nuevo_usuario)
            mostrar_exito(f"Usuario {nuevo_usuario} configurado")
            return
        mostrar_error("Nombre de usuario no válido")

def configurar_autenticacion():
    mostrar_titulo("Configuración de Autenticación")
    metodo_path = SYSTEM_DIR / "login_method.txt"
    
    if metodo_path.exists():
        metodo_actual = metodo_path.read_text().strip()
        if metodo_actual == "no":
            mostrar_error("Método no configurado")
        else:
            metodo = "Huella digital" if metodo_actual == "termux-fingerprint" else "Desconocido"
            console.print(f"Método actual: [bold magenta]{metodo}[/bold magenta]")
            if not Confirm.ask("¿Cambiar método?"):
                mostrar_informacion("Método no modificado")
                return
    
    console.print("\n[bold green]Opciones:[/bold green]")
    console.print(" [bold cyan]1[/bold cyan] - Autenticación por huella")
    console.print(" [bold cyan]2[/bold cyan] - Desactivar protección")
    
    opcion = Prompt.ask("\nSeleccione opción", choices=["1", "2"])
    
    if opcion == "1":
        if verificar_termux_api():
            metodo_path.write_text("termux-fingerprint")
            mostrar_exito("Autenticación por huella activada")
        else:
            mostrar_error("Termux-API no instalado")
            mostrar_informacion("Instale con: pkg install termux-api")
    else:
        metodo_path.write_text("no")
        mostrar_exito("Protección desactivada")

def probar_autenticacion():
    mostrar_titulo("Prueba de Autenticación")
    metodo_path = SYSTEM_DIR / "login_method.txt"
    
    if not metodo_path.exists():
        mostrar_error("Método no configurado")
        time.sleep(2)
        return
    
    metodo = metodo_path.read_text().strip()
    
    if metodo == "termux-fingerprint":
        console.print("\n[bold yellow]Probando autenticación...[/bold yellow]")
        try:
            subprocess.run(['termux-fingerprint'], check=True)
            mostrar_exito("Autenticación exitosa")
        except:
            mostrar_error("Autenticación fallida")
        console.print("\n[bold cyan]Presione Enter para continuar...[/bold cyan]")
        input()
    else:
        mostrar_error("Método de huella no configurado")
        time.sleep(2)

def mostrar_estado_actual():
    estado_tabla = Table(
        title="[bold magenta]Estado Actual[/bold magenta]",
        box=ROUNDED,
        header_style="bold cyan",
        title_style="bold yellow"
    )
    estado_tabla.add_column("Configuración", style="magenta")
    estado_tabla.add_column("Valor", style="cyan")
    
    user_path = SYSTEM_DIR / "user.txt"
    if user_path.exists():
        usuario = user_path.read_text().strip()
        estado_tabla.add_row("Usuario", f"[bold]{usuario}[/bold]")
    
    metodo_path = SYSTEM_DIR / "login_method.txt"
    if metodo_path.exists():
        metodo = metodo_path.read_text().strip()
        estado = "[bold green]Activada" if metodo == "termux-fingerprint" else "[bold yellow]Desactivada"
        estado_tabla.add_row("Autenticación", estado)
    
    banner_path = THEMES_DIR / "banner.txt"
    if banner_path.exists():
        estado_tabla.add_row("Banner", "[bold green]Configurado[/bold green]")
    
    console.print(estado_tabla)

def menu_principal():
    while True:
        console.print("\n" * 2)
        mostrar_titulo("Panel Principal")
        mostrar_estado_actual()
        
        menu_tabla = Table(
            box=ROUNDED,
            show_header=False
        )
        menu_tabla.add_column("Opción", style="magenta", width=10)
        menu_tabla.add_column("Descripción", style="cyan")
        
        menu_tabla.add_row("1", "Configurar banner")
        menu_tabla.add_row("2", "Configurar tema Termux")
        menu_tabla.add_row("3", "Configurar usuario")
        menu_tabla.add_row("4", "Configurar autenticación")
        menu_tabla.add_row("5", "Probar autenticación")
        menu_tabla.add_row("6", "Salir del sistema")
        
        console.print(menu_tabla)
        
        opcion = Prompt.ask("\nSeleccione opción", choices=["1", "2", "3", "4", "5", "6"])
        
        if opcion == "1":
            configurar_banner()
        elif opcion == "2":
            configurar_tema_termux()
        elif opcion == "3":
            configurar_usuario()
        elif opcion == "4":
            configurar_autenticacion()
        elif opcion == "5":
            probar_autenticacion()
        elif opcion == "6":
            console.print("\n[bold green]Saliendo del sistema...[/bold green]")
            time.sleep(1)
            exit(0)

def inicio():
    console.print(Panel.fit(
        "[bold white]Sistema de Configuración Stellar[/bold white]",
        style="bold white on rgb(50,57,150)",
        padding=(1, 2),
        subtitle="[yellow]Bienvenido al panel de configuración[/yellow]"
    ))
    
    user_path = SYSTEM_DIR / "user.txt"
    if not user_path.exists():
        mostrar_advertencia("Usuario no configurado")
        configurar_usuario()
    
    metodo_path = SYSTEM_DIR / "login_method.txt"
    if not metodo_path.exists():
        mostrar_advertencia("Autenticación no configurada")
        configurar_autenticacion()
    
    time.sleep(1)
    menu_principal()

if __name__ == "__main__":
    inicio()