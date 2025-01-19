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

            company_name = data.get("company")[0]("name")

            abuser_score = data.get("company")[0]("abuser_score")

            domain = data.get("company")[0]("domain")

            type = data.get("company")[0]("type")

            network = data.get("company")[0]("network")

            abuse_name = data.get("abuse")[0]("name")

            address = data.get("abuse")[0]("address")

            phone = data.get("abuse")[0]("phone")

            asn = data.get("asn")[0]("asn")

            abuser_score = data.get("asn")[0]("abuser_score")

            route = data.get("asn")[0]("route")

            descr = data.get("asn")[0]("descr")

            active = data.get("asn")[0]("active")

            org = data.get("asn")[0]("org")

            asn_domain = data.get("asn")[0]("domain")

            abuse = data.get("asn")[0]("abuse")

            asn_type = data.get("asn")[0]("type")

            created = data.get("asn")[0]("created")

            updated = data.get("asn")[0]("updated")

            asn_rir = data.get("asn")[0]("rir")

            calling_code = data.get("location")[0]("calling_code")

            continent = data.get("location")[0]("continent")

            country = data.get("location")[0]("country")

            state = data.get("location")[0]("state")

            city = data.get("location")[0]("city")

            latitude = data.get("location")[0]("latitude")

            longitude = data.get("location")[0]("longitude")

            zip = data.get("location")[0]("zip")

            timezone = data.get("location")[0]("timezone")
 

            console.print(" ")
            table = Table(title="Datos de la IP", title_justify="center", title_style="bold green")
            table.add_column("[bold green]Información", style="code", no_wrap=False)
            table.add_column("[bold green]Valor", style="code")

            table.add_row("[bold underline][code][bold green]Información de Red[/bold underline]", "")
            table.add_row("Red", ip)
            table.add_row("Tipo de IP", )
            table.add_row("TLD", )
            table.add_row("ASN", )
            table.add_row("Empresa", )
            table.add_row("RIR", )
            table.add_row("Es una IP no autorizada", )
            table.add_row("Es un móvil", )
            table.add_row("Es un rastreador", )
            table.add_row("Es un centro de datos", )
            table.add_row("Es una red Tor", )
            table.add_row("Es un proxy", )
            table.add_row("Es una VPN", )
            table.add_row("Es una IP sospechosa", )
            table.add_row("Nivel de fraude", )
            table.add_row("Es una IP activa", )
            table.add_row("Dominio", )
            table.add_row("Fecha de creación", )
            table.add_row("Correo de la empresa", )

            table.add_row("", "")

            table.add_row("[bold underline][code][bold green]Información Geográfica[/bold underline]", "")
            table.add_row("País", )
            table.add_row("Capital", )
            table.add_row("Ciudad", )
            table.add_row("Región", )
            table.add_row("Código de región", )
            table.add_row("Nombre de país", )
            table.add_row("Código de país", )
            table.add_row("ISO3", )
            table.add_row("Código de continente", )
            table.add_row("En Europa", )
            table.add_row("Código postal", )
            table.add_row("Latitud", )
            table.add_row("Longitud", )
            table.add_row("Zona horaria", )
            table.add_row("UTC Offset", )
            table.add_row("Código de llamada", )
            table.add_row("Moneda", )
            table.add_row("Nombre de moneda", )
            table.add_row("Idioma", )
            table.add_row("Área del país", )
            table.add_row("Población del país", )

            console.print(table)
            console.print(" ")
            break
        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Error de red: {e}[/bold red]")
        except ValueError as e:
            console.print(f"[bold red]Error de datos: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error inesperado: {e}[/bold red]")
