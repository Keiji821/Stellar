import requests
from bs4 import BeautifulSoup
import subprocess
import socket
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import re
import time
from urllib.parse import urlparse
from fake_useragent import UserAgent

console = Console()

def create_session():
    session = requests.Session()
    retry_policy = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retry_policy))
    session.mount('http://', HTTPAdapter(max_retries=retry_policy))
    return session

def fetch_website_data(url):
    session = create_session()
    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        
        response = session.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as error:
        console.print(f"[bold red]Error de red: {error}[/bold red]")
        return None

def get_nmap_info(ip_address):
    try:
        nmap_command = [
            'nmap', '-v', '-sV', '-sC', '-A', 
            '--script', 'http-headers,http-title,ssl-cert,http-enum,http-server-header,http-security-headers,http-methods,http-auth',
            '--version-intensity', '9', '--reason', '--open', '--script-timeout', '30s',
            ip_address
        ]
        
        nmap_result = subprocess.check_output(nmap_command, text=True, stderr=subprocess.STDOUT, timeout=300)

        open_ports = []
        service_info = []
        script_output = []
        host_details = {}
        service_details = {}

        lines = nmap_result.splitlines()
        current_service = None
        
        for line in lines:
            if '/tcp' in line and 'open' in line:
                open_ports.append(line.strip())
                if 'Service:' in line:
                    service_match = re.search(r'(\d+)/tcp\s+open\s+(\S+)\s+(.+)', line)
                    if service_match:
                        port = service_match.group(1)
                        service = service_match.group(2)
                        version = service_match.group(3)
                        service_details[port] = f"{service} - {version}"
            
            if 'Service Info:' in line:
                service_info.append(line.strip())
            
            if 'NSE:' in line or 'Nmap script:' in line or 'http-' in line.lower() or 'ssl-' in line.lower():
                if not any(x in line for x in ['NSE: Loaded', 'NSE: Script Pre-scanning', 'NSE: Script Post-scanning']):
                    script_output.append(line.strip())
            
            if 'Host is up' in line:
                host_details['host_status'] = line.strip()
            if 'Not shown:' in line:
                host_details['filtered_ports'] = line.strip()
            if 'Service detection performed' in line:
                service_info.append(line.strip())
            if 'PORT' in line and 'STATE' in line and 'SERVICE' in line:
                continue

        detailed_service_info = []
        for port, info in service_details.items():
            detailed_service_info.append(f"Puerto {port}: {info}")
        
        ports_info = '\n'.join(open_ports) if open_ports else "No se encontraron puertos abiertos"
        services_details = '\n'.join(detailed_service_info + service_info) if detailed_service_info or service_info else "No disponible"
        scripts_details = '\n'.join(script_output) if script_output else "No disponible"
        
        host_info = ""
        if host_details:
            host_info = '\n'.join([f"{k}: {v}" for k, v in host_details.items()])

        return ports_info, services_details, scripts_details, host_info
    except subprocess.CalledProcessError as e:
        console.print(f"[bold yellow]Advertencia: Nmap devolvió error, intentando con comando básico...[/bold yellow]")
        try:
            nmap_simple = ['nmap', '-v', '--open', ip_address]
            nmap_result_simple = subprocess.check_output(nmap_simple, text=True, stderr=subprocess.STDOUT, timeout=180)
            
            open_ports = []
            for line in nmap_result_simple.splitlines():
                if '/tcp' in line and 'open' in line:
                    open_ports.append(line.strip())
            
            ports_info = '\n'.join(open_ports) if open_ports else "No se encontraron puertos abiertos"
            return ports_info, "No disponible", "No disponible", "No disponible"
        except Exception as e2:
            return f"Error en Nmap: {e2}", "", "", ""
    except subprocess.TimeoutExpired:
        return "Escaneo Nmap excedió el tiempo límite", "", "", ""
    except Exception as e:
        return f"Error inesperado: {e}", "", "", ""

def analyze_url(url):
    if not re.match(r'^https?://', url):
        url = 'https://' + url

    with Progress(
        SpinnerColumn(spinner_name="dots"),
        TextColumn("[progress.description]{task.description}"),
        TimeElapsedColumn(),
        transient=True
    ) as progress:
        task = progress.add_task("[red]Conectando a la URL...", total=100)

        for _ in range(0, 30):
            progress.update(task, advance=1)
            time.sleep(0.05)

        response = fetch_website_data(url)
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
        meta_viewport = soup.find('meta', attrs={'name': 'viewport'})
        meta_robots = soup.find('meta', attrs={'name': 'robots'})
        meta_author = soup.find('meta', attrs={'name': 'author'})

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
        content_type = response.headers.get('Content-Type', 'No disponible')
        x_powered_by = response.headers.get('X-Powered-By', 'No disponible')
        x_frame_options = response.headers.get('X-Frame-Options', 'No disponible')
        x_content_type_options = response.headers.get('X-Content-Type-Options', 'No disponible')
        strict_transport_security = response.headers.get('Strict-Transport-Security', 'No disponible')
        
        if ip_address != "No disponible":
            open_ports, service_versions, script_info, host_info = get_nmap_info(ip_address)
        else:
            open_ports, service_versions, script_info, host_info = "No disponible", "", "", ""

    table = Table(title="Información del sitio web", title_justify="center", title_style="bold red")
    table.add_column("Información", style="green", no_wrap=False)
    table.add_column("Valor", style="bold white")

    table.add_row("URL", url)
    table.add_row("Título", title)
    table.add_row("Descripción", meta_description['content'] if meta_description else "No disponible")
    table.add_row("Palabras clave", meta_keywords['content'] if meta_keywords else "No disponible")
    table.add_row("Viewport", meta_viewport['content'] if meta_viewport else "No disponible")
    table.add_row("Robots", meta_robots['content'] if meta_robots else "No disponible")
    table.add_row("Autor", meta_author['content'] if meta_author else "No disponible")
    table.add_row("Dominio", domain)
    table.add_row("Dirección IP", ip_address)
    table.add_row("Servidor", server_info)
    table.add_row("Tipo de contenido", content_type)
    table.add_row("X-Powered-By", x_powered_by)
    table.add_row("X-Frame-Options", x_frame_options)
    table.add_row("X-Content-Type-Options", x_content_type_options)
    table.add_row("Strict-Transport-Security", strict_transport_security)
    table.add_row("Puertos abiertos", open_ports)
    table.add_row("Servicios y versiones", service_versions)
    table.add_row("Scripts de Nmap", script_info)
    table.add_row("Información del host", host_info)

    console.print(table)

    console.print("[bold green]Analizando enlaces...[/bold green]")
    links = soup.find_all('a', href=True)
    internal_links = set()
    external_links = set()
    
    for link in links:
        href = link['href']
        if href.startswith('/') or domain in href or not href.startswith(('http://', 'https://')):
            internal_links.add(href)
        else:
            external_links.add(href)
    
    console.print(f"[bold cyan]Enlaces internos encontrados ({len(internal_links)}):[/bold cyan]")
    for link in internal_links:
        console.print(f"- {link}")
    
    console.print(f"\n[bold cyan]Enlaces externos encontrados ({len(external_links)}):[/bold cyan]")
    for link in external_links:
        console.print(f"- {link}")

    console.print("\n[bold green]Analizando formularios...[/bold green]")
    forms = soup.find_all('form')
    console.print(f"[bold cyan]Formularios encontrados ({len(forms)}):[/bold cyan]")
    for form in forms:
        form_action = form.get('action', 'No especificado')
        form_method = form.get('method', 'GET')
        form_inputs = form.find_all('input')
        console.print(f"- Action: {form_action}, Method: {form_method}, Inputs: {len(form_inputs)}")
        
        for input_field in form_inputs:
            input_type = input_field.get('type', 'text')
            input_name = input_field.get('name', 'sin nombre')
            console.print(f"  - Input: type={input_type}, name={input_name}")

def main():
    target_url = console.input("[bold green]Ingrese la URL: [/bold green]")
    analyze_url(target_url)

if __name__ == "__main__":
    main()