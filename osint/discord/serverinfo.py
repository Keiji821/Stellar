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
            except:
                return {'widget': widget}
        
        return {'widget': widget}

    def get_widget_data(self, server_id):
        try:
            response = requests.get(f"https://discord.com/api/guilds/{server_id}/widget.json", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return {
                    'online_members': data.get('members', []),
                    'voice_channels': [ch['name'] for ch in data.get('channels', [])],
                    'invite': data.get('instant_invite')
                }
            return {'error': True}
        except:
            return {'error': True}

    def build_display(self, data):
        members_table = Table.grid(padding=(0, 2))
        members_table.add_column(style='bold', width=30)
        members_table.add_column(width=10)
        
        online_members = data['widget'].get('online_members', [])
        for member in online_members[:75]:
            username = f"{member.get('username', '?')}#{member.get('discriminator', '0000')}"
            status = member.get('status', 'offline')
            members_table.add_row(
                username,
                Text(f"◉ {status.upper()}", style=self.status_colors.get(status, 'magenta'))
            )

        info_table = Table(show_header=False)
        info_table.add_column(style='bold green')
        info_table.add_column(style='cyan')
        
        server_name = data.get('name', 'Unknown')
        info_table.add_row('SERVIDOR', server_name)
        
        if 'total_members' in data:
            info_table.add_row('MIEMBROS', f"{len(online_members)}/{data['total_members']}")
        else:
            info_table.add_row('EN LÍNEA', str(len(online_members)))
        
        if 'boosts' in data:
            info_table.add_row('BOOSTS', str(data['boosts']))
        
        if data['widget'].get('voice_channels'):
            info_table.add_row('CANALES', ', '.join(data['widget']['voice_channels']))

        if data['widget'].get('invite'):
            info_table.add_row('INVITACIÓN', data['widget']['invite'])

        return Panel(
            Panel(info_table, border_style="blue") + "\n" + Panel(members_table, border_style="blue"),
            title="[bold green]INFORMACIÓN DEL SERVIDOR[/]",
            border_style="green"
        )

    async def run(self):
        server_id = console.input("[bold green]ID del servidor: [/]")
        token = console.input("[bold green]Token del bot (opcional): [/]")
        
        data = await self.get_data(server_id, token if token else None)
        console.print(self.build_display(data))
        
        if self.bot:
            await self.bot.close()

asyncio.run(ServerAnalyzer().run())