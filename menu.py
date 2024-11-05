from rich.console import Console
from rich.markdown import Markdown

console = Console()

MARKDOWN = """
# Comandos de Stellar
"""
md = Markdown(MARKDOWN)
console.print(md)

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
        {"name": "metadatainfo", "description": "Recupera los metadatos de una imagen, archivo o video."}
    ]}
]

for category in categories:
    console.print(f"  {category['title']}")
    for command in category["commands"]:
        console.print(f"   {command['name']}", ">", command["description"])

console.print()
console.print("CTRL + Z", " Esto detendrá cualquier comando o proceso existente.")
console.print()