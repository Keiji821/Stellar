import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box
import re

console = Console()

def entrada_richeada(texto):
    return Prompt.ask(f"[bold green]{texto}[/]")

def verificar_enlace(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        return res.status_code == 200
    except requests.RequestException:
        return False

def requiere_captcha(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        return bool(soup.find("iframe", {"src": re.compile(r"recaptcha|hcaptcha")}))
    except requests.RequestException:
        return False

def buscar_en_sitio(nombre_sitio, url, selector_servidores, selector_nombre, selector_enlace, max_resultados=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        servidores = soup.select(selector_servidores)

        for servidor in servidores:
            nombre = servidor.select_one(selector_nombre)
            enlace = servidor.select_one(selector_enlace)
            if nombre and enlace:
                nombre_texto = nombre.text.strip()
                href = enlace.get("href")
                if href:
                    url_servidor = f"{url.split('/')[0]}//{url.split('/')[2]}{href}"
                    if verificar_enlace(url_servidor) and not requiere_captcha(url_servidor):
                        resultados.append((nombre_texto, url_servidor))
            if len(resultados) >= max_resultados:
                break
    except Exception as e:
        console.print(Panel(f"[red]Error en {nombre_sitio}:[/] {e}", box=box.ROUNDED))
    return resultados

def mostrar_tabla(titulo, datos):
    if not datos:
        console.print(Panel(f"[red]No se encontraron resultados en {titulo}[/]", box=box.ROUNDED))
        return

    tabla = Table(title=titulo, box=box.ROUNDED, title_style="bold magenta")
    tabla.add_column("Nombre", style="cyan", no_wrap=True)
    tabla.add_column("Enlace", style="green")

    for nombre, url in datos:
        tabla.add_row(nombre, url)

    console.print(tabla)

def mostrar_links_crudos(enlaces):
    if not enlaces:
        console.print(Panel("[red]No se encontraron enlaces en buscadores[/]", box=box.ROUNDED))
        return

    panel = Panel.fit("\n".join(f"[green]{link}[/]" for link in enlaces),
                      title="Enlaces crudos encontrados",
                      title_align="left", box=box.ROUNDED)
    console.print(panel)

def main():
    query = entrada_richeada("Introduce el nombre del servidor o tema de interés")
    max_resultados = 10

    sitios = {
        "DiscordServers.com": (
            f"https://discordservers.com/search/{query}",
            "a.card", "h3", "a"
        ),
        "Discord.me": (
            f"https://discord.me/servers/tag/{query}",
            "div.server-listing", "h4", "a"
        ),
        "Discord.st": (
            f"https://discord.st/servers/search?q={query}",
            "div.server", "h3", "a"
        ),
        "DiscordHub.com": (
            f"https://discordhub.com/servers/search?q={query}",
            "div.server", "h3", "a"
        ),
        "DiscordList.gg": (
            f"https://discordlist.gg/search?q={query}",
            "div.server-card", "h3", "a"
        ),
        "DiscordHome.com": (
            f"https://discordhome.com/servers/search?q={query}",
            "div.server", "h3", "a"
        )
    }

    enlaces = []
    for nombre, (url, selector_servidores, selector_nombre, selector_enlace) in sitios.items():
        resultados = buscar_en_sitio(nombre, url, selector_servidores, selector_nombre, selector_enlace, max_resultados)
        enlaces.extend(resultados)

    if enlaces:
        mostrar_links_crudos([url for _, url in enlaces])
        mostrar_tabla("Resultados encontrados", enlaces)
    else:
        console.print(Panel("[red]No se encontraron servidores que coincidan con tu búsqueda.[/]", box=box.ROUNDED))

if __name__ == "__main__":
    main()