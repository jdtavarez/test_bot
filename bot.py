import os 
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event 
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} has connected to Discord!\n'
        f'{guild.name} (id: {guild.id} )'
    )

    for channel in guild.channels: 
        if channel.name == "jobs":
            break

    print (
        f'{channel.id}'
    )

    await channel.send("Hello there... I'm the jobs bot")

@client.event
async def on_raw_reaction_add(payload):
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = await client.fetch_user(payload.user_id)

    await user.send("hi I see you reacted to my message")

client.run(TOKEN)