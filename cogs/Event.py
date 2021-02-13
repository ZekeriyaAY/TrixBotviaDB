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
        c.execute("INSERT INTO ServerConfig (ServerId) VALUES (?)", (guild.id,))
        c.execute("INSERT INTO AutoRoleConfig (ServerId, AutoRoleId) VALUES(?, ?)", (guild.id, everyoneRoleId,))
        c.execute("INSERT INTO LeaveConfig (ServerId) VALUES (?)", (guild.id,))
        c.execute("INSERT INTO GreetConfig (ServerId) VALUES (?)", (guild.id,))
        c.execute("INSERT INTO LogConfig (ServerId) VALUES (?)", (guild.id,))
        c.execute("INSERT INTO LevelConfig (ServerId) VALUES (?)", (guild.id,))
        conn.commit()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # GELEN ÜYE DB'de KAYITLI DEĞİLSE KAYDINI YAPAR
        c.execute("SELECT * FROM LevelSystem WHERE ServerId = ? AND MemberId = ?", (member.guild.id, member.id,))
        status = c.fetchone()
        if status is None:
            c.execute("INSERT INTO LevelSystem (ServerId, MemberId) VALUES (?, ?)", (member.guild.id, member.id,))
            conn.commit()

        # GELEN ÜYEYE ROL VERİR
        c.execute("SELECT AutoRoleStatus FROM AutoRoleConfig WHERE ServerId = ?", (member.guild.id,))
        status = c.fetchone()
        if status[0] == 'on':
            autoRole = get_autorole(member, member)
            if autoRole == member.guild.id: # @everyone ise
                pass
            else:
                for i in '<@&>':
                    autoRole = autoRole.replace(i, '')
                role = get(member.guild.roles, id=int(autoRole))
                await member.add_roles(role)

        # GELEN ÜYEYİ TEXT CHNL'da DUYURUR
        c.execute("SELECT GreetStatus FROM GreetConfig WHERE ServerId = ?", (member.guild.id,))
        status = c.fetchone()
        if status[0] == 'on':
            pass

        # GELEN ÜYEYE DM MESAJI ATAR
        c.execute("SELECT GreetDMStatus FROM GreetConfig WHERE ServerId = ?", (member.guild.id,))
        status = c.fetchone()
        if status[0] == 'on':
            pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # GİDEN ÜYEYİ TEXT CHNL'da DUYURUR
        c.execute("SELECT LeaveStatus FROM LeaveConfig WHERE ServerId = ?", (member.guild.id,))
        status = c.fetchone()
        if status[0] == 'on':
            pass

        # GİDEN ÜYEYE DM MESAJI ATAR
        c.execute("SELECT LeaveDMStatus FROM LeaveConfig WHERE ServerId = ?", (member.guild.id,))
        status = c.fetchone()
        if status[0] == 'on':
            pass


def setup(client):
    client.add_cog(Event(client))
