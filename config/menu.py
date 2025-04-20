from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from rich.text import Text
from rich.box import ROUNDED
import time

console = Console()

menu_data = {
    "SISTEMA": [
        ("reload", "Recarga el banner"),
        ("clear", "Limpia la pantalla"),
        ("bash", "Reinicia la sesión"),
        ("ui", "Personalizar temas e interfaz"),
        ("uninstall", "Desinstala todo el sistema"),
        ("update", "Actualiza desde GitHub")
    ],
    "UTILIDADES": [
        ("ia", "Asistente IA con API"),
        ("ia-image", "Generación de imágenes IA"),
        ("traductor", "Traducción en tiempo real"),
        ("myip", "Muestra tu IP e información")
    ],
    "OSINT": [
        ("ipinfo", "Análisis detallado de IP"),
        ("phoneinfo", "Info de números telefónicos"),
        ("urlinfo", "Escaneo de URLs y dominios"),
        ("metadatainfo", "Extracción de metadatos"),
        ("emailsearch", "Búsqueda de correos electrónicos"),
        ("userfinder", "Búsqueda de nombres de usuario")
    ],
    "DISCORD": [
        ("userinfo", "Info de ID de usuario"),
        ("serverinfo", "Info de servidores"),
        ("inviteinfo", "Info de enlaces")
    ],
    "PENTESTING": [
        ("ddos", "Ataque DDOS a URL objetivo")
    ]
}

def display_menu():
    try:
        while True:
            console.clear()
            
            banner = Panel(
                "[bold bright_cyan]STELLAR OS[/] [bright_black](v1.0.0)[/]",
                subtitle="[bright_black]by Keiji821[/]",
                border_style="bright_cyan",
                style="bold",
                box=ROUNDED
            )
            
            main_table = Table.grid(padding=(0, 2))
            main_table.add_column(style="bold cyan", width=20)
            main_table.add_column(style="bright_white")
            
            for category, commands in menu_data.items():
                main_table.add_row(
                    Panel.fit(
                        f"[bold bright_cyan]{category}[/]",
                        border_style="bright_cyan",
                        style="bold"
                    ),
                    ""
                )
                
                for cmd, desc in commands:
                    main_table.add_row(
                        f"[bold green]› {cmd}[/]",
                        f"[bright_white]{desc}[/]"
                    )
                main_table.add_row("", "")
            
            content = Panel.fit(
                main_table,
                border_style="bright_cyan",
                padding=(1, 4)
            )
            
            console.print(banner, justify="center")
            console.print(content, justify="center")
            
            help_panel = Panel.fit(
                "[bright_black]TAB:Autocompletado  ↑/↓:Navegar  ENTER:Ejecutar  CTRL+C:Salir[/]",
                border_style="yellow"
            )
            console.print(help_panel, justify="center")
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        console.print("\n[bold red]Saliendo del sistema...[/]")

if __name__ == "__main__":
    display_menu()