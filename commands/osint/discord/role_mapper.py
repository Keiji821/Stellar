import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

class DiscordRoleMapper:
    def __init__(self, bot_token):
        self.headers = {'Authorization': f'Bot {bot_token}'}
        self.base_url = "https://discord.com/api/v10"

    def get_server_roles(self, guild_id):
        try:
            roles = requests.get(
                f"{self.base_url}/guilds/{guild_id}/roles",
                headers=self.headers
            ).json()
            
            members = requests.get(
                f"{self.base_url}/guilds/{guild_id}/members?limit=1000",
                headers=self.headers
            ).json()

            role_members = {role['id']: 0 for role in roles}
            for member in members:
                for role_id in member.get('roles', []):
                    if role_id in role_members:
                        role_members[role_id] += 1

            sorted_roles = sorted(
                roles,
                key=lambda x: x['position'],
                reverse=True
            )

            return [{
                'name': role['name'],
                'id': role['id'],
                'position': role['position'],
                'color': f"#{role['color']:06x}" if role['color'] else "Default",
                'members': role_members.get(role['id'], 0)
            } for role in sorted_roles]

        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/]")
            return None

    def display_results(self, guild_id, roles):
        table = Table(title=f"Mapa de Roles del Servidor: {guild_id}")
        table.add_column("Rol", style="cyan")
        table.add_column("Posición", justify="right")
        table.add_column("Color")
        table.add_column("Miembros", justify="right")
        table.add_column("ID", style="dim")

        for role in roles:
            table.add_row(
                role['name'],
                str(role['position']),
                role['color'],
                str(role['members']),
                role['id']
            )

        console.print(table)

if __name__ == "__main__":
    bot_token = Prompt.ask("[bold green]Ingrese el token del bot[/bold green]")
    analyzer = DiscordRoleMapper(bot_token)
    
    guild_id = Prompt.ask("[bold green]ID del servidor[/bold green]")
    
    roles = analyzer.get_server_roles(guild_id)
    if roles:
        analyzer.display_results(guild_id, roles)
    else:
        console.print("[red]No se pudieron obtener los roles[/]")