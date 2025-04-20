from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from rich.text import Text
from rich.box import ROUNDED

console = Console()

menu_data = {
    "SISTEMA": [
        ("reload", "Recarga el banner"),
        ("clear", "Limpia la pantalla"),
        ("bash", "Reinicia la sesión"),
        ("ui", "Personalizar temas e interfaz"),
        ("uninstall", "Desinstala todo el sistema"),
        ("update", "Actualiza desde el repositorio de GitHub")
    ],
    "UTILIDADES": [
        ("ia", "Asistente IA con API integrada"),
        ("ia-image", "Generación de imágenes con IA"),
        ("traductor", "Traducción en tiempo real"),
        ("myip", "Muestra tu IP real y información")
    ],
    "OSINT": [
        ("ipinfo", "Análisis detallado de IP"),
        ("phoneinfo", "Información de números telefónicos"),
        ("urlinfo", "Escaneo de URLs y dominios"),
        ("metadatainfo", "Extracción de metadatos"),
        ("emailsearch", "Búsqueda de correos electrónicos"),
        ("userfinder", "Búsqueda de nombres de usuario")
    ],
    "OSINT - DISCORD": [
        ("userinfo", "Información sobre un ID de usuario"),
        ("serverinfo", "Información sobre un servidor"),
        ("searchinvites", "Busca invitaciones por palabras clave"),
        ("inviteinfo", "Información sobre enlaces de invitación")
    ],
    "PENTESTING": [
        ("ddos", "Ataque DDOS hacia una URL objetivo")
    ],
    "ATAJOS": [
        ("CTRL+Z", "Detención segura de procesos"),
        ("CTRL+C", "Terminación forzada de procesos")
    ]
}

def display_menu():
    banner = Panel.fit(
        Text.from_markup(
            "[bold bright_cyan]╭───────────────────────────────────────╮\n"
            "│    [blink]STELLAR OS[/blink] [bright_black](v1.0.0)[/bright_black]    │\n"
            "╰───────────────────────────────────────╯[/bold bright_cyan]",
            justify="center"
        ),
        subtitle="[bright_black]by Keiji821[/]",
        border_style="bright_cyan",
        style=Style(bold=True, bgcolor="black"),
        box=ROUNDED
    )
    
    console.print(banner, justify="center")
    
    main_table = Table.grid(padding=(0, 2), expand=True)
    main_table.add_column(style="bold cyan", justify="left", width=20)
    main_table.add_column(style="bright_white", justify="left", ratio=1)
    
    for category, commands in menu_data.items():
        category_panel = Panel.fit(
            f"[bold bright_cyan]{category}[/]",
            border_style="dim cyan",
            style=Style(bold=True, bgcolor="black"),
            box=ROUNDED
        )
        main_table.add_row(category_panel, "")
        
        for cmd, desc in commands:
            main_table.add_row(
                f"[bold green]  › {cmd}[/]",
                f"[bright_white]{desc}[/]"
            )
        main_table.add_row("", "")
    
    console.print(main_table)
    
    shortcuts = Panel.fit(
        "[bright_black]TAB: Autocompletado  ↑/↓: Navegación  ENTER: Ejecutar  ESC: Salir[/]",
        border_style="dim yellow",
        style=Style(bold=True, bgcolor="black"),
        box=ROUNDED
    )
    console.print(shortcuts, justify="center")

if __name__ == "__main__":
    display_menu()