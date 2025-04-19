from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich.style import Style
from rich.text import Text
import keyboard
import time
import os

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
        ("ia", "Asistente IA con API integrada"),
        ("ia-image", "Generación de imágenes con IA"),
        ("traductor", "Traducción en tiempo real"),
        ("myip", "Muestra tu IP real")
    ],
    "OSINT": [
        ("ipinfo", "Análisis detallado de IP"),
        ("phoneinfo", "Info de números telefónicos"),
        ("urlinfo", "Escaneo de URLs y dominios"),
        ("metadatainfo", "Extracción de metadatos"),
        ("emailsearch", "Búsqueda de correos electrónicos"),
        ("userfinder", "Búsqueda de nombres de usuario")
    ],
    "OSINT - DISCORD": [
        ("userinfo", "Obtiene información sobre un ID"),
        ("serverinfo", "Info sobre un servidor"),
        ("searchinvites", "Busca invitaciones públicas"),
        ("inviteinfo", "Analiza enlaces de invitación"),
    ],
    "PENTESTING": [
        ("ddos", "⚠️ Ataque DDOS (Ético solo para pruebas)")
    ],
    "ATAJOS": [
        ("CTRL+Z", "Detención segura de procesos"),
        ("CTRL+C", "Terminación forzada de procesos")
    ]
}

class StellarMenu:
    def __init__(self):
        self.selected_index = 0
        self.commands = []
        self.generate_commands_list()
        
    def generate_commands_list(self):
        """Convierte el menú en una lista plana para navegación"""
        self.commands = []
        for category in menu_data.values():
            for cmd, desc in category:
                self.commands.append((cmd, desc))
    
    def display_header(self):
        """Muestra el encabezado animado"""
        title = Text("STELLAR OS", style="bold #8A2BE2")
        title.stylize("blink", 0, 6)  # Efecto parpadeo en "STELLAR"
        
        header = Panel.fit(
            title + " [bright_black](v1.0.0)[/]",
            subtitle="[italic #9370DB]by Keiji821[/]",
            border_style="#9932CC",
            style="#4B0082"
        )
        return header
    
    def display_menu(self):
        """Renderiza el menú interactivo"""
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3)
        )
        
        # Header
        layout["header"].update(self.display_header())
        
        # Cuerpo principal
        grid = Table.grid(padding=(0, 2), expand=True)
        grid.add_column(style="bold #9370DB", width=18)
        grid.add_column(style="#E6E6FA")
        
        for category, items in menu_data.items():
            # Panel de categoría con borde degradado
            category_panel = Panel.fit(
                f"[bold #DA70D6]{category}[/]",
                border_style="#9932CC",
                style="#4B0082"
            )
            grid.add_row(category_panel, "")
            
            for i, (cmd, desc) in enumerate(items):
                # Resaltar el comando seleccionado
                if self.selected_index == self.commands.index((cmd, desc)):
                    cmd_style = "bold reverse #FF00FF"
                    desc_style = "bold #FF1493"
                else:
                    cmd_style = "bold #BA55D3"
                    desc_style = "#D8BFD8"
                
                grid.add_row(
                    f"[{cmd_style}]• {cmd}[/]",
                    f"[{desc_style}]{desc}[/]"
                )
            grid.add_row("", "")
        
        layout["main"].update(grid)
        
        # Footer interactivo
        footer_text = Text()
        footer_text.append(" TAB: Autocompletado ", style="on #483D8B")
        footer_text.append(" ↑/↓: Navegación ", style="on #6A5ACD")
        footer_text.append(" ENTER: Ejecutar ", style="on #9370DB")
        footer_text.append(" ESC: Salir ", style="on #8A2BE2")
        
        layout["footer"].update(
            Panel.fit(
                footer_text,
                border_style="#4B0082"
            )
        )
        
        return layout
    
    def run(self):
        """Bucle principal interactivo"""
        with Live(self.display_menu(), refresh_per_second=10, screen=True) as live:
            while True:
                time.sleep(0.1)
                
                if keyboard.is_pressed('up'):
                    self.selected_index = max(0, self.selected_index - 1)
                    live.update(self.display_menu())
                elif keyboard.is_pressed('down'):
                    self.selected_index = min(len(self.commands)-1, self.selected_index + 1)
                    live.update(self.display_menu())
                elif keyboard.is_pressed('enter'):
                    selected_cmd = self.commands[self.selected_index][0]
                    self.execute_command(selected_cmd)
                elif keyboard.is_pressed('esc'):
                    console.print("[bold purple]Saliendo de Stellar OS...[/]")
                    break
    
    def execute_command(self, command):
        """Ejecuta el comando seleccionado"""
        console.clear()
        
        if command == "clear":
            console.clear()
        elif command == "reload":
            console.print("[bold green]Recargando interfaz...[/]")
            time.sleep(1)
        elif command == "ddos":
            console.print("[bold red]⚠️ ADVERTENCIA: El uso de DDoS es ilegal sin autorización[/]")
            console.print("[yellow]Este sistema solo para pruebas éticas con permiso[/]")
        else:
            console.print(f"[bold purple]Ejecutando: {command}[/]")
            time.sleep(1)
        
        self.display_menu()

if __name__ == "__main__":
    try:
        os.system('')  # Habilita secuencias ANSI en Windows
        menu = StellarMenu()
        menu.run()
    except KeyboardInterrupt:
        console.print("\n[bold purple]Sesión terminada[/]")