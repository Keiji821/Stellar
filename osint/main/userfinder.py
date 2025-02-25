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
        self.username: str = username.strip()
        self.console: Console = Console()
        self.session: requests.Session = self._get_session()
        self.platforms: Dict[str, Dict[str, str]] = {
            "Twitter": {"url": "https://twitter.com/{}", "indicador": "This account doesn’t exist", "status_code": "404"},
            "Instagram": {"url": "https://instagram.com/{}", "indicador": "La página no está disponible", "status_code": "200"},
            "Facebook": {"url": "https://www.facebook.com/{}", "indicador": "Página no encontrada", "status_code": "200"},
            "Pinterest": {"url": "https://pinterest.com/{}", "indicador": "Lo sentimos, esta página no está disponible", "status_code": "404"},
            "YouTube": {"url": "https://www.youtube.com/@{}", "indicador": "Este canal no está disponible", "status_code": "200"},
            "TikTok": {"url": "https://www.tiktok.com/@{}", "indicador": "Couldn't find this account", "status_code": "200"},
            "Reddit": {"url": "https://www.reddit.com/user/{}", "indicador": "Sorry, nobody on Reddit goes by that name", "status_code": "404"},
            "GitHub": {"url": "https://github.com/{}", "indicador": "Not Found", "status_code": "404"},
            "LinkedIn": {"url": "https://www.linkedin.com/in/{}", "indicador": "This profile is not available", "status_code": "404"},
            "Twitch": {"url": "https://www.twitch.tv/{}", "indicador": "This channel is unavailable", "status_code": "404"},
            "Snapchat": {"url": "https://www.snapchat.com/add/{}", "indicador": "Sorry, we couldn't find that user", "status_code": "404"},
            "Spotify": {"url": "https://open.spotify.com/user/{}", "indicador": "Page not found", "status_code": "404"},
            "Steam": {"url": "https://steamcommunity.com/id/{}", "indicador": "The specified profile could not be found", "status_code": "404"},
            "Tumblr": {"url": "https://{}.tumblr.com", "indicador": "There's nothing here", "status_code": "404"},
            "Flickr": {"url": "https://www.flickr.com/people/{}", "indicador": "Page Not Found", "status_code": "404"},
            "Vimeo": {"url": "https://vimeo.com/{}", "indicador": "Sorry, we couldn’t find that page", "status_code": "404"},
            "SoundCloud": {"url": "https://soundcloud.com/{}", "indicador": "Oops! We can’t find that page", "status_code": "404"},
            "Medium": {"url": "https://medium.com/@{}", "indicador": "Page not found", "status_code": "404"},
            "DeviantArt": {"url": "https://{}.deviantart.com", "indicador": "Page Not Found", "status_code": "404"},
            "Quora": {"url": "https://www.quora.com/profile/{}", "indicador": "Oops! The page you were looking for doesn’t exist", "status_code": "404"},
            "Wikipedia": {"url": "https://en.wikipedia.org/wiki/User:{}", "indicador": "User does not exist", "status_code": "404"},
            "Patreon": {"url": "https://www.patreon.com/{}", "indicador": "This page is not available", "status_code": "404"},
            "Dribbble": {"url": "https://dribbble.com/{}", "indicador": "Page not found", "status_code": "404"},
            "Behance": {"url": "https://www.behance.net/{}", "indicador": "Page Not Found", "status_code": "404"},
            "Goodreads": {"url": "https://www.goodreads.com/{}", "indicador": "Page not found", "status_code": "404"},
            "Bandcamp": {"url": "https://bandcamp.com/{}", "indicador": "Page not found", "status_code": "404"},
            "CodePen": {"url": "https://codepen.io/{}", "indicador": "Page not found", "status_code": "404"},
            "HackerRank": {"url": "https://www.hackerrank.com/{}", "indicador": "Page not found", "status_code": "404"},
            "LeetCode": {"url": "https://leetcode.com/{}", "indicador": "Page not found", "status_code": "404"},
            "Kaggle": {"url": "https://www.kaggle.com/{}", "indicador": "Page not found", "status_code": "404"},
            "StackOverflow": {"url": "https://stackoverflow.com/users/{}", "indicador": "Page not found", "status_code": "404"},
            "Keybase": {"url": "https://keybase.io/{}", "indicador": "Page not found", "status_code": "404"},
            "Bitbucket": {"url": "https://bitbucket.org/{}", "indicador": "Page not found", "status_code": "404"},
            "GitLab": {"url": "https://gitlab.com/{}", "indicador": "Page not found", "status_code": "404"},
            "ReverbNation": {"url": "https://www.reverbnation.com/{}", "indicador": "Page not found", "status_code": "404"},
            "VK": {"url": "https://vk.com/{}", "indicador": "Page not found", "status_code": "404"},
            "Imgur": {"url": "https://imgur.com/user/{}", "indicador": "User not found", "status_code": "404"},
            "Foursquare": {"url": "https://foursquare.com/{}", "indicador": "Page not found", "status_code": "404"},
            "WordPress": {"url": "https://{}.wordpress.com", "indicador": "Not Found", "status_code": "404"},
            "Vero": {"url": "https://www.vero.com/{}", "indicador": "Not found", "status_code": "404"},
            "Badoo": {"url": "https://badoo.com/profile/{}", "indicador": "Profile not found", "status_code": "404"},
            "OkCupid": {"url": "https://www.okcupid.com/profile/{}", "indicador": "Profile not found", "status_code": "404"},
            "Weibo": {"url": "https://weibo.com/{}", "indicador": "Page not found", "status_code": "404"},
            "Blogger": {"url": "https://{}.blogspot.com", "indicador": "404", "status_code": "404"},
            "Xing": {"url": "https://www.xing.com/profile/{}", "indicador": "Page not found", "status_code": "404"},
            "Redbubble": {"url": "https://www.redbubble.com/people/{}", "indicador": "Sorry, this page isn’t available", "status_code": "404"},
            "StackExchange": {"url": "https://stackexchange.com/users/{}", "indicador": "Page not found", "status_code": "404"},
            "Etsy": {"url": "https://www.etsy.com/shop/{}", "indicador": "Shop not found", "status_code": "404"},
            "TripAdvisor": {"url": "https://www.tripadvisor.com/members/{}", "indicador": "Profile Not Found", "status_code": "404"},
            "500px": {"url": "https://500px.com/{}", "indicador": "Page not found", "status_code": "404"},
            "eBay": {"url": "https://www.ebay.com/usr/{}", "indicador": "User not found", "status_code": "404"},
            "Amazon": {"url": "https://www.amazon.com/{}", "indicador": "Page not found", "status_code": "404"},
            # Anime & Art Forums/Páginas
            "Danbooru": {"url": "https://danbooru.donmai.us/users?search[name]={}", "indicador": "No users found", "status_code": "200"},
            "MyAnimeList": {"url": "https://myanimelist.net/profile/{}", "indicador": "Page Not Found", "status_code": "404"},
            "AniList": {"url": "https://anilist.co/user/{}", "indicador": "Not Found", "status_code": "404"},
            "AnimePlanet": {"url": "https://www.anime-planet.com/users/{}", "indicador": "not found", "status_code": "404"},
            "Kitsu": {"url": "https://kitsu.io/users/{}", "indicador": "Not Found", "status_code": "404"},
            "FurAffinity": {"url": "https://www.furaffinity.net/user/{}", "indicador": "No such user", "status_code": "404"},
            "ArtStation": {"url": "https://www.artstation.com/{}", "indicador": "Page Not Found", "status_code": "404"},
            "Weasyl": {"url": "https://www.weasyl.com/~{}", "indicador": "User not found", "status_code": "404"},
            "Newgrounds": {"url": "https://www.newgrounds.com/artist/{}", "indicador": "No such artist", "status_code": "404"},
            "Pixiv": {"url": "https://www.pixiv.net/member.php?id={}", "indicador": "Page not found", "status_code": "404"},
            "Crunchyroll": {"url": "https://www.crunchyroll.com/profile/{}", "indicador": "Page not found", "status_code": "404"}
        }
        self.user_agents: List[str] = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36",
            "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15A5341f Safari/604.1",
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
            "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
            "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18"
        ]

    def _get_session(self) -> requests.Session:
        s = requests.Session()
        r = Retry(total=3, backoff_factor=0.5, status_forcelist=[500,502,503,504])
        a = HTTPAdapter(max_retries=r)
        s.mount("http://", a)
        s.mount("https://", a)
        return s

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
            og_title = soup.find("meta", property="og:title")
            og_title_text = og_title["content"].strip() if og_title and og_title.get("content") else ""
            og_desc = soup.find("meta", property="og:description")
            og_desc_text = og_desc["content"].strip() if og_desc and og_desc.get("content") else ""
            meta_keywords = soup.find("meta", {"name": "keywords"})
            keywords = meta_keywords["content"].strip() if meta_keywords and meta_keywords.get("content") else ""
            h1 = soup.find("h1")
            h1_text = h1.get_text().strip() if h1 else ""
            ext_info = (
                f"Descripción: {desc or 'No disponible'}\n"
                f"OG Title: {og_title_text or 'No disponible'}\n"
                f"OG Desc: {og_desc_text or 'No disponible'}\n"
                f"Keywords: {keywords or 'No disponible'}\n"
                f"H1: {h1_text or 'No disponible'}"
            )
            return title, ext_info
        except Exception:
            return "No disponible", "Sin descripción"

    def _check_platform(self, platform: str) -> Tuple[bool, str, str, str]:
        conf = self.platforms[platform]
        url = conf["url"].format(quote(self.username))
        try:
            resp = self.session.get(url, headers=self._headers(), timeout=10, allow_redirects=True)
            if str(resp.status_code) != conf["status_code"] and conf["indicador"] not in resp.text:
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
            futures = {executor.submit(self._check_platform, plat): plat for plat in self.platforms}
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