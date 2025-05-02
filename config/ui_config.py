from rich.console import Console
import os
from os import system

console = Console()

os.system("clear")

os.chdir("themes")

# themes/termux
dracula = """
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
color15=#E6E6E6"""

nord = """
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
color15=#FFFFFF"""

gruvbox = """
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
color15=#EBDBB2"""

tokyo_night = """
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
color15=#FFFFFF"""

one_dark = """
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
color15=#FFFFFF"""

# colors/banner/background
colors = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "bright_black", "bright_red", "bright_green", "bright_yellow", 
    "bright_blue", "bright_magenta", "bright_cyan", "bright_white",
    "dark_red", "dark_green", "dark_yellow", "dark_blue",
    "dark_magenta", "dark_cyan", "grey0", "grey19", "grey30",
    "grey37", "grey46", "grey50", "grey54", "grey58", "grey62",
    "grey66", "grey70", "grey74", "grey78", "grey82", "grey85",
    "grey89", "grey93", "grey100", "orange1", "orange3", "orange4"
]

banner = console.input("[bold green]¿Desea configurar el contenido del banner? (y/n): [/bold green]")
if banner=="y":
    console.print("[bold green]Presione [code][bold yellow][Enter][/code] [bold green]para configurar su banner[/bold green]")
    os.system("rm -rf banner.txt && nano banner.txt")

banner_color = console.input("[bold green]¿Desea configurar el color de su banner? (y/n): [/bold green]")
if banner_color=="y":
    bcolor = console.input("[bold green]¿Desea ver los colores disponibles? (y/n): [/bold green]")
    if bcolor=="y":       
        for color in colors:
           console.print(f"[{color}]{color}[/{color}]")
           console.print("")

    color_selection = console.input("[bold green]Ingrese el color a configurar: [/bold green]")
    os.system(f"echo {color_selection} > banner_color.txt")


banner_background = console.input("[bold green]¿Desea que su banner tenga un fondo? (y/n): [/bold green]")
if banner_background=="y":
    os.system("echo Sí > banner_background.txt")
    banner_background_color = console.input("[bold green]¿Desea agregar un color al fondo de su banner? (y/n): [/bold green]")
    if banner_background_color=="y":
        for color in colors:
            console.print(f"[{color}]{color}[/{color}]")
            console.print("")
    banner_background_color_selection = console.input("[bold green]Ingrese el color a configurar: [/bold green]")
    os.system(f"echo {banner_background_color_selection} > banner_background_color.txt")


termux_background = console.input("[bold green]¿Desea agregar un tema de fondo para su Termux? (y/n): [/bold green]")
if termux_background=="y":
    termux_background_list = console.input("[bold green]Pulse [code][bold yellow][Enter][/code] [bold green]para ver un listado de temas por defecto[/bold green]")

    console.print("[bold cyan]Temas por defecto[/bold cyan]")
    console.print("""
• dracula
• nord
• gruvbox
• tokyo_night
• one_dark
""")
    console.print("""[bold cyan]Opciones[/bold cyan]

• Ingrese "s" para elegir un banner por defecto
• Ingrese "c" para configurar un banner desde cero
""")
    termux_background_select = console.input("[bold green]Ingrese una opción: [/bold green]")    
    if termux_background_select=="s":
        theme = console.input("[bold green]Ingrese el tema por defecto a usar: [/bold green]")
        os.chdir("$HOME/.termux")
        if theme=="dracula":
            os.system(f"rm -rf colors.properties && echo {dracula} > colors.properties")
        if theme=="nord":
            os.system(f"rm -rf colors.properties && echo {nord} > colors.properties")
        if theme=="gruvbox":
            os.system(f"rm -rf colors.properties && echo {gruvbox} > colors.properties")
        if theme=="tokyo_night":
            os.system(f"rm -rf colors.properties && echo {tokyo_night} > colors.properties")
        if theme=="one_dark":
            os.system(f"rm -rf colors.properties && echo {one_dark} > colors.properties")
    if termux_background_select=="c":
        os.system("cd && cd .termux && rm -rf colors.properties && nano colors properties")

console.print("")
console.print("[code]Configuraciónes aplicadas correctamente[/code]", style="bold green", justify="center")
console.print("""
Escriba el comando "bash" o "login" para aplicar los cambios correctamente, para aplicar el tema de fondo de Termux reinicie la aplicación.""", justify="center")
console.print("")
