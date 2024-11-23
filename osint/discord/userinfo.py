import discord
from rich.console import Console
from discord.ext import commands

console = Console()

TOKEN = console.input("[bold green]El token de tu bot: [/bold green]")
USER_ID = console.input("[bold green]ID: [/bold green]")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    console.print(f"[bold green]Bot conectado como {bot.user}[bold green]")
    
    user = await bot.fetch_user(USER_ID)
    if user:
        console.print("[bold red]Información del Usuario:[/bold red]")
        console.print(f"[bold green]Nombre: {user.name}[/bold green]")
        console.print(f"[bold green]Discriminador: {user.discriminator}[/bold green]")
        console.print(f"[bold green]ID: {user.id}[/bold green]")
        console.print(f"[bold green]Avatar URL: {user.avatar}[/bold green]")
        console.print(f"Bot: {'Sí' if user.bot else 'No'}")
        console.print(f"[bold green]Cuenta creada el: {user.created_at}[/bold green]")
    else:
        console.print(f"[bold green]No se pudo encontrar información para el ID: {USER_ID}[/bold green]")
    
    await bot.close()

bot.run(TOKEN)