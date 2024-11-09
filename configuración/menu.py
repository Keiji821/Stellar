from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.panel import Panel
from rich import print 

console = Console()

console.print(" ")
markdown = Markdown("/n Hola")
console.print(f"[code]{markdown}[/code]")
console.print(Panel(":dvd: Versión V1.0.", title="[bold red]Comandos de Stellar[/bold red]"), style="bold yellow")

console.print(" ")

categories = [
    {"title": "SISTEMA", "commands": [
        {"name": ":gear: reload", "description": "Esto recargara el banner y actualizará stellar."},
        {"name": ":gear: clear", "description": "Esto limpiara la pantalla de su terminal."},
        {"name": ":gear: bash", "description": "Esto reiniciara su terminal."}
    ]},
    {"title": "UTILIDADES", "commands": [
        {"name": ":gear: ia", "description": "Un pequeño servicio de inteligencia artificial mediante un api gratis."}
    ]},
    {"title": "OSINT", "commands": [
        {"name": ":gear: ipinfo", "description": "Obtiene la información de una ip, ya sea IPV4 o IPV6."},
        {"name": ":gear: phoneinfo", "description": "Obtiene la información de un número de teléfono."},
        {"name": ":gear: urlinfo", "description": "Obtiene información relevante de una url o enlace."},
        {"name": ":gear: metadatainfo", "description": "Recupera los metadatos de una imagen, archivo o video."},
        {"name": ":gear: emailsearch", "description": "Busca correos electrónicos con el nombre y apellido proporcionados."}
    ]}
]

for category in categories:
    table = Table(title=f"[bold red]{category['title']}[/bold red]", title_justify="center")
    table.add_column("Comando", style="green", no_wrap=False)
    table.add_column("Descripción", style="white")

    for command in category["commands"]:
        table.add_row(command["name"], command["description"])

    console.print(table)

console.print(Panel("CTRL + Z │ Esto detendrá cualquier comando o proceso existente.", title="[bold red]Nota[/bold red]"), style="bold yellow")
console.print(" ")
console.print(" ")
