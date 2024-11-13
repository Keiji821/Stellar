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
        {"name": "bash", "description": "Esto reiniciará su terminal."}
    ]},
    {"title": "UTILIDADES", "commands": [
        {"name": "ia", "description": "Un pequeño servicio de inteligencia artificial mediante un API gratis."},
        {"name": "myip", "description": "Muestra tu ip real y recupera información de la misma."},
    ]},
    {"title": "OSINT", "commands": [
        {"name": "ipinfo", "description": "Obtiene la información de una IP, ya sea IPv4 o IPv6."},
        {"name": "phoneinfo", "description": "Obtiene la información de un número de teléfono."},
        {"name": "urlinfo", "description": "Obtiene información relevante de una URL o enlace."},
        {"name": "metadatainfo", "description": "Recupera los metadatos de una imagen, archivo o video."},
        {"name": "emailsearch", "description": "Busca correos electrónicos con el nombre y apellido proporcionados."}
    ]}
]

colors = ["green", "yellow", "red"]

for i, category in enumerate(categories):
    color = colors[i % len(colors)]
    console.print(f"[bold {color}]▸ {category['title']}[/bold {color}]")
    for command in category["commands"]:
        console.print(f"   [bold yellow]{command['name']}[/bold yellow]: {command['description']}")
    console.print(" ")

console.print("[code]CTRL + Z │ Esto detendrá cualquier comando o proceso existente.[/code]", justify=("center"))
console.print("[code]CTRL + C │ Esto forzará a cualquier proceso activo a que se detenga, debes pulsar varias veces las dos combinaciones las veces que haga falta hasta que se detenga el proceso.[/code]", justify=("center"))
console.print(" ")
console.print(" ")