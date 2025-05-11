from rich.console import Console
import os
from os import system
from rich.table import Table

console = Console()

os.path.expanduser("~/Stellar/config/themes")

with open("user.txt", encoding="utf-8") as f:
    user = f.read().strip()


table = Table(title="Lista", title_justify="center", title_style="bold green")
table.add_column(f"[bold green] Información", style="bold white", no_wrap=False)
table.add_column("[bold green]Descripción", style="bold white")

table.add_row("[code]General[/code]")
table.add_row("Usuario", user)
table.add_row("[code]Preferencias[/code]")

console.print(table, style="bright_cyan", justify="center")
console.print("")

