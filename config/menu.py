from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.style import Style

console = Console()

menu_data = {
    "SISTEMA": [
        ("reload", "Recargar configuración"),
        ("clear", "Limpiar terminal"),
        ("update", "Actualizar Stellar OS"),
        ("config", "Configuración avanzada")
    ],
    "HERRAMIENTAS": [
        ("net-scan", "Escaneo de red"),
        ("osint", "Investigación digital"),
        ("crypt", "Herramientas criptográficas"),
        ("forensic", "Análisis forense")
    ],
    "UTILIDADES": [
        ("vpn", "Gestión de conexiones VPN"),
        ("proxy", "Configuración de proxy"),
        ("tor", "Control de servicio Tor"),
        ("logs", "Visualización de registros")
    ]
}

def display_menu():
    console.print(
        Panel.fit(
            "[bold cyan]STELLAR OS[/] [bright_black](v1.0.0)[/]",
            subtitle="[bright_black]by Keiji821[/]",
            border_style="cyan",
            style="bold"
        )
    )
    
    table = Table.grid(padding=(0, 2))
    table.add_column(style="bold cyan", justify="left")
    table.add_column(style="bright_white", justify="left")
    
    for category, commands in menu_data.items():
        table.add_row(
            Panel.fit(
                f"[bold]{category}[/]",
                border_style="dim cyan",
                style="bold"
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
            "[bright_black]TAB: Autocompletado  ↑/↓: Navegación  CTRL+C: Salir[/]",
            border_style="dim cyan"
        )
    )

display_menu()