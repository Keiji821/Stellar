import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

class DiscordRoleMapper:
    def __init__(self, bot_token):
        self.headers = {'Authorization': f'Bot {bot_token}'}
        self.base_url = "https://discord.com/api/v10"

    def _make_request(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            console.print(f"[red]Error API: {response.status_code} - {response.text}[/]")
            return None
        except Exception as e:
            console.print(f"[red]Error de conexión: {str(e)}[/]")
            return None

    def get_server_roles(self, guild_id):
        roles = self._make_request(f"{self.base_url}/guilds/{guild_id}/roles")
        if not roles or not isinstance(roles, list):
            return None

        members = self._make_request(f"{self.base_url}/guilds/{guild_id}/members?limit=1000") or []
        
        role_members = {role['id']: 0 for role in roles if isinstance(role, dict)}
        for member in members:
            if isinstance(member, dict):
                for role_id in member.get('roles', []):
                    role_members[role_id] = role_members.get(role_id, 0) + 1

        return sorted(
            [
                {
                    'name': role.get('name', 'N/A'),
                    'id': role.get('id', ''),
                    'position': role.get('position', 0),
                    'color': f"#{role['color']:06x}" if role.get('color') else "Default",
                    'members': role_members.get(role.get('id'), 0)
                }
                for role in roles
                if isinstance(role, dict)
            ],
            key=lambda x: x['position'],
            reverse=True
        )

    def display_results(self, guild_id, roles):
        if not roles:
            console.print("[red]No se recibieron datos válidos de roles[/]")
            return

        table = Table(title=f"Mapa de Roles: {guild_id}")
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
        console.print("[red]No se pudieron obtener los roles. Verifique:")
        console.print("- Token válido con permisos 'guilds' y 'members'")
        console.print("- ID correcto del servidor")
        console.print("- El bot está agregado al servidor[/]")