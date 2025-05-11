from rich.console import Console
import os
from os import system
from rich.table import Table

console = Console()

os.path.expanduser("~/Stellar/config/themes")

user = open("user.txt", encoding="utf-8") as f:
    return f.read().strip()

table = Table(title="Lista", title_justify="center", title_style="bold green")
table.add_column(f"[bold green] Información", style="bold white", no_wrap=False)
table.add_column("[bold green]Descripción", style="bold white")

table.add.row("Usuario", user)

console.print(table, style="bright_cyan", justify="center")
console.print("")

