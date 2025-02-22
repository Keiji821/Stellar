import requests
from time import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
import random
from typing import Dict, Tuple, List
from requests.exceptions import RequestException
from urllib.parse import quote
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.style import Style
import json

console = Console()

PLATAFORMAS: Dict[str, Dict[str, str]] = {
    "Twitter": {"url": "https://twitter.com/{}", "indicador": "This account doesn’t exist", "status_code": 404},
    "Instagram": {"url": "https://instagram.com/{}", "indicador": "La página no está disponible", "status_code": 200},
    "Facebook": {"url": "https://www.facebook.com/{}", "indicador": "Página no encontrada", "status_code": 200},
    "Pinterest": {"url": "https://pinterest.com/{}", "indicador": "Lo sentimos, esta página no está disponible", "status_code": 404},
    "YouTube": {"url": "https://www.youtube.com/@{}", "indicador": "Este canal no está disponible", "status_code": 200},
    "TikTok": {"url": "https://www.tiktok.com/@{}", "indicador": "Couldn't find this account", "status_code": 200},
    "Reddit": {"url": "https://www.reddit.com/user/{}", "indicador": "Sorry, nobody on Reddit goes by that name", "status_code": 404},
    "GitHub": {"url": "https://github.com/{}", "indicador": "Not Found", "status_code": 404},
    "LinkedIn": {"url": "https://www.linkedin.com/in/{}", "indicador": "This profile is not available", "status_code": 404},
    "Twitch": {"url": "https://www.twitch.tv/{}", "indicador": "This channel is unavailable", "status_code": 404},
    "Snapchat": {"url": "https://www.snapchat.com/add/{}", "indicador": "Sorry, we couldn't find that user", "status_code": 404},
    "Spotify": {"url": "https://open.spotify.com/user/{}", "indicador": "Page not found", "status_code": 404},
    "Steam": {"url": "https://steamcommunity.com/id/{}", "indicador": "The specified profile could not be found", "status_code": 404},
    "Tumblr": {"url": "https://{}.tumblr.com", "indicador": "There's nothing here", "status_code": 404},
    "Flickr": {"url": "https://www.flickr.com/people/{}", "indicador": "Page Not Found", "status_code": 404},
    "Vimeo": {"url": "https://vimeo.com/{}", "indicador": "Sorry, we couldn’t find that page", "status_code": 404},
    "SoundCloud": {"url": "https://soundcloud.com/{}", "indicador": "Oops! We can’t find that page", "status_code": 404},
    "Medium": {"url": "https://medium.com/@{}", "indicador": "Page not found", "status_code": 404},
    "DeviantArt": {"url": "https://{}.deviantart.com", "indicador": "Page Not Found", "status_code": 404},
    "Quora": {"url": "https://www.quora.com/profile/{}", "indicador": "Oops! The page you were looking for doesn’t exist", "status_code": 404},
    "Wikipedia": {"url": "https://en.wikipedia.org/wiki/User:{}", "indicador": "User does not exist", "status_code": 404},
    "Patreon": {"url": "https://www.patreon.com/{}", "indicador": "This page is not available", "status_code": 404},
    "Dribbble": {"url": "https://dribbble.com/{}", "indicador": "Page not found", "status_code": 404},
    "Behance": {"url": "https://www.behance.net/{}", "indicador": "Page Not Found", "status_code": 404},
    "Goodreads": {"url": "https://www.goodreads.com/{}", "indicador": "Page not found", "status_code": 404},
    "Bandcamp": {"url": "https://bandcamp.com/{}", "indicador": "Page not found", "status_code": 404},
    "CodePen": {"url": "https://codepen.io/{}", "indicador": "Page not found", "status_code": 404},
    "HackerRank": {"url": "https://www.hackerrank.com/{}", "indicador": "Page not found", "status_code": 404},
    "LeetCode": {"url": "https://leetcode.com/{}", "indicador": "Page not found", "status_code": 404},
    "Kaggle": {"url": "https://www.kaggle.com/{}", "indicador": "Page not found", "status_code": 404},
    "StackOverflow": {"url": "https://stackoverflow.com/users/{}", "indicador": "Page not found", "status_code": 404},
    "Keybase": {"url": "https://keybase.io/{}", "indicador": "Page not found", "status_code": 404},
    "Bitbucket": {"url": "https://bitbucket.org/{}", "indicador": "Page not found", "status_code": 404},
    "GitLab": {"url": "https://gitlab.com/{}", "indicador": "Page not found", "status_code": 404},
    "ReverbNation": {"url": "https://www.reverbnation.com/{}", "indicador": "Page not found", "status_code": 404},
}

USER_AGENTS: List[str] = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
]

def obtener_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://www.google.com/",
        "DNT": "1" if random.random() > 0.5 else "0"
    }

def extraer_info(respuesta):
    try:
        sopa = BeautifulSoup(respuesta.text, "html.parser")
        titulo = sopa.title.string.strip() if sopa.title else "No disponible"
        meta_desc = sopa.find("meta", {"name": "description"})
        descripcion = meta_desc["content"].strip() if meta_desc and meta_desc.get("content") else "Sin descripción"
        return titulo, descripcion
    except Exception:
        return "No disponible", "Sin descripción"

def buscar_usuario(plataforma, username):
    config = PLATAFORMAS[plataforma]
    url = config["url"].format(quote(username))
    try:
        respuesta = requests.get(url, headers=obtener_headers(), timeout=10, allow_redirects=False)
        existencia = (
            respuesta.status_code != config["status_code"] and
            config["indicador"] not in respuesta.text and
            not any(config["indicador"] in redireccion.text for redireccion in respuesta.history)
        )
        if existencia:
            titulo, descripcion = extraer_info(respuesta)
            return True, url, titulo, descripcion
    except RequestException:
        pass
    return False, url, "No disponible", "Sin información"

def mostrar_resultado(plataforma, encontrado, url, nombre, descripcion):
    estado = Text("Encontrado", style="bold green") if encontrado else Text("No encontrado", style="bold white")
    panel = Panel(
        Text.assemble(
            (f"Plataforma: {plataforma}\n", "bold white"),
            (f"Estado: ", "bold white"), estado, "\n",
            (f"URL: {url}\n", "bold white"),
            (f"Nombre: {nombre}\n", "bold white"),
            (f"Descripción: {descripcion}", "bold white")
        ),
        border_style="bold green" if encontrado else "bold white",
        title=f"Resultado en {plataforma}",
        title_align="left"
    )
    console.print(panel)

def guardar_resultados(username, resultados):
    with open(f"resultados_{username}.json", "w", encoding="utf-8") as archivo:
        json.dump(resultados, archivo, ensure_ascii=False, indent=4)
    console.print(f"[bold green]Resultados guardados en 'resultados_{username}.json'[/bold green]")

def mostrar_resumen(encontrados, no_encontrados):
    resumen = Panel(
        Text.assemble(
            (f"Resumen de búsqueda:\n", "bold white"),
            (f"Plataformas encontradas: {encontrados}\n", "bold green"),
            (f"Plataformas no encontradas: {no_encontrados}", "bold white")
        ),
        border_style="bold green",
        title="Resumen",
        title_align="left"
    )
    console.print(resumen)

def verificar_usuario(username):
    resultados = []
    encontrados = 0
    no_encontrados = 0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        task = progress.add_task("[bold white]Buscando en plataformas...", total=len(PLATAFORMAS))

        with ThreadPoolExecutor(max_workers=8) as executor:
            futuros = {executor.submit(buscar_usuario, plataforma, username): plataforma for plataforma in PLATAFORMAS}
            for futuro in as_completed(futuros):
                plataforma = futuros[futuro]
                try:
                    encontrado, url, nombre, bio = futuro.result()
                    resultados.append({
                        "plataforma": plataforma,
                        "encontrado": encontrado,
                        "url": url,
                        "nombre": nombre,
                        "descripcion": bio
                    })
                    mostrar_resultado(plataforma, encontrado, url, nombre, bio)
                    if encontrado:
                        encontrados += 1
                    else:
                        no_encontrados += 1
                except Exception as e:
                    console.print(f"[!] Error en {plataforma}: {str(e)}", style="bold white")
                finally:
                    progress.update(task, advance=1)

    if resultados:
        guardar_resultados(username, resultados)
        mostrar_resumen(encontrados, no_encontrados)

if __name__ == "__main__":
    usuario = console.input("[bold green]Introduce el nombre de usuario: [/bold green]")
    inicio = time()
    verificar_usuario(usuario.strip())
    console.print(f"[bold green]Tiempo total: {time() - inicio:.2f}s[/bold green]")