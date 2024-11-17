import requests
from bs4 import BeautifulSoup
import re
import time
import random
from rich.console import Console
from rich.table import Table
from rich.progress import track
from urllib.parse import quote
import concurrent.futures

console = Console()

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/81.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS;EN-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 Edge/12.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"
]

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

def buscar_correos(url, consulta, filtro_dominios=None):
    headers = {"User-Agent": random.choice(user_agents)}
    emails_encontrados = set()
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    try:
        response = requests.get(url, timeout=10, headers=headers, proxies=proxies)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        found_emails = re.findall(pattern, text)
        
        if filtro_dominios:
            found_emails = [email for email in found_emails if any(dom in email for dom in filtro_dominios)]
        
        emails_encontrados.update(found_emails)

    except requests.exceptions.HTTPError as e:
        console.print(f"[bold red]Error al acceder a {url}:[/bold red] {e}")
    except requests.RequestException as e:
        console.print(f"[bold red]Error de conexión a {url}:[/bold red] {e}")

    return emails_encontrados

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
        f"https://www.bing.com/search?q={quote(consulta + ' email')}",
        f"https://search.yahoo.com/search?p={quote(consulta + ' email')}",
        f"https://duckduckgo.com/?q={quote(consulta + ' email')}",
        f"https://www.ecosia.org/search?q={quote(consulta + ' email')}",
        f"https://www.ask.com/web?q={quote(consulta + ' email')}",
        f"https://www.you.com/search?q={quote(consulta + ' email')}",
        f"https://search.aol.com/aol/search?q={quote(consulta + ' email')}",
        f"https://www.github.com/search?q={quote(consulta)}",
        f"https://www.stackoverflow.com/search?q={quote(consulta)}",
        f"https://www.researchgate.net/search?q={quote(consulta)}",
        f"https://www.facebook.com/search/top?q={quote(consulta)}"
    ]

    emails = set()

    filtro_dominios = input("Ingrese dominios de correo que desea filtrar (separados por coma, o deje vacío para todos): ").strip()
    if filtro_dominios:
        filtro_dominios = filtro_dominios.split(",")

    console.print(f"\n[bold green]Buscando correos electrónicos para:[/bold green] {consulta}\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        resultados = list(executor.map(lambda url: buscar_correos(url, consulta, filtro_dominios), urls))

    for resultado in resultados:
        emails.update(resultado)

    table = Table(title="Direcciones de Correo Electrónico Encontradas")
    table.add_column("Email", style="red")

    if emails:
        for email in sorted(emails):
            table.add_row(email)
        console.print(table)
    else:
        console.print("[bold yellow]No se encontraron correos electrónicos.[/bold yellow]")

if __name__ == "__main__":
    email_finder()