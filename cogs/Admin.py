import sqlite3
from discord.ext import commands


conn = sqlite3.connect('Database.db')
c = conn.cursor()

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["prefixDeğiştir", "prefixdeğiştir", "prefixdeğiş", "prefixayarla"])
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        serverId = str(ctx.guild.id)
        c.execute("UPDATE ServerConfig SET Prefix = ? WHERE ServerId = ?", (prefix, serverId))
        conn.commit()
        await ctx.channel.send(f'**{ctx.guild.name}** sunucusunun prefix(önek)i  **{prefix}**  ile değiştirildi.')

    @commands.command(aliases=["otoRolDeğiştir", "otoroldeğiştir", "otoroldeğiş", "otorolayarla"])
    @commands.has_permissions(administrator=True)
    async def changeautorole(self, ctx, role):
        serverId = str(ctx.guild.id)
        c.execute("UPDATE ServerConfig SET AutoRoleId = ? WHERE ServerId = ?", (role, serverId))
        conn.commit()
        await ctx.channel.send(f'**{ctx.guild.name}** sunucusunun oto rolü  **{role}**  ile değiştirildi.')

def setup(client):
    client.add_cog(Admin(client))
