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

            ip = data.get("ip")
            
            rir = data.get("rir")

            is_bogon = data.get("is_bogon")

            is_mobile = data.get("is_mobile")

            is_crawler = data.get("is_crawler")

            is_datacenter = data.get("is_datacenter")

            is_tor = data.get("is_tor")

            is_proxy = data.get("is_proxy")

            is_vpn = data.get("is_vpn")

            is_abuser = data.get("is_abuser")

            company_name = data.get("company", {}).get("name")

            abuser_score = data.get("company", {}).get("abuser_score")

            domain = data.get("company", {}).get("domain")

            type = data.get("company", {}).get("type")

            network = data.get("company", {}).get("network")

            abuse_name = data.get("abuse", {}).get("name")

            address = data.get("abuse", {}).get("address")

            phone = data.get("abuse", {}).get("phone")

            asn = data.get("asn", {}).get("asn")

            abuser_score = data.get("asn", {}).get("abuser_score")

            route = data.get("asn", {}).get("route")

            descr = data.get("asn", {}).get("descr")

            active = data.get("asn", {}).get("active")

            org = data.get("asn", {}).get("org")

            asn_domain = data.get("asn", {}).get("domain")

            abuse = data.get("asn", {}).get("abuse")

            asn_type = data.get("asn", {}).get("type")

            created = data.get("asn", {}).get("created")

            updated = data.get("asn", {}).get("updated")

            asn_rir = data.get("asn", {}).get("rir")

            calling_code = data.get("location", {}).get("calling_code")

            continent = data.get("location", {}).get("continent")

            country = data.get("location", {}).get("country")

            state = data.get("location", {}).get("state")

            city = data.get("location", {}).get("city")

            latitude = str(data.get("location", {}).get("latitude"))

            longitude = str(data.get("location", {}).get("longitude"))

            zip = str(data.get("location", {}).get("zip"))

            timezone = data.get("location", {}).get("timezone")
 

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
