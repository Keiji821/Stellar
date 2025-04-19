from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.style import Style

console = Console()

menu_data = {
    "SISTEMA": [
        ("reload", "Recarga el banner"),
        ("clear", "Limpia la pantalla"),
        ("bash", "Reinicia la sesión"),
        ("ui", "Personalizar temas e interfaz"),
        ("uninstall", "Desinstala todo el sistema"),
        ("update", "Actualiza y busca actualizaciones en el repositorio de github.")
    ],
    "UTILIDADES": [
        ("ia", "Asistente IA con API integrada"),
        ("ia-image", "Generación de imágenes con IA"),
        ("traductor", "Traducción en tiempo real"),
        ("myip", "Muestra tu IP real y información completa")
    ],
    "OSINT": [
        ("ipinfo", "Análisis detallado de IP"),
        ("phoneinfo", "Obtiene información de números de teléfonos"),
        ("urlinfo", "Escaneo de URLs y dominios"),
        ("metadatainfo", "Extracción de metadatos"),
        ("emailsearch", "Búsqueda de correos electrónicos"),
        ("userfinder", "Busqueda de nombres de usuario")
    ],
    "OSINT - DISCORD": [
        ("userinfo", "Obtiene información sobre un ID"),
        ("serverinfo", "Obtiene información sobre un servidor"),
        ("searchinvites", "Obtiene enlaces de invitación por palabras claves de fuentes públicas"),
        ("inviteinfo", "Obtiene información sobre un enlace de invitación"),
    ],
    "PENTESTING": [
        ("ddos", "Realiza un ataque DDOS hacia una url")
    ],
    "ATAJOS": [
        ("CTRL+Z", "Detención segura de procesos"),
        ("CTRL+C", "Terminación forzada de procesos")
    ]
}

def display_menu():
    console.print(
        Panel.fit(
            "[bright_cyan]STELLAR OS[/] [bright_black](v1.0.0)[/]",
            subtitle="[bright_black]by Keiji821[/]",
            border_style="bright_cyan",
            style="bold"
        )
    )

    table = Table.grid(padding=(0, 2))
    table.add_column(style="bold cyan", justify="left", width=18)
    table.add_column(style="bright_white", justify="left")

    for category, commands in menu_data.items():
        table.add_row(
            Panel.fit(
                f"[bold]{category}[/]",
                border_style="dim cyan",
                style="bold",
                justify="center"
            )
        )
        for cmd, desc in commands:
            table.add_row(
                f"[bold green]• {cmd}[/]",
                f"[bright_white]{desc}[/]"
            )
        table.add_row("")

    console.print(table)

    console.print(
        Panel.fit(
            "[bright_black]TAB: Autocompletado  ↑/↓: Navegación  ENTER: Ejecutar[/]",
            border_style="dim yellow"
        )
    )

display_menu()