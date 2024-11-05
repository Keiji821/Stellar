from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.panel import Panel

console = Console()

MARKDOWN = """
# Comandos de Stellar
"""
md = Markdown(MARKDOWN)
console.print(md, style="bold magenta")

console.print()

categories = [
    {"title": "PRINCIPALES", "commands": [
        {"name": "reload", "description": "Reinicia su sesión de termux/bash."}
    ]},
    {"title": "UTILIDADES", "commands": [
        {"name": "ia", "description": "Un pequeño servicio de inteligencia artificial."}
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
    table = Table(title=f"[bold blue]{category['title']}[/bold blue]", title_justify="center")
    table.add_column("Comando", style="cyan", no_wrap=True)
    table.add_column("Descripción", style="magenta")

    for command in category["commands"]:
        table.add_row(command["name"], command["description"])

    console.print(table)

console.print()
console.print(Panel("CTRL + Z : Esto detendrá cualquier comando o proceso existente.", title="[bold red]Atención[/bold red]"), style="bold yellow")
print(" ")
print(" ")