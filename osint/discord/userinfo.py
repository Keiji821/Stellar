import discord
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datetime import datetime
import asyncio

console = Console()

class DiscordUserLookup:
    def __init__(self):
        self.bot = None

    def formatear_fecha(self, fecha_str):
        try:
            fecha = datetime.fromisoformat(fecha_str.replace('Z', '+00:00'))
            return fecha.strftime("%d/%m/%Y a las %H:%M:%S")
        except:
            return fecha_str

    def mostrar_insignias(self, insignias):
        if not insignias:
            return "Ninguna"
        return ", ".join(insignia.replace("_", " ").title() for insignia in insignias)

    def obtener_info_api(self, user_id):
        try:
            response = requests.get(f"https://discordlookup.mesalytic.moe/v1/user/{user_id}", timeout=10)
            if response.status_code == 404:
                return {"error": "Usuario no encontrado"}
            elif response.status_code != 200:
                return {"error": f"Error {response.status_code}"}
            return response.json()
        except requests.exceptions.RequestException:
            return {"error": "Error de conexión"}

    async def obtener_info_discord_py(self, user_id, token):
        try:
            self.bot = discord.Client(intents=discord.Intents.default())
            await self.bot.login(token)
            user = await self.bot.fetch_user(int(user_id))
            return user
        except Exception as e:
            return {"error": f"Error con el bot: {e}"}
        finally:
            if self.bot:
                await self.bot.close()

    def mostrar_info(self, datos, datos_extra=None):
        tabla = Table(show_header=False, box=None)
        tabla.add_column(style="bold green", width=20)
        tabla.add_column(style="blue")

        tabla.add_row("Usuario", datos.get("username", "Desconocido"))
        tabla.add_row("Nombre global", datos.get("global_name", "N/A"))
        tabla.add_row("ID", datos.get("id", "N/A"))
        tabla.add_row("Creación", self.formatear_fecha(datos.get("created_at", "N/A")))

        avatar = datos.get("avatar", {})
        tabla.add_row("Avatar", avatar.get("link", "N/A"))
        tabla.add_row("Animado", "Sí" if avatar.get("is_animated", False) else "No")
        tabla.add_row("Insignias", self.mostrar_insignias(datos.get("badges")))

        if datos_extra and isinstance(datos_extra, discord.User):
            tabla.add_row("Bot", "Sí" if datos_extra.bot else "No")
            tabla.add_row("Tag", datos_extra.discriminator)
            tabla.add_row("Nombre completo", f"{datos_extra.name}#{datos_extra.discriminator}")

        console.print(Panel.fit(
            tabla,
            title="[bold cyan]Información del Usuario[/]",
            border_style="cyan",
            padding=(1, 4)
        ))

    async def run(self):
        user_id = console.input("[bold green]» Ingrese el ID de usuario: [/]")

        if not user_id.isdigit():
            console.print("[red]✘ El ID debe ser un número[/]")
            return

        token = console.input("[bold green]» Token de bot (opcional): [/]")

        with console.status("[bold blue]Buscando información...[/]", spinner="dots"):
            datos = self.obtener_info_api(user_id)
            if 'error' in datos:
                console.print(f"[red]✘ {datos['error']}[/]")
                return

            datos_extra = None
            if token.strip():
                datos_extra = await self.obtener_info_discord_py(user_id, token.strip())
                if isinstance(datos_extra, dict) and 'error' in datos_extra:
                    console.print(f"[red]{datos_extra['error']}[/]")
                    datos_extra = None

        self.mostrar_info(datos, datos_extra)

if __name__ == "__main__":
    console.print("\n[bold cyan]Discord User ID Lookup[/]\n")
    lookup = DiscordUserLookup()
    asyncio.run(lookup.run())