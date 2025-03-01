import requests
from bs4 import BeautifulSoup
import re
import random
import concurrent.futures
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from urllib.parse import quote

console = Console()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
]

EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def obtener_headers():
    return {"User-Agent": random.choice(USER_AGENTS), "Accept-Language": "es-ES,es;q=0.9"}

def buscar_correos(url, filtro_dominios=None):
    emails_encontrados = set()
    session = requests.Session()
    
    try:
        respuesta = session.get(url, timeout=7, headers=obtener_headers())
        respuesta.raise_for_status()
        sopa = BeautifulSoup(respuesta.content, 'html.parser')
        texto = sopa.get_text()
        correos = re.findall(EMAIL_PATTERN, texto)
        
        if filtro_dominios:
            correos = [email for email in correos if any(dom in email for dom in filtro_dominios)]
        
        emails_encontrados.update(correos)
        
    except requests.HTTPError as e:
        console.print(f"[bold red]Error HTTP en {url}:[/bold red] {e}")
    except requests.RequestException as e:
        console.print(f"[bold red]Error de conexión a {url}:[/bold red] {e}")
    except Exception as e:
        console.print(f"[bold red]Error inesperado en {url}:[/bold red] {e}")
    
    return emails_encontrados

def email_finder():
    try:
        nombre = console.input("[bold green]Ingrese el nombre: [/bold green]").strip()
        apellido = console.input("[bold green]Ingrese el apellido: [/bold green]").strip()
        consulta = f"{nombre} {apellido}".strip()
        
        if not nombre or not apellido:
            console.print("[bold red]Nombre o apellido no pueden estar vacíos.[/bold red]")
            return
        
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
        
        filtro_dominios = console.input("Ingrese dominios de correo que desea filtrar (separados por coma, o deje vacío para todos): ").strip()
        if filtro_dominios:
            filtro_dominios = filtro_dominios.split(",")
        
        console.print(f"\n[bold green]Buscando correos electrónicos para:[/bold green] {consulta}\n")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            resultados = list(executor.map(lambda url: buscar_correos(url, filtro_dominios), urls))
        
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
    
    except Exception as e:
        console.print(f"[bold red]Error inesperado:[/bold red] {e}")

if __name__ == "__main__":
    email_finder()