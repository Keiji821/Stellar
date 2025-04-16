from rich.console import Console
from rich.style import Style
from rich.rule import Rule
from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED

console = Console()

def print_fullwidth(text, style=""):
    console.print(text.ljust(console.width), style=style)

menu_data = {    
    "🌌 SISTEMA": [        
        ("reload", "Recarga el banner estelar"),
        ("clear", "Limpia el cosmos terminal"),
        ("bash", "Reinicia la constelación"),
        ("ui", "Personaliza tu universo visual")
    ],
    "✨ UTILIDADES": [
        ("ia", "Asistente cósmico con IA"),
        ("ia-image", "Genera nebulosas digitales"),
        ("traductor", "Traduce lenguajes estelares"),
        ("myip", "Localiza tu posición galáctica")
    ],
    "🔍 HERRAMIENTAS OSINT": [
        ("ipinfo", "Analiza constelaciones IP"),
        ("phoneinfo", "Rastrea comunicaciones interestelares"),
        ("urlinfo", "Explora galaxias web"),
        ("metadatainfo", "Descubre secretos de archivos cósmicos"),
        ("emailsearch", "Busca mensajes en el vacío digital"),
        ("userfinder", "Rastrea entidades en la red")
    ],
    "💬 DISCORD": [
        ("userinfo", "Decodifica identidades discordianas")
    ]
}

console.print("\n")
console.print(Panel.fit(
    Text(" STELLAR OS ", justify="center", style="bold #FF66B2"),
    subtitle="by Keiji821",
    style="#23DCEF",
    border_style="#FF66B2",
    box=ROUNDED,
    padding=(1, 2)
)

console.print(Rule(style="#FF66B2"))
console.print("\n")

for categoria, comandos in menu_data.items():
    console.print(f" {categoria} ", style="bold #23DCEF on #1A1A2E")
    console.print(Rule(style="#FF66B2"))

    for cmd, desc in comandos:
        console.print(
            f"[#FF66B2]{' ' * 2}[/]"
            f"[bold #23DCEF]{cmd.ljust(18)}[/]"
            f"[#C9CBFF]{desc}[/]"
        )
    console.print("\n")

console.print(Rule(style="#FF66B2"))
console.print(Panel.fit(
    " Navegación: [bold #23DCEF]TAB[/] Autocompletado • [bold #23DCEF]↑↓[/] Movimiento ",
    style="#C9CBFF",
    border_style="#FF66B2",
    box=ROUNDED
))
console.print("\n")