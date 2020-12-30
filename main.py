import discord
from discord.ext import commands
import logging
import json
import os


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

def get_prefix(client):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[client.guild.id]

def get_autorole(client):
    with open('autoroles.json', 'r') as f:
        roles = json.load(f)
    return roles[str(client.guild.id)]

DESCRIPTION = ''
BOT_PREFIX = get_prefix
print(BOT_PREFIX)
client = commands.Bot(command_prefix=commands.when_mentioned_or(BOT_PREFIX),
                    description=DESCRIPTION, intents=intents)

initial_extensions = ['commands',
                    'admin',
                    'events']

if __name__ == '__main__':
    for extension in initial_extensions:
        print(f'{extension} yüklendi.')
        client.load_extension(extension)
        

@client.event
async def on_ready():
    print("-------------------------------------------")
    print(f'{client.user} ONLINE')
    print(f'{len(client.guilds)} sunucuda toplam {str(len(set(client.get_all_members())))} kullanıcının erişimi var.')
    for guild in client.guilds:
        print(f'Botun aktif olduğu sunucular: {guild.name}')
        if guild == "GUILD":
            break
    print(f'Ping: {round(client.latency * 1000)}ms')
    await client.change_presence(activity=discord.Game(name=f'TrixBot | © @zek#0243'))
    print("-------------------------------------------")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)











client.run(os.environ.get('TOKEN'))
