import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box

console = Console()

class DiscordRoleMapper:
    def __init__(self, token=None):
        self.headers = {'Authorization': f'Bot {token}'} if token else {}
        self.base_url = "https://discord.com/api/v10"
        self.token = token

    def _fetch(self, url, public=False):
        try:
            response = requests.get(
                url,
                headers={} if public else self.headers,
                timeout=15
            )
            return response.json() if response.status_code == 200 else None
        except requests.RequestException:
            return None

    def get_roles(self, identifier):
        if self.token:
            guild_data = self._fetch(f"{self.base_url}/guilds/{identifier}")
            if guild_data:
                return self._process_private_roles(identifier, guild_data.get('name', 'Unknown'))
        
        if 'discord.gg/' in identifier:
            invite_code = identifier.split('/')[-1]
        else:
            invite_code = identifier
            
        invite_data = self._fetch(f"{self.base_url}/invites/{invite_code}?with_counts=true", public=True)
        if invite_data and invite_data.get('guild'):
            return self._process_public_roles(invite_data)
        
        return None

    def _process_private_roles(self, guild_id, guild_name):
        roles = self._fetch(f"{self.base_url}/guilds/{guild_id}/roles") or []
        members = self._fetch(f"{self.base_url}/guilds/{guild_id}/members?limit=1000") or []
        
        role_counts = {role['id']: 0 for role in roles if 'id' in role}
        for member in members:
            for role_id in member.get('roles', []):
                if role_id in role_counts:
                    role_counts[role_id] += 1
        
        return {
            'name': guild_name,
            'id': guild_id,
            'type': 'private',
            'roles': sorted(
                [
                    {
                        'name': r.get('name', 'N/A'),
                        'position': r.get('position', 0),
                        'color': f"#{r['color']:06x}" if r.get('color') else "Default",
                        'members': role_counts.get(r.get('id'), 0)
                    }
                    for r in roles
                    if isinstance(r, dict)
                ],
                key=lambda x: x['position'],
                reverse=True
            )
        }

    def _process_public_roles(self, invite_data):
        guild = invite_data['guild']
        roles = self._fetch(f"{self.base_url}/guilds/{guild['id']}/roles", public=True) or []
        return {
            'name': guild.get('name', 'Unknown'),
            'id': guild['id'],
            'type': 'public',
            'roles': sorted(
                [
                    {
                        'name': r.get('name', 'N/A'),
                        'position': r.get('position', 0),
                        'color': f"#{r['color']:06x}" if r.get('color') else "Default"
                    }
                    for r in roles
                    if isinstance(r, dict)
                ],
                key=lambda x: x['position'],
                reverse=True
            )
        }

    def display(self, data):
        if not data:
            console.print("\n[bold red]Error: No se pudieron obtener datos[/]")
            console.print("[bold yellow]Soluciones:[/]")
            console.print("- Verificar ID/invitación")
            console.print("- Usar token válido para más detalles")
            console.print("- Asegurar que el bot esté en el servidor (con token)")
            console.print("")
            return

        table = Table(
            title=f"[bold]{data['name']}[/] - Modo {'Privado' if data['type'] == 'private' else 'Público'}",
            box=box.ROUNDED,
            header_style="bold magenta"
        )
        table.add_column("Rol", style="bold cyan", width=25)
        table.add_column("Posición", justify="center")
        table.add_column("Color", justify="center")
        if data['type'] == 'private':
            table.add_column("Miembros", justify="center")

        for role in data['roles']:
            row = [
                role['name'],
                str(role['position']),
                role['color']
            ]
            if data['type'] == 'private':
                row.append(str(role.get('members', 0)))
            table.add_row(*row)

        console.print(table)
        console.print(f"[dim]ID Servidor: {data['id']}[/]")

def main():
    token = Prompt.ask("[bold green]Token bot (opcional)[/]", default="", show_default=False)
    identifier = Prompt.ask("[bold green]ID servidor o invitación[/]")
    
    mapper = DiscordRoleMapper(token.strip() or None)
    role_data = mapper.get_roles(identifier.strip())
    mapper.display(role_data)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Cancelado[/]")
    except Exception as e:
        console.print(f"\n[bold red]Error: {str(e)}[/]")