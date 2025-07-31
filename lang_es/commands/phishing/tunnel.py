#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel
import subprocess
import signal
import sys
import time
import socket
import glob
import os
from pathlib import Path

console = Console()

def handler(signum, frame):
    console.print("\n[bold red]Deteniendo servicios...[/bold red]")
    subprocess.run(["pkill", "-f", "python main.py"], stderr=subprocess.DEVNULL, timeout=5)
    subprocess.run(["pkill", "-f", "cloudflared tunnel run"], stderr=subprocess.DEVNULL, timeout=5)
    sys.exit(0)

def install_cloudflared():
    try:
        subprocess.run(["pkg", "install", "cloudflared", "-y"], 
                      check=True, 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)
        return True
    except:
        console.print(Panel(
            "[bold red]ERROR: Instala Cloudflared manualmente[/bold red]\n"
            "Ejecuta: [bold white]pkg install cloudflared[/bold white]",
            title="Error Crítico",
            expand=False
        ))
        return False

def setup_cloudflared():
    cloudflared_dir = Path.home() / ".cloudflared"
    cloudflared_dir.mkdir(exist_ok=True)
    
    try:
        subprocess.run(["cloudflared", "--version"], 
                      check=True, 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)
    except:
        if not install_cloudflared():
            sys.exit(1)
    
    cert_file = cloudflared_dir / "cert.pem"
    if not cert_file.exists():
        console.print(Panel(
            "[bold yellow]AUTORIZACIÓN REQUERIDA[/bold yellow]\n"
            "[cyan]Sigue las instrucciones en tu navegador[/cyan]",
            title="Login Cloudflare",
            expand=False
        ))
        subprocess.run(["cloudflared", "tunnel", "login"], check=True)
    
    cred_file = cloudflared_dir / "kami-tunnel.json"
    if not cred_file.exists():
        console.print("[yellow]Creando túnel Kami...[/yellow]")
        try:
            result = subprocess.run(
                ["cloudflared", "tunnel", "create", "kami-tunnel"],
                capture_output=True,
                text=True,
                check=True
            )
            
            output = result.stdout
            if "Created tunnel" in output:
                for line in output.split('\n'):
                    if "Created tunnel" in line:
                        tunnel_id = line.split()[-1]
                        src_file = cloudflared_dir / f"{tunnel_id}.json"
                        if src_file.exists():
                            src_file.rename(cred_file)
                            break
        except subprocess.CalledProcessError:
            console.print(Panel(
                "[bold red]ERROR AL CREAR TÚNEL[/bold red]\n"
                "Ejecuta manualmente:\n"
                "[bold white]cloudflared tunnel create kami-tunnel[/bold white]\n"
                "Luego renombra el archivo .json resultante a:\n"
                f"[bold white]~/.cloudflared/kami-tunnel.json[/bold white]",
                title="Error de Configuración",
                expand=False
            ))
            sys.exit(1)
    
    config_file = cloudflared_dir / "config.yml"
    config_content = f"tunnel: kami-tunnel\ncredentials-file: {cred_file}\nprotocol: http2\nmetrics: 0\nno-autoupdate: true"
    config_file.write_text(config_content)

def install_python_deps():
    try:
        import waitress, flask, rich
    except ImportError:
        subprocess.run(["pip", "install", "waitress", "flask", "rich"], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)

def start_flask_app(port):
    return subprocess.Popen(
        ["python", "main.py", "--port", str(port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def get_free_port():
    s = socket.socket()
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

def run_cloudflared_tunnel(port):
    console.print(Panel(
        f"[bold green]TÚNEL ACTIVO EN PUERTO {port}[/bold green]",
        title="Estado",
        expand=False
    ))
    
    cmd = [
        "cloudflared", "tunnel",
        "--config", f"{Path.home()}/.cloudflared/config.yml",
        "run", "--url", f"http://localhost:{port}"
    ]
    
    with subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    ) as process:
        try:
            tunnel_url = None
            for line in process.stdout:
                if "https://" in line:
                    parts = line.split('https://')
                    if len(parts) > 1:
                        tunnel_url = "https://" + parts[1].strip()
                        console.print(Panel(
                            f"[bold cyan]URL DEL TÚNEL:[/bold cyan]\n[green]{tunnel_url}[/green]",
                            expand=False
                        ))
                console.print(f"[dim]{line.strip()}[/dim]")
        except KeyboardInterrupt:
            handler(None, None)

def main():
    signal.signal(signal.SIGINT, handler)
    console.print(Panel("[bold cyan]KAMI SERVER - CLOUDFLARE TUNNEL[/bold cyan]", expand=False))
    
    with console.status("[bold green]Configurando entorno...[/bold green]"):
        setup_cloudflared()
        install_python_deps()
    
    port = get_free_port()
    console.print(f"[yellow]Usando puerto automático: {port}[/yellow]")
    
    flask_process = start_flask_app(port)
    time.sleep(2)
    
    try:
        run_cloudflared_tunnel(port)
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")
    finally:
        handler(None, None)

if __name__ == "__main__":
    main()