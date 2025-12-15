import random
import re
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import perf_counter
from urllib.parse import quote, urlparse
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.exceptions import RequestException
from urllib3.util.retry import Retry
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
from rich.text import Text
from rich.table import Table
from rich import box

class UserSearch:
    def __init__(self, username: str) -> None:
        self.username = username.strip()
        self.console = Console()
        self.session = self._get_session()
        self.platforms = self._get_platforms()
        self.results = []
        self.stats = {"found": 0, "not_found": 0, "errors": 0}

    def _get_session(self) -> requests.Session:
        session = requests.Session()
        retry = Retry(
            total=3,
            backoff_factor=0.8,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET"]
        )
        adapter = HTTPAdapter(max_retries=retry, pool_maxsize=100)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def _get_platforms(self) -> list[dict]:
        return [
            {"name": "Twitter", "url": "https://twitter.com/{}", "indicators": ["Esta cuenta no existe", "Cuenta suspendida"], "success_codes": [200], "parser": self._parse_generic},
            {"name": "Instagram", "url": "https://instagram.com/{}", "indicators": ["Lo sentimos", "página no está disponible"], "success_codes": [200], "parser": self._parse_instagram},
            {"name": "Facebook", "url": "https://www.facebook.com/{}", "indicators": ["Página no encontrada", "content not found"], "success_codes": [200], "parser": self._parse_facebook},
            {"name": "Pinterest", "url": "https://pinterest.com/{}", "indicators": ["Lo sentimos, esta página no está disponible"], "success_codes": [200, 404], "parser": self._parse_generic},
            {"name": "GitHub", "url": "https://github.com/{}", "indicators": ["Not found", "Page not found"], "success_codes": [200], "parser": self._parse_github},
            {"name": "Reddit", "url": "https://reddit.com/user/{}", "indicators": ["page not found", "doesn't exist"], "success_codes": [200], "parser": self._parse_reddit},
            {"name": "YouTube", "url": "https://youtube.com/@{}", "indicators": ["404", "not found"], "success_codes": [200], "parser": self._parse_youtube},
            {"name": "LinkedIn", "url": "https://linkedin.com/in/{}", "indicators": ["Page not found"], "success_codes": [200], "parser": self._parse_linkedin},
            {"name": "TikTok", "url": "https://tiktok.com/@{}", "indicators": ["Couldn't find this account"], "success_codes": [200], "parser": self._parse_tiktok},
            {"name": "Twitch", "url": "https://twitch.tv/{}", "indicators": ["Channel not found"], "success_codes": [200], "parser": self._parse_twitch},
            {"name": "Spotify", "url": "https://open.spotify.com/user/{}", "indicators": ["Page not found"], "success_codes": [200], "parser": self._parse_spotify},
            {"name": "Steam", "url": "https://steamcommunity.com/id/{}", "indicators": ["The specified profile could not be found"], "success_codes": [200], "parser": self._parse_steam},
            {"name": "Vimeo", "url": "https://vimeo.com/{}", "indicators": ["Sorry, we couldn't find that page"], "success_codes": [200], "parser": self._parse_vimeo},
            {"name": "Flickr", "url": "https://flickr.com/people/{}", "indicators": ["Page not found"], "success_codes": [200], "parser": self._parse_flickr},
            {"name": "SoundCloud", "url": "https://soundcloud.com/{}", "indicators": ["Page not found"], "success_codes": [200], "parser": self._parse_soundcloud},
            {"name": "Medium", "url": "https://medium.com/@{}", "indicators": ["404", "page not found"], "success_codes": [200], "parser": self._parse_medium},
            {"name": "DeviantArt", "url": "https://{}.deviantart.com", "indicators": ["Page not found"], "success_codes": [200], "parser": self._parse_deviantart},
            {"name": "Dribbble", "url": "https://dribbble.com/{}", "indicators": ["The page you were looking for doesn't exist"], "success_codes": [200], "parser": self._parse_dribbble},
            {"name": "Behance", "url": "https://behance.net/{}", "indicators": ["Page not found"], "success_codes": [200], "parser": self._parse_behance},
            {"name": "VK", "url": "https://vk.com/{}", "indicators": ["error", "page not found"], "success_codes": [200], "parser": self._parse_vk},
            {"name": "Telegram", "url": "https://t.me/{}", "indicators": ["doesn't exist"], "success_codes": [200], "parser": self._parse_telegram},
            {"name": "Quora", "url": "https://quora.com/profile/{}", "indicators": ["Page Not Found"], "success_codes": [200], "parser": self._parse_quora},
            {"name": "Tumblr", "url": "https://{}.tumblr.com", "indicators": ["nothing here"], "success_codes": [200], "parser": self._parse_tumblr},
            {"name": "Patreon", "url": "https://patreon.com/{}", "indicators": ["page not available"], "success_codes": [200], "parser": self._parse_patreon},
            {"name": "Last.fm", "url": "https://last.fm/user/{}", "indicators": ["Page not found"], "success_codes": [200], "parser": self._parse_lastfm}
        ]

    def _get_user_agent(self) -> str:
        agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
        ]
        return random.choice(agents)

    def _headers(self) -> dict:
        return {
            "User-Agent": self._get_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Referer": "https://www.google.com/",
            "DNT": "1" if random.random() > 0.5 else "0",
            "Upgrade-Insecure-Requests": "1"
        }

    def _parse_generic(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Sin título"
        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc["content"].strip() if meta_desc and meta_desc.get("content") else ""
        if not description:
            og_desc = soup.find("meta", property="og:description")
            if og_desc and og_desc.get("content"):
                description = og_desc["content"].strip()
            else:
                first_paragraph = soup.find("p")
                if first_paragraph:
                    description = first_paragraph.get_text().strip()[:200] + "..." if len(first_paragraph.get_text()) > 200 else first_paragraph.get_text().strip()
        return title, description

    def _parse_instagram(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Instagram"
        meta_desc = soup.find("meta", property="og:description")
        description = meta_desc["content"].strip() if meta_desc and meta_desc.get("content") else ""
        return title, description

    def _parse_facebook(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Facebook"
        profile_name = soup.select_one("span[class*='fullname']")
        if profile_name:
            title = profile_name.get_text().strip()
        description = ""
        about_section = soup.select_one("div[data-testid='profile_sheet_about']")
        if about_section:
            description = about_section.get_text().strip()[:300] + "..." if len(about_section.get_text()) > 300 else about_section.get_text().strip()
        return title, description

    def _parse_github(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "GitHub"
        real_name = soup.select_one("span[itemprop='name']")
        if real_name:
            title = real_name.get_text().strip()
        bio = soup.select_one("div[class*='user-profile-bio']")
        description = bio.get_text().strip() if bio else ""
        return title, description

    def _parse_reddit(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Reddit"
        karma_element = soup.select_one("span[id='profile--id-card--highlight-tooltip--karma']")
        if karma_element:
            title += f" | Karma: {karma_element.get_text().strip()}"
        description_element = soup.select_one("div[class*='usertext-body']")
        description = description_element.get_text().strip() if description_element else ""
        return title, description

    def _parse_youtube(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "YouTube"
        subscribers = soup.select_one("yt-formatted-string[id='subscriber-count']")
        if subscribers:
            title += f" | {subscribers.get_text().strip()}"
        description_element = soup.select_one("yt-formatted-string[id='description']")
        description = description_element.get_text().strip() if description_element else ""
        return title, description

    def _parse_linkedin(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "LinkedIn"
        position = soup.select_one("div[class*='text-body-medium']")
        if position:
            title = position.get_text().strip()
        location = soup.select_one("span[class*='text-body-small']")
        description = location.get_text().strip() if location else ""
        return title, description

    def _parse_tiktok(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "TikTok"
        stats = soup.select("strong[class*='count-infos']")
        description = ""
        if stats and len(stats) >= 3:
            followers = stats[0].get_text().strip()
            following = stats[1].get_text().strip()
            likes = stats[2].get_text().strip()
            description = f"Followers: {followers} | Following: {following} | Likes: {likes}"
        return title, description

    def _parse_twitch(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Twitch"
        followers = soup.select_one("p[data-a-target='followers-count']")
        if followers:
            title += f" | Followers: {followers.get_text().strip()}"
        description_element = soup.select_one("div[data-a-target='user-profile-bio']")
        description = description_element.get_text().strip() if description_element else ""
        return title, description

    def _parse_spotify(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Spotify"
        meta_desc = soup.find("meta", property="og:description")
        description = meta_desc["content"].strip() if meta_desc and meta_desc.get("content") else ""
        return title, description

    def _parse_steam(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Steam"
        real_name = soup.select_one(".actual_persona_name")
        if real_name:
            title = real_name.get_text().strip()
        description_element = soup.select_one(".profile_summary")
        description = description_element.get_text().strip() if description_element else ""
        return title, description

    def _parse_vimeo(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Vimeo"
        stats = soup.select(".js-stats_count")
        if stats and len(stats) >= 3:
            videos = stats[0].get_text().strip()
            followers = stats[1].get_text().strip()
            following = stats[2].get_text().strip()
            description = f"Videos: {videos} | Followers: {followers} | Following: {following}"
        else:
            description = ""
        return title, description

    def _parse_flickr(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Flickr"
        real_name = soup.select_one(".title-name")
        if real_name:
            title = real_name.get_text().strip()
        description_element = soup.select_one(".description")
        description = description_element.get_text().strip() if description_element else ""
        return title, description

    def _parse_soundcloud(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "SoundCloud"
        stats = soup.select(".sc-visuallyhidden")
        description = ""
        for stat in stats:
            text = stat.get_text().strip()
            if "Followers" in text or "Following" in text:
                description += text + " "
        return title, description.strip()

    def _parse_medium(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Medium"
        bio = soup.select_one(".bio")
        description = bio.get_text().strip() if bio else ""
        return title, description

    def _parse_deviantart(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "DeviantArt"
        stats = soup.select(".deviation-count")
        description = ""
        if stats and len(stats) > 0:
            for stat in stats:
                description += stat.get_text().strip() + " "
        return title, description.strip()

    def _parse_dribbble(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Dribbble"
        location = soup.select_one(".location")
        description = location.get_text().strip() if location else ""
        return title, description

    def _parse_behance(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Behance"
        stats = soup.select(".ProfileInfo-statValue")
        description = ""
        if stats and len(stats) >= 3:
            projects = stats[0].get_text().strip()
            followers = stats[1].get_text().strip()
            following = stats[2].get_text().strip()
            description = f"Projects: {projects} | Followers: {followers} | Following: {following}"
        return title, description

    def _parse_vk(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "VK"
        info = soup.select(".pp_info")
        description = info[0].get_text().strip() if info else ""
        return title, description

    def _parse_telegram(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Telegram"
        description_element = soup.select_one(".tgme_page_description")
        description = description_element.get_text().strip() if description_element else ""
        return title, description

    def _parse_quora(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Quora"
        credentials = soup.select_one(".CredentialListItem")
        description = credentials.get_text().strip() if credentials else ""
        return title, description

    def _parse_tumblr(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Tumblr"
        description_element = soup.select_one(".description")
        description = description_element.get_text().strip() if description_element else ""
        return title, description

    def _parse_patreon(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Patreon"
        creator_info = soup.select_one(".creator-info")
        description = creator_info.get_text().strip() if creator_info else ""
        return title, description

    def _parse_lastfm(self, soup: BeautifulSoup, response: requests.Response) -> tuple[str, str]:
        title = soup.title.string.strip() if soup.title else "Last.fm"
        stats = soup.select(".header-metadata-item")
        description = ""
        if stats:
            for stat in stats:
                description += stat.get_text().strip() + " "
        return title, description.strip()

    def _check_platform(self, platform: dict) -> dict:
        try:
            url = platform["url"].format(quote(self.username))
            response = self.session.get(
                url,
                headers=self._headers(),
                timeout=12,
                allow_redirects=True,
                stream=False
            )
            
            account_exists = True
            if response.status_code not in platform["success_codes"]:
                account_exists = False
            else:
                for indicator in platform["indicators"]:
                    if indicator.lower() in response.text.lower():
                        account_exists = False
                        break
            
            title, description = "Sin título", "Sin descripción"
            if account_exists:
                soup = BeautifulSoup(response.text, "html.parser")
                title, description = platform["parser"](soup, response)
            
            return {
                "platform": platform["name"],
                "found": account_exists,
                "url": url,
                "title": title,
                "description": description,
                "status": "success"
            }
            
        except RequestException as e:
            return {
                "platform": platform["name"],
                "found": False,
                "url": platform["url"].format(quote(self.username)),
                "title": "Error de conexión",
                "description": str(e),
                "status": "error"
            }
        except Exception as e:
            return {
                "platform": platform["name"],
                "found": False,
                "url": platform["url"].format(quote(self.username)),
                "title": "Error inesperado",
                "description": str(e),
                "status": "error"
            }

    def _display_result(self, result: dict) -> None:
        if result["status"] == "error":
            self.console.print(
                Panel(
                    f"[bold red]Plataforma: {result['platform']}[/bold red]\n"
                    f"[bold yellow]URL: {result['url']}[/bold yellow]\n"
                    f"[white]Error: {result['description']}[/white]",
                    border_style="bold red",
                    title=f"[red]Error en {result['platform']}[/red]"
                )
            )
            return
        
        status_text = "[bold green]ENCONTRADO[/bold green]" if result["found"] else "[bold red]NO ENCONTRADO[/bold red]"
        title_color = "bold green" if result["found"] else "bold yellow"
        
        self.console.print(
            Panel(
                f"[bold white]Plataforma: {result['platform']}[/bold white]\n"
                f"[white]Estado: {status_text}[/white]\n"
                f"[bold cyan]URL: {result['url']}[/bold cyan]\n"
                f"[{title_color}]Título: {result['title']}[/{title_color}]\n"
                f"[white]Descripción:\n{result['description']}[/white]",
                border_style="bold green" if result["found"] else "bold red",
                title=f"Resultado en {result['platform']}"
            )
        )

    def _display_summary(self, total_time: float) -> None:
        summary = Panel(
            f"[bold white]RESUMEN DE BÚSQUEDA[/bold white]\n\n"
            f"[bold green]✓ Plataformas encontradas:[/bold green] {self.stats['found']}\n"
            f"[bold red]✗ Plataformas no encontradas:[/bold red] {self.stats['not_found']}\n"
            f"[bold yellow]⚠ Errores:[/bold yellow] {self.stats['errors']}\n\n"
            f"[bold cyan]⏱ Tiempo total: {total_time:.2f} segundos[/bold cyan]\n"
            f"[bold magenta]🔍 Usuario buscado:[/bold magenta] {self.username}",
            border_style="bold green",
            title="[bold green]RESUMEN FINAL[/bold green]"
        )
        self.console.print(summary, justify="center")
        
        table = Table(
            title="Resultados por Plataforma",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta"
        )
        table.add_column("Plataforma", style="cyan", width=20)
        table.add_column("Estado", justify="center")
        table.add_column("URL", style="yellow")
        
        for result in self.results:
            status = "[green]ENCONTRADO[/green]" if result["found"] else (
                "[red]NO ENCONTRADO[/red]" if result["status"] == "success" else "[yellow]ERROR[/yellow]"
            )
            table.add_row(
                result["platform"],
                status,
                result["url"]
            )
        
        self.console.print(table)

    def run(self) -> None:
        start_time = perf_counter()
        
        with Progress(
            SpinnerColumn(),
            *Progress.get_default_columns(),
            TimeElapsedColumn(),
            console=self.console,
            transient=True,
        ) as progress:
            task = progress.add_task("[cyan]Buscando usuario...", total=len(self.platforms))
            
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = [executor.submit(self._check_platform, platform) for platform in self.platforms]
                
                for future in as_completed(futures):
                    result = future.result()
                    self.results.append(result)
                    
                    if result["status"] == "error":
                        self.stats["errors"] += 1
                    elif result["found"]:
                        self.stats["found"] += 1
                    else:
                        self.stats["not_found"] += 1
                    
                    progress.update(task, advance=1)
                    self._display_result(result)
        
        total_time = perf_counter() - start_time
        self._display_summary(total_time)

if __name__ == "__main__":
    console = Console()
    console.print(
        Panel(
            "[bold green]BUSCADOR DE USUARIOS MULTIPLATAFORMA[/bold green]\n\n"
            "[bold white]Ingrese un nombre de usuario para buscar en diferentes plataformas[/bold white]",
            border_style="bold blue"
        )
    )
    
    user_input = console.input("[bold green]>> Introduce el nombre de usuario: [/bold green]")
    console.print()
    
    if user_input.strip():
        UserSearch(user_input).run()
    else:
        console.print("[bold red]Error: Debes ingresar un nombre de usuario válido[/bold red]")