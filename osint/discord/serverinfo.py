import discord
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

console = Console()

class DiscordServerAnalyzer:
    def __init__(self):
        self.bot = None

    async def get_detailed_info(self, guild_id, token=None):
        widget_data = self.get_widget_data(guild_id)
        
        if token:
            try:
                self.bot = discord.Client(intents=discord.Intents.default())
                await self.bot.login(token)
                
                guild = await self.bot.fetch_guild(int(guild_id))
                return {
                    "name": guild.name,
                    "total_members": guild.member_count,
                    "channels": len(guild.channels),
                    "roles": len(guild.roles),
                    "emojis": len(guild.emojis),
                    "boosts": guild.premium_subscription_count,
                    "widget": widget_data
                }
            except Exception as e:
                return {"widget": widget_data, "error": str(e)}
        
        return {"widget": widget_data}

    def get_widget_data(self, guild_id):
        try:
            response = requests.get(
                f"https://discord.com/api/guilds/{guild_id}/widget.json",
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                return {
                    "online_members": len(data.get("members", [])),
                    "voice_channels": [ch["name"] for ch in data.get("channels", [])],
                    "invite_url": data.get("instant_invite")
                }
            return {"error": "Widget disabled"}
        except:
            return {"error": "Connection error"}

    def display_results(self, data):
        table = Table(show_header=False, box=None)
        table.add_column(style="bold yellow", width=25)
        table.add_column(style="cyan")

        server_name = data.get("name") or "Unknown Server"
        table.add_row("Server Name", server_name)

        if "total_members" in data:
            table.add_row("Total Members", str(data["total_members"]))
        
        table.add_row("Online Now", str(data["widget"].get("online_members", 0)))

        if "channels" in data:
            table.add_row("Total Channels", str(data["channels"]))
        
        if data["widget"].get("voice_channels"):
            table.add_row("Voice Channels", ", ".join(data["widget"]["voice_channels"]))

        if "boosts" in data:
            table.add_row("Server Boosts", str(data["boosts"]))
        
        if "error" in data:
            console.print(f"[bold red]Error: {data['error']}[/]")

        console.print(Panel.fit(
            table,
            title="[bold green]SERVER ANALYSIS[/]",
            border_style="green",
            padding=(1, 4)
        ))

    async def run(self):
        guild_id = console.input("[bold magenta]Enter Server ID: [/]")
        token = console.input("[bold blue]Enter Bot Token (optional): [/]", password=True)
        
        data = await self.get_detailed_info(guild_id, token if token else None)
        self.display_results(data)
        
        if token and self.bot:
            await self.bot.close()

if __name__ == "__main__":
    analyzer = DiscordServerAnalyzer()
    import asyncio
    asyncio.run(analyzer.run())