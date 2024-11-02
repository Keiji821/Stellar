import requests
from rich.console import Console
from rich.table import Table

console = Console()

IpQuery = console.input("[bold green]Ingrese la IP: [/bold green]")

try:
    response1 = requests.get(f'https://ipapi.co/{IpQuery}/json/')
    response1.raise_for_status()
    data1 = response1.json()

    response2 = requests.get(f'https://api.ipapi.is/?ip={IpQuery}')
    response2.raise_for_status()
    data2 = response2.json()
except requests.exceptions.RequestException as e:
    console.print(f"[bold red]Error de red: {e}[/bold red]")
    exit()
except ValueError as e:
    console.print(f"[bold red]Error de datos: {e}[/bold red]")
    exit()
except Exception as e:
    console.print(f"[bold red]Error inesperado: {e}[/bold red]")
    exit()

table1 = Table(title="Información de la IP", title_justify="center", title_style="bold magenta")
table1.add_column("Información", style="cyan", no_wrap=True)
table1.add_column("Valor", style="magenta")

table.add_row("Red", data1.get("network", "No disponible"))

table.add_row("Tipo de IP", data1.get("version", "No disponible"))

table.add_row("TLD", data1.get("country_tld", "No disponible"))

table.add_row("ASN", data1.get("asn", "No disponible"))

table.add_row("Empresa", data1.get("org", "No disponible"))

table.add_row("RIR", data2.get("rir", "No disponible"))

table.add_row("Es una IP no autorizada", data2.get("is_bogon", "No disponible"))

table.add_row("Es un móvil", data2.get("is_mobile", "No disponible")),

table.add_row("Es un rastreador", data2.get("is_crawler", "No disponible"))
    
table.add_row("Es un centro de datos", data2.get("is_datacenter", "No disponible"))

table.add_row("Es una red Tor", data2.get("is_tor", "No disponible"))

table.add_row("Es un proxy", data2.get("is_proxy", "No disponible"))

table.add_row("Es una VPN", data2.get("is_vpn", "No disponible"))

table.add_row("Es una IP sospechosa", data2.get("is_abuser", "No disponible"))
 
table.add_row("País", data1.get("country", "No disponible"))

table.add_row("Capital", data1.get("country_capital", "No disponible"))

table.add_row("Ciudad", data1.get("city", "No disponible"))

table.add_row("Región", data1.get("region", "No disponible"))

table.add_row("Código de región", data1.get("region_code", "No disponible"))

table.add_row("Nombre de país", data1.get("country_name", "No disponible"))

table.add_row("Código de país", data1.get("country_code", "No disponible"))
    
table.add_row("ISO3", data1.get("country_code_iso3", "No disponible"))

table.add_row("Código de continente", data1.get("continent_code", "No disponible"))

table.add_row("En Europa", data1.get("in_eu", "No disponible"))

table.add_row("Código postal", data1.get("postal", "No disponible"))

table.add_row("Latitud", data1.get("latitude", "No disponible"))

table.add_row("Longitud", data1.get("longitude", "No disponible"))
    
table.add_row("Zona horaria", data1.get("timezone", "No disponible"))

table.add_row("UTC Offset", data1.get("utc_offset", "No disponible"))

table.add_row("Código de llamada", data1.get("country_calling_code", "No disponible"))

table.add_row("Moneda", data1.get("currency", "No disponible"))

table.add_row("Nombre de moneda", data1.get("currency_name", "No disponible"))

table.add_row("Idioma", data1.get("languages", "No disponible"))

table.add_row("Área del país", data1.get("country_area", "No disponible"))

table.add_row("Población del país", data1.get("country_population", "No disponible"))