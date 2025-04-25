import discord
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from datetime import datetime, timezone
from discord import Embed, ActivityType

console = Console()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

MAX_MESSAGES_PER_CHANNEL = 100
MAX_TOTAL_MESSAGES = 50

def get_input(prompt, type_cast=str, optional=False):
    while True:
        value = console.input(prompt).strip()
        if not value and optional:
            return None
        try:
            return type_cast(value)
        except ValueError:
            console.print("[red]¡Valor inválido![/]")

user_id = get_input("[bold green]ID del usuario: [/]", int)
token = get_input("[bold green]Token del bot: [/]")
server_id = get_input("[bold green]ID del servidor (opcional): [/]", int, True)

def fmt_fecha(dt):
    if not dt: return "—"
    return f"{dt.strftime('%d/%m/%Y %H:%M:%S')} ({format_delta(dt)})"

def format_delta(dt):
    now = datetime.now(timezone.utc)
    delta = now - dt
    days = delta.days
    if days == 0: return "hoy"
    if days == 1: return "ayer"
    if days < 30: return f"hace {days} días"
    months = days // 30
    if months < 12: return f"hace {months} meses"
    years = months // 12
    return f"hace {years} años"

def get_badges(flags):
    badge_map = {
        "staff": "<:staff:1041825305650515998> Discord Staff",
        "partner": "<:partner:1041825332523610163> Partner",
        "hypesquad": "<:hypesquad:1041825358881767464> HypeSquad",
        "hypesquad_bravery": "<:bravery:1041825384691794000> Bravery",
        "hypesquad_brilliance": "<:brilliance:1041825409188507648> Brilliance",
        "hypesquad_balance": "<:balance:1041825432864325642> Balance",
        "bug_hunter": "<:bughunter:1041825458556477440> Bug Hunter I",
        "bug_hunter_level_2": "<:bughunter2:1041825484565336074> Bug Hunter II",
        "early_supporter": "<:earlysupporter:1041825511334322246> Early Supporter",
        "verified_bot_developer": "<:dev:1041825537825902632> Dev Verificado",
        "certified_moderator": "<:mod:1041825563440517120> Moderador Certificado",
        "active_developer": "<:activedev:1041825589363114054> Dev Activo",
        "premium": "<:nitro:1041825613621825566> Nitro",
        "system": "⚙️ Sistema",
        "verified": "<:verified:1041825640997658644> Verificado"
    }
    badges = [v for k, v in badge_map.items() if getattr(flags, k, False)]
    return " ".join(badges) if badges else "Ninguna"

def get_activity_details(activity):
    if isinstance(activity, discord.Spotify):
        return f"🎵 {activity.title} - {activity.artist}"
    if isinstance(activity, discord.CustomActivity):
        return f"📝 {activity.name}"
    if activity.type == ActivityType.streaming:
        return f"🎮 {activity.name} ({activity.platform})"
    return f"{activity.type_emoji} {activity.name}" if hasattr(activity, 'type_emoji') else activity.name

async def fetch_user_data(user):
    data = {
        "General": [
            ("Nombre", f"{user}"),
            ("ID", user.id),
            ("Bot", "✅ Sí" if user.bot else "❌ No"),
            ("Sistema", "✅ Sí" if user.system else "❌ No"),
            ("Creado", fmt_fecha(user.created_at)),
            ("Insignias", get_badges(user.public_flags)),
        ],
        "Media": [
            ("Avatar", user.avatar.url if user.avatar else "—"),
            ("Banner", user.banner.url if user.banner else "—"),
            ("Banner Server", member.guild_avatar.url if member and member.guild_avatar else "—")
        ],
        "Bio": [
            ("Biografía", user.bio if hasattr(user, 'bio') else "—"),
            ("Nombre completo", f"{user.name}#{user.discriminator}"),
        ]
    }
    return data

async def fetch_member_data(member):
    roles = [role.mention for role in member.roles if role != member.guild.default_role]
    permissions = [perm for perm, value in member.guild_permissions if value]
    
    return {
        "Servidor": [
            ("Apodo", member.nick or "—"),
            ("Unido", fmt_fecha(member.joined_at)),
            ("Boost", fmt_fecha(member.premium_since)),
            ("Roles", f"{len(roles)} roles" + (f"\nTop: {member.top_role.mention}" if roles else "")),
            ("Jerarquía", f"#{len(member.roles)} en jerarquía"),
            ("Permisos", ", ".join(perm.replace('_', ' ').title() for perm in permissions[:5]) + ("..." if len(permissions)>5 else "")),
            ("En Timeout", fmt_fecha(member.timed_out_until) if member.is_timed_out() else "No"),
            ("Mobile", "✅" if member.mobile_status != discord.Status.offline else "❌"),
            ("Web", "✅" if member.web_status != discord.Status.offline else "❌"),
            ("Escritorio", "✅" if member.desktop_status != discord.Status.offline else "❌")
        ],
        "Actividades": [
            (activity.type.name.title(), get_activity_details(activity))
            for activity in member.activities if not isinstance(activity, discord.Spotify)
        ] or [("Sin actividades", "—")],
        "Roles Detallados": [
            (role.name, role.color)
            for role in member.roles if role != member.guild.default_role
        ] or [("Sin roles adicionales", "—")]
    }

async def fetch_messages(guild, user_id):
    messages = []
    for channel in guild.text_channels:
        if not channel.permissions_for(guild.me).read_message_history:
            continue
        try:
            async for msg in channel.history(limit=MAX_MESSAGES_PER_CHANNEL):
                if msg.author.id == user_id and len(messages) < MAX_TOTAL_MESSAGES:
                    messages.append({
                        "content": msg.content,
                        "channel": channel.name,
                        "timestamp": msg.created_at,
                        "attachments": len(msg.attachments),
                        "embeds": len(msg.embeds),
                        "reactions": len(msg.reactions)
                    })
                    if len(messages) >= MAX_TOTAL_MESSAGES:
                        break
        except Exception as e:
            continue
    return messages

@client.event
async def on_ready():
    try:
        user = await client.fetch_user(user_id)
        member = None
        messages = []
        server_data = {}

        if server_id:
            guild = client.get_guild(server_id)
            if guild:
                member = await guild.fetch_member(user_id)
                messages = await fetch_messages(guild, user_id)
                server_data = await fetch_member_data(member) if member else {}

        user_data = await fetch_user_data(user)
        
        # Mostrar datos principales
        main_table = Table.grid(padding=(0, 2))
        main_table.add_column(style="bold cyan", width=25)
        main_table.add_column(style="bold yellow")
        
        for category, items in user_data.items():
            main_table.add_row(Panel.fit(
                "\n".join(f"[bold]{k}:[/] {v}" for k, v in items),
                title=f"[magenta]{category}[/]",
                border_style="green"
            ))
        
        if server_data:
            server_panels = []
            for category, items in server_data.items():
                tbl = Table(show_header=False, box=None, show_lines=True)
                tbl.add_column(style="bold blue")
                tbl.add_column(style="white")
                for k, v in items:
                    tbl.add_row(k, str(v))
                server_panels.append(Panel.fit(tbl, title=f"[cyan]{category}[/]", border_style="blue"))
            
            main_table.add_row(*server_panels)

        console.print(Panel.fit(main_table, title=f"[bold underline]🔍 INVESTIGACIÓN DE {user}"))
        
        # Mostrar mensajes
        if messages:
            msg_table = Table(title="Últimos Mensajes", box=box.ROUNDED)
            msg_table.add_column("Canal", style="cyan")
            msg_table.add_column("Fecha", style="yellow")
            msg_table.add_column("Contenido", style="white")
            msg_table.add_column("Adjuntos", justify="right")
            
            for msg in messages:
                content = Markdown(msg['content']) if len(msg['content']) < 100 else msg['content'][:97] + "..."
                msg_table.add_row(
                    msg['channel'],
                    msg['timestamp'].strftime("%d/%m %H:%M"),
                    content,
                    f"📎{msg['attachments']} 🖼️{msg['embeds']} ❤️{msg['reactions']}"
                )
            
            console.print(Panel(msg_table, title="📨 HISTORIAL DE MENSAJES", border_style="yellow"))

    except discord.NotFound:
        console.print("[bold red]❌ Usuario no encontrado[/]")
    except discord.Forbidden:
        console.print("[bold red]🔒 Sin permisos para acceder al servidor[/]")
    finally:
        await client.close()

client.run(token)
