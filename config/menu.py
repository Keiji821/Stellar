from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print

console = Console()

console.print("[code][bold green]Comandos de Stellar[/bold green][/code]", justify=("center"))

categories = [
    {"title": "SISTEMA", "commands": [
        {"name": "reload", "description": "Esto recargará el banner y actualizará Stellar."},
        {"name": "clear", "description": "Esto limpiará la pantalla de su terminal."},
        {"name": "bash", "description": "Esto reiniciará su terminal."},
        {"name": "ui", "description": "Te permite personalizar el banner y la fuente del banner asi como el texto de la input."}
    ]},
    {"title": "UTILIDADES", "commands": [
        {"name": "ia", "description": "Un pequeño servicio de inteligencia artificial mediante una API gratis."},
        {"name": "myip", "description": "Muestra tu ip real y recupera información de la misma."},
    ]},
    {"title": "OSINT", "commands": [
        {"name": "ipinfo", "description": "Obtiene la información de una IP, ya sea IPv4 o IPv6."},
        {"name": "phoneinfo", "description": "Obtiene la información de un número de teléfono."},
        {"name": "urlinfo", "description": "Obtiene información relevante de una URL o enlace."},
        {"name": "metadatainfo", "description": "Recupera los metadatos de una imagen, archivo o video."},
        {"name": "emailsearch", "description": "Busca correos electrónicos con el nombre y apellido proporcionados."},
        {"name": "userfinder", "description": "Verifica si existe el usuario y obtiene información sobre el nombre de usuario proporcionado."}
    ]},
    {"title": "OSINT/Discord", "commands": [
        {"name": "userinfo", "description": "Obtiene información sobre el ID ingresado."},
    ]}
]

colors = ["green"]

for i, category in enumerate(categories):
    color = colors[i % len(colors)]
    console.print(f"[bold {color}]▸ {category['title']}[/bold {color}]")
    for command in category["commands"]:
        console.print(f"   [bold yellow]{command['name']}[/bold yellow]: {command['description']}")
    console.print(" ")

console.print("[code][bold yellow]CTRL + Z[/bold yellow][/code] [bold green]Esto detendrá cualquier comando o proceso existente.[/bold green]")
console.print(" ")
console.print("[code][bold yellow]CTRL + C[/bold yellow][/code] [bold green]Esto forzará a cualquier proceso activo a que se detenga, debes pulsar varias veces las dos combinaciones las veces que haga falta hasta que se detenga el proceso.[/bold green]")
console.print(" ")
console.print(" ")
