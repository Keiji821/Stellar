import discord
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.markdown import Markdown
from datetime import datetime
from discord.ext import commands
import asyncio

console = Console()

def get_input(prompt):
    return console.input(f"[bold cyan]{prompt}: [/bold cyan]")

TOKEN = get_input("Token del bot")
USER_ID = get_input("ID del usuario")

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def get_extended_user_info(guild, user_id):
    try:
        member = await guild.fetch_member(user_id)
        return member
    except:
        return None

def create_main_table(user):
    table = Table(width=60)
    
    creation_date = user.created_at.strftime("%d/%m/%Y %H:%M:%S")
    avatar_url = str(user.avatar_url) if user.avatar else "Ninguno"
    
    basic_info = {
        "Nombre": user.name,
        "Tag completo": f"{user.name}#{user.discriminator}",
        "ID": str(user.id),
        "Bot": "✅" if user.bot else "❌",
        "Cuenta creada": creation_date,
        "Avatar": avatar_url,
        "Banner": str(user.banner_url) if hasattr(user, 'banner_url') else "Ninguno",
        "Color de acento": str(user.accent_color) if hasattr(user, 'accent_color') else "Predeterminado"
    }

    for key, value in basic_info.items():
        table.add_row(key, value)
    
    return table

def create_member_table(member):
    if not member:
        return Panel("No se encontró en servidores comunes")
    
    table = Table(width=80)
    
    join_date = member.joined_at.strftime("%d/%m/%Y %H:%M:%S") if member.joined_at else "Desconocido"
    roles = "\n".join([role.name for role in member.roles[1:]]) if len(member.roles) > 1 else "Ninguno"
    
    member_info = {
        "Apodo": member.nick or "Ninguno",
        "Unió al servidor": join_date,
        "Roles": roles,
        "Estado": str(member.status).title(),
        "Actividad": member.activity.name if member.activity else "Ninguna",
        "Booster": "✅" if member.premium_since else "❌",
        "Permisos": str(member.guild_permissions.value)
    }

    for key, value in member_info.items():
        table.add_row(key, value)
    
    return Panel(table)

def create_connections_table(user):
    try:
        connections = user.connections if hasattr(user, 'connections') else []
    except:
        connections = []
    
    if not connections:
        return Panel("No se encontraron conexiones vinculadas")
    
    table = Table()
    table.add_column("Plataforma")
    table.add_column("Nombre")
    table.add_column("ID")
    
    for connection in connections:
        table.add_row(connection.type.title(), connection.name, str(connection.id))
    
    return Panel(table)

@bot.event
async def on_ready():
    console.clear()
    console.print(Panel.fit(f"✔ Conectado como: {bot.user}"))
    
    try:
        user = await bot.fetch_user(int(USER_ID))
        if not user:
            raise discord.NotFound
        
        guild = next((g for g in bot.guilds if g.get_member(int(USER_ID))), None)
        member = await get_extended_user_info(guild, int(USER_ID)) if guild else None
        
        console.print(Columns([
            Panel.fit(create_main_table(user)),
            create_member_table(member)
        ]))
        
        console.print(create_connections_table(user))
        
        if member and member.activities:
            activities = "\n".join([f"• {act.type.name.title()}: {act.name}" 
                                  for act in member.activities if act])
            console.print(Panel(Markdown(f"**Actividades recientes:**\n{activities}")))
            
    except discord.NotFound:
        console.print(Panel.fit("❌ Usuario no encontrado"))
    except discord.HTTPException as e:
        console.print(Panel.fit(f"⚠ Error de Discord: {str(e)}"))
    except Exception as e:
        console.print(Panel.fit(f"⚠ Error inesperado: {str(e)}"))
    finally:
        await bot.close()
        console.print(Panel.fit("🔍 Búsqueda completada"))

def main():
    console.print(Panel.fit("🔍 Discord User Investigator"))
    
    try:
        bot.run(TOKEN)
    except discord.LoginFailure:
        console.print(Panel.fit("❌ Token inválido"))
    except KeyboardInterrupt:
        console.print("\n⚠ Búsqueda cancelada"))

if __name__ == "__main__":
    main()