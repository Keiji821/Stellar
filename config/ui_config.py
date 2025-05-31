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

monokai = """
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
color15=#f9f8f5"""

solarized_dark = """
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
color15=#fdf6e3"""

catppuccin_latte = """
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
color15=#BCC0CC"""

cyberpunk_neon = """
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
color15=#FFFFFF"""

everforest = """
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
color15=#DEE2D9"""

material_ocean = """
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
color15=#A6ADC8"""

horizon = """
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
color15=#E6E6E6"""

matrix = """
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
color15=#FFFFFF"""

hacker_purple = """
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
color15=#FFFFFF"""

cyberpunk_red = """
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
color15=#FFFFFF"""

hacker_retro = """
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
if banner_background=="n":
    os.system("echo No > banner_background.txt")    
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
• solarized_dark
• monokai
• catppuccin_latte
• everforest
• horizon
• material_ocean
• cyberpunk_neon
• matrix
• hacker_purple
• cyberpunk_red
• hacker_retro
""")
    console.print("""[bold cyan]Opciones[/bold cyan]

• Ingrese "s" para elegir un banner por defecto
• Ingrese "c" para configurar un banner desde cero
""")
    termux_background_select = console.input("[bold green]Ingrese una opción: [/bold green]")    
    if termux_background_select=="s":
        theme = console.input("[bold green]Ingrese el tema por defecto a usar: [/bold green]")
        
        if theme=="dracula":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{dracula}\nEOF')
        if theme=="nord":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{nord}\nEOF')
        if theme=="gruvbox":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{gruvbox}\nEOF')
        if theme=="tokyo_night":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{tokyo_night}\nEOF')
        if theme=="one_dark":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{one_dark}\nEOF')
        if theme=="solarized_dark":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{solarized_dark}\nEOF')
        if theme=="monokai":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{monokai}\nEOF')
        if theme=="catppuccin_latte":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{catppuccin_latte}\nEOF')
        if theme=="everforest":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{everforest}\nEOF')
        if theme=="horizon":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{horizon}\nEOF')
        if theme=="material_ocean":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{material_ocean}\nEOF')
        if theme=="cyberpunk_neon":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{cyberpunk_neon}\nEOF')
        if theme=="matrix":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{matrix}\nEOF')
        if theme=="hacker_purple":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{hacker_purple}\nEOF')
        if theme=="cyberpunk_red":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{cyberpunk_red}\nEOF')
        if theme=="hacker_retro":
            os.system(f'cat << "EOF" > ~/.termux/colors.properties\n{hacker_retro}\nEOF')
    if termux_background_select=="c":
        os.system("cd && cd .termux && rm -rf colors.properties && nano colors.properties")

console.print("")
console.print("[code]Configuraciónes aplicadas correctamente[/code]", style="bold green", justify="center")
console.print("""
Escriba el comando "bash" o "login" para aplicar los cambios correctamente, para aplicar el tema de fondo de Termux reinicie la aplicación.""", justify="center")
console.print("")
