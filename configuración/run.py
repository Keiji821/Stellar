from rich.console import Console
from rich.table import Table
from rich.progress import Progress
import os
from os import system
import time

console = Console()

with Progress() as progress:

    task1 = progress.add_task("[red]...", total=1000)
    task2 = progress.add_task("[green]...", total=1000)
    task3 = progress.add_task("[cyan]...", total=1000)
    task4 = progress.add_task("[red]...", total=1000)
    task5 = progress.add_task("[green]...", total=1000)
    task6 = progress.add_task("[cyan]...", total=1000)
    task7 = progress.add_task("[red]...", total=1000)
    task8 = progress.add_task("[green]...", total=1000)
    task9 = progress.add_task("[cyan]...", total=1000)
    task10 = progress.add_task("[red]...", total=1000)
    task11 = progress.add_task("[green]...", total=1000)
    task12 = progress.add_task("[cyan]...", total=1000)
    task13 = progress.add_task("[red]...", total=1000)
    task14 = progress.add_task("[green]...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        os.system("clear")
        progress.update(task2, advance=0.9)
        os.system("pkill tor &>/dev/null &")
        progress.update(task3, advance=0.9)
        os.system("pkill cloudflared &>/dev/null &")
        progress.update(task4, advance=0.9)
        os.system("sleep 5")
        progress.update(task5, advance=0.9)
        os.system("export ALL_PROXY=socks5h://localhost:9050")
        progress.update(task6, advance=0.9)
        os.system("tor &>/dev/null &")
        progress.update(task7, advance=0.9)
        os.system("sleep 5")
        progress.update(task8, advance=0.9)
        os.system("cloudflared --url Stellar &>/dev/null &")
        progress.update(task9, advance=0.9)
        os.system("sleep 5")
        progress.update(task10, advance=0.9)
        os.system("cd")
        progress.update(task11, advance=0.9)
        os.system("cd Stellar")
        progress.update(task12, advance=0.9)
        os.system("bash update.sh &>/dev/null &")
        progress.update(task13, advance=0.9)
        os.system("git pull --force")
        progress.update(task14, advance=0.9)
        os.system("cp ~/Stellar/configuración/.bash_profile ~/.")
        time.sleep(0.02)