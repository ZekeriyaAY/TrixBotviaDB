from discord.ext import commands
from discord.utils import get

from Utility import get_autorole
import sqlite3

conn = sqlite3.connect('Database.db')
c = conn.cursor()

class Event(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        everyoneRoleId = guild.roles[0].id
        c.execute("INSERT INTO ServerConfig (ServerId, AutoRoleId) VALUES(?, ?)", (guild.id,everyoneRoleId))
        conn.commit()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        autoRole = get_autorole(member, member)
        for i in '<@&>':
            autoRole = autoRole.replace(i, '')

        role = get(member.guild.roles, id=int(autoRole))
        await member.add_roles(role)


def setup(client):
    client.add_cog(Event(client))
