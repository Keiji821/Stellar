#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel
import subprocess
import signal
import sys
import time
import os
from pathlib import Path

console = Console()

def handler(signum, frame):
    console.print("\n[bold red]Deteniendo servicios...[/bold red]")
    subprocess.run(["pkill", "-f", "python main.py"], 
                   stderr=subprocess.DEVNULL,
                   timeout=5)
    subprocess.run(["pkill", "-f", "cloudflared tunnel run"],
                   stderr=subprocess.DEVNULL,
                   timeout=5)
    sys.exit(0)

def setup_environment():
    cloudflared_dir = Path.home() / ".cloudflared"
    cloudflared_dir.mkdir(exist_ok=True)
    
    cert_file = cloudflared_dir / "cert.pem"
    if not cert_file.exists():
        console.print("[bold yellow]Obteniendo certificado de Cloudflare...[/bold yellow]")
        try:
            subprocess.run(["cloudflared", "tunnel", "login"], 
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            console.print(Panel(
                "[bold red]ERROR: Autenticación requerida[/bold red]\n"
                "Por favor inicia sesión manualmente con:\n"
                "[bold cyan]cloudflared tunnel login[/bold cyan]\n"
                "y luego vuelve a ejecutar este script",
                title="Autenticación Necesaria",
                expand=False
            ))
            sys.exit(1)
    
    cred_file = cloudflared_dir / "kami-tunnel.json"
    if not cred_file.exists():
        console.print("[bold yellow]Creando túnel persistente...[/bold yellow]")
        try:
            subprocess.run(["cloudflared", "tunnel", "create", "kami-tunnel"], 
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            console.print(Panel(
                f"[bold red]ERROR creando túnel:[/bold red]\n{e.stderr.decode().strip()}",
                title="Error de Configuración",
                expand=False
            ))
            sys.exit(1)
    
    config_file = cloudflared_dir / "config.yml"
    config_content = f"""\
tunnel: kami-tunnel
credentials-file: {cred_file}
protocol: http2
metrics: 0
no-autoupdate: true
"""
    config_file.write_text(config_content)
    
    try:
        result = subprocess.run(["cloudflared", "--version"], 
                              check=True,
                              capture_output=True,
                              text=True)
        console.print(f"[dim]Cloudflared: {result.stdout.strip()}[/dim]")
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print(Panel(
            "[bold red]ERROR: Cloudflared no instalado[/bold red]\n"
            "Instala con: [bold]pkg install cloudflared[/bold]",
            title="Dependencia Faltante",
            expand=False
        ))
        sys.exit(1)
    
    try:
        import waitress, flask, rich
        console.print("[dim]Dependencias Python: OK[/dim]")
    except ImportError:
        console.print("[bold yellow]Instalando dependencias Python...[/bold yellow]")
        subprocess.run(["pip", "install", "waitress", "flask", "rich"], check=True)

def start_flask_app():
    try:
        console.print("[dim]Iniciando servidor Flask...[/dim]")
        return subprocess.Popen(
            ["python", "main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except Exception as e:
        console.print(f"[bold red]ERROR iniciando Flask:[/bold red] {str(e)}")
        sys.exit(1)

def run_cloudflared_tunnel(port):
    console.print(Panel(
        f"[green]Túnel activo en puerto {port}[/green]\n"
        "[yellow]Nota: La primera conexión puede tardar 1-2 minutos[/yellow]",
        title="Estado del Túnel",
        expand=False
    ))
    
    cmd = [
        "cloudflared", "tunnel",
        "--config", str(Path.home() / ".cloudflared" / "config.yml"),
        "run", "--url", f"http://localhost:{port}"
    ]
    
    with subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    ) as process:
        try:
            for line in process.stdout:
                if "Connection registered" in line:
                    console.print(f"[bold green]✓ Túnel activo:[/bold green] {line.split()[-1]}")
                console.print(f"[dim][cloudflared][/dim] {line.strip()}")
        except KeyboardInterrupt:
            handler(None, None)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    
    console.print(Panel(
        "[bold cyan]SERVIDOR KAMI CON CLOUDFLARE TUNNEL[/bold cyan]",
        expand=False
    ))
    
    try:
        with console.status("[bold green]Configurando entorno...[/bold green]"):
            setup_environment()
        
        flask_process = start_flask_app()
        time.sleep(3)
        
        puerto = console.input("\n[bold green]>> Puerto local (default 50000): [/bold green]") or "50000"
        
        run_cloudflared_tunnel(puerto)
    except Exception as e:
        console.print(f"[bold red]Error crítico:[/bold red] {str(e)}")
    finally:
        handler(None, None)