from rich.console import Console
import os
from os import system
from rich.table import Table

console = Console()



table = Table(title="Lista", title_justify="center", title_style="bold green")
table.add_column(f"[bold green] Información", style="bold white", no_wrap=False)
table.add_column("[bold green]Descripción", style="bold white")


console.print(table, style="bright_cyan", justify="center")
console.print("")

