from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
import pyfiglet

console = Console()

banner = pyfiglet.figlet_format("Comandos", font="cyberlarge")
console.print(
    Panel.fit(
        banner,
        title="[bold cyan]Stellar[/bold cyan]",
        subtitle="[italic]by Keiji821[/italic]",
        border_style="bright_blue",
    ),
    justify="center"
)

console.print(
    Panel.fit(
        "[bold white]Stellar[/bold white] mejora Termux con:[bold cyan]\n• Interfaz personalizable\n• Comandos OSINT/Hacking\n• Integración con Tor[/bold cyan]",
        border_style="blue",
    ),
    justify="center"
)

table = Table(
    title="📜 [bold green]Lista de Comandos[/bold green]",
    title_justify="center",
    border_style="bright_blue",
    header_style="bold magenta",
    show_header=True,
    show_edge=True,
    show_lines=True
)
table.add_column("[bold cyan]Comando", style="cyan", min_width=15)
table.add_column("[bold cyan]Descripción", style="white", min_width=30)
table.add_column("[bold cyan]Estado", justify="center", min_width=15)

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
    table.add_row(Rule(f"[bold]{category}[/bold]", style="bold green"))
    for cmd, desc, status in items:
        color = "green" if "🟢" in status else "red"
        table.add_row(f"• {cmd}", desc, f"[{color}]{status}[/{color}]")

console.print(table, justify="center")

console.print(
    Panel.fit(
        "[bold yellow]🚀 ¡Próximamente más comandos![/bold yellow]",
        border_style="green",
    ),
    justify="center"
)