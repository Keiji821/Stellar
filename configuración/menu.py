from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print

console = Console()

categories = [
    {"title": "SISTEMA", "commands": [
        {"name": ":gear: reload", "description": "Esto recargará el banner y actualizará Stellar."},
        {"name": ":gear: clear", "description": "Esto limpiará la pantalla de su terminal."},
        {"name": ":gear: bash", "description": "Esto reiniciará su terminal."}
    ]},
    {"title": "UTILIDADES", "commands": [
        {"name": ":gear: ia", "description": "Un pequeño servicio de inteligencia artificial mediante un API gratis."},
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

colors = ["green", "yellow", "red"]

for i, category in enumerate(categories):
    color = colors[i % len(colors)]
    console.print(f"[bold {color}]▸ {category['title']}[/bold {color}]")
    for command in category["commands"]:
        console.print(f"   [bold yellow]{command['name']}[/bold yellow]: [italic white]{command['description']}[/italic white]")
    console.print(" ")

console.print("[code]CTRL + Z │ Esto detendrá cualquier comando o proceso existente.[/code]")
console.print(" ")
console.print(" ")