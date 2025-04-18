import discord
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
import asyncio

console = Console()

class ServerAnalyzer:
    def __init__(self):
        self.bot = None
        self.status_colors = {
            'online': 'green',
            'idle': 'yellow',
            'dnd': 'red',
            'offline': 'dim'
        }

    async def get_data(self, server_id, token=None):
        widget = self.get_widget_data(server_id)
        
        if token:
            try:
                self.bot = discord.Client(intents=discord.Intents.default())
                await self.bot.login(token)
                guild = await self.bot.fetch_guild(int(server_id))
                return {
                    'name': guild.name,
                    'total_members': guild.member_count,
                    'boosts': guild.premium_subscription_count,
                    'widget': widget
                }
            except Exception as e:
                console.print(f"[red]Error con el bot: {e}[/]")
                return {'widget': widget}
            finally:
                if self.bot:
                    await self.bot.close()
        
        return {'widget': widget}

    def get_widget_data(self, server_id):
        try:
            response = requests.get(f"https://discord.com/api/guilds/{server_id}/widget.json", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return {
                    'name': data.get('name'),
                    'online_members': data.get('members', []),
                    'voice_channels': [ch['name'] for ch in data.get('channels', [])],
                    'invite': data.get('instant_invite')
                }
            return {'error': 'Widget desactivado'}
        except Exception as e:
            return {'error': f'Error de conexión: {e}'}

    def build_display(self, data):
        info_table = Table.grid(expand=True)
        info_table.add_column(style="bold green", width=20)
        info_table.add_column(style="cyan")
        
        server_name = data.get('name') or data['widget'].get('name', 'Desconocido')
        info_table.add_row("Servidor", server_name)
        
        if 'total_members' in data:
            online_count = len(data['widget'].get('online_members', []))
            info_table.add_row("Miembros", f"{online_count}/{data['total_members']}")
        else:
            info_table.add_row("En línea", str(len(data['widget'].get('online_members', []))))
        
        if 'boosts' in data:
            info_table.add_row("Boosts", str(data['boosts']))
        
        if data['widget'].get('voice_channels'):
            info_table.add_row("Canales de voz", ", ".join(data['widget']['voice_channels']))
        
        if data['widget'].get('invite'):
            info_table.add_row("Invitación", data['widget']['invite'])
        
        members_table = Table.grid(padding=(0, 1))
        members_table.add_column(style="bold", width=30)
        members_table.add_column(width=10)
        
        if data['widget'].get('online_members'):
            for member in data['widget']['online_members'][:50]:  # Mostrar máximo 50 miembros
                username = f"{member.get('username', '?')}#{member.get('discriminator', '0000')}"
                status = member.get('status', 'offline')
                members_table.add_row(username, Text(f"◉ {status.upper()}", style=self.status_colors.get(status, 'magenta')))
        
        content = [
            Panel(info_table, title="Información General", border_style="blue"),
            Panel(members_table, title="Miembros Conectados", border_style="blue")
        ]
        
        return Panel(
            *content,
            title="[bold green]Información del servidor[/]",
            border_style="green",
            padding=(1, 2)
        )

    async def run(self):
        server_id = console.input("[bold green]ID del servidor: [/]")
        token = console.input("[bold green]Token del bot (opcional): [/]")
        
        data = await self.get_data(server_id, token if token else None)
        
        if 'error' in data['widget']:
            console.print(f"[red]Error: {data['widget']['error']}[/]")
            return
        
        console.print(self.build_display(data))

if __name__ == "__main__":
    analyzer = ServerAnalyzer()
    asyncio.run(analyzer.run())