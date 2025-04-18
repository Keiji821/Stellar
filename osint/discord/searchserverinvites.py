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
        if res.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

def requiere_captcha(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        # Buscar elementos típicos de CAPTCHA
        if soup.find("iframe", {"src": re.compile(r"recaptcha|hcaptcha")}):
            return True
        return False
    except requests.RequestException:
        return False


def buscar_discordservers(query, max_resultados=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []
    try:
        url = f"https://discordservers.com/search/{query}"
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        servidores = soup.select("a.card")

        for servidor in servidores:
            nombre = servidor.select_one("h3")
            enlace = servidor.get("href")
            if nombre and enlace:
                nombre_texto = nombre.text.strip()
                url_servidor = f"https://discordservers.com{enlace}"
                if verificar_enlace(url_servidor) and not requiere_captcha(url_servidor):
                    resultados.append((nombre_texto, url_servidor))
            if len(resultados) >= max_resultados:
                break
        return resultados
    except Exception as e:
        console.print(Panel(f"[red]Error en DiscordServers.com:[/] {e}", box=box.ROUNDED))
        return []

def buscar_discordme(query, max_resultados=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []
    try:
        url = f"https://discord.me/servers/tag/{query}"
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        servidores = soup.select("div.server-listing")

        for servidor in servidores:
            nombre = servidor.select_one("h4")
            enlace = servidor.select_one("a")
            if nombre and enlace:
                nombre_texto = nombre.text.strip()
                href = enlace.get("href")
                if href:
                    url_servidor = f"https://discord.me{href}"
                    if verificar_enlace(url_servidor) and not requiere_captcha(url_servidor):
                        resultados.append((nombre_texto, url_servidor))
            if len(resultados) >= max_resultados:
                break
        return resultados
    except Exception as e:
        console.print(Panel(f"[red]Error en Discord.me:[/] {e}", box=box.ROUNDED))
        return []

def buscar_findadiscord(query, max_resultados=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []
    try:
        url = f"https://findadiscord.com/search/?term={query}"
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        tarjetas = soup.select("div.card")  # Ajusta este selector según la estructura real

        for tarjeta in tarjetas:
            nombre = tarjeta.select_one("h5.card-title")
            enlace = tarjeta.select_one("a")
            if nombre and enlace:
                nombre_txt = nombre.text.strip()
                href = enlace.get("href")
                full_url = f"https://findadiscord.com{href}"
                if verificar_enlace(full_url) and not requiere_captcha(full_url):
                    resultados.append((nombre_txt, full_url))
            if len(resultados) >= max_resultados:
                break
        return resultados
    except Exception as e:
        console.print(Panel(f"[red]Error en FindADiscord:[/] {e}", box=box.ROUNDED))
        return []

def buscar_discord_st(query, max_resultados=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []
    try:
        url = f"https://discord.st/servers/search?q={query}"
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        servidores = soup.select("div.server")  # Ajusta este selector según la estructura real

        for servidor in servidores:
            nombre = servidor.select_one("h3")
            enlace = servidor.select_one("a")
            if nombre and enlace:
                nombre_texto = nombre.text.strip()
                href = enlace.get("href")
                if href:
                    url_servidor = f"https://discord.st{href}"
                    if verificar_enlace(url_servidor) and not requiere_captcha(url_servidor):
                        resultados.append((nombre_texto, url_servidor))
            if len(resultados) >= max_resultados:
                break
        return resultados
    except Exception as e:
        console.print(Panel(f"[red]Error en Discord.st:[/] {e}", box=box.ROUNDED))
        return []

def buscar_discordhub(query, max_resultados=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []
    try:
        url = f"https://discordhub.com/servers/search?q={query}"
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        servidores = soup.select("div.server")  # Ajusta este selector según la estructura real

        for servidor in servidores:
            nombre = servidor.select_one("h3")
            enlace = servidor.select_one("a")
            if nombre and enlace:
                nombre_texto = nombre.text.strip()
                href = enlace.get("href")
                if href:
                    url_servidor = f"https://discordhub.com{href}"
                    if verificar_enlace(url_servidor) and not requiere_captcha(url_servidor):
                        resultados.append((nombre_texto, url_servidor))
            if len(resultados) >= max_resultados:
                break
        return resultados
    except Exception as e:
        console.print(Panel(f"[red]Error en DiscordHub.com:[/] {e}", box=box.ROUNDED))
        return []

def buscar_discordlist_gg(query, max_resultados=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []
    try:
        url = f"https://discordlist.gg/search?q={query}"
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        servidores = soup.select("div.server-card")  # Ajusta este selector según la estructura real

        for servidor in servidores:
            nombre = servidor.select_one("h3")
            enlace = servidor.select_one("a")
            if nombre and enlace:
                nombre_texto = nombre.text.strip()
                href = enlace.get("href")
                if href:
                    url_servidor = f"https://discordlist.gg{href}"
                    if verificar_enlace(url_servidor) and not requiere_captcha(url_servidor):
                        resultados.append((nombre_texto, url_servidor))
            if len(resultados) >= max_resultados:
                break
        return resultados
    except Exception as e:
        console.print(Panel(f"[red]Error en DiscordList.gg:[/] {e}", box=box.ROUNDED))
        return []

def buscar_discordhome(query, max_resultados=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []
    try:
        url = f"https://discordhome.com/servers/search?q={query}"
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        servidores = soup.select("div.server")


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
    console.print(Panel("[bold magenta]Buscador de servidores de Discord[/]", box=box.ROUNDED))
    query = entrada_richeada("Introduce el nombre del servidor o tema de interés")
    max_resultados = 10

    enlaces = []
    enlaces.extend(buscar_discordservers(query, max_resultados))
    enlaces.extend(buscar_discordme(query, max_resultados))

    if enlaces:
        mostrar_links_crudos([url for _, url in enlaces])
        mostrar_tabla("Resultados encontrados", enlaces)
    else:
        console.print(Panel("[red]No se encontraron servidores que coincidan con tu búsqueda.[/]", box=box.ROUNDED))


if __name__ == "__main__":
    main()