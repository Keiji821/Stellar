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


            console.print(table)
            console.print(" ")
        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Error de red: {e}[/bold red]")
        except ValueError as e:
            console.print(f"[bold red]Error de datos: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error inesperado: {e}[/bold red]")
