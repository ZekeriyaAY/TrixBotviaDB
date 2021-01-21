import discord
from discord.ext import commands
import os
import sqlite3
from Utility import get_prefix

conn = sqlite3.connect('Database.db')
c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS ServerConfig (ServerId INTEGER UNIQUE,"
          "Prefix TEXT DEFAULT '+', Language TEXT DEFAULT 'tr', LogControl TEXT DEFAULT 'false',"
          "LogChannel INTEGER, GreetMsgControl TEXT DEFAULT 'false',"
          "GreetMsg TEXT, GreetChannel INTEGER,"
          "GreetDmMsgControl TEXT DEFAULT 'false', GreetDmMsg TEXT,"
          "LeaveMsgControl TEXT DEFAULT 'false', LeaveMsg TEXT,"
          "LeaveChannel INTEGER, AutoRoleControl TEXT DEFAULT 'false',"
          "AutoRoleId INTEGER, LevelControl TEXT DEFAULT 'false',"
          "LevelMsg TEXT, LevelChannel INTEGER)")

intents = discord.Intents.default()
intents.members = True
DESCRIPTION = 'TrixBot Hoşgeldin'
client = commands.Bot(command_prefix=get_prefix, intents=intents, description=DESCRIPTION)


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
    await client.change_presence(activity=discord.Game(name=f'TrixBot'))
    print("-------------------------------------------")
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)



client.run(os.environ.get('TOKEN'))