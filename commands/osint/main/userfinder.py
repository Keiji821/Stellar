import random
import requests
from time import time
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from typing import Tuple, Dict, List
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

class UserSearch:
    def __init__(self, username: str) -> None:
        self.username = username.strip()
        self.console = Console()
        self.session = self._get_session()
        self.platforms = self._get_platforms()
        self.user_agents = self._get_user_agents()

    def _get_session(self) -> requests.Session:
        session = requests.Session()
        retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def _get_platforms(self) -> Dict[str, Dict[str, str]]:
        return {
            "Twitter": {"url": "https://twitter.com/{}", "indicator": "This account doesn’t exist", "status_code": "404"},
            "Instagram": {"url": "https://instagram.com/{}", "indicator": "La página no está disponible", "status_code": "200"},
            "Facebook": {"url": "https://www.facebook.com/{}", "indicator": "Página no encontrada", "status_code": "200"},
            "Pinterest": {"url": "https://pinterest.com/{}", "indicator": "Lo sentimos, esta página no está disponible", "status_code": "404"},
            # Add more platforms here as needed...
        }

    def _get_user_agents(self) -> List[str]:
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            # Add more user agents here as needed...
        ]

    def _headers(self) -> Dict[str, str]:
        return {
            "User-Agent": random.choice(self.user_agents),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "es-ES,es;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://www.google.com/",
            "DNT": "1" if random.random() > 0.5 else "0"
        }

    def _extract_info(self, resp: requests.Response) -> Tuple[str, str]:
        try:
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.title.string.strip() if soup.title and soup.title.string else "No disponible"
            meta_desc = soup.find("meta", {"name": "description"})
            desc = meta_desc["content"].strip() if meta_desc and meta_desc.get("content") else ""
            return title, desc
        except Exception:
            return "No disponible", "Sin descripción"

    def _check_platform(self, platform: str) -> Tuple[bool, str, str, str]:
        config = self.platforms[platform]
        url = config["url"].format(quote(self.username))
        try:
            resp = self.session.get(url, headers=self._headers(), timeout=10, allow_redirects=True)
            if str(resp.status_code) != config["status_code"] and config["indicator"] not in resp.text:
                title, info = self._extract_info(resp)
                return True, url, title, info
        except Exception:
            pass
        return False, url, "No disponible", "Sin información"

    def _display_result(self, platform: str, found: bool, url: str, title: str, info: str) -> None:
        status_text = Text("Encontrado", style="bold green") if found else Text("No encontrado", style="bold red")
        panel = Panel(
            Text.assemble(
                (f"Plataforma: {platform}\n", "bold white"),
                ("Estado: ", "bold white"), status_text, "\n",
                (f"URL: {url}\n", "bold white"),
                (f"Nombre: {title}\n", "bold white"),
                (f"Información:\n{info}", "bold white")
            ),
            border_style="bold green" if found else "bold red",
            title=f"Resultado en {platform}",
            title_align="left"
        )
        self.console.print(panel)

    def _display_summary(self, found: int, not_found: int, total_time: float) -> None:
        summary = Panel(
            Text.assemble(
                ("Resumen de búsqueda:\n", "bold white"),
                (f"Plataformas encontradas: {found}\n", "bold green"),
                (f"Plataformas no encontradas: {not_found}\n", "bold red"),
                (f"Tiempo total: {total_time:.2f}s", "bold cyan")
            ),
            border_style="bold green",
            title="Resumen",
            title_align="left"
        )
        self.console.print(summary)

    def run(self) -> None:
        start = time()
        total_found, total_not_found = 0, 0
        with ThreadPoolExecutor(max_workers=12) as executor:
            futures = {executor.submit(self._check_platform, platform): platform for platform in self.platforms}
            for future in as_completed(futures):
                platform = futures[future]
                try:
                    found, url, title, info = future.result()
                    self._display_result(platform, found, url, title, info)
                    total_found += 1 if found else 0
                    total_not_found += 0 if found else 1
                except Exception as e:
                    self.console.print(f"[!] Error en {platform}: {e}", style="bold red")
        total_time = time() - start
        self._display_summary(total_found, total_not_found, total_time)

if __name__ == "__main__":
    user_input = Console().input("[bold green]Introduce el nombre de usuario o real: [/bold green]")
    Console().print()
    UserSearch(user_input).run()
