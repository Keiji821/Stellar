import discord

client = discord.Client()

token = input("Ingresa un token de un bot: ")

@client.event
async def on_ready():
    print("Logged in as", client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!lookup"):
        user_id = message.content.split(" ")[1]
        user = client.get_user(int(user_id))
        if user:
            print("Username:", user.name)
            print("Discriminator:", user.discriminator)
            print("Avatar:", user.avatar_url)
            print("Status:", user.status)
            print("Joined at:", user.joined_at)

client.run(token)