
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
        self.bot = commands.Bot(command_prefix="!", intents=intents)

    def formatear_fecha(self, fecha):
        return fecha.strftime("%d/%m/%Y a las %H:%M:%S") if isinstance(fecha, datetime) else "N/A"

    def mostrar_insignias(self, flags):
        insignias = []
        if flags.early_supporter: insignias.append("Soporte Temprano")
        if flags.partner: insignias.append("Partner")
        if flags.hypesquad: insignias.append("HypeSquad")
        if flags.bug_hunter: insignias.append("Cazador de Bugs")
        if flags.verified_bot_developer: insignias.append("Dev Verificado")
        if flags.discord_certified_moderator: insignias.append("Moderador Certificado")
        return ", ".join(insignias) if insignias else "Ninguna"

    def construir_panel_usuario(self, user, member=None):
        tabla = Table(show_header=False, box=None)
        tabla.add_column(style="bold green", width=25)
        tabla.add_column(style="cyan")

        tabla.add_row("Nombre", f"{user.name}#{user.discriminator}")
        tabla.add_row("ID", str(user.id))
        tabla.add_row("Bot", "Sí" if user.bot else "No")
        tabla.add_row("Creado el", self.formatear_fecha(user.created_at))
        tabla.add_row("Avatar", user.avatar.url if user.avatar else "Sin avatar")
        tabla.add_row("Insignias", self.mostrar_insignias(user.public_flags))

        if hasattr(user, 'banner') and user.banner:
            tabla.add_row("Banner", user.banner.url)

        if member:
            tabla.add_row("Apodo", member.nick or "Ninguno")
            tabla.add_row("Unido al servidor", self.formatear_fecha(member.joined_at))
            tabla.add_row("Estado", str(member.status).title())
            roles = [r.name for r in member.roles if r.name != "@everyone"]
            tabla.add_row("Roles", ", ".join(roles) if roles else "Ninguno")

            if member.activity:
                actividad = f"{member.activity.name} ({member.activity.type.name})"
                tabla.add_row("Actividad", actividad)

        return Panel(tabla, title="[bold cyan]Información del Usuario[/]", border_style="cyan")

    async def obtener_mensajes_usuario(self, member: discord.Member):
        mensajes = []
        for canal in member.guild.text_channels:
            if not canal.permissions_for(member.guild.me).read_message_history:
                continue
            try:
                async for mensaje in canal.history(limit=50):
                    if mensaje.author.id == member.id:
                        mensajes.append(f"[{canal.name}] {mensaje.created_at.strftime('%d/%m/%Y %H:%M')} - {mensaje.content}")
                    if len(mensajes) >= 10:
                        break
            except Exception:
                continue
        return mensajes

    async def analizar(self, user_id: int, token: str, server_id: int = None):
        try:
            await self.bot.login(token)
            user = await self.bot.fetch_user(user_id)
            member = None
            mensajes = []

            if server_id:
                try:
                    guild = await self.bot.fetch_guild(server_id)
                    await guild.chunk()
                    member = guild.get_member(user_id)
                    if member:
                        mensajes = await self.obtener_mensajes_usuario(member)
                except discord.Forbidden:
                    console.print("[red]El bot no tiene acceso al servidor especificado.[/]")
                except discord.NotFound:
                    console.print("[red]Servidor no encontrado.[/]")

            console.print(self.construir_panel_usuario(user, member))

            if mensajes:
                tabla = Table(title="[bold yellow]Últimos Mensajes[/]", box=None)
                for msg in mensajes:
                    tabla.add_row(Text(msg, overflow="fold"))
                console.print(tabla)

        except discord.LoginFailure:
            console.print("[red]Token inválido.[/]")
        except discord.NotFound:
            console.print("[red]Usuario no encontrado.[/]")
        except Exception as e:
            console.print(f"[red]Error inesperado: {e}[/]")
        finally:
            await self.bot.close()

    async def run(self):
        user_id = console.input("[bold green]ID del usuario: [/]").strip()
        token = console.input("[bold green]Token del bot: [/]").strip()
        server_id_input = console.input("[bold green]ID del servidor (opcional): [/]").strip()

        if not user_id.isdigit():
            console.print("[red]El ID debe ser numérico.[/]")
            return

        user_id = int(user_id)
        server_id = int(server_id_input) if server_id_input.isdigit() else None
        await self.analizar(user_id, token, server_id)

if __name__ == "__main__":
    analyzer = DiscordUserAnalyzer()
    asyncio.run(analyzer.run())