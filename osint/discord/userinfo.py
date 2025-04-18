import discord
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import asyncio
from datetime import datetime

console = Console()

class DiscordUserFetcher:
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        self.bot = discord.Client(intents=intents)

    def formatear_fecha(self, fecha):
        if isinstance(fecha, datetime):
            return fecha.strftime("%d/%m/%Y a las %H:%M:%S")
        return "N/A"

    def mostrar_info(self, user: discord.User, member: discord.Member = None):
        tabla = Table(show_header=False, box=None)
        tabla.add_column(style="bold green", width=20)
        tabla.add_column(style="blue")

        tabla.add_row("Usuario", f"{user.name}#{user.discriminator}")
        tabla.add_row("ID", str(user.id))
        tabla.add_row("Bot", "Sí" if user.bot else "No")
        tabla.add_row("Creado el", self.formatear_fecha(user.created_at))
        tabla.add_row("Avatar", user.avatar.url if user.avatar else "Sin avatar")

        if member:
            tabla.add_row("Apodo", member.nick or "Ninguno")
            tabla.add_row("Estado", str(member.status).title())
            tabla.add_row("Unido el", self.formatear_fecha(member.joined_at))

            roles = [role.name for role in member.roles if role.name != "@everyone"]
            roles_str = ", ".join(roles) if roles else "Ninguno"
            tabla.add_row("Roles", roles_str)

        console.print(Panel.fit(
            tabla,
            title="[bold cyan]Información del Usuario[/]",
            border_style="cyan",
            padding=(1, 4)
        ))

    async def run(self):
        user_id = console.input("[bold green]ID del usuario: [/]").strip()
        guild_id = console.input("[bold green]ID del servidor (opcional): [/]").strip()
        token = console.input("[bold green]Token del bot: [/]").strip()

        if not user_id.isdigit():
            console.print("[red]El ID debe ser numérico.[/]")
            return

        try:
            await self.bot.login(token)

            user = await self.bot.fetch_user(int(user_id))
            member = None

            if guild_id.isdigit():
                try:
                    guild = await self.bot.fetch_guild(int(guild_id))
                    member = await guild.fetch_member(int(user_id))
                except discord.HTTPException:
                    console.print("[yellow]No se pudo obtener información extendida del servidor.[/]")

            self.mostrar_info(user, member)

        except discord.LoginFailure:
            console.print("[red]Token inválido.[/]")
        except discord.NotFound:
            console.print("[red]Usuario no encontrado.[/]")
        except Exception as e:
            console.print(f"[red]Error inesperado: {e}[/]")
        finally:
            await self.bot.close()

if __name__ == "__main__":
    fetcher = DiscordUserFetcher()
    asyncio.run(fetcher.run())