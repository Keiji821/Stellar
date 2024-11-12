import requests
from bs4 import BeautifulSoup
import re
import time
import random
from rich.console import Console
from rich.table import Table
from rich.progress import track
from urllib.parse import quote

console = Console()

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/81.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0",
]

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

def email_finder():
    nombre = input("Ingrese el nombre: ").strip()
    apellido = input("Ingrese el apellido: ").strip()
    consulta = f"{nombre} {apellido}".strip()

    urls = [
        f"https://www.linkedin.com/search/results/content/?keywords={quote(consulta)}",
        f"https://twitter.com/search?q={quote(consulta)}",
        f"https://www.instagram.com/{quote(nombre)}.{quote(apellido)}/",
        f"https://www.pinterest.com/search/pins/?q={quote(consulta)}",
        f"https://www.tumblr.com/search/{quote(consulta)}",
        f"https://www.reddit.com/search/?q={quote(consulta)}",
        f"https://www.medium.com/search?q={quote(consulta)}",
        f"https://www.quora.com/search?q={quote(consulta)}",
        f"https://www.bing.com/search?q={quote(consulta) + ' email')}",
        f"https://search.yahoo.com/search?p={quote(consulta) + ' email')}",
        f"https://duckduckgo.com/?q={quote(consulta) + ' email')}",
        f"https://www.ecosia.org/search?q={quote(consulta) + ' email')}",
        f"https://www.ask.com/web?q={quote(consulta) + ' email')}",
        f"https://www.you.com/search?q={quote(consulta) + " email")}",
        f"https://search.aol.com/aol/search?q={quote(consulta) + ' email')}",
    ]

    emails = set()
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    console.print(f"\n[bold green]Buscando correos electrónicos para:[/bold green] {consulta}\n")

    for url in track(urls, description="Buscando en múltiples fuentes..."):
        headers = {"User-Agent": random.choice(user_agents)}

        try:
            response = requests.get(url, timeout=10, headers=headers, proxies=proxies)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            found_emails = re.findall(pattern, text)
            emails.update(found_emails)

            time.sleep(random.uniform(2, 5))

        except requests.exceptions.HTTPError as e:
            console.print(f"[bold red]Error al acceder a {url}:[/bold red] {e}")
        except requests.RequestException as e:
            console.print(f"[bold red]Error de conexión a {url}:[/bold red] {e}")

    table = Table(title="Direcciones de Correo Electrónico Encontradas")
    table.add_column("Email", style="red")

    if emails:
        for email in sorted(emails):
            table.add_row(email)
        console.print(table)
    else:
        console.print("[bold yellow]No se encontraron correos electrónicos.[/bold yellow]")

email_finder()
print(" ")