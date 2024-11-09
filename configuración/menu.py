from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.panel import Panel

console = Console()

print(" ")

console.print("`Comandos de Stellar`")

console.print(" ")

categories = [
    {"title": "SISTEMA", "commands": [
        {"name": "reload", "description": "Esto recargara el banner."}
        {"name": "clear", "description": "Esto limpiara la pantalla de su terminal."}
        {"name": "bash", "description": "Esto reiniciara su terminal."}
    ]},
    {"title": "UTILIDADES", "commands": [
        {"name": "ia", "description": "Un pequeño servicio de inteligencia artificial mediante un api gratis."}
    ]},
    {"title": "OSINT", "commands": [
        {"name": "ipinfo", "description": "Obtiene la información de una ip, ya sea IPV4 o IPV6."},
        {"name": "phoneinfo", "description": "Obtiene la información de un número de teléfono."},
        {"name": "urlinfo", "description": "Obtiene información relevante de una url o enlace."},
        {"name": "metadatainfo", "description": "Recupera los metadatos de una imagen, archivo o video."},
        {"name": "emailsearch", "description": "Busca correos electrónicos con el nombre y apellido proporcionados."}
    ]}
]

for category in categories:
    table = Table(title=f"[bold red]{category['title']}[/bold red]", title_justify="center")
    table.add_column("Comando", style="green", no_wrap=True)
    table.add_column("Descripción", style="white")

    for command in category["commands"]:
        table.add_row(command["name"], command["description"])

    console.print(table)

console.print()
console.print(Panel("CTRL + Z : Esto detendrá cualquier comando o proceso existente.", title="[bold red]Nota[/bold red]"), style="bold yellow")
print(" ")
print(" ")
