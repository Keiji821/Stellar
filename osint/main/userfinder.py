import asyncio
import aiohttp
import httpx
import random
import logging
import aiocache
from selectolax.parser import HTMLParser
from rich.console import Console
from rich.table import Table
from urllib.parse import quote

console = Console()

PLATAFORMAS = {
    "Twitter": {"url": "https://twitter.com/{}", "indicador": "This account doesn’t exist", "status_code": 404},
    "Instagram": {"url": "https://instagram.com/{}", "indicador": "La página no está disponible", "status_code": 200},
    "GitHub": {"url": "https://github.com/{}", "indicador": "Not Found", "status_code": 404},
    "TikTok": {"url": "https://www.tiktok.com/@{}", "indicador": "Couldn't find this account", "status_code": 200},
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/101.0 Safari/537.36",
]

PROXIES = [
    "http://proxy1:port",
    "http://proxy2:port",
    "http://proxy3:port"
]

logging.basicConfig(filename="debug.log", level=logging.INFO, format="%(asctime)s - %(message)s")


async def random_delay():
    """Introduce un retraso aleatorio para evitar detección masiva"""
    await asyncio.sleep(random.uniform(0.5, 2.0))


async def obtener_headers():
    """Genera headers aleatorios"""
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml",
        "Referer": "https://www.google.com/",
    }


@aiocache.cached(ttl=60)
async def fetch(session, url):
    """Realiza la solicitud con caché"""
    try:
        async with session.get(url, headers=await obtener_headers(), timeout=10) as response:
            return await response.text(), response.status
    except Exception as e:
        logging.error(f"Error al acceder a {url}: {e}")
        return None, None


async def extraer_info(html):
    """Extrae metadatos del perfil con Selectolax"""
    try:
        tree = HTMLParser(html)
        titulo = tree.css_first("title").text(strip=True) if tree.css_first("title") else "No disponible"
        desc_meta = tree.css_first('meta[name="description"]')
        descripcion = desc_meta.attrs["content"].strip() if desc_meta else "Sin descripción"
        return titulo, descripcion
    except Exception:
        return "No disponible", "Sin descripción"


async def buscar_usuario(session, plataforma, username):
    """Verifica si el usuario existe en una plataforma"""
    await random_delay()
    config = PLATAFORMAS[plataforma]
    url = config["url"].format(quote(username))

    html, status = await fetch(session, url)
    if not html:
        return plataforma, False, url, "No disponible", "Sin información"

    encontrado = status != config["status_code"] and config["indicador"] not in html
    if encontrado:
        titulo, descripcion = await extraer_info(html)
        return plataforma, True, url, titulo, descripcion

    return plataforma, False, url, "No disponible", "Sin información"


async def verificar_usuario(username):
    """Ejecuta la búsqueda en todas las plataformas en paralelo"""
    async with aiohttp.ClientSession() as session:
        tasks = [buscar_usuario(session, plataforma, username) for plataforma in PLATAFORMAS]
        resultados = await asyncio.gather(*tasks)

    mostrar_resultados(username, resultados)


def mostrar_resultados(username, resultados):
    """Muestra los resultados en consola"""
    tabla = Table(title=f"Resultados para '{username}'", show_header=True, header_style="bold blue")
    tabla.add_column("Plataforma", justify="left", style="cyan")
    tabla.add_column("Estado", justify="center", style="bold")
    tabla.add_column("URL", justify="left", max_width=35)
    tabla.add_column("Nombre", justify="left", max_width=20)
    tabla.add_column("Descripción", justify="left", max_width=40)

    for plataforma, encontrado, url, nombre, descripcion in resultados:
        estado = "[green]✔ Encontrado[/green]" if encontrado else "[red]❌ No encontrado[/red]"
        tabla.add_row(plataforma, estado, f"[link={url}]{url}[/link]", nombre[:20], descripcion[:40])

    console.print(tabla)


if __name__ == "__main__":
    username = console.input("[bold green]Introduce el nombre de usuario: [/bold green]").strip()
    asyncio.run(verificar_usuario(username))