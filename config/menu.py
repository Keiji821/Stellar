from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich.box import ROUNDED
import pyfiglet

console = Console()

banner = pyfiglet.figlet_format("Stellar OS", font="cyberlarge")
console.print(
    Panel.fit(
        f"[bright_blue]{banner}[/bright_blue]",
        title="[bold cyan]Termux Edition[/bold cyan]",
        subtitle="[italic]by Keiji821[/italic]",
        border_style="bright_blue",
        box=ROUNDED,
        padding=(1, 4)
    ),
    justify="center"
)

features = """[bold white]✦ Interfaz personalizable[/bold white]
[bold cyan]✦ Comandos OSINT/Hacking[/bold cyan]
[bold magenta]✦ Integración con Tor[/bold magenta]"""

console.print(
    Panel.fit(
        features,
        title="[bold]Características Principales[/bold]",
        border_style="bright_green",
        box=ROUNDED,
        width=60
    ),
    justify="center"
)

table = Table(
    title="[bold green]📋 Lista Completa de Comandos[/bold green]",
    box=ROUNDED,
    border_style="bright_blue",
    header_style="bold magenta",
    show_header=True,
    show_edge=True,
    width=80,
    padding=(0, 1))
    
table.add_column("[bold cyan]Categoría[/bold cyan]", width=20)
table.add_column("[bold cyan]Comando[/bold cyan]", width=20)
table.add_column("[bold cyan]Descripción[/bold cyan]", width=30)
table.add_column("[bold cyan]Estado[/bold cyan]", justify="center", width=10)

commands = {
    "Sistema": [
        ("reload", "Recarga el banner", "🟢 Activo"),
        ("ui", "Personaliza la interfaz", "🟢 Activo"),
        ("uninstall", "Desinstala Stellar", "🟢 Activo"),
        ("update", "Actualiza desde GitHub", "🟢 Activo"),
        ("bash", "Reinicia la sesión", "🟢 Activo")
    ],
    "Utilidades": [
        ("ia", "Chat con IA (API gratuita)", "🔴 En mantenimiento"),
        ("ia-image", "Generador de imágenes IA", "🔴 En mantenimiento"),
        ("traductor", "Traducción en tiempo real", "🟢 Activo"),
        ("myip", "Muestra tu IP pública", "🟢 Activo")
    ],
    "OSINT": [
        ("ipinfo", "Información de una IP", "🟢 Activo"),
        ("urlinfo", "Analizador de URLs", "🟢 Activo"),
        ("userfinder", "Busca usuarios en redes", "🟢 Activo"),
        ("phoneinfo", "Info de números telefónicos", "🟢 Activo"),
        ("metadatainfo", "Extrae metadatos de archivos", "🟢 Activo"),
        ("emailsearch", "Búsqueda de correos", "🟢 Activo")
    ],
    "OSINT/Discord": [
        ("userinfo", "Obtiene info de usuario por ID", "🟢 Activo"),
        ("serverinfo", "Info de servidor por ID", "🟢 Activo"),
        ("searchinvites", "Busca invitaciones", "🟢 Activo"),
        ("inviteinfo", "Analiza enlaces de invitación", "🟢 Activo")
    ],
    "OSINT/Instagram": [
        ("profileinfo", "Obtiene metadatos de perfil", "🔴 En mantenimiento")
    ],
    "Pentesting": [
        ("ddos", "Ataque DDOS (IP+Puerto)", "🟢 Activo")
    ]
}

for category, items in commands.items():
    table.add_row(
        f"[bold yellow]{category}[/bold yellow]", 
        "", 
        "", 
        "", 
        style="on dark_blue"
    )
    for cmd, desc, status in items:
        color = "green" if "🟢" in status else ("yellow" if "🟡" in status else "red")
        table.add_row(
            "",
            f"[bright_white]• {cmd}[/bright_white]",
            desc,
            f"[{color}]{status}[/{color}]"
        )

console.print(table, justify="center")

console.print(
    Panel.fit(
        "[bold yellow]🚀 Desarrollo activo - Más comandos próximamente![/bold yellow]",
        border_style="bright_red",
        box=ROUNDED
    ),
    justify="center"
)