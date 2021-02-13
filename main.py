import discord
from discord.ext import commands
import os
import sqlite3
from Utility import get_prefix

conn = sqlite3.connect('Database.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS ServerConfig (ServerId INTEGER UNIQUE, Prefix TEXT DEFAULT '+', Language TEXT DEFAULT 'tr')")
c.execute("CREATE TABLE IF NOT EXISTS AutoRoleConfig (ServerId INTEGER UNIQUE, AutoRoleStatus TEXT DEFAULT 'off', AutoRoleId INTEGER)")
c.execute("CREATE TABLE IF NOT EXISTS LeaveConfig (ServerId INTEGER UNIQUE, LeaveStatus TEXT DEFAULT 'off', LeaveChannelId INTEGER, LeaveMsg TEXT DEFAULT 'Aramızdan ayrıldı :(', LeaveDMStatus TEXT DEFAULT 'off', LeaveDMMsg TEXT DEFAULT 'Aramızdan ayrılmana üzüldük :(')")
c.execute("CREATE TABLE IF NOT EXISTS GreetConfig (ServerId INTEGER UNIQUE, GreetStatus TEXT DEFAULT 'off', GreetChannelId INTEGER, GreetMsg TEXT DEFAULT 'Sunucuya Hoş Geldin!', GreetDMStatus TEXT DEFAULT 'off', GreetDMMsg TEXT DEFAULT 'Aramıza hoş geldin')")
c.execute("CREATE TABLE IF NOT EXISTS LogConfig (ServerId INTEGER UNIQUE, LogStatus TEXT DEFAULT 'off', LogChannelId INTEGER)")
c.execute("CREATE TABLE IF NOT EXISTS LevelConfig (ServerId INTEGER UNIQUE, LevelStatus TEXT DEFAULT 'off', LevelChannelStatus TEXT DEFAULT 'off', LevelChannelId INTEGER, LevelMsg TEXT DEFAULT 'Tebrikler, Level atladın!')")
c.execute("CREATE TABLE IF NOT EXISTS LevelSystem (ServerId INTEGER, MemberId INTEGER, MemberLevel INTEGER DEFAULT 0, MemberXP INTEGER DEFAULT 0)")


intents = discord.Intents.default()
intents.members = True
DESCRIPTION = 'TrixBot Yardım Merkezi | created by z3k#9977'
client = commands.Bot(command_prefix=get_prefix, intents=intents, description=DESCRIPTION)
#client.remove_command("help")

print("-------------------------------------------")
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != '__init__.py':
        client.load_extension(f'cogs.{filename[:-3]}')
        print(filename)

@client.event
async def on_ready():
    print("-------------------------------------------")
    print(f'{client.user} ONLINE')
    print(f'{len(client.guilds)} sunucuda bağlantı kuruldu.')
    print(f'Botun aktif olduğu sunucular: ')
    for guild in client.guilds:
        print(f'\t {guild.name}(id: {guild.id})')
        if guild == "GUILD":
            break

    print(f'Ping: {round(client.latency * 1000)}ms')
    await client.change_presence(activity=discord.Streaming(name="ERYSTRIX", url="https://www.twitch.tv/erystrix"))
    print("-------------------------------------------")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)


client.run(os.environ.get('TOKEN'))