from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
import os
import time

console = Console()

commands = [
    "cd && pkill tor &",
    "cd && pkill cloudflared &",
    "cd && export ALL_PROXY=socks5h://localhost:9050",
    "cd && tor &",
    "sleep 10",
    "cd && cloudflared --url Stellar &",
    "sleep 10",
    "bash Stellar/update.sh &>/dev/null &",
    "cd Stellar && git pull --force &>/dev/null &",
    "cp ~/Stellar/configuración/.bash_profile ~/."
]

with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(bar_width=None, style="green"),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    console=console,
    refresh_per_second=10,
) as progress:
    
    task = progress.add_task("[bold green]Ejecución de comandos...[/bold green]", total=len(commands))

    for command in commands:
        progress.update(task, description=f"[code][bold yellow]Ejecutando:[/bold yellow][/code] [underline]{command}[/underline]", advance=1)
        os.system(command)
        time.sleep(0.5)