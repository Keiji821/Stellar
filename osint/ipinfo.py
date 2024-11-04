import requests
import subprocess
from rich.console import Console
from rich.table import Table
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

console = Console()

def obtener_datos_ip(ip):
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)

    urls = [f'https://ipapi.co/{ip}/json/', f'https://api.ipapi.is/?ip={ip}']
    datos = [session.get(url, timeout=5).json() for url in urls]
    return datos

def escanear_puertos(ip):
    resultado = subprocess.run(['nmap', '-p-', ip], capture_output=True, text=True)
    return resultado.stdout

def crear_tabla(datos, ip):
    data1, data2 = datos
    table = Table(title="Información de la IP", title_justify="center", title_style="bold magenta")
    table.add_column("Información de Red y Geográfica", style="cyan", no_wrap=True)
    table.add_column("Valor", style="magenta")

    campos_red = [
        ("Red", "network", 0), ("Tipo de IP", "version", 0), ("TLD", "country_tld", 0), ("ASN", "asn", 0),
        ("Empresa", "org", 0), ("RIR", "rir", 1), ("Es una IP no autorizada", "is_bogon", 1),
        ("Es un móvil", "is_mobile", 1), ("Es un rastreador", "is_crawler", 1), ("Es un centro de datos", "is_datacenter", 1),
        ("Es una red Tor", "is_tor", 1), ("Es un proxy", "is_proxy", 1), ("Es una VPN", "is_vpn", 1),
        ("Es una IP sospechosa", "is_abuser", 1), ("Nivel de fraude", "abuser_score", 1),
        ("Es una IP activa", "active", 1), ("Dominio", "domain", 1), ("Fecha de creación", "created", 1),
        ("Correo de abuso", "email", 1)
    ]

    campos_geo = [
        ("País", "country", 0), ("Capital", "country_capital", 0), ("Ciudad", "city", 0), ("Región", "region", 0),
        ("Código de región", "region_code", 0), ("Nombre de país", "country_name", 0),
        ("Código de país", "country_code", 0), ("ISO3", "country_code_iso3", 0), ("Código de continente", "continent_code", 0),
        ("En Europa", "in_eu", 0), ("Código postal", "postal", 0), ("Latitud", "latitude", 0),
        ("Longitud", "longitude", 0), ("Zona horaria", "timezone", 0), ("UTC Offset", "utc_offset", 0),
        ("Código de llamada", "country_calling_code", 0), ("Moneda", "currency", 0),
        ("Nombre de moneda", "currency_name", 0), ("Idioma", "languages", 0), ("Área del país", "country_area", 0),
        ("Población del país", "country_population", 0)
    ]

    table.add_row("[bold underline]Información de Red[/bold underline]", "")
    for titulo, key, source in campos_red:
        valor = str(datos[source].get(key, "No disponible"))
        if valor != "No disponible":
            table.add_row(titulo, valor)
    table.add_row("", "")
    table.add_row("[bold underline]Información Geográfica[/bold underline]", "")
    for titulo, key, source in campos_geo:
        valor = str(datos[source].get(key, "No disponible"))
        if valor != "No disponible":
            table.add_row(titulo, valor)
    
    console.print(table)

    console.print("[bold underline]Escaneo de Puertos[/bold underline]", "")
    console.print(escanear_puertos(ip))

def main():
    ip = console.input("[bold green]Ingrese la IP: [/bold green]")
    datos = obtener_datos_ip(ip)
    crear_tabla(datos, ip)

if __name__ == "__main__":
    main()