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
        ("emailsearch", "Búsqueda de correos")
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

def create_main_panel(content):
    return Panel(
        content,
        title="[blink]╭─[/][bright_cyan] STELLAR TERMINAL [/][blink]─╮[/]",
        subtitle="[bright_black]by Keiji821[/]",
        border_style="bright_cyan",
        style=Style(bold=True),
        box=ROUNDED,
        width=80
    )

def display_menu():
    while True:
        try:
            console.clear()
            
            main_table = Table.grid(padding=(0, 2), expand=True)
            main_table.add_column(style="bold cyan", width=20)
            main_table.add_column(style="bright_white")
            
            for category, commands in menu_data.items():
                category_panel = Panel.fit(
                    f"[bold bright_cyan]{category}[/]",
                    border_style=Style(color="cyan", blink=True),
                    style="bold"
                )
                main_table.add_row(category_panel, "")
                
                for cmd, desc in commands:
                    main_table.add_row(
                        f"[bold green]› {cmd}[/]",
                        f"[bright_white]{desc}[/]"
                    )
                main_table.add_row("", "")
            
            content = Panel.fit(
                main_table,
                border_style=Style(color="cyan", blink=True),
                padding=(1, 4)
            )
            
            console.print(
                create_main_panel(content),
                justify="center"
            )
            
            console.print(
                Panel.fit(
                    "[bright_black]TAB: Autocompletado  ↑/↓: Navegar  ENTER: Ejecutar  CTRL+C: Salir[/]",
                    border_style=Style(color="yellow", blink=True)
                ),
                justify="center"
            )
            
            time.sleep(0.5)
            
        except KeyboardInterrupt:
            console.print("\n[bold red]Saliendo del sistema...[/]")
            break

if __name__ == "__main__":
    display_menu()