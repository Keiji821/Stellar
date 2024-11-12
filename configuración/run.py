from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
import os
import time

console = Console()

commands = [
    "pkill tor &>logs.txt",
    "pkill cloudflared &>logs.txt",
    "export ALL_PROXY=socks5h://localhost:9050",
    "tor &>logs.txt &",
    "sleep 1",
    "cloudflared --url Stellar &>logs.txt &",
    "cd && cd Stellar && bash update.sh &>logs.txt",
    "git pull --force",
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
    
    task = progress.add_task("[cyan]Ejecución de comandos...", total=len(commands))

    for command in commands:
        progress.update(task, description=f"[cyan]Ejecutando: {command}", advance=1)
        os.system(command)
        time.sleep(0.5)