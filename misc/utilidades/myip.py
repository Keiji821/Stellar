import requests
import os
from rich.progress import Progress, SpinnerColumn
from rich.console import Console
from rich.table import Table
import socket

console = Console()

def obtener_info_dispositivo(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        response.raise_for_status()
        data = response.json()
        return data.get('is_mobile', 'Desconocido'), data.get('os', 'Desconocido')
    except requests.RequestException:
        return 'Error al obtener', 'Desconocido'

def obtener_puerto_remoto(ip):
    try:
        sock = socket.create_connection((ip, 80), timeout=5)
        sock.close()
        return 80
    except socket.error:
        return 'Desconocido'

def obtener_ip_publica():
    comandos = [
        "(command -v dig &> /dev/null && (dig +short @ident.me || dig +short @tnedi.me))",
        "(command -v nc &> /dev/null && (nc ident.me 23 < /dev/null || nc tnedi.me 23 < /dev/null))",
        "(command -v curl &> /dev/null && (curl -sf ident.me || curl -sf tnedi.me))",
        "(command -v wget &> /dev/null && (wget -qO- ident.me || wget -qO- tnedi.me))"
    ]
    
    for comando in comandos:
        ip = os.popen(comando).read().strip()
        if ip:
            return ip
    console.print("[bold red]Error: No se pudo obtener la IP pública.[/bold red]")
    return None

def mostrar_info_ip(ip):
    with Progress(SpinnerColumn("dots")) as progress:
        task = progress.add_task("[red]Cargando...")

        try:
            response1 = requests.get(f'https://ipapi.co/{ip}/json/')
            progress.update(task, advance=30)
            response1.raise_for_status()
            data1 = response1.json()

            response2 = requests.get(f'https://api.ipapi.is/?ip={ip}')
            progress.update(task, advance=70)
            response2.raise_for_status()
            data2 = response2.json()

            es_movil, sistema_operativo = obtener_info_dispositivo(ip)
            puerto_remoto = obtener_puerto_remoto(ip)

            table = Table(title="Datos de la IP", title_justify="center", title_style="bold red")
            table.add_column("Información", style="green")
            table.add_column("Valor", style="white")

            table.add_row("[bold underline]Información de Red[/bold underline]", "")
            table.add_row("Red", str(data1.get("network", "No disponible")))
            table.add_row("Tipo de IP", str(data1.get("version", "No disponible")))
            table.add_row("TLD", str(data1.get("country_tld", "No disponible")))
            table.add_row("ASN", str(data1.get("asn", "No disponible")))
            table.add_row("Empresa", str(data1.get("org", "No disponible")))
            table.add_row("RIR", str(data2.get("rir", "No disponible")))
            table.add_row("Es una IP no autorizada", str(data2.get("is_bogon", "No disponible")))
            table.add_row("Es un móvil", str(data1.get("is_mobile", "No disponible")))
            table.add_row("Es un rastreador", str(data2.get("is_crawler", "No disponible")))
            table.add_row("Es un centro de datos", str(data2.get("is_datacenter", "No disponible")))
            table.add_row("Es una red Tor", str(data2.get("is_tor", "No disponible")))
            table.add_row("Es un proxy", str(data2.get("is_proxy", "No disponible")))

            table.add_row("[bold underline]Información Geográfica[/bold underline]", "")
            table.add_row("País", str(data1.get("country", "No disponible")))
            table.add_row("Capital", str(data1.get("country_capital", "No disponible")))
            table.add_row("Ciudad", str(data1.get("city", "No disponible")))
            table.add_row("Región", str(data1.get("region", "No disponible")))
            table.add_row("Código de región", str(data1.get("region_code", "No disponible")))
            table.add_row("Nombre de país", str(data1.get("country_name", "No disponible")))
            table.add_row("Código de país", str(data1.get("country_code", "No disponible")))

            table.add_row("[bold underline]Información adicional[/bold underline]", "")
            table.add_row("Es Móvil", es_movil)
            table.add_row("Sistema Operativo", sistema_operativo)
            table.add_row("Puerto Remoto", str(puerto_remoto))

            console.print(table)
        except requests.RequestException as e:
            console.print(f"[bold red]Error de red: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error inesperado: {e}[/bold red]")

ip_publica = obtener_ip_publica()
if ip_publica:
    mostrar_info_ip(ip_publica)