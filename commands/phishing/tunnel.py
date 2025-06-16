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

def setup_environment():
    os.environ['DNS_SERVER'] = '1.1.1.1'
    try:
        subprocess.run(["cloudflared", "--version"], 
                      check=True, 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)
    except:
        console.print("[bold yellow]Instalando cloudflared...[/bold yellow]")
        subprocess.run(["pkg", "install", "cloudflared", "-y"], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)
    try:
        import waitress, flask, rich
    except ImportError:
        console.print("[bold yellow]Instalando dependencias Python...[/bold yellow]")
        subprocess.run(["pip", "install", "waitress", "flask", "rich"], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)

console.print(Panel("[bold cyan]INICIANDO SERVIDOR KAMI[/bold cyan]", expand=False))
setup_environment()

try:
    with console.status("[bold green]Iniciando servicios...[/bold green]") as status:
        flask_proc = subprocess.Popen(
            ["python", "main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(3)

    puerto = console.input("\n[bold green]>> Ingresa puerto (ENTER para 50000): [/bold green]") or "50000"
    
    signal.signal(signal.SIGINT, handler)
    
    cloudflared_cmd = [
        "cloudflared", "tunnel",
        "--url", f"http://127.0.0.1:{puerto}",
        "--protocol", "http2",
        "--no-autoupdate",
        "--metrics", "localhost:0"
    ]
    
    subprocess.run(cloudflared_cmd)

except KeyboardInterrupt:
    handler(None, None)
except Exception as e:
    console.print(f"[bold red]Error: {str(e)}[/bold red]")
    sys.exit(1)