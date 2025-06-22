import requests
from bs4 import BeautifulSoup
import re
import random
import time
from rich.console import Console
from rich.table import Table
from urllib.parse import urlparse

class InstagramScraperPro:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br'
        })
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Instagram 295.0.0.19.105 Android',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1'
        ]
        self.timeout = 25
        self.max_retries = 2

    def _random_delay(self):
        time.sleep(random.uniform(10, 18))

    def _get_html(self, username):
        for attempt in range(self.max_retries):
            try:
                self._random_delay()
                headers = {'User-Agent': random.choice(self.user_agents)}
                response = self.session.get(
                    f"https://www.instagram.com/{username}/",
                    headers=headers,
                    timeout=self.timeout
                )
                if response.status_code == 200:
                    return response.text
                elif response.status_code == 404:
                    return None
            except requests.exceptions.RequestException:
                if attempt == self.max_retries - 1:
                    return None
                continue
        return None

    def _parse_profile_data(self, html, username):
        soup = BeautifulSoup(html, 'html.parser')
        meta_description = soup.find('meta', property='og:description')
        title = soup.find('title')
        
        stats = None
        if meta_description:
            stats = re.search(
                r'(\d+[\d,]*\.?\d+)\s*Followers,\s*(\d+[\d,]*\.?\d+)\s*Following,\s*(\d+[\d,]*\.?\d+)\s*Posts',
                meta_description['content']
            )

        return {
            'username': username,
            'full_name': self._clean_text(title.text.split('(')[0].replace('• Instagram', '')) if title else 'N/A',
            'biography': self._clean_text(meta_description['content'].split('-')[0]) if meta_description else 'N/A',
            'followers': self._parse_number(stats.group(1)) if stats else 0,
            'following': self._parse_number(stats.group(2)) if stats else 0,
            'posts': self._parse_number(stats.group(3)) if stats else 0,
            'profile_pic': self._get_meta_content(soup, 'og:image'),
            'is_private': 'Private' in title.text if title else False,
            'url': f"https://www.instagram.com/{username}/"
        }

    def _clean_text(self, text):
        return text.strip().replace('\n', ' ').replace('\r', '')

    def _parse_number(self, num_str):
        return int(num_str.replace(',', '').replace('.', ''))

    def _get_meta_content(self, soup, property_name):
        meta = soup.find('meta', property=property_name)
        return meta['content'] if meta else 'N/A'

    def get_profile(self, username):
        if not username or not isinstance(username, str):
            return None
            
        html = self._get_html(username)
        return self._parse_profile_data(html, username) if html else None

def display_profile(profile, console):
    if not profile:
        console.print("[red]Error: No se pudo obtener el perfil. Verifica el nombre de usuario o tu conexión.[/red]")
        return

    table = Table(title=f"Información de @{profile['username']}", show_header=False)
    table.add_column("Campo", style="cyan")
    table.add_column("Valor", style="green")

    fields = [
        ("Nombre completo", profile['full_name']),
        ("Biografía", profile['biography']),
        ("Seguidores", f"{profile['followers']:,}"),
        ("Siguiendo", f"{profile['following']:,}"),
        ("Publicaciones", f"{profile['posts']:,}"),
        ("Privado", "Sí" if profile['is_private'] else "No"),
        ("URL del perfil", profile['url']),
        ("Foto de perfil", urlparse(profile['profile_pic']).path if profile['profile_pic'] != 'N/A' else 'N/A')
    ]

    for field, value in fields:
        table.add_row(field, value)

    console.print(table)

if __name__ == "__main__":
    console = Console()
    username = console.input("[bold cyan]Nombre de usuario de Instagram: [/]").strip()
    
    scraper = InstagramScraperPro()
    profile = scraper.get_profile(username)
    
    display_profile(profile, console)