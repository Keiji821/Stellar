import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

class DiscordMutualServers:
    def __init__(self, bot_token):
        self.headers = {'Authorization': f'Bot {bot_token}'}
        self.base_url = "https://discord.com/api/v10"

    def get_mutual_servers(self, user1_id, user2_id):
        try:
            user1_guilds = requests.get(
                f"{self.base_url}/users/{user1_id}/guilds",
                headers=self.headers
            ).json()
            
            user2_guilds = requests.get(
                f"{self.base_url}/users/{user2_id}/guilds",
                headers=self.headers
            ).json()

            mutual_guilds = []
            user1_guild_ids = {g['id'] for g in user1_guilds}
            
            for guild in user2_guilds:
                if guild['id'] in user1_guild_ids:
                    guild_details = requests.get(
                        f"{self.base_url}/guilds/{guild['id']}",
                        headers=self.headers
                    ).json()
                    mutual_guilds.append({
                        'name': guild['name'],
                        'id': guild['id'],
                        'member_count': guild_details.get('approximate_member_count', 'N/A')
                    })

            return mutual_guilds

        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/]")
            return None

    def display_results(self, user1_id, user2_id, mutual_guilds):
        table = Table(title=f"Servidores en Comun: {user1_id} <-> {user2_id}")
        table.add_column("Servidor", style="cyan")
        table.add_column("ID", style="dim")
        table.add_column("Miembros", justify="right")

        for guild in mutual_guilds:
            table.add_row(
                guild['name'],
                guild['id'],
                str(guild['member_count'])
            )

        console.print(table)

if __name__ == "__main__":
    bot_token = Prompt.ask("[bold green]Ingrese el token del bot[/bold green]")
    analyzer = DiscordMutualServers(bot_token)
    
    user1_id = Prompt.ask("[bold green]ID del primer usuario[/bold green]")
    user2_id = Prompt.ask("[bold green]ID del segundo usuario[/bold green]")
    
    mutuals = analyzer.get_mutual_servers(user1_id, user2_id)
    if mutuals:
        analyzer.display_results(user1_id, user2_id, mutuals)
    else:
        console.print("[red]No se encontraron servidores en comun[/]")