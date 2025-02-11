import requests
from time import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from bs4 import BeautifulSoup
import random
from typing import Dict, Tuple, List
from requests.exceptions import RequestException
from urllib.parse import quote

console = Console()

PLATAFORMAS: Dict[str, Dict[str, str]] = {
    "Twitter": {
        "url": "https://twitter.com/{}",
        "indicador": "This account doesn’t exist",
        "status_code": 404
    },
    "Instagram": {
        "url": "https://instagram.com/{}",
        "indicador": "La página no está disponible",
        "status_code": 200
    },
    "Facebook": {
        "url": "https://www.facebook.com/{}",
        "indicador": "Página no encontrada",
        "status_code": 200
    },
    "Pinterest": {
        "url": "https://pinterest.com/{}",
        "indicador": "Lo sentimos, esta página no está disponible",
        "status_code": 404
    },
    "YouTube": {
        "url": "https://www.youtube.com/@{}",
        "indicador": "Este canal no está disponible",
        "status_code": 200
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "indicador": "Couldn't find this account",
        "status_code": 200
    }
}

USER_AGENTS: List[str] = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
]

def obtener_headers() -> Dict[str, str]:
    """Genera headers aleatorios para las solicitudes HTTP"""
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": "https://www.google.com/",
        "DNT": "1" if random.random() > 0.5 else "0"
    }

def extraer_info(respuesta: requests.Response) -> Tuple[str, str]:
    """Extrae metadatos de la página web"""
    try:
        sopa = BeautifulSoup(respuesta.text, "html.parser")
        titulo = sopa.title.string.strip() if sopa.title else "No disponible"
        meta_desc = sopa.find("meta", {"name": "description"})
        descripcion = meta_desc["content"].strip() if meta_desc and meta_desc.get("content") else "Sin descripción"
        return titulo, descripcion
    except Exception as e:
        return "No disponible", "Sin descripción"

def buscar_usuario(plataforma: str, username: str) -> Tuple[bool, str, str, str]:
    """Verifica la existencia de un usuario en una plataforma específica"""
    config = PLATAFORMAS[plataforma]
    url = config["url"].format(quote(username))
    
    try:
        respuesta = requests.get(
            url,
            headers=obtener_headers(),
            timeout=10,
            allow_redirects=False
        )
        
        existencia = (
            respuesta.status_code != config["status_code"] and
            config["indicador"] not in respuesta.text and
            not any(config["indicador"] in redireccion.text for redireccion in respuesta.history)
        )
        
        if existencia:
            titulo, descripcion = extraer_info(respuesta)
            return True, url, titulo, descripcion
            
    except RequestException as e:
        pass
        
    return False, url, "No disponible", "Sin información"

def crear_tabla() -> Table:
    """Crea la estructura de la tabla para resultados"""
    tabla = Table(title="Resultados de Búsqueda", show_header=True, header_style="bold blue")
    tabla.add_column("Plataforma", justify="left")
    tabla.add_column("Estado", justify="center")
    tabla.add_column("URL", justify="left", max_width=30)
    tabla.add_column("Nombre", justify="left", max_width=20)
    tabla.add_column("Descripción", justify="left", max_width=40)
    return tabla

def procesar_resultados(futuros: dict, progreso: Progress, tarea: int) -> Table:
    """Procesa los resultados de las solicitudes concurrentes"""
    tabla = crear_tabla()
    
    for futuro in as_completed(futuros):
        plataforma = futuros[futuro]
        try:
            encontrado, url, nombre, bio = futuro.result()
            estado = "[green]Encontrado[/green]" if encontrado else "[red]No encontrado[/red]"
            tabla.add_row(
                plataforma,
                estado,
                f"[link={url}]{url}[/link]",
                nombre[:20] + "..." if len(nombre) > 20 else nombre,
                bio[:40] + "..." if len(bio) > 40 else bio
            )
        except Exception as e:
            tabla.add_row(plataforma, "[red]Error[/red]", "", "Error", str(e))
        finally:
            progreso.advance(tarea)
    
    return tabla

def verificar_usuario(username: str) -> None:
    """Coordina la verificación del usuario en todas las plataformas"""
    with Progress() as progreso:
        tarea = progreso.add_task("Buscando en redes sociales...", total=len(PLATAFORMAS))
        
        with ThreadPoolExecutor(max_workers=8) as executor:
            futuros = {executor.submit(buscar_usuario, plataforma, username): plataforma 
                      for plataforma in PLATAFORMAS}
            
            tabla = procesar_resultados(futuros, progreso, tarea)
    
    console.print(tabla)

if __name__ == "__main__":
    usuario = console.input("[bold green]Introduce el nombre de usuario: [/bold green]")
    inicio = time()
    verificar_usuario(usuario.strip())
    console.print(f"[bold yellow]Tiempo total: {time() - inicio:.2f}s[/bold yellow]")