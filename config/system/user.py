from rich.console import Console
import os
from os import system
from rich.table import Table

console = Console()

with open("user.txt", encoding="utf-8") as f:
    user = f.read().strip()

os.path.expanduser("~")
os.chdir("Stellar/config/themes")

with open("banner_color.txt", encoding="utf-8") as f:
    banner_color = f.read().strip()

with open("banner_background.txt", encoding="utf-8") as f:
    banner_background = f.read().strip()

with open("banner_background_color.txt", encoding="utf-8") as f:
    banner_background_color = f.read().strip()


table = Table(title="Perfil", title_justify="center", title_style="bold green")
table.add_column(f"[bold green] Información", style="bold white", no_wrap=False)
table.add_column("[bold green]Descripción", style="bold white")

table.add_row("[code]General[/code]")
table.add_row("Usuario", user)
table.add_row("[code]Preferencias[/code]")
table.add_row("Color del banner", banner_color)
table.add_row("Fondo del banner", banner_background)
table.add_row("Color del fondo del banner", banner_background_color)

console.print(table, style="bright_cyan", justify="center")
console.print("")

