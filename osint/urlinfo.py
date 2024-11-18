import requests
from bs4 import BeautifulSoup
import subprocess
import socket
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, SpinnerColumn, TextColumn, TimeElapsedColumn
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import re
import time
from urllib.parse import urlparse

console = Console()

def crear_sesion():
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    session.mount('http://', HTTPAdapter(max_retries=retries))
    return session

def obtener_datos_web(url):
    session = crear_sesion()
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error de red: {e}[/bold red]")
        return None

def obtener_info_nmap(ip_address):
    try:
        nmap_output = subprocess.check_output(['nmap', '-v', '-A', ip_address], text=True)

        open_ports = []
        os_info = "No disponible"
        service_versions = "No disponible"

        for line in nmap_output.splitlines():
            if re.search(r'\bopen\b', line):
                open_ports.append(line.strip())

            if "OS details" in line:
                os_info = line.split(":")[1].strip()

            if "Service Info" in line:
                service_versions = line.split(":")[1].strip()

        open_ports = '\n'.join(open_ports) if open_ports else "No disponible"
        return open_ports, os_info, service_versions
    except subprocess.CalledProcessError:
        return "Error al ejecutar Nmap", "", ""

def analyze_url(url):
    if not re.match(r'^https?://', url):
        url = 'https://' + url

    with Progress(
        SpinnerColumn(spinner_name="dots"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(complete_style="green", finished_style="green", pulse_style="bright_yellow"),
        TimeElapsedColumn(),
        transient=True
    ) as progress:
        task = progress.add_task("[red]Conectando a la URL...", total=100)

        for _ in range(0, 30):
            progress.update(task, advance=1)
            time.sleep(0.05)

        response = obtener_datos_web(url)
        if not response:
            return

        progress.update(task, description="[yellow]Analizando HTML...", completed=30)
        for _ in range(30, 60):
            progress.update(task, advance=1)
            time.sleep(0.05)

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No disponible"
        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})

        domain = urlparse(url).netloc
        try:
            ip_address = socket.gethostbyname(domain)
        except socket.gaierror:
            ip_address = "No disponible"

        progress.update(task, description="[blue]Ejecutando Nmap...", completed=60)
        for _ in range(60, 100):
            progress.update(task, advance=1)
            time.sleep(0.05)

        server_info = response.headers.get('Server', 'No disponible')
        open_ports, os_info, service_versions = obtener_info_nmap(ip_address) if ip_address != "No disponible" else ("No disponible", "", "")

    table = Table(title="Información del sitio web", title_justify="center", title_style="bold red")
    table.add_column("Información", style="bold green")
    table.add_column("Valor", style="bold white")

    table.add_row("URL", url)
    table.add_row("Título", title)
    table.add_row("Descripción", meta_description['content'] if meta_description else "No disponible")
    table.add_row("Palabras clave", meta_keywords['content'] if meta_keywords else "No disponible")
    table.add_row("Dirección IP", ip_address)
    table.add_row("Servidor", server_info)
    table.add_row("Puertos abiertos", open_ports)
    table.add_row("Sistema operativo", os_info if os_info else "No disponible")
    table.add_row("Servicios y versiones", service_versions if service_versions else "No disponible")

    console.print(table)

    console.print("[bold green]Verificando enlaces internos...[/bold green]")
    links = soup.find_all('a', href=True)
    internal_links = set()
    for link in links:
        href = link['href']
        if href.startswith('/') or domain in href:
            internal_links.add(href)
    console.print(f"[bold cyan]Enlaces internos encontrados:[/bold cyan] {len(internal_links)}")
    for link in internal_links:
        console.print(f"- {link}")

def main():
    url = console.input("[bold green]Ingrese la URL: [/bold green]")
    analyze_url(url)

if __name__ == "__main__":
    main()