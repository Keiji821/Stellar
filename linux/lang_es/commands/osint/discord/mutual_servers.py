import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress

console = Console()

class DiscordMutualServers:
    def __init__(self, bot_token):
        self.headers = {'Authorization': f'Bot {bot_token}'}
        self.base_url = "https://discord.com/api/v10"
        self.bot_guilds_cache = None

    def validate_token(self):
        try:
            response = requests.get(f"{self.base_url}/users/@me", headers=self.headers)
            if response.status_code == 200:
                bot_data = response.json()
                console.print(f"[green]✓ Token válido para: {bot_data['username']}#{bot_data['discriminator']}[/]")
                return True
            console.print(f"[red]✗ Token inválido. Error: {response.status_code}[/]")
            return False
        except Exception as e:
            console.print(f"[red]Error de conexión: {str(e)}[/]")
            return False

    def get_bot_guilds(self):
        if self.bot_guilds_cache:
            return self.bot_guilds_cache
        try:
            response = requests.get(f"{self.base_url}/users/@me/guilds", headers=self.headers)
            if response.status_code == 200:
                self.bot_guilds_cache = {guild['id']: guild for guild in response.json()}
                return self.bot_guilds_cache
            console.print(f"[red]Error obteniendo servidores: {response.status_code}[/]")
            return None
        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/]")
            return None

    def get_user_guilds(self, user_id):
        bot_guilds = self.get_bot_guilds()
        if not bot_guilds:
            return None
        try:
            response = requests.get(f"{self.base_url}/users/{user_id}/guilds", headers=self.headers)
            if response.status_code == 200:
                user_guilds = response.json()
                return [guild for guild in user_guilds if guild['id'] in bot_guilds]
            console.print(f"[red]Error usuario {user_id}: {response.status_code}[/]")
            return None
        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/]")
            return None

    def get_mutual_servers(self, user1_id, user2_id):
        with Progress() as progress:
            task = progress.add_task("[cyan]Buscando servidores...", total=3)
            
            progress.update(task, description="[cyan]Usuario 1...")
            user1_guilds = self.get_user_guilds(user1_id)
            progress.update(task, advance=1)
            
            if not user1_guilds:
                return None
                
            progress.update(task, description="[cyan]Usuario 2...")
            user2_guilds = self.get_user_guilds(user2_id)
            progress.update(task, advance=1)
            
            if not user2_guilds:
                return None
                
            progress.update(task, description="[cyan]Comparando...")
            user1_guild_ids = {guild['id'] for guild in user1_guilds}
            mutual_guilds = [
                guild for guild in user2_guilds
                if guild['id'] in user1_guild_ids
            ]
            progress.update(task, advance=1)
            
            return mutual_guilds

    def display_results(self, user1_id, user2_id, mutual_guilds):
        if not mutual_guilds:
            console.print("[red]No se encontraron servidores en común[/]")
            return

        table = Table(title=f"Servidores en Comun: {user1_id} <-> {user2_id}")
        table.add_column("Servidor", style="cyan")
        table.add_column("ID", style="dim")
        table.add_column("Miembros", justify="right")

        for guild in mutual_guilds:
            table.add_row(guild['name'], guild['id'], str(guild.get('member_count', 'N/A')))
        console.print(table)

if __name__ == "__main__":
    bot_token = Prompt.ask("[bold green]Ingrese el token del bot[/bold green]")
    analyzer = DiscordMutualServers(bot_token)
    
    if not analyzer.validate_token():
        console.print("[red]No se puede continuar con token inválido[/]")
        exit()
        
    user1_id = Prompt.ask("[bold green]ID del primer usuario[/bold green]")
    user2_id = Prompt.ask("[bold green]ID del segundo usuario[/bold green]")

    mutuals = analyzer.get_mutual_servers(user1_id, user2_id)
    analyzer.display_results(user1_id, user2_id, mutuals or [])