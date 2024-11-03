import requests
from bs4 import BeautifulSoup
import subprocess
import socket
from rich.console import Console
from rich.table import Table

console = Console()

def analyze_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No disponible"
        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})

        domain = url.split("//")[-1].split('/')[0]
        ip_address = socket.gethostbyname(domain)

        server_info = response.headers.get('Server', 'No disponible')

        try:
            nmap_output = subprocess.check_output(['nmap', '-p-', '--open', '-T4', '-oG', '-', ip_address], text=True)
            open_ports = [line.split()[1] for line in nmap_output.splitlines() if 'Ports:' in line]
        except subprocess.CalledProcessError:
            open_ports = ["Error al ejecutar Nmap"]

        table = Table(title="Información del sitio web", title_justify="center", title_style="bold magenta")
        table.add_column("Información", style="cyan", no_wrap=False)
        table.add_column("Valor", style="magenta", no_wrap=False)

        table.add_row("URL", url)
        table.add_row("Título", title)
        table.add_row("Descripción", meta_description['content'] if meta_description else 'No disponible')
        table.add_row("Palabras clave", meta_keywords['content'] if meta_keywords else 'No disponible')
        table.add_row("Puertos abiertos", ', '.join(open_ports) if open_ports else 'No disponible')
        table.add_row("Dirección IP", ip_address)
        table.add_row("Servidor", server_info)

        console.print(table)

    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

def main():
    url = console.input("[bold green]Ingrese la URL: [/bold green]")
    analyze_url(url)

if __name__ == "__main__":
    main()