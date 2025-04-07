from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.style import Style

console = Console(style="grey15 on grey23")

command_data = {
    "SISTEMA": {
        "color": "dodger_blue2",
        "commands": {
            "reload": "Recargar configuración de Stellar",
            "clear": "Limpiar pantalla de terminal",
            "bash": "Reiniciar sesión de terminal",
            "ui": "Personalizar interfaz y temas"
        }
    },
    "UTILIDADES": {
        "color": "sea_green3",
        "commands": {
            "ia": "Asistente de inteligencia artificial",
            "ia-image": "Generador de imágenes con IA",
            "traductor": "Traductor multidioma",
            "myip": "Analizador de dirección IP"
        }
    },
    "OSINT": {
        "color": "dark_orange3",
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
        "color": "medium_purple3",
        "commands": {
            "userinfo": "Obtención de datos de usuario"
        }
    }
}

console.print("\n")
console.print(" CENTRO DE COMANDOS STELLAR ".center(80), style="bold grey93 on grey23")
console.print(" v3.1.0 ".center(80), style="grey70 on grey23")
console.print("\n")

for category, data in command_data.items():
    console.print(f" {category} ", style=f"bold {data['color']} on grey23")
    
    for cmd, desc in data["commands"].items():
        console.print(f"  [bold grey93]{cmd.ljust(12)}[/] [grey78]{desc}[/]")
    
    console.print("\n")

console.print(" ATAJOS DE TECLADO ".center(80), style="bold grey93 on grey23")
console.print("\n")
console.print(f"  [bold grey93]{"CTRL + Z".ljust(12)}[/] [grey78]{"Detención segura de procesos"}[/]")
console.print(f"  [bold grey93]{"CTRL + C".ljust(12)}[/] [grey78]{"Terminación forzada de procesos"}[/]")
console.print("\n")
console.print(" Presione [bold grey93]TAB[/] para autocompletar • [bold grey93]↑↓[/] para navegar ".center(80), style="grey78 on grey23")
console.print("\n")