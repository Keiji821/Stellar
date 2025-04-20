import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box
import re
import time
import random

console = Console()
timeout_duration = 20

def entrada_richeada(texto):
    return Prompt.ask(f"[bold green]{texto}[/]")

def realizar_solicitud(url, headers, max_reintentos=3):
    for intento in range(max_reintentos):
        try:
            time.sleep(random.uniform(1, 3))
            res = requests.get(url, headers=headers, timeout=timeout_duration)
            return res
        except requests.RequestException as e:
            if intento < max_reintentos - 1:
                time.sleep(2)
            else:
                raise e

def verificar_enlace(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = realizar_solicitud(url, headers)
        return res.status_code == 200
    except requests.RequestException:
        return False

def requiere_captcha(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = realizar_solicitud(url, headers)
        soup = BeautifulSoup(res.text, "html.parser")
        return bool(soup.find("iframe", {"src": re.compile(r"recaptcha|hcaptcha")}))
    except requests.RequestException:
        return False

def buscar_en_sitio(nombre_sitio, url, selector_servidores, selector_nombre, selector_enlace, max_resultados=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resultados = []
    try:
        res = realizar_solicitud(url, headers)
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
        console.print(Panel(f"[red]Error en {nombre_sitio}:[/] {str(e)}", box=box.ROUNDED))
    return resultados

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
        try:
            resultados = buscar_en_sitio(nombre, url, selector_servidores, selector_nombre, selector_enlace, max_resultados)
            enlaces.extend(resultados)
        except Exception as e:
            console.print(Panel(f"[red]Error en {nombre}:[/] {str(e)}", box=box.ROUNDED))

    if enlaces:
        console.print(Panel(f"[green]Se encontraron {len(enlaces)} resultados.[/]", box=box.ROUNDED))
    else:
        console.print(Panel("[red]No se encontraron servidores que coincidan con tu búsqueda.[/]", box=box.ROUNDED))

if __name__ == "__main__":
    main()
