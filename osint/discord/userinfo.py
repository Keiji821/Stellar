import discord
from rich.console import Console
from rich.table import Table
from discord.ext import commands

console = Console()

TOKEN = console.input("[bold green]El token de tu bot: [/bold green]")
USER_ID = console.input("[bold green]ID: [/bold green]")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    console.print(" ")
    console.print(f"[bold green]Bot conectado como {bot.user}[bold green]")
    console.print(" ")
    
    user = await bot.fetch_user(USER_ID)
    if user:
        console.print(" ")
        table = Table(title="Datos del ID", title_justify="center", title_style="bold red")
        table.add_column("Información", style="green", no_wrap=False)
        table.add_column("Valor", style="white")

        table.add_row("Nombre", user.name)
        table.add_row("Discriminador", user.discriminator)
        table.add_row("ID", user.id)
        table.add_row("Avatar URL", {user.avatar})
        table.add_row("Bot", f"{'Sí' if user.bot else 'No'}")
        table.add_row("Cuenta creada el", user.created_at)
        console.print(table)
        console.print(" ")
    else:
        console.print(f"[bold green]No se pudo encontrar información para el ID: {USER_ID}[/bold green]")
    
    await bot.close()

bot.run(TOKEN)