import discord
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

console = Console()

class DiscordServerInfo:
    def __init__(self):
        self.bot = None

    async def obtener_info(self, id_servidor, token=None):
        info_widget = self.obtener_widget(id_servidor)
        
        if token:
            try:
                self.bot = discord.Client(intents=discord.Intents.default())
                await self.bot.login(token)
                servidor = await self.bot.fetch_guild(int(id_servidor))
                
                return {
                    "nombre": servidor.name,
                    "miembros": servidor.member_count,
                    "canales": len(servidor.channels),
                    "widget": info_widget
                }
            except:
                return {"widget": info_widget}
        
        return {"widget": info_widget}

    def obtener_widget(self, id_servidor):
        try:
            respuesta = requests.get(f"https://discord.com/api/guilds/{id_servidor}/widget.json", timeout=10)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                return {
                    "nombre": datos.get("name"),
                    "miembros_online": datos.get("members", []),
                    "canales_voz": [canal["name"] for canal in datos.get("channels", [])],
                    "invitacion": datos.get("instant_invite")
                }
            return {"error": "Widget desactivado"}
        except:
            return {"error": "Error de conexión"}

    def mostrar_miembros(self, miembros):
        console.print(f"\n[bold cyan]Miembros en línea ({len(miembros)}):[/]\n")
        for miembro in miembros:
            nombre = f"{miembro.get('username', '?')}#{miembro.get('discriminator', '0000')}"
            estado = miembro.get('status', 'desconocido')
            
            color_estado = {
                "online": "green",
                "idle": "yellow",
                "dnd": "red",
                "offline": "dim"
            }.get(estado, "magenta")
            
            console.print(f"[white]{nombre.ljust(30)}[/] [bold {color_estado}]◉ {estado.capitalize()}[/]")

    def mostrar_info(self, datos):
        if "error" in datos.get("widget", {}):
            console.print("[bold red]✘ Widget desactivado[/]")
            return

        tabla = Table(show_header=False, box=None)
        tabla.add_column(style="bold green", width=20)
        tabla.add_column(style="blue")

        nombre = datos.get("nombre") or datos["widget"].get("nombre")
        tabla.add_row("Servidor", nombre)

        if "miembros" in datos:
            tabla.add_row("Miembros totales", str(datos["miembros"]))
        
        tabla.add_row("En línea", str(len(datos["widget"].get("miembros_online", []))))

        if "canales" in datos:
            tabla.add_row("Canales totales", str(datos["canales"]))
        
        if datos["widget"].get("canales_voz"):
            tabla.add_row("Canales de voz", ", ".join(datos["widget"]["canales_voz"]))

        console.print(Panel.fit(
            tabla,
            title="[bold green]Información del Servidor[/]",
            border_style="green",
            padding=(1, 4)
        ))

        if datos["widget"].get("miembros_online"):
            self.mostrar_miembros(datos["widget"]["miembros_online"])

    async def ejecutar(self):
        id_servidor = console.input("[bold green]ID del servidor: [/]")
        token = console.input("[bold green]Token del bot (opcional): [/]")
        
        datos = await self.obtener_info(id_servidor, token if token else None)
        self.mostrar_info(datos)
        
        if self.bot:
            await self.bot.close()

if __name__ == "__main__":
    import asyncio
    info = DiscordServerInfo()
    asyncio.run(info.ejecutar())