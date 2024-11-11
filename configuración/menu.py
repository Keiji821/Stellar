from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.panel import Panel
from rich import print 

console = Console()

console.print(" ")
console.print(Panel(":dvd: Versión V1.0.", title="[code][bold magenta]Comandos de Stellar[/bold magenta][/code]", border_style="bold cyan", style="bold purple"))
console.print(" ")

categories = [
    {"title": "SISTEMA", "commands": [
        {"name": ":gear: reload", "description": "Esto recargará el banner y actualizará Stellar."},
        {"name": ":gear: clear", "description": "Esto limpiará la pantalla de su terminal."},
        {"name": ":gear: bash", "description": "Esto reiniciará su terminal."}
    ]},
    {"title": "UTILIDADES", "commands": [
        {"name": ":gear: ia", "description": "Un pequeño servicio de inteligencia artificial mediante un API gratis."}
        {"name": ":gear: myip", "description": "Muestra tu ip real y recupera información de la misma."},
    ]},
    {"title": "OSINT", "commands": [
        {"name": ":gear: ipinfo", "description": "Obtiene la información de una IP, ya sea IPv4 o IPv6."},
        {"name": ":gear: phoneinfo", "description": "Obtiene la información de un número de teléfono."},
        {"name": ":gear: urlinfo", "description": "Obtiene información relevante de una URL o enlace."},
        {"name": ":gear: metadatainfo", "description": "Recupera los metadatos de una imagen, archivo o video."},
        {"name": ":gear: emailsearch", "description": "Busca correos electrónicos con el nombre y apellido proporcionados."}
    ]}
]

for category in categories:
    table = Table(title=f"[bold magenta]{category['title']}[/bold magenta]", title_justify="center", border_style="bright_cyan")
    table.add_column("Comando", style="bold cyan", no_wrap=False)
    table.add_column("Descripción", style="bold white")

    for command in category["commands"]:
        table.add_row(f"[bold yellow]{command['name']}[/bold yellow]", f"[italic white]{command['description']}[/italic white]")

    console.print(Panel(table, border_style="bright_magenta", style="bold purple"))

console.print(Panel("CTRL + Z │ Esto detendrá cualquier comando o proceso existente.", title="[code][bold magenta]Nota[/bold magenta][/code]", border_style="bold cyan", style="bold purple"))
console.print(" ")
console.print(" ")