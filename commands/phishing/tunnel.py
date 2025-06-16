#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel
import subprocess
import signal
import sys
import time
import os

console = Console()

def handler(signum, frame):
    console.print("\n[bold red]Deteniendo servicios...[/bold red]")
    subprocess.run(["pkill", "-f", "python main.py"], stderr=subprocess.DEVNULL)
    subprocess.run(["pkill", "-f", "cloudflared"], stderr=subprocess.DEVNULL)
    sys.exit(0)

console.print(Panel("[bold cyan]INICIANDO SERVIDOR KAMI[/bold cyan]", expand=False))
os.environ['DNS_SERVER'] = '1.1.1.1'

try:
    with console.status("[bold green]Iniciando servicios...[/bold green]") as status:
        subprocess.Popen(["python", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(3)
        
    console.print(Panel.fit(
        "[bold yellow]DATOS DEL SERVIDOR[/bold yellow]\n"
        "Puerto predeterminado: [bold]50000[/bold]\n"
        "Protocolo: [bold]HTTP/2[/bold]",
        title="Información"
    ))

    puerto = console.input("\n[bold green]>> Ingresa puerto (ENTER para 50000): [/bold green]") or "50000"
    console.print(f"\n[bold yellow]URL pública:[/bold yellow] https://kami-{puerto}.trycloudflare.com")

    signal.signal(signal.SIGINT, handler)
    subprocess.run([
        "cloudflared", "tunnel",
        "--url", f"http://127.0.0.1:{puerto}",
        "--protocol", "http2"
    ])

except KeyboardInterrupt:
    handler(None, None)
except Exception as e:
    console.print(f"[bold red]Error:[/bold red] {str(e)}")
    sys.exit(1)