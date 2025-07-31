import asyncio
import discord
from discord.ext import commands
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

console.print("[bold green]Ingresa el token de tu bot[/]")
token = console.input("[bold green]> Token:[/] ")

console.print("[bold green]¿Cuántos códigos de invitación vas a analizar? (1 o más)[/]")
n = int(console.input("[bold green]> Cantidad:[/] "))

invite_codes = []
for i in range(n):
    console.print(f"[bold green]Ingreso de código {i + 1}[/]")
    code = console.input("[bold green]> Código (ej. discord.gg/abc123 o abc123):[/] ").strip()
    invite_codes.append(code.split("/")[-1])

intents = discord.Intents.none()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    console.print(Panel(f"[bold green]{bot.user} conectado. Analizando invitaciones...[/]", title="[bold green]Listo[/]"))
    for code in invite_codes:
        try:
            invite = await bot.fetch_invite(code, with_counts=True, with_expiration=True)
            table = Table(title=f"[bold cyan]Invitación: {code}[/]", style="cyan")
            table.add_column("[bold magenta]Campo[/]", style="magenta", no_wrap=True)
            table.add_column("[bold white]Valor[/]", style="white")

            table.add_row("Servidor", f"{invite.guild.name} ({invite.guild.id})")
            table.add_row("Canal", f"{invite.channel.name} ({invite.channel.id})")
            table.add_row("Creador", f"{invite.inviter} ({invite.inviter.id})" if invite.inviter else "Desconocido")
            table.add_row("Usos", str(invite.uses))
            table.add_row("Máx. usos", str(invite.max_uses) if invite.max_uses else "Ilimitado")
            table.add_row("Expira", str(invite.expires_at) if invite.expires_at else "Nunca")
            table.add_row("Temporal", "Sí" if invite.temporary else "No")

            console.print(table)
            console.print("")

        except discord.NotFound:
            console.print(f"[bold red]Invitación inválida o expirada: {code}[/]")
        except discord.HTTPException:
            console.print(f"[bold red]Error al obtener la invitación: {code}[/]")

    await bot.close()

bot.run(token)
