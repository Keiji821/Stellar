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
    return dt.strftime("%d/%m/%Y %H:%M:%S") if isinstance(dt, datetime) else "N/A"

def badges(flags):
    m = {
        "staff":"Discord Staff","partner":"Partner","hypesquad":"HypeSquad",
        "bug_hunter":"Bug Hunter I","bug_hunter_level_2":"Bug Hunter II",
        "early_supporter":"Soporte Temprano","verified_bot_developer":"Dev Bot Verif.",
        "certified_moderator":"Mod Certificado","active_developer":"Dev Activo"
    }
    return ", ".join(n for k,n in m.items() if getattr(flags, k, False)) or "Ninguna"

async def fetch_msgs(guild, uid, per_channel=50, max_total=20):
    msgs = []
    for ch in guild.text_channels:
        if not ch.permissions_for(guild.me).read_message_history: continue
        try:
            async for m in ch.history(limit=per_channel):
                if m.author.id == uid:
                    ts = m.created_at.strftime("%d/%m %H:%M")
                    msgs.append(f"[{ch.name} | {ts}] {m.content}")
                    if len(msgs) >= max_total:
                        return msgs
        except:
            pass
    return msgs

@client.event
async def on_ready():
    user = await client.fetch_user(user_id)
    member = None
    msgs = []
    if server_id:
        try:
            guild = await client.fetch_guild(server_id)
            await guild.chunk()
            member = guild.get_member(user_id)
            if member:
                msgs = await fetch_msgs(guild, user_id)
        except discord.Forbidden:
            console.print("[yellow]Sin permisos para ese servidor[/]")
        except discord.NotFound:
            console.print("[yellow]Servidor no encontrado[/]")

    t = Table(show_header=False, box=None)
    t.add_column(style="bold green", width=24)
    t.add_column(style="cyan")
    t.add_row("Usuario", f"{user.name}#{user.discriminator}")
    t.add_row("ID", str(user.id))
    t.add_row("Bot", "Sí" if user.bot else "No")
    t.add_row("Creado", fmt_fecha(user.created_at))
    t.add_row("Avatar", user.avatar.url if user.avatar else "—")
    t.add_row("Banner", getattr(user, "banner").url if getattr(user, "banner", None) else "—")
    t.add_row("Insignias", badges(user.public_flags))
    if member:
        t.add_row("Apodo", member.nick or "—")
        t.add_row("Unido", fmt_fecha(member.joined_at))
        t.add_row("Estado", str(member.status).capitalize())
        acts = [f"{a.name}({a.type.name})" for a in member.activities if isinstance(a, discord.Activity)]
        t.add_row("Actividades", ", ".join(acts) if acts else "—")
        r = [rol.name for rol in member.roles if rol.name!="@everyone"]
        t.add_row("Roles", ", ".join(r) if r else "Ninguno")
        t.add_row("Color top role", str(member.top_role.color))
        if member.premium_since:
            t.add_row("Boost desde", fmt_fecha(member.premium_since))
        devs = []
        for attr, name in [("desktop_status","Escritorio"),("mobile_status","Móvil"),("web_status","Web")]:
            if getattr(member,attr, None):
                devs.append(name)
        t.add_row("Dispositivos", ", ".join(devs) if devs else "Desconocido")
    else:
        t.add_row("En servidor", "No")

    console.print(Panel.fit(t, title="[bold magenta]Usuario Detallado[/]", border_style="magenta"))
    if msgs:
        tb = Table(show_header=False, box=None)
        for m in msgs:
            tb.add_row(m)
        console.print(Panel(tb, title="[bold yellow]Últimos Mensajes[/]", border_style="yellow"))
        console.print("")
    await client.close()

client.run(token)