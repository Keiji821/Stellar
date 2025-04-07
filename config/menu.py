from rich.console import Console
from rich.style import Style
from rich.rule import Rule

console = Console(style="grey78 on grey23")

def print_fullwidth(text, style=""):
    console.print(text.ljust(console.width), style=style)

menu_data = {    "SISTEMA":         
        ("reload", "Recarga el banner"),
        ("clear", "Limpia la pantalla"),
        ("bash", "Reinicia la sesión"),
        ("ui", "Personalizar temas e interfaz")
    ],
    "UTILIDADES": [
        ("ia", "Asistente IA con API integrada"),
        ("ia-image", "Generación de imágenes con IA"),
        ("traductor", "Traducción en tiempo real"),
        ("myip", "Muestra tu IP y información completa")
    ],
    "HERRAMIENTAS OSINT": [
        ("ipinfo", "Análisis detallado de IP"),
        ("phoneinfo", "Obtiene información de números de teléfonos"),
        ("urlinfo", "Escaneo de URLs y dominios"),
        ("metadatainfo", "Extracción de metadatos"),
        ("emailsearch", "Búsqueda de correos electrónicos"),
        ("userfinder", "Busqueda de nombres de usuario")
    ],
    "DISCORD": [
        ("userinfo", "Obtiene información sobre un ID")
    ]
}

console.print("\n")
console.print(Rule(style="grey23"))
console.print(" Comandos de Stellar ".center(console.width), style="bold grey93 on grey23")
console.print(" Hecho por Keiji821 ".center(console.width), style="grey70 on grey23")
console.print(Rule(style="grey23"))
console.print("\n")

for categoria, comandos in menu_data.items():
    console.print(f" {categoria} ", style="bold grey93 on grey23")
    console.print(Rule(style="grey23"))
    
    for cmd, desc in comandos:
        console.print(
            f"[grey78]{' ' * 2}[/]"
            f"[bold grey93]{cmd.ljust(18)}[/]"
            f"[grey78]{desc}[/]"
            f"[grey78]{' ' * (console.width - len(cmd) - len(desc) - 4)}[/]"
        )
    
    console.print("\n")

console.print(Rule(style="grey23"))
console.print(" Atajos del sistema ".center(console.width), style="bold grey93 on grey23")
console.print(Rule(style="grey23"))
console.print(
    f"[grey78]{' ' * 2}[/][bold grey93]CTRL+Z[/][grey78]{' ' * 10}[/]"
    f"[grey78]Detención segura de procesos[/]"
    f"[grey78]{' ' * (console.width - 37)}[/]"
)
console.print(
    f"[grey78]{' ' * 2}[/][bold grey93]CTRL+C[/][grey78]{' ' * 10}[/]"
    f"[grey78]Terminación forzada de procesos[/]"
    f"[grey78]{' ' * (console.width - 39)}[/]"
)
console.print("\n")
console.print(Rule(style="grey23"))
console.print(
    " Navegación: [bold grey93]TAB[/] Autocompletado • [bold grey93]↑↓[/] Movimiento ".center(console.width),
    style="grey70 on grey23"
)
console.print(Rule(style="grey23"))
console.print("\n")