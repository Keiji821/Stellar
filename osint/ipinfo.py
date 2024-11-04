import requests
import subprocess
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

console = Console()

def obtener_datos_ip(ip):
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)

    urls = [f'https://ipapi.co/{ip}/json/', f'https://api.ipapi.is/?ip={ip}']
    datos = []

    for url in urls:
        try:
            response = session.get(url, timeout=5)
            response.raise_for_status()
            datos.append(response.json())
        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Error de red: {e}[/bold red]")
            return None

    return datos

def escanear_puertos(opcion, ip_o_rango):
    comandos = {
        1: ["nmap", "-v", "-A", ip_o_rango],
        2: ["nmap", "-v", "-sn", ip_o_rango],
        3: ["nmap", "-v", "-iR", "10000", "-Pn", "-p", "80"]
    }

    with Progress(SpinnerColumn(), TextColumn("[bold green]Escaneando puertos...[/bold green]")) as progress:
        task = progress.add_task("", start=False)
        progress.start_task(task)
        try:
            resultado = subprocess.check_output(comandos[opcion], text=True)
            progress.stop()
            return resultado
        except subprocess.CalledProcessError as e:
            progress.stop()
            console.print(f"[bold red]Error al ejecutar nmap: {e}[/bold red]")
            return "No disponible"

def agregar_filas(table, datos, section_title, campos):
    table.add_row(f"[bold underline]{section_title}[/bold underline]", "")
    for titulo, key, source in campos:
        valor = str(datos[source].get(key, "No disponible"))
        if valor != "No disponible":
            table.add_row(titulo, valor)

def main():
    ip = console.input("[bold green]Ingrese la IP: [/bold green]")
    datos = obtener_datos_ip(ip)
    
    if not datos:
        console.print("[bold red]No se pudo obtener la información de la IP.[/bold red]")
        return

    console.print("[bold blue]Selecciona el tipo de escaneo Nmap:[/bold blue]")
    console.print("1: Escaneo detallado (-A)")
    console.print("2: Escaneo de red (-sn)")
    console.print("3: Escaneo aleatorio de puertos (-iR)")
    opcion = int(console.input("[bold green]Opción (1, 2 o 3): [/bold green]"))

    if opcion not in (1, 2, 3):
        console.print("[bold red]Opción no válida.[/bold red]")
        return

    ip_o_rango = ip if opcion in (1, 2) else ""

    data1, data2 = datos
    table = Table(title="Información de la IP", title_justify="center", title_style="bold magenta")
    table.add_column("Información de Red y Geográfica", style="cyan", no_wrap=True)
    table.add_column("Valor", style="magenta")

    campos_red = [
        ("Red", "network", 0),
        ("Tipo de IP", "version", 0),
        ("TLD", "country_tld", 0),
        ("ASN", "asn", 0),
        ("Empresa", "org", 0),
        ("RIR", "rir", 1),
        ("Es una IP no autorizada", "is_bogon", 1),
        ("Es un móvil", "is_mobile", 1),
        ("Es un rastreador", "is_crawler", 1),
        ("Es un centro de datos", "is_datacenter", 1),
        ("Es una red Tor", "is_tor", 1),
        ("Es un proxy", "is_proxy", 1),
        ("Es una VPN", "is_vpn", 1),
        ("Es una IP sospechosa", "is_abuser", 1),
        ("Nivel de fraude", "abuser_score", 1),
        ("Es una IP activa", "active", 1),
        ("Dominio", "domain", 1),
        ("Fecha de creación", "created", 1),
        ("Correo de abuso", "email", 1),
    ]

    campos_geo = [
        ("País", "country", 0),
        ("Capital", "country_capital", 0),
        ("Ciudad", "city", 0),
        ("Región", "region", 0),
        ("Código de región", "region_code", 0),
        ("Nombre de país", "country_name", 0),
        ("Código de país", "country_code", 0),
        ("ISO3", "country_code_iso3", 0),
        ("Código de continente", "continent_code", 0),
        ("En Europa", "in_eu", 0),
        ("Código postal", "postal", 0),
        ("Latitud", "latitude", 0),
        ("Longitud", "longitude", 0),
        ("Zona horaria", "timezone", 0),
        ("UTC Offset", "utc_offset", 0),
        ("Código de llamada", "country_calling_code", 0),
        ("Moneda", "currency", 0),
        ("Nombre de moneda", "currency_name", 0),
        ("Idioma", "languages", 0),
        ("Área del país", "country_area", 0),
        ("Población del país", "country_population", 0),
    ]

    agregar_filas(table, datos, "Información de Red", campos_red)
    table.add_row("", "")
    agregar_filas(table, datos, "Información Geográfica", campos_geo)

    resultado_nmap = escanear_puertos(opcion, ip_o_rango)

    if resultado_nmap != "No disponible":
        table.add_row("[bold underline]Escaneo de Puertos[/bold underline]", "")
        for line in resultado_nmap.splitlines():
            if "open" in line or "filtered" in line or "closed" in line:
                parts = line.split()
                puerto_info = " ".join(parts[0:2])
                descripcion = " ".join(parts[2:])
                table.add_row(puerto_info, descripcion)

    console.print(table)

if __name__ == "__main__":
    main()