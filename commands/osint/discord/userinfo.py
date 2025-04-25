import discord
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

console = Console()
user_id = int(console.input("[bold green]ID del usuario: [/]").strip())
token = console.input("[bold green]Token del bot: [/]").strip()
server_input = console.input("[bold green]ID del servidor (opcional): [/]").strip()
server_id = int(server_input) if server_input.isdigit() else None

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def fmt_fecha(dt):
    return dt.strftime("%d/%m/%Y %H:%M:%S") if isinstance(dt, datetime) else "—"

def get_badges(flags):
    mapa = {
        "staff": "Discord Staff", "partner": "Partner", "hypesquad": "HypeSquad",
        "bug_hunter": "Bug Hunter I", "bug_hunter_level_2": "Bug Hunter II",
        "early_supporter": "Soporte Temprano", "verified_bot_developer": "Dev Bot Verif.",
        "certified_moderator": "Mod Certificado", "active_developer": "Dev Activo"
    }
    return ", ".join(n for k, n in mapa.items() if getattr(flags, k, False)) or "Ninguna"

async def fetch_msgs(guild, uid, per_channel=50, max_total=20):
    mensajes = []
    for canal in guild.text_channels:
        if not canal.permissions_for(guild.me).read_message_history:
            continue
        try:
            async for m in canal.history(limit=per_channel):
                if m.author.id == uid:
                    timestamp = m.created_at.strftime("%d/%m %H:%M")
                    mensajes.append(f"[{canal.name} | {timestamp}] {m.content}")
                    if len(mensajes) >= max_total:
                        return mensajes
        except:
            continue
    return mensajes

@client.event
async def on_ready():
    try:
        user = await client.fetch_user(user_id)
    except discord.NotFound:
        console.print("[bold red]Usuario no encontrado[/]")
        return await client.close()
    
    member = None
    mensajes = []

    if server_id:
        try:
            guild = await client.fetch_guild(server_id)
            await guild.chunk()
            member = guild.get_member(user_id)
            if member:
                mensajes = await fetch_msgs(guild, user_id)
        except discord.Forbidden:
            console.print("[yellow]Sin permisos para ese servidor[/]")
        except discord.NotFound:
            console.print("[yellow]Servidor no encontrado[/]")

    tabla = Table(show_header=False, box=None)
    tabla.add_column(style="bold green", width=24)
    tabla.add_column(style="cyan")

    tabla.add_row("Usuario", f"{user.name}#{user.discriminator}")
    tabla.add_row("ID", str(user.id))
    tabla.add_row("Bot", "Sí" if user.bot else "No")
    tabla.add_row("Creado", fmt_fecha(user.created_at))
    tabla.add_row("Avatar", user.avatar.url if user.avatar else "—")
    tabla.add_row("Banner", getattr(user, "banner").url if getattr(user, "banner", None) else "—")
    tabla.add_row("Insignias", get_badges(user.public_flags))

    if member:
        tabla.add_row("Apodo", member.nick or "—")
        tabla.add_row("Unido", fmt_fecha(member.joined_at))
        tabla.add_row("Estado", str(member.status).capitalize())
        
        actividades = [
            f"{a.name} ({a.type.name})" 
            for a in member.activities 
            if isinstance(a, discord.Activity)
        ]
        tabla.add_row("Actividades", ", ".join(actividades) if actividades else "—")

        roles = [r.name for r in member.roles if r.name != "@everyone"]
        tabla.add_row("Roles", ", ".join(roles) if roles else "Ninguno")
        tabla.add_row("Color top role", str(member.top_role.color))

        if member.premium_since:
            tabla.add_row("Boost desde", fmt_fecha(member.premium_since))

        dispositivos = []
        for atributo, nombre in [
            ("desktop_status", "Escritorio"),
            ("mobile_status", "Móvil"),
            ("web_status", "Web")
        ]:
            estado = getattr(member, atributo, None)
            if estado and estado != discord.Status.offline:
                dispositivos.append(nombre)
        tabla.add_row("Dispositivos", ", ".join(dispositivos) if dispositivos else "Desconocido")
    else:
        tabla.add_row("En servidor", "No")

    console.print(Panel.fit(tabla, title="[bold magenta]Usuario Detallado[/]", border_style="magenta"))

    if mensajes:
        tabla_mensajes = Table(show_header=False, box=None)
        for m in mensajes:
            tabla_mensajes.add_row(m)
        console.print(Panel(tabla_mensajes, title="[bold yellow]Últimos Mensajes[/]", border_style="yellow"))
    
    await client.close()

client.run(token)