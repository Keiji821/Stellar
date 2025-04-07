from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich import box
from rich.style import Style

console = Console()

console.print(
    Panel.fit(
        Text("Comandos de Stellar", justify="center", style="bold green"),
        border_style="bright_blue",
        padding=(1, 4),
        title="✨",
        subtitle="by Stellar Team"
    )
)

categories = [
    {
        "title": "SISTEMA", 
        "commands": [
            {"name": "reload", "description": "Recarga el banner y actualiza Stellar"},
            {"name": "clear", "description": "Limpia la pantalla de la terminal"},
            {"name": "bash", "description": "Reinicia la terminal"},
            {"name": "ui", "description": "Personaliza banner, fuente y texto de input"}
        ],
        "color": "bright_cyan"
    },
    {
        "title": "UTILIDADES", 
        "commands": [
            {"name": "ia", "description": "Servicio de IA mediante API gratuita"},
            {"name": "ia-image", "description": "Genera imágenes con IA"},
            {"name": "traductor", "description": "Servicio de traducción"},
            {"name": "myip", "description": "Muestra tu IP e información relacionada"}
        ],
        "color": "bright_magenta"
    },
    {
        "title": "OSINT", 
        "commands": [
            {"name": "ipinfo", "description": "Obtiene información de una IP"},
            {"name": "phoneinfo", "description": "Consulta información de teléfonos"},
            {"name": "urlinfo", "description": "Analiza URLs y enlaces"},
            {"name": "metadatainfo", "description": "Extrae metadatos de archivos"},
            {"name": "emailsearch", "description": "Busca correos electrónicos"},
            {"name": "userfinder", "description": "Verifica nombres de usuario"}
        ],
        "color": "bright_yellow"
    },
    {
        "title": "OSINT/Discord", 
        "commands": [
            {"name": "userinfo", "description": "Obtiene información de IDs de Discord"}
        ],
        "color": "bright_red"
    }
]

for category in categories:
    table = Table(
        title=f"[b {category['color']}]{category['title']}[/]",
        border_style=category['color'],
        box=box.ROUNDED,
        header_style=f"b {category['color']}",
        title_justify="left"
    )
    table.add_column("Comando", style="bold yellow", width=15)
    table.add_column("Descripción", style="bright_white")
    
    for cmd in category['commands']:
        table.add_row(cmd['name'], cmd['description'])
    
    console.print(table)
    console.print()

hotkeys_table = Table(
    title="[b]Atajos de teclado[/]",
    border_style="bright_green",
    box=box.DOUBLE_EDGE
)
hotkeys_table.add_column("Combinación", style="bold yellow")
hotkeys_table.add_column("Acción", style="bright_white")
hotkeys_table.add_row("CTRL + Z", "Detiene cualquier comando o proceso")
hotkeys_table.add_row("CTRL + C", "Fuerza la detención de procesos activos")

console.print(hotkeys_table)