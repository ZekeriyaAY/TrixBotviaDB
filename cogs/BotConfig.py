import discord
from discord.ext import commands
import sqlite3

conn = sqlite3.connect('Database.db')
c = conn.cursor()

class BotConfig(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["chngprefix", "prefixdeğiştir", "prefixdegistir"])
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        serverId = str(ctx.guild.id)
        c.execute("UPDATE ServerConfig SET Prefix = ? WHERE ServerId = ?", (prefix, serverId))
        conn.commit()

        embed = discord.Embed(title=":white_check_mark: PREFİX(ÖN EK) DEĞİŞTİ :white_check_mark:",
                              description=f'Botun prefix(önek)i: ***{prefix}***',
                              color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.command(aliases=["changelanguage", "chnglang", "chnglanguage", "dildeğiştir", "dildegistir"])
    @commands.has_permissions(administrator=True)
    async def changelang(self, ctx, lang):
        serverId = str(ctx.guild.id)
        c.execute("UPDATE ServerConfig SET Language = ? WHERE ServerId = ?", (lang, serverId))
        conn.commit()

        embed = discord.Embed(title=":white_check_mark: BOT DİLİ DEĞİŞTİ :white_check_mark:",
                              description=f'Botun mesaj dili: ***{lang}***',
                              color=discord.Color.green())
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(BotConfig(client))