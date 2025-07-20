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

def dracula():
    return """
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
"""

def nord():
    return """
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
"""

def gruvbox():
    return """
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
"""

def tokyo_night():
    return """
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
"""

def one_dark():
    return """
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
"""

def monokai():
    return """
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
"""

def solarized_dark():
    return """
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
"""

def catppuccin_latte():
    return """
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
"""

def cyberpunk_neon():
    return """
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
"""

def everforest():
    return """
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
"""

def material_ocean():
    return """
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
"""

def horizon():
    return """
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
"""

def matrix():
    return """
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
"""

def hacker_purple():
    return """
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
"""

def cyberpunk_red():
    return """
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
"""

def hacker_retro():
    return """
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

THEMES = {
    "dracula": dracula(),
    "nord": nord(),
    "gruvbox": gruvbox(),
    "tokyo_night": tokyo_night(),
    "one_dark": one_dark(),
    "monokai": monokai(),
    "solarized_dark": solarized_dark(),
    "catppuccin_latte": catppuccin_latte(),
    "cyberpunk_neon": cyberpunk_neon(),
    "everforest": everforest(),
    "material_ocean": material_ocean(),
    "horizon": horizon(),
    "matrix": matrix(),
    "hacker_purple": hacker_purple(),
    "cyberpunk_red": cyberpunk_red(),
    "hacker_retro": hacker_retro()
}

COLORS = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "bright_black", "bright_red", "bright_green", "bright_yellow", 
    "bright_blue", "bright_magenta", "bright_cyan", "bright_white",
    "dark_red", "dark_green", "dark_yellow", "dark_blue",
    "dark_magenta", "dark_cyan", "grey0", "grey19", "grey30",
    "grey37", "grey46", "grey50", "grey54", "grey58", "grey62",
    "grey66", "grey70", "grey74", "grey78", "grey82", "grey85",
    "grey89", "grey93", "grey100", "orange1", "orange3", "orange4"
]

def error(mensaje):
    console.print(f"[bold red]✖[/bold red] {mensaje}")

def exito(mensaje):
    console.print(f"[bold green]✓[/bold green] {mensaje}")

def pregunta(mensaje):
    console.print(f"[bold yellow]?[/bold yellow] {mensaje}")

def informacion(mensaje):
    console.print(f"[bold cyan]→[/bold cyan] {mensaje}")

def verificar_termux_api():
    try:
        result = subprocess.run(['pkg', 'list-installed'], 
                               capture_output=True, text=True, check=True)
        return 'termux-api' in result.stdout
    except subprocess.CalledProcessError:
        return False

def configurar_banner():
    if Confirm.ask("[bold green]¿Configurar contenido del banner?[/bold green]"):
        banner_path = THEMES_DIR / "banner.txt"
        subprocess.run(["nano", str(banner_path)])
        exito("Banner configurado correctamente")
    
    if Confirm.ask("[bold green]¿Configurar color del banner?[/bold green]"):
        for color in COLORS:
            console.print(f"[{color}]{color}[/{color}]")
        color = Prompt.ask("[green]Seleccione color[/green]", choices=COLORS)
        (THEMES_DIR / "banner_color.txt").write_text(color)
        exito(f"Color del banner configurado: {color}")
    
    if Confirm.ask("[bold green]¿Agregar fondo al banner?[/bold green]"):
        (THEMES_DIR / "banner_background.txt").write_text("si")
        for color in COLORS:
            console.print(f"[{color}]{color}[/{color}]")
        bg_color = Prompt.ask("[green]Seleccione color de fondo[/green]", choices=COLORS)
        (THEMES_DIR / "banner_background_color.txt").write_text(bg_color)
        exito(f"Color de fondo configurado: {bg_color}")
    else:
        (THEMES_DIR / "banner_background.txt").write_text("no")
        exito("Fondo de banner desactivado")

def configurar_tema_termux():
    if not Confirm.ask("[bold green]¿Configurar tema de Termux?[/bold green]"):
        return
    
    console.print("[bold cyan]Temas disponibles:[/bold cyan]")
    theme_table = Table(show_header=True, header_style="bold magenta", box=SQUARE)
    theme_table.add_column("Nombre", style="cyan")
    theme_table.add_column("Preview", width=30)
    
    for name in THEMES:
        colors = THEMES[name].split('\n')
        preview = Text("")
        for i in range(1, 8):
            if any(f"color{i}=" in line for line in colors):
                color_line = [line for line in colors if f"color{i}=" in line][0]
                color_val = color_line.split('=')[1]
                preview.append("■■■ ", style=f"on {color_val}")
        theme_table.add_row(name, preview)
    
    console.print(theme_table)
    
    opcion = Prompt.ask("[green]Seleccione una opción[/green]", choices=["s", "c"], default="s")
    
    if opcion == "s":
        tema = Prompt.ask("[green]Ingrese el nombre del tema[/green]", choices=list(THEMES.keys()))
        TERMUX_COLORS_PATH.write_text(THEMES[tema])
        exito(f"Tema {tema} aplicado correctamente")
    else:
        subprocess.run(["nano", str(TERMUX_COLORS_PATH)])
        exito("Tema personalizado configurado")

def configurar_usuario():
    user_path = SYSTEM_DIR / "user.txt"
    
    if user_path.exists():
        usuario_actual = user_path.read_text().strip()
        if usuario_actual == "Stellar":
            error("Usuario no configurado")
        else:
            pregunta(f"Usuario actual: [bold magenta]{usuario_actual}[/bold magenta]")
            if not Confirm.ask("[yellow]¿Reemplazar usuario?[/yellow]", default=False):
                informacion("Usuario no modificado")
                return
    
    while True:
        nuevo_usuario = Prompt.ask("[cyan]Ingrese nuevo usuario[/cyan]", default="").strip()
        if nuevo_usuario:
            user_path.write_text(nuevo_usuario)
            exito(f"Usuario [bold]{nuevo_usuario}[/bold] configurado correctamente")
            return
        error("Nombre vacío no permitido")

def configurar_autenticacion():
    metodo_path = SYSTEM_DIR / "login_method.txt"
    
    if metodo_path.exists():
        metodo_actual = metodo_path.read_text().strip()
        if metodo_actual == "no":
            error("No tiene método de desbloqueo configurado")
        else:
            metodo = "Huella digital" if metodo_actual == "termux-fingerprint" else "Desconocido"
            pregunta(f"Método actual: [bold magenta]{metodo}[/bold magenta]")
            if not Confirm.ask("[yellow]¿Reemplazar método?[/yellow]", default=False):
                informacion("Método no modificado")
                return
    
    table = Table(box=ROUNDED, show_header=False)
    table.add_column("Opciones", style="cyan")
    table.add_row("[bold green]1)[/bold green] Huella digital")
    table.add_row("[bold green]2)[/bold green] Desactivar protección")
    console.print(table)

    opcion = Prompt.ask("[cyan]Seleccione [1-2][/cyan]", choices=["1", "2"], default="1")

    if opcion == "1":
        if verificar_termux_api():
            metodo_path.write_text("termux-fingerprint")
            exito("Autenticación por huella digital activada")
        else:
            error("Termux-API no está instalado")
            informacion("Instale con: [bold]pkg install termux-api[/bold]")
    else:
        metodo_path.write_text("no")
        exito("Protección desactivada")

def probar_autenticacion():
    metodo_path = SYSTEM_DIR / "login_method.txt"
    
    if not metodo_path.exists():
        error("No tiene método de autenticación configurado")
        time.sleep(1.5)
        return
    
    metodo = metodo_path.read_text().strip()
    
    if metodo == "termux-fingerprint":
        rprint("\n[bold yellow]Probando autenticación...[/bold yellow]")
        try:
            subprocess.run(['termux-fingerprint'], check=True)
            exito("Autenticación exitosa")
        except subprocess.CalledProcessError:
            error("Autenticación fallida")
        Prompt.ask("[yellow]Presione Enter para continuar...[/yellow]")
    else:
        error("Método de huella no configurado")
        time.sleep(1.5)

def mostrar_encabezado():
    rprint(Panel.fit(
        "[bold white]Configuración de Stellar[/bold white]",
        style="bold white on blue",
        subtitle="[yellow]Sistema de Temas y Autenticación[/yellow]"
    ))

def mostrar_estado():
    estado_table = Table(show_header=False, box=None)
    estado_table.add_column("Configuración", style="magenta")
    estado_table.add_column("Valor", style="cyan")
    
    user_path = SYSTEM_DIR / "user.txt"
    if user_path.exists():
        usuario = user_path.read_text().strip()
        estado_table.add_row("Usuario:", f"[bold]{usuario}[/bold]")
    
    metodo_path = SYSTEM_DIR / "login_method.txt"
    if metodo_path.exists():
        metodo = metodo_path.read_text().strip()
        estado = "[bold green]Huella activada" if metodo == "termux-fingerprint" else "[bold yellow]Protección desactivada"
        estado_table.add_row("Seguridad:", estado)
    
    banner_path = THEMES_DIR / "banner.txt"
    if banner_path.exists():
        estado_table.add_row("Banner:", "[bold green]Configurado[/bold green]")
    
    console.print(estado_table)

def menu_principal():
    while True:
        mostrar_encabezado()
        mostrar_estado()
        
        menu_table = Table(box=ROUNDED, show_header=False)
        menu_table.add_column("Opciones", style="cyan")
        menu_table.add_row("[bold green]1)[/bold green] Configurar banner")
        menu_table.add_row("[bold green]2)[/bold green] Configurar tema Termux")
        menu_table.add_row("[bold green]3)[/bold green] Configurar usuario")
        menu_table.add_row("[bold green]4)[/bold green] Configurar autenticación")
        menu_table.add_row("[bold green]5)[/bold green] Probar autenticación")
        menu_table.add_row("[bold green]6)[/bold green] Salir")
        console.print(menu_table)
        
        opcion = Prompt.ask("[cyan]Seleccione opción [1-6][/cyan]", choices=["1", "2", "3", "4", "5", "6"])
        
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
            rprint("\n[bold green]Saliendo del sistema...[/bold green]")
            exit(0)

def inicio():
    rprint(Panel.fit(
        "[bold white]Sistema de Configuración Stellar[/bold white]",
        style="bold white on magenta",
        subtitle="[yellow]Bienvenido[/yellow]"
    ))
    
    menu_principal()

if __name__ == "__main__":
    inicio()