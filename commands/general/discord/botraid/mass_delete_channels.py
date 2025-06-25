import discord
import asyncio
from rich.prompt import Prompt, Confirm
from rich.console import Console

console = Console()

def get_inputs():
    token = Prompt.ask("[bold green]Ingrese el token del bot[/]", password=True)
    guild_id = Prompt.ask("[bold green]Ingrese el ID del servidor[/]")
    return token, int(guild_id)

async def delete_channels(bot, guild_id):
    guild = bot.get_guild(guild_id)
    if not guild:
        console.print("[red]Servidor no encontrado[/]")
        return False

    if not Confirm.ask(f"[bold green]¿Eliminar TODOS los canales de {guild.name}?[/]"):
        return False

    console.print("[bold green]Eliminando canales...[/]")
    for channel in guild.channels:
        try:
            await channel.delete()
            await asyncio.sleep(1)  # Evitar rate limits
            console.print(f"[dim]Eliminado: #{channel.name}[/]")
        except Exception as e:
            console.print(f"[red]Error en #{channel.name}: {str(e)}[/]")
    return True

async def main():
    token, guild_id = get_inputs()
    bot = discord.Client(intents=discord.Intents.default())

    @bot.event
    async def on_ready():
        console.print(f"[green]✔ Bot conectado como: {bot.user.name}[/]")
        if await delete_channels(bot, guild_id):
            console.print("[bold green]¡Operación completada![/]")
        await bot.close()

    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
