import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.progress import track
from rich import box
from fake_useragent import UserAgent
import re
import time
import random
import concurrent.futures
import urllib.parse

console = Console()
timeout_duration = 30
ua = UserAgent()

def obtener_agente_aleatorio():
    return ua.random

def realizar_solicitud(url, max_reintentos=3):
    headers = {"User-Agent": obtener_agente_aleatorio()}
    for intento in range(max_reintentos):
        try:
            time.sleep(random.uniform(1.2, 3.8))
            res = requests.get(url, headers=headers, timeout=timeout_duration)
            res.raise_for_status()
            return res
        except (requests.RequestException, requests.Timeout) as e:
            if intento < max_reintentos - 1:
                time.sleep(2)
            else:
                return None
    return None

def verificar_enlace(url):
    return realizar_solicitud(url) is not None

def requiere_captcha(res):
    if not res:
        return False
    try:
        return bool(re.search(r"recaptcha|hcaptcha", res.text, re.IGNORECASE))
    except Exception:
        return False

def buscar_en_sitio(nombre_sitio, config, max_resultados=12):
    url, selector_servidores, selector_nombre, selector_enlace = config
    resultados = []
    try:
        res = realizar_solicitud(url)
        if not res:
            return resultados
            
        if requiere_captcha(res):
            return resultados
            
        soup = BeautifulSoup(res.text, "html.parser")
        servidores = soup.select(selector_servidores)[:max_resultados]

        for servidor in servidores:
            try:
                nombre = servidor.select_one(selector_nombre)
                enlace = servidor.select_one(selector_enlace)
                
                if not (nombre and enlace):
                    continue
                    
                nombre_texto = nombre.text.strip()
                href = enlace.get("href")
                
                if not href:
                    continue
                    
                url_servidor = urllib.parse.urljoin(url, href)
                resultados.append((nombre_texto, url_servidor))
            except Exception:
                continue
    except Exception:
        pass
    return resultados

def procesar_sitio(sitio):
    nombre, config = sitio
    resultados = buscar_en_sitio(nombre, config)
    return nombre, resultados

def main():
    console.print(Panel("[bold green]BUSCADOR AVANZADO DE SERVIDORES DISCORD[/]", box=box.DOUBLE))
    query = Prompt.ask("[bold green]Introduce el nombre del servidor o tema de interés[/]").strip()
    
    if not query:
        console.print("[red]Error: Término de búsqueda vacío[/]")
        return
        
    query_codificada = urllib.parse.quote(query)
    sitios = {
        "DiscordServers.com": (
            f"https://discordservers.com/search/{query_codificada}",
            "a.card", "h3", "a"
        ),
        "Discord.me": (
            f"https://discord.me/servers/tag/{query_codificada}",
            "div.server-listing", "h4", "a"
        ),
        "Discord.st": (
            f"https://discord.st/servers/search?q={query_codificada}",
            "div.server", "h3", "a"
        ),
        "DiscordHub.com": (
            f"https://discordhub.com/servers/search?q={query_codificada}",
            "div.server", "h3", "a"
        ),
        "DiscordList.gg": (
            f"https://discordlist.gg/search?q={query_codificada}",
            "div.server-card", "h3", "a"
        ),
        "DiscordHome.com": (
            f"https://discordhome.com/servers/search?q={query_codificada}",
            "div.server", "h3", "a"
        ),
        "DiscordServers.me": (
            f"https://discordservers.me/search?q={query_codificada}",
            "div.server-card", "h3", "a"
        ),
        "DiscordAdvertise.xyz": (
            f"https://discordadvertise.xyz/search?q={query_codificada}",
            "div.server", "h3", "a"
        ),
        "DiscordStreet.com": (
            f"https://discordstreet.com/search?q={query_codificada}",
            "div.server-card", "h3", "a"
        )
    }

    enlaces = []
    total_encontrados = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(procesar_sitio, item) for item in sitios.items()]
        
        for future in track(concurrent.futures.as_completed(futures), 
                          total=len(sitios), 
                          description="[bold cyan]Analizando plataformas..."):
            nombre_sitio, resultados = future.result()
            if resultados:
                total_encontrados += len(resultados)
                enlaces.extend(resultados)
                console.print(f"[green]✓ {nombre_sitio}:[/] {len(resultados)} servidores")
            else:
                console.print(f"[yellow]✗ {nombre_sitio}:[/] Sin resultados")

    if enlaces:
        tabla = Table(
            title=f"[bold green]Resultados para: {query}[/]", 
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta"
        )
        tabla.add_column("Servidor", style="bold cyan", width=32)
        tabla.add_column("Enlace", style="bold blue")
        
        for nombre, url in sorted(enlaces, key=lambda x: x[0].lower())[:25]:
            tabla.add_row(nombre, url)
            
        console.print(Panel.fit(
            f"[bold green]Total encontrados:[/] {total_encontrados} servidores en {len(sitios)} plataformas",
            title="Éxito",
            border_style="green",
            box=box.DOUBLE
        ))
        console.print(tabla)
    else:
        console.print(Panel(
            "[bold red]No se encontraron servidores que coincidan con tu búsqueda[/]",
            title="Resultados",
            border_style="red",
            box=box.DOUBLE
        ))
    
    console.print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Búsqueda cancelada[/]")
        console.print()
    except Exception:
        console.print(Panel("[bold red]Error crítico durante la ejecución[/]", box=box.DOUBLE))
        console.print()