import requests
from bs4 import BeautifulSoup
import re
import json
import random
import time
from rich.console import Console

console = Console()

class InstagramScraperPro:
    def __init__(self):
        self.session = requests.Session()
        self.user_agents = [
            'Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Instagram 295.0.0.19.105 Android (33/13; 480dpi; 1080x2260; samsung; SM-S901B; s5e9925; qcom; en_US; 438409712)',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        
    def _random_delay(self):
        time.sleep(random.uniform(8, 15))
        
    def _get_html(self, username):
        try:
            self._random_delay()
            headers = {'User-Agent': random.choice(self.user_agents)}
            response = self.session.get(
                f"https://www.instagram.com/{username}/",
                headers=headers,
                timeout=20
            )
            return response.text if response.status_code == 200 else None
        except Exception as e:
            return None

    def _extract_data(self, html, username):
        soup = BeautifulSoup(html, 'html.parser')
        
        meta_description = soup.find('meta', property='og:description')
        title = soup.find('title').text if soup.find('title') else 'N/A'
        image = soup.find('meta', property='og:image')['content'] if soup.find('meta', property='og:image') else 'N/A'
        
        stats = None
        if meta_description:
            stats = re.search(r'(\d+) Followers, (\d+) Following, (\d+) Posts', meta_description['content'])
        
        is_private = False
        if 'Private' in title:
            is_private = True
        
        return {
            'username': username,
            'full_name': title.split('(')[0].replace('• Instagram', '').strip() if '(' in title else title.replace('• Instagram', '').strip(),
            'biography': meta_description['content'].split('-')[0].strip() if meta_description else 'N/A',
            'followers': int(stats.group(1)) if stats else 0,
            'following': int(stats.group(2)) if stats else 0,
            'posts': int(stats.group(3)) if stats else 0,
            'profile_pic': image,
            'is_private': is_private,
            'url': f"https://www.instagram.com/{username}/"
        }

    def get_profile(self, username):
        html = self._get_html(username)
        if not html:
            return None
        
        profile_data = self._extract_data(html, username)
        
        return profile_data

scraper = InstagramScraperPro()
username = console.input("[bold green]Ingrese el nombre de usuario de Instagram: [/bold green]")

profile = scraper.get_profile(username)

if profile:
    console.print(f"""
[bold]👤 Usuario:[/] @{profile['username']}
[bold]🏷 Nombre:[/] {profile['full_name']}
[bold]📝 Biografía:[/] {profile['biography']}
[bold]👥 Seguidores:[/] {profile['followers']}
[bold]🔄 Siguiendo:[/] {profile['following']}
[bold]📸 Posts:[/] {profile['posts']}
[bold]🖼 Foto:[/] {profile['profile_pic']}
[bold]🔒 Privado:[/] {'Sí' if profile['is_private'] else 'No'}
[bold]🔗 Perfil:[/] {profile['url']}
""")
else:
    console.print("[bold red]Error: Revisa conexión e intentalo de nuevo[/bold red]")
