import discord
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from datetime import datetime, timezone

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
    return dt.strftime('%d/%m/%Y %H:%M:%S')

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
        "verified": "<:verified:1041825640997658644> Verificado"
    }
    badges = [v for k, v in badge_map.items() if getattr(flags, k, False)]
    return " ".join(badges) if badges else "Ninguna"

async def fetch_user_data(user, member=None):
    data = [
        ("Nombre", f"{user}"),
        ("ID", user.id),
        ("Bot", "✅ Sí" if user.bot else "❌ No"),
        ("Sistema", "✅ Sí" if user.system else "❌ No"),
        ("Creado", fmt_fecha(user.created_at)),
        ("Insignias", get_badges(user.public_flags)),
        ("Avatar", user.avatar.url if user.avatar else "—"),
        ("Banner", user.banner.url if user.banner else "—"),
        ("Biografía", user.bio if hasattr(user, 'bio') and user.bio else "—"),
        ("Nombre completo", f"{user.name}#{user.discriminator}"),
    ]
    
    if member:
        data.extend([
            ("Apodo", member.nick or "—"),
            ("Unido al servidor", fmt_fecha(member.joined_at)),
            ("Boost", fmt_fecha(member.premium_since) if member.premium_since else "—"),
            ("Roles", ", ".join([role.name for role in member.roles if role != member.guild.default_role]) or "—"),
            ("Jerarquía", f"#{len(member.roles)} en jerarquía"),
            ("Permisos", ", ".join([perm.replace('_', ' ').title() for perm, value in member.guild_permissions if value])[:50] + "..." if len([perm for perm, value in member.guild_permissions if value]) > 5 else ""),
            ("En Timeout", fmt_fecha(member.timed_out_until) if member.is_timed_out() else "No"),
            ("Estado Mobile", "✅" if member.mobile_status != discord.Status.offline else "❌"),
            ("Estado Web", "✅" if member.web_status != discord.Status.offline else "❌"),
            ("Estado Escritorio", "✅" if member.desktop_status != discord.Status.offline else "❌"),
        ])
    
    return data

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
        
        if server_id:
            guild = client.get_guild(server_id)
            if guild:
                member = await guild.fetch_member(user_id)
                messages = await fetch_messages(guild, user_id)
        
        user_data = await fetch_user_data(user, member)
        
        data_str = "\n".join(f"[bold]{k}:[/] {v}" for k, v in user_data)
        
        console.print(Panel(
            data_str,
            title=f"[bold underline]🔍 INFORMACIÓN DE {user}[/bold underline]",
            border_style="green"
        ))
        
        if messages:
            console.print("\n[bold yellow]Últimos Mensajes:[/bold yellow]")
            for msg in messages:
                content = Markdown(msg['content']) if len(msg['content']) < 100 else msg['content'][:97] + "..."
                console.print(f"- [bold cyan]{msg['channel']}[/bold cyan] - {msg['timestamp'].strftime('%d/%m %H:%M')}")
                console.print(f"  {content}")
                console.print(f"  Adjuntos: [red]📎{msg['attachments']}[/red] Embeds: [blue]🖼️{msg['embeds']}[/blue] Reacciones: [purple]❤️{msg['reactions']}[/purple]\n")

    except discord.NotFound:
        console.print("[bold red]❌ Usuario no encontrado[/]")
    except discord.Forbidden:
        console.print("[bold red]🔒 Sin permisos para acceder al servidor[/]")
    finally:
        await client.close()

client.run(token)
