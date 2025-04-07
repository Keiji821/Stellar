from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.box import ROUNDED
from rich.style import Style

console = Console()

console.print(
    Panel.fit(
        Text("Comandos de Stellar", justify="center", style="bold #4682B4"),
        border_style="dim white",
        padding=(1, 4),
        style="on black",
        subtitle="v3.1.0"
    )
)

command_data = {
    "SISTEMA": {
        "color": "#4682B4",
        "commands": {
            "reload": "Recargar configuración de Stellar",
            "clear": "Limpiar pantalla de terminal",
            "bash": "Reiniciar sesión de terminal", 
            "ui": "Personalizar interfaz y temas"
        }
    },
    "UTILIDADES": {
        "color": "#5F9EA0",
        "commands": {
            "ia": "Asistente de inteligencia artificial",
            "ia-image": "Generador de imágenes con IA",
            "traductor": "Traductor multidioma",
            "myip": "Analizador de dirección IP"
        }
    },
    "OSINT": {
        "color": "#DAA520",
        "commands": {
            "ipinfo": "Analizador avanzado de IP",
            "phoneinfo": "Buscador de información telefónica",
            "urlinfo": "Escáner de URLs y dominios",
            "metadatainfo": "Extractor de metadatos",
            "emailsearch": "Buscador de correos electrónicos",
            "userfinder": "Rastreador de nombres de usuario"
        }
    },
    "DISCORD": {
        "color": "#9370DB",
        "commands": {
            "userinfo": "Obtención de datos de usuario"
        }
    }
}

for category, data in command_data.items():
    table = Table(
        title=f"[bold {data['color']}]{category}[/]",
        border_style=data["color"],
        box=ROUNDED,
        header_style=f"bold {data['color']}",
        padding=(0, 2),
        expand=True
    )
    table.add_column("Comando", style="bold bright_white", width=18)
    table.add_column("Descripción", style="bright_black")
    
    for cmd, desc in data["commands"].items():
        table.add_row(
            f"[bold #FFD700]{cmd}[/]",
            f"[bright_white]{desc}[/]"
        )
    
    console.print(table)
    console.print()

hotkeys_table = Table(
    title="[bold #4682B4]ATAJOS DE TECLADO[/]",
    box=ROUNDED,
    border_style="bright_white",
    padding=(0, 2),
    width=60
)
hotkeys_table.add_column("Combinación", style="bold bright_white", width=15)
hotkeys_table.add_column("Acción", style="bright_black")
hotkeys_table.add_row("[bold #FFD700]CTRL + Z[/]", "Detención segura de procesos")
hotkeys_table.add_row("[bold #FFD700]CTRL + C[/]", "Terminación forzada de procesos")

console.print(hotkeys_table)
console.print()

console.print(
    Panel.fit(
        Text("Presione [bold #FFD700]TAB[/] para autocompletar • [bold #4682B4]↑↓[/] para navegar", 
            justify="center"),
        border_style="dim white",
        style="on black"
    )
)