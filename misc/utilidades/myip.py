import requests
from rich.progress import Progress, SpinnerColumn
from rich.console import Console
from rich.table import Table
import os

console = Console()

output = os.popen("""
IP=$(
  (command -v dig &> /dev/null &&
    (dig +short @ident.me ||
     dig +short @tnedi.me)) ||
  (command -v nc &> /dev/null &&
    (nc ident.me 23 < /dev/null ||
     nc tnedi.me 23 < /dev/null)) ||
  (command -v curl &> /dev/null &&
    (curl -sf ident.me ||
     curl -sf tnedi.me)) ||
  (command -v wget &> /dev/null &&
    (wget -qO- ident.me ||
     wget -qO- tnedi.me)) ||
  (command -v openssl &> /dev/null &&
    (openssl s_client -quiet -connect ident.me:992 2> /dev/null ||
     openssl s_client -quiet -connect tnedi.me:992 2> /dev/null)) ||
  (command -v ssh &> /dev/null &&
    (ssh -qo StrictHostKeyChecking=accept-new ident.me ||
     ssh -qo StrictHostKeyChecking=accept-new tnedi.me)) ||
  (echo "Could not find public IP through api.ident.me" >&2
   exit 42)
)
echo "Found public IP $IP"
""").read()

ip = output.strip()

with Progress(SpinnerColumn("dots")) as progress:
    task = progress.add_task("[red]Cargando...")
    try:
        response1 = requests.get(f'https://ipapi.co/{ip}/json/')
        progress.update(task, advance=20)
        response1.raise_for_status()
        data1 = response1.json()

        response2 = requests.get(f'https://api.ipapi.is/?ip={ip}')
        progress.update(task, advance=30)
        response2.raise_for_status()
        data2 = response2.json()
        progress.update(task, advance=50)
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error de red: {e}[/bold red]")
        exit()
    except ValueError as e:
        console.print(f"[bold red]Error de datos: {e}[/bold red]")
        exit()
    except Exception as e:
        console.print(f"[bold red]Error inesperado: {e}[/bold red]")
        exit()

console.print(" ")

table = Table(title="Tú IP", title_justify="center", title_style="bold green")

table.add_column("Información", style="green", no_wrap=False)
table.add_column("Valor", style="white")

# Información de red
table.add_row("[bold underline]Información de Red[/bold underline]", "")
table.add_row("Red", str(data1.get("network", "No disponible")))
table.add_row("Tipo de IP", str(data1.get("version", "No disponible")))
table.add_row("TLD", str(data1.get("country_tld", "No disponible")))
table.add_row("ASN", str(data1.get("asn", "No disponible")))
table.add_row("Empresa", str(data1.get("org", "No disponible")))
table.add_row("RIR", str(data2.get("rir", "No disponible")))
table.add_row("Es una IP no autorizada", str(data2.get("is_bogon", "No disponible")))
table.add_row("Es un móvil", str(data2.get("is_mobile", "No disponible")))
table.add_row("Es un rastreador", str(data2.get("is_crawler", "No disponible")))
table.add_row("Es un centro de datos", str(data2.get("is_datacenter", "No disponible")))
table.add_row("Es una red Tor", str(data2.get("is_tor", "No disponible")))
table.add_row("Es un proxy", str(data2.get("is_proxy", "No disponible")))
table.add_row("Es una VPN", str(data2.get("is_vpn", "No disponible")))
table.add_row("Es una IP sospechosa", str(data2.get("is_abuser", "No disponible")))
table.add_row("Nivel de fraude", str(data2.get("asn", {}).get("abuser_score", "No disponible")))
table.add_row("Es una IP activa", str(data2.get("asn", {}).get("active", "No disponible")))
table.add_row("Dominio", str(data2.get("asn", {}).get("domain", "No disponible")))
table.add_row("Fecha de creación", str(data2.get("asn", {}).get("created", "No disponible")))
table.add_row("Correo de la empresa", str(data2.get("abuse", {}).get("email", "No disponible")))

# Información geográfica
table.add_row("", "")
table.add_row("[bold underline]Información Geográfica[/bold underline]", "")
table.add_row("País", str(data1.get("country", "No disponible")))
table.add_row("Capital", str(data1.get("country_capital", "No disponible")))
table.add_row("Ciudad", str(data1.get("city", "No disponible")))
table.add_row("Región", str(data1.get("region", "No disponible")))
table.add_row("Código de región", str(data1.get("region_code", "No disponible")))
table.add_row("Nombre de país", str(data1.get("country_name", "No disponible")))
table.add_row("Código de país", str(data1.get("country_code", "No disponible")))
table.add_row("ISO3", str(data1.get("country_code_iso3", "No disponible")))
table.add_row("Código de continente", str(data1.get("continent_code", "No disponible")))
table.add_row("En Europa", str(data1.get("in_eu", "No disponible")))
table.add_row("Código postal", str(data1.get("postal", "No disponible")))
table.add_row("Latitud", str(data1.get("latitude", "No disponible")))
table.add_row("Longitud", str(data1.get("longitude", "No disponible")))
table.add_row("Zona horaria", str(data1.get("timezone", "No disponible")))
table.add_row("UTC Offset", str(data1.get("utc_offset", "No disponible")))
table.add_row("Código de llamada", str(data1.get("country_calling_code", "No disponible")))
table.add_row("Moneda", str(data1.get("currency", "No disponible")))
table.add_row("Nombre de moneda", str(data1.get("currency_name", "No disponible")))
table.add_row("Idioma", str(data1.get("languages", "No disponible")))
table.add_row("Área del país", str(data1.get("country_area", "No disponible")))
table.add_row("Población del país", str(data1.get("country_population", "No disponible")))

console.print(table)
console.print(" ")
