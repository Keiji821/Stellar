import requests
import os
from rich.progress import Progress, SpinnerColumn
from rich.console import Console
from rich.table import Table

console = Console()

os.system("""
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
echo $IP > ip_address.txt""")

with open("ip_address.txt", "r") as f:
    IpQuery = f.read().strip()
if not IpQuery:
    console.print("[bold red]Error[/bold red]")
else:
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
            if is_bogon == "True":
                is_bogon = "Sí"
            if is_bogon == "False":
                is_bogon = "No"

            is_mobile = str(data.get("is_mobile"))
            if is_mobile == "True":
                is_mobile = "Sí"
            if is_mobile == "False":
                is_mobile = "No"

            is_crawler = str(data.get("is_crawler"))
            if is_crawler == "True":
                is_crawler = "Sí"
            if is_crawler == "False":
                is_crawler = "No"

            is_datacenter = str(data.get("is_datacenter"))
            if is_datacenter == "True":
                is_datacenter = "Sí"
            if is_datacenter == "False":
                is_datacenter = "No"

            is_tor = str(data.get("is_tor"))
            if is_tor == "True":
                is_tor = "Sí"
            if is_tor == "False":
                is_tor = "No"  

            is_proxy = str(data.get("is_proxy"))
            if is_proxy == "True":
                is_proxy = "Sí"
            if is_proxy == "False":
                is_proxy = "No"

            is_vpn = str(data.get("is_vpn"))
            if is_vpn == "True":
                is_vpn = "Sí"
            if is_vpn == "False":
                is_vpn = "No"

            is_abuser = str(data.get("is_abuser"))
            if is_abuser == "True":
                is_abuser = "Sí"
            if is_abuser == "False":
                is_abuser = "No"

            company_name = str(data.get("company", {}).get("name"))

            abuser_score = str(data.get("company", {}).get("abuser_score"))

            domain = str(data.get("company", {}).get("domain"))

            type = str(data.get("company", {}).get("type"))

            network = str(data.get("company", {}).get("network"))

            abuse_name = str(data.get("abuse", {}).get("name"))

            address = str(data.get("abuse", {}).get("address"))

            phone = str(data.get("abuse", {}).get("phone"))

            asn = str(data.get("asn", {}).get("asn"))

            abuser_score2 = str(data.get("asn", {}).get("abuser_score"))

            route = str(data.get("asn", {}).get("route"))

            descr = str(data.get("asn", {}).get("descr"))

            active = str(data.get("asn", {}).get("active"))
            if active == "True":
                active = "Sí"
            if active == "False":
                active = "No"

            org = str(data.get("asn", {}).get("org"))

            asn_domain = str(data.get("asn", {}).get("domain"))

            abuse = str(data.get("asn", {}).get("abuse"))

            asn_type = str(data.get("asn", {}).get("type"))

            created = str(data.get("asn", {}).get("created"))

            updated = str(data.get("asn", {}).get("updated"))

            asn_rir = str(data.get("asn", {}).get("rir"))

            calling_code = str(data.get("location", {}).get("calling_code"))

            continent = str(data.get("location", {}).get("continent"))
            continent_tr = {
              'SA': 'Sudamérica',
              'EU': 'Europa',
}
            continentes = continent_tr.get(continent)

            country = str(data.get("location", {}).get("country"))

            state = str(data.get("location", {}).get("state"))

            city = str(data.get("location", {}).get("city"))

            latitude = str(data.get("location", {}).get("latitude"))

            longitude = str(data.get("location", {}).get("longitude"))

            zip = str(data.get("location", {}).get("zip"))

            timezone = str(data.get("location", {}).get("timezone"))


            console.print(" ")
            table = Table(title="Tú IP real", title_justify="center", title_style="bold green")
            table.add_column("[bold green]Información", style="code", no_wrap=False)
            table.add_column("[bold green]Valor", style="code")

            table.add_row("[bold underline][code][bold green]Información de Red[/bold underline]", "")
            table.add_row("IP", ip)
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
            table.add_row("[bold underline][code][bold green]Información de la empresa[/bold underline]", "")
            table.add_row("Red", network)
            table.add_row("Nombre de la compañía", company_name)
            table.add_row("Puntaje del abuser", abuser_score)
            table.add_row("Dominio", domain)
            table.add_row("Tipo", type)
            table.add_row("", "")
            table.add_row("[bold underline][code][bold green]Información del abuser[/bold underline]", "")
            table.add_row("Nombre del abuser", abuse_name)
            table.add_row("Dirección", address)
            table.add_row("Teléfono", phone)
            table.add_row("", "")
            table.add_row("[bold underline][code][bold green]Información del ASN[/bold underline]", "")
            table.add_row("Asn", asn)
            table.add_row("Puntaje del abuser", abuser_score2)
            table.add_row("Router", route)
            table.add_row("Descripción", descr)
            table.add_row("Activo", active)
            table.add_row("Organización", org)
            table.add_row("Dominio del asn", asn_domain)
            table.add_row("Abuser", abuse)
            table.add_row("Tipo de asn", asn_type)
            table.add_row("Creado el", created)
            table.add_row("Actualizado el", updated)
            table.add_row("Rir del asn", asn_rir)
            table.add_row("", "")
            table.add_row("[bold underline][code][bold green]Información Geográfica[/bold underline]", "")
            table.add_row("Continente", continentes)
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
        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Error de red: {e}[/bold red]")
        except ValueError as e:
            console.print(f"[bold red]Error de datos: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error inesperado: {e}[/bold red]")
