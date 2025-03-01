import requests
from rich.console import Console
from rich.table import Table

console = Console()

API_KEY = "Kastg_fKlIk2c1LRc8969in2g9_free"

https://api.kastg.xyz/api/tool/translate?input=Hello%20World!%20This%20is%20the%20output%20in%20french&to=fr&from=auto

table = Table(title="Traductor", title_justify="center", title_style="bold magenta")
table.add_column("", style="bold white", no_wrap=False)

table.add_row("")

console.print(table)
