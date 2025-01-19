import requests
from rich.progress import Progress, SpinnerColumn
from rich.console import Console
from rich.table import Table

console = Console()

while True:
    IpQuery = console.input("[bold green]Ingrese la IP: [/bold green]").strip()
    if not IpQuery:
        console.print("[bold red]Error: No se puede dejar la IP vacía. Intente de nuevo.[/bold red]")
        continue

    with Progress(SpinnerColumn("dots")) as progress:
        task = progress.add_task("[red]Cargando...")
        try:
            response = requests.get(f'https://api.ipapi.is/?ip={IpQuery}')
            progress.update(task, advance=30)
            response.raise_for_status()
            data = response.json()
            progress.update(task, advance=50)

            ip = str(data.get("ip"))
            
            rir = str(data.get("rir"))

            is_bogon = str(data.get("is_bogon"))

            is_mobile = str(data.get("is_mobile"))

            is_crawler = str(data.get("is_crawler"))

            is_datacenter = str(data.get("is_datacenter"))

            is_tor = str(data.get("is_tor"))

            is_proxy = str(data.get("is_proxy"))

            is_vpn = str(data.get("is_vpn"))

            is_abuser = str(data.get("is_abuser"))

            company_name = str(data.get("company", {}).get("name"))

            abuser_score = str(data.get("company", {}).get("abuser_score"))

            domain = str(data.get("company", {}).get("domain"))

            type = str(data.get("company", {}).get("type"))

            network = str(data.get("company", {}).get("network"))

            abuse_name = str(data.get("abuse", {}).get("name"))

            address = str(data.get("abuse", {}).get("address"))

            phone = str(data.get("abuse", {}).get("phone"))

            asn = str(data.get("asn", {}).get("asn"))

            abuser_score = str(data.get("asn", {}).get("abuser_score"))

            route = str(data.get("asn", {}).get("route"))

            descr = str(data.get("asn", {}).get("descr"))

            active = str(data.get("asn", {}).get("active"))

            org = str(data.get("asn", {}).get("org"))

            asn_domain = str(data.get("asn", {}).get("domain"))

            abuse = str(data.get("asn", {}).get("abuse"))

            asn_type = str(data.get("asn", {}).get("type"))

            created = str(data.get("asn", {}).get("created"))

            updated = str(data.get("asn", {}).get("updated"))

            asn_rir = str(data.get("asn", {}).get("rir"))

            calling_code = str(data.get("location", {}).get("calling_code"))

            continent = str(data.get("location", {}).get("continent"))

            country = str(data.get("location", {}).get("country"))

            state = str(data.get("location", {}).get("state"))

            city = str(data.get("location", {}).get("city"))

            latitude = str(data.get("location", {}).get("latitude"))

            longitude = str(data.get("location", {}).get("longitude"))

            zip = str(data.get("location", {}).get("zip"))

            timezone = str(data.get("location", {}).get("timezone"))
 

            console.print(" ")
            table = Table(title="Datos de la IP", title_justify="center", title_style="bold green")
            table.add_column("[bold green]Información", style="code", no_wrap=False)
            table.add_column("[bold green]Valor", style="code")

            table.add_row("[bold underline][code][bold green]Información de Red[/bold underline]", "")
            table.add_row("Red", ip)
            table.add_row("Rir", rir)
            table.add_row("Es una IP no asignada", is_bogon)
            table.add_row("Es un móvil", is_mobile)
            table.add_row("Es un rastreador", is_crawler)
            table.add_row("Es un centro de datos", is_datacenter)
            table.add_row("Es una red Tor", is_tor)
            table.add_row("Es un proxy", is_proxy)
            table.add_row("Es una VPN", is_vpn)
            table.add_row("Es una IP sospechosa", is_abuser)

            table.add_row("", "")

            table.add_row("[bold underline][code][bold green]Información Geográfica[/bold underline]", "")
            table.add_row("Continente", continent)
            table.add_row("País", country)
            table.add_row("Estado", state)
            table.add_row("Ciudad", city)
            table.add_row("Código postal", zip)
            table.add_row("Latitud", latitude)
            table.add_row("Longitud", longitude)
            table.add_row("Zona horaria", timezone)
            table.add_row("Código de llamada", calling_code)

            console.print(table)
            console.print(" ")
            break
        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Error de red: {e}[/bold red]")
        except ValueError as e:
            console.print(f"[bold red]Error de datos: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error inesperado: {e}[/bold red]")
