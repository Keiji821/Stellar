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

table_data1 = [
    (" "),
    ("Red", data1.get("network", "No disponible")),
    ("Tipo de IP", data1.get("version", "No disponible")),
    ("TLD", data1.get("country_tld", "No disponible")),
    ("ASN", data1.get("asn", "No disponible")),
    ("Empresa", data1.get("org", "No disponible")),
    ("RIR", data2.get("rir", "No disponible")),
    ("Es una IP no autorizada", data2.get("is_bogon", "No disponible")),
    ("Es un móvil", data2.get("is_mobile", "No disponible")),
    ("Es un rastreador", data2.get("is_crawler", "No disponible")),
    ("Es un centro de datos", data2.get("is_datacenter", "No disponible")),
    ("Es una red Tor", data2.get("is_tor", "No disponible")),
    ("Es un proxy", data2.get("is_proxy", "No disponible")),
    ("Es una VPN", data2.get("is_vpn", "No disponible")),
    ("Es una IP sospechosa", data2.get("is_abuser", "No disponible")),
    (" "),
]

table_data2 = [
    (" "),
    ("País", data1.get("country", "No disponible")),
    ("Capital", data1.get("country_capital", "No disponible")),
    ("Ciudad", data1.get("city", "No disponible")),
    ("Región", data1.get("region", "No disponible")),
    ("Código de región", data1.get("region_code", "No disponible")),
    ("Nombre de país", data1.get("country_name", "No disponible")),
    ("Código de país", data1.get("country_code", "No disponible")),
    ("ISO3", data1.get("country_code_iso3", "No disponible")),
    ("Código de continente", data1.get("continent_code", "No disponible")),
    ("En Europa", data1.get("in_eu", "No disponible")),
    ("Código postal", data1.get("postal", "No disponible")),
    ("Latitud", data1.get("latitude", "No disponible")),
    ("Longitud", data1.get("longitude", "No disponible")),
    ("Zona horaria", data1.get("timezone", "No disponible")),
    ("UTC Offset", data1.get("utc_offset", "No disponible")),
    ("Código de llamada", data1.get("country_calling_code", "No disponible")),
    ("Moneda", data1.get("currency", "No disponible")),
    ("Nombre de moneda", data1.get("currency_name", "No disponible")),
    ("Idioma", data1.get("languages", "No disponible")),
    ("Área del país", data1.get("country_area", "No disponible")),
    ("Población del país", data1.get("country_population", "No disponible")),
    (" "),
]

table1 = Table(title="Información de red", title_justify="center", title_style="bold magenta")
table1.add_column("Información", style="cyan", no_wrap=True)
table1.add_column("Valor", style="magenta")

for info, valor in table_data1:
    table1.add_row(info, str(valor))

table2 = Table(title="Información Geográfica", title_justify="center", title_style="bold magenta")
table2.add_column("Información", style="cyan", no_wrap=True)
table2.add_column("Valor", style="magenta")

for info, valor in table_data2:
    table2.add_row(info, str(valor))

console.print(table1)
console.print(table2)