import discord
from discord.ext import commands
import os
import json

def get_prefix(client, msg):
    with open('./jsons/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(msg.guild.id)]


def get_autorole(client, msg):
    with open('./jsons/auto_roles.json', 'r') as f:
        roles = json.load(f)
    return roles[str(msg.guild.id)]


def get_autorole_int(client, msg):
    with open('./jsons/auto_roles_int.json', 'r') as f:
        roles = json.load(f)
    return roles[str(client.guild.id)]

DESCRIPTION = 'TrixBot created by zek#0243'
client = commands.Bot(command_prefix=get_prefix, description=DESCRIPTION)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != '__init__.py':
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    print("-------------------------------------------")
    print(f'{client.user} ONLINE')
    print(f'{len(client.guilds)} sunucuda bağlantı kuruldu.')
    print(f'Botun aktif olduğu sunucular: ')
    for guild in client.guilds:
        print(f'\t {guild.name}')
        if guild == "GUILD":
            break
    print(f'Ping: {round(client.latency * 1000)}ms')
    await client.change_presence(activity=discord.Game(name=f'TrixBot | z3k#9999'))
    print("-------------------------------------------")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)


client.run((os.environ.get('TOKEN')))