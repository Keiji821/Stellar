import discord
from discord.ext import commands

TOKEN = input("El token de tu bot: ")
USER_ID = input("ID: ")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    
    # Realizar la búsqueda del usuario
    user = await bot.fetch_user(USER_ID)
    if user:
        print("Información del Usuario:")
        print(f"Nombre: {user.name}")
        print(f"Discriminador: {user.discriminator}")
        print(f"ID: {user.id}")
        print(f"Avatar URL: {user.avatar}")
        print(f"Bot: {'Sí' if user.bot else 'No'}")
        print(f"Creado el: {user.created_at}")
    else:
        print(f"No se pudo encontrar información para el ID: {USER_ID}")
    
    await bot.close()

bot.run(TOKEN)