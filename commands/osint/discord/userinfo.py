import discord
from discord.ext import commands
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from datetime import datetime
import asyncio

console = Console()

class DiscordUserAnalyzer:
    def __init__(self):
        intents = discord.Intents.all()
        self.client = discord.Client(intents=intents)

    def format_date(self, date):
        return date.strftime("%d/%m/%Y a las %H:%M:%S") if isinstance(date, datetime) else "N/A"

    def get_badges(self, flags: discord.PublicUserFlags):
        badge_map = {
            'staff': "Discord Staff",
            'partner': "Partner",
            'hypesquad': "HypeSquad",
            'bug_hunter': "Bug Hunter Nivel 1",
            'bug_hunter_level_2': "Bug Hunter Nivel 2",
            'early_supporter': "Soporte Temprano",
            'verified_bot_developer': "Dev Bot Verificado",
            'certified_moderator': "Moderador Certificado",
            'active_developer': "Dev Activo",
        }
        return ", ".join(name for attr, name in badge_map.items() if getattr(flags, attr, False)) or "Ninguna"

    def build_user_panel(self, user: discord.User, member: discord.Member = None):
        table = Table(show_header=False, box=None)
        table.add_column(style="bold green", width=28)
        table.add_column(style="cyan")

        # Basic user info
        table.add_row("Usuario", f"{user.name}#{user.discriminator}")
        table.add_row("ID", str(user.id))
        table.add_row("Bot", "Sí" if user.bot else "No")
        table.add_row("Creado el", self.format_date(user.created_at))
        avatar = user.avatar.url if user.avatar else "Sin avatar"
        table.add_row("Avatar", avatar)
        banner = getattr(user, 'banner', None)
        table.add_row("Banner", banner.url if banner else "Sin banner")
        # Badges
        table.add_row("Insignias", self.get_badges(user.public_flags))

        # Member-specific info
        if member:
            table.add_row("Apodo", member.nick or "Ninguno")
            table.add_row("Unido el", self.format_date(member.joined_at))
            table.add_row("Estado", str(member.status).capitalize())
            # Activities
            if member.activities:
                acts = [f"{act.name} ({act.type.name})" for act in member.activities if isinstance(act, discord.Activity)]
                table.add_row("Actividades", ", ".join(acts))
            # Roles
            roles = [r.name for r in member.roles if r.name != "@everyone"]
            table.add_row("Roles", ", ".join(roles) if roles else "Ninguno")
            # Top role color
            table.add_row("Color del Rol Máximo", str(member.top_role.color))
            # Boost
            if member.premium_since:
                table.add_row("Boost desde", self.format_date(member.premium_since))
            # Device statuses
            try:
                devs = []
                if member.desktop_status: devs.append("Escritorio")
                if member.mobile_status: devs.append("Móvil")
                if member.web_status: devs.append("Web")
                table.add_row("Dispositivos", ", ".join(devs) if devs else "Desconocido")
            except AttributeError:
                pass
        else:
            table.add_row("Estado en servidor", "No en el servidor")

        panel = Panel.fit(table, title="[bold magenta]Información Detallada[/]", border_style="magenta", padding=(1,2))
        return panel

    async def fetch_messages(self, guild: discord.Guild, user_id: int, limit_per_channel: int = 50, max_messages: int = 20):
        messages = []
        for channel in guild.text_channels:
            if not channel.permissions_for(guild.me).read_message_history:
                continue
            try:
                async for msg in channel.history(limit=limit_per_channel):
                    if msg.author.id == user_id:
                        timestamp = msg.created_at.strftime("%d/%m/%Y %H:%M")
                        messages.append(f"[{channel.name} | {timestamp}] {msg.content}")
                        if len(messages) >= max_messages:
                            return messages
            except Exception:
                continue
        return messages

    async def analyze(self, user_id: int, token: str, server_id: int = None):
        await self.client.login(token)
        await self.client.connect()
        await self.client.wait_until_ready()

        user = await self.client.fetch_user(user_id)
        member = None
        messages = []

        if server_id:
            try:
                guild = await self.client.fetch_guild(server_id)
                await guild.chunk()
                member = guild.get_member(user_id)
                if member:
                    messages = await self.fetch_messages(guild, user_id)
            except discord.Forbidden:
                console.print("[yellow]Sin permisos para el servidor especificado.[/]")
            except discord.NotFound:
                console.print("[yellow]Servidor no encontrado.[/]")

        console.print(self.build_user_panel(user, member))

        if messages:
            msg_table = Table(title="[bold yellow]Últimos Mensajes[/]", show_header=False, box=None)
            for m in messages:
                msg_table.add_row(Text(m, overflow="fold"))
            console.print(msg_table)

        await self.client.close()

    async def run(self):
        uid = console.input("[bold green]ID del usuario: [/]").strip()
        token = console.input("[bold green]Token del bot: [/]").strip()
        sid = console.input("[bold green]ID del servidor (opcional): [/]").strip()

        if not uid.isdigit():
            console.print("[red]El ID del usuario debe ser numérico.[/]")
            return
        user_id = int(uid)
        server_id = int(sid) if sid.isdigit() else None

        try:
            await self.analyze(user_id, token, server_id)
        except discord.LoginFailure:
            console.print("[red]Token inválido.[/]")
        except Exception as e:
            console.print(f"[red]Error inesperado: {e}[/]")

if __name__ == "__main__":
    analyzer = DiscordUserAnalyzer()
    asyncio.run(analyzer.run())
