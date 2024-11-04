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

print(" ")

table = Table(title="Datos de la IP", title_justify="center", title_style="bold magenta")

table.add_column("Información de red", style="cyan", no_wrap=False)
table.add_column("Valor", style="magenta")
table.add_column("Información geográfica", style="cyan")
table.add_column("Valor", style="magenta")

table.add_row("Red", str(data1.get("network", "No disponible")), "País", str(data1.get("country", "No disponible")),)

table.add_row("Tipo de IP", str(data1.get("version", "No disponible")), "Capital", str(data1.get("country_capital", "No disponible")),)

table.add_row("TLD", str(data1.get("country_tld", "No disponible")), "Ciudad", str(data1.get("city", "No disponible")),)

table.add_row("ASN", str(data1.get("asn", "No disponible")), "Región", str(data1.get("region", "No disponible")),)

table.add_row("Empresa", str(data1.get("org", "No disponible")), "Código de región", str(data1.get("region_code", "No disponible")),)

table.add_row("RIR", str(data2.get("rir", "No disponible")), "Nombre de país", str(data1.get("country_name", "No disponible")),)

table.add_row("Es una IP no autorizada", str(data2.get("is_bogon", "No disponible")), "Código de país", str(data1.get("country_code", "No disponible")),)

table.add_row("Es un móvil", str(data2.get("is_mobile", "No disponible")), "ISO3",
str(data1.get("country_code_iso3", "No disponible")),)

table.add_row("Es un rastreador", str(data2.get("is_crawler", "No disponible")), "Código de continente", str(data1.get("continent_code", "No disponible")),)

table.add_row("Es un centro de datos", str(data2.get("is_datacenter", "No disponible")), "En Europa", str(data1.get("in_eu", "No disponible")),)

table.add_row("Es una red Tor", str(data2.get("is_tor", "No disponible")), "Código postal", str(data1.get("postal", "No disponible")),)

table.add_row("Es un proxy", str(data2.get("is_proxy", "No disponible")), "Latitud", str(data1.get("latitude", "No disponible")),)

table.add_row("Es una VPN", str(data2.get("is_vpn", "No disponible")), "Longitud", str(data1.get("longitude", "No disponible")),)

table.add_row("Es una IP sospechosa", str(data2.get("is_abuser", "No disponible")), "Zona horaria", str(data1.get("timezone", "No disponible")),)

table.add_row(" ", " ", "UTC Offset", str(data1.get("utc_offset", "No disponible")),)

table.add_row(" ", " ", "Código de llamada",
str(data1.get("country_calling_code", "No disponible")),)

table.add_row(" ", " ", "Moneda", str(data1.get("currency", "No disponible")),)

table.add_row(" ", " ", "Nombre de moneda", str(data1.get("currency_name", "No disponible")),)

table.add_row(" ", " ", "Idioma", str(data1.get("languages", "No disponible")),)

table.add_row(" ", " ", "Área del país", str(data1.get("country_area", "No disponible")),)

table.add_row(" ", " ", "Población del país", str(data1.get("country_population", "No disponible")),)

table.add_row("Nivel de fraude: ", str(data2.get("asn")["abuser_score"]),)

table.add_row("Es una ip activa: ", str(data2.get("asn")["active"]),)

table.add_row("Dominio: ", str(data2.get("asn")["domain"]),)

table.add_row("Fecha de creación: ", str(data2.get("asn")["created"]),)

table.add_row("Nivel de fraude: ", str(data2.get("abuse")["email"]),)
print(" ")

console = Console()
console.print(table)