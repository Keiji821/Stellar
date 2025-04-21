import discord
import asyncio
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

console = Console()

class DiscordUserFetcher:
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        self.bot = discord.Client(intents=intents)

    def formatear_fecha(self, fecha):
        return fecha.strftime("%d/%m/%Y a las %H:%M:%S") if isinstance(fecha, datetime) else "N/A"

    def mostrar_insignias(self, flags):
        insignias = {
            "staff": "Discord Staff",
            "partner": "Partner",
            "hypesquad": "HypeSquad",
            "bug_hunter": "Bug Hunter",
            "bug_hunter_level_2": "Bug Hunter Nivel 2",
            "verified_bot_developer": "Dev Bot Verificado",
            "early_supporter": "Soporte Temprano",
            "hypesquad_bravery": "Bravery",
            "hypesquad_brilliance": "Brilliance",
            "hypesquad_balance": "Balance",
            "active_developer": "Desarrollador Activo"
        }
        lista = [nombre for clave, nombre in insignias.items() if getattr(flags, clave, False)]
        return ", ".join(lista) if lista else "Ninguna"

    def mostrar_info(self, user: discord.User, member: discord.Member = None):
        tabla = Table(show_header=False, box=None, padding=(0, 1))
        tabla.add_column(style="bold green", width=22)
        tabla.add_column(style="cyan")

        tabla.add_row("Usuario", f"{user.name}#{user.discriminator}")
        tabla.add_row("ID", str(user.id))
        tabla.add_row("Bot", "Sí" if user.bot else "No")
        tabla.add_row("Creado el", self.formatear_fecha(user.created_at))
        tabla.add_row("Avatar", user.avatar.url if user.avatar else "Sin avatar")
        tabla.add_row("Insignias", self.mostrar_insignias(user.public_flags))

        if member:
            tabla.add_row("Estado", str(member.status).title())
            tabla.add_row("Apodo", member.nick or "Ninguno")
            tabla.add_row("Unido el", self.formatear_fecha(member.joined_at))
            roles = [r.name for r in member.roles if r.name != "@everyone"]
            tabla.add_row("Roles", ", ".join(roles) if roles else "Ninguno")
        else:
            tabla.add_row("Estado", "Desconocido (no está en el servidor)")

        panel = Panel(tabla, title="[bold cyan]Información del Usuario[/]", border_style="bright_cyan", padding=(1, 4))
        console.print(panel)

    async def run(self):
        user_id = console.input("[bold green]ID del usuario: [/]").strip()
        token = console.input("[bold green]Token del bot: [/]").strip()
        server_id_input = console.input("[bold green]ID del servidor (opcional): [/]").strip()

        if not user_id.isdigit():
            console.print("[red]El ID debe ser numérico.[/]")
            return

        try:
            await self.bot.login(token)
            user = await self.bot.fetch_user(int(user_id))
            member = None

            if server_id_input.isdigit():
                try:
                    guild = await self.bot.fetch_guild(int(server_id_input))
                    member = await guild.fetch_member(int(user_id))
                except discord.Forbidden:
                    console.print("[yellow]No se tienen permisos para acceder al servidor.[/]")
                except discord.NotFound:
                    console.print("[yellow]El usuario no está en ese servidor.[/]")

            self.mostrar_info(user, member)

        except discord.LoginFailure:
            console.print("[red]Token inválido.[/]")
        except discord.NotFound:
            console.print("[red]Usuario no encontrado.[/]")
        except Exception as e:
            console.print(f"[red]Error inesperado: {e}[/]")
        finally:
            if self.bot.is_closed() is False:
                await self.bot.close()

if __name__ == "__main__":
    fetcher = DiscordUserFetcher()
    asyncio.run(fetcher.run())