import requests
from bs4 import BeautifulSoup
import subprocess
import socket
from rich.console import Console
from rich.table import Table
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

console = Console()

def obtener_datos_web(url):
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error de red: {e}[/bold red]")
        return None

def obtener_info_nmap(ip_address):
    try:
        nmap_output = subprocess.check_output(['nmap', '-p-', '--open', '-T4', '-oG', '-', ip_address], text=True)
        open_ports = [line.split()[1] for line in nmap_output.splitlines() if 'Ports:' in line]
        return ', '.join(open_ports) if open_ports else "No disponible"
    except subprocess.CalledProcessError:
        return "Error al ejecutar Nmap"

def analyze_url(url):
    response = obtener_datos_web(url)
    if not response:
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No disponible"
    meta_description = soup.find('meta', attrs={'name': 'description'})
    meta_keywords = soup.find('meta', attrs={'name': 'keywords'})

    domain = url.split("//")[-1].split('/')[0]
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        ip_address = "No disponible"

    server_info = response.headers.get('Server', 'No disponible')
    open_ports = obtener_info_nmap(ip_address) if ip_address != "No disponible" else "No disponible"

    table = Table(title="Información del sitio web", title_justify="center", title_style="bold magenta")
    table.add_column("Información", style="cyan")
    table.add_column("Valor", style="magenta")

    table.add_row("URL", url)
    table.add_row("Título", title)
    table.add_row("Descripción", meta_description['content'] if meta_description else "No disponible")
    table.add_row("Palabras clave", meta_keywords['content'] if meta_keywords else "No disponible")
    table.add_row("Dirección IP", ip_address)
    table.add_row("Servidor", server_info)
    table.add_row("Puertos abiertos", open_ports)

    console.print(table)

def main():
    url = console.input("[bold green]Ingrese la URL: [/bold green]")
    analyze_url(url)

if __name__ == "__main__":
    main()