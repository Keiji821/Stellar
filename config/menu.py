from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.box import ROUNDED

console = Console()

console.print(
    Panel.fit(
        Text("STELLAR COMMAND CENTER", justify="center", style="bold #FF6B6B"),
        border_style="#4ECDC4",
        padding=(1, 4),
        style="on #292F36",
        subtitle="v3.1.0"
    )
)

command_data = {
    "🛠️ SISTEMA": {
        "color": "#4ECDC4",
        "commands": {
            "reload": "Recarga la configuración de Stellar",
            "clear": "Limpia la terminal completamente",
            "bash": "Reinicia la sesión terminal",
            "ui": "Personaliza interfaz y temas"
        }
    },
    "🔍 UTILIDADES": {
        "color": "#FFD166",
        "commands": {
            "ia": "Asistente de IA con API gratuita",
            "ia-image": "Generador de imágenes con IA",
            "traductor": "Traductor multidioma en tiempo real",
            "myip": "Analizador de dirección IP"
        }
    },
    "🕵️‍♂️ OSINT": {
        "color": "#06D6A0",
        "commands": {
            "ipinfo": "Analizador avanzado de IP",
            "phoneinfo": "Buscador de información telefónica",
            "urlinfo": "Escáner de URLs y dominios",
            "metadatainfo": "Extractor de metadatos",
            "emailsearch": "Buscador de correos electrónicos",
            "userfinder": "Rastreador de nombres de usuario"
        }
    },
    "🤖 DISCORD": {
        "color": "#EF476F",
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
        title_justify="left",
        expand=True
    )
    table.add_column("Comando", style="bold #F8F9FA", min_width=15)
    table.add_column("Descripción", style="#ADB5BD")
    
    for cmd, desc in data["commands"].items():
        table.add_row(
            f"[bold #FFD166]{cmd}[/]",
            f"[#F8F9FA]{desc}[/]"
        )
    
    console.print(table, justify="center")
    console.print()

hotkeys_panel = Panel.fit(
    Text("ATAJOS CLAVE", justify="center", style="bold #4ECDC4"),
    border_style="#FF6B6B",
    padding=(1, 4),
    style="on #292F36"
)
console.print(hotkeys_panel)

hotkeys_table = Table(
    box=ROUNDED,
    border_style="#4ECDC4",
    show_header=False,
    padding=(0, 2)
)
hotkeys_table.add_column("Key", style="bold #FFD166", justify="right")
hotkeys_table.add_column("Action", style="#F8F9FA", justify="left")
hotkeys_table.add_row("[bold]CTRL + Z[/]", "Detención segura de procesos")
hotkeys_table.add_row("[bold]CTRL + C[/]", "Terminación forzada de procesos")

console.print(hotkeys_table, justify="center")
console.print()

console.print(
    Panel.fit(
        Text("Presiona [bold #FFD166]TAB[/] para autocompletar • [bold #4ECDC4]↑↓[/] para navegar", 
            justify="center"),
        border_style="#4ECDC4",
        style="#F8F9FA"
    )
)