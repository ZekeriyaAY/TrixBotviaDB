import sqlite3
from discord.ext import commands
import discord
from Utility import get_prefix, get_autorole

conn = sqlite3.connect('Database.db')
c = conn.cursor()

class Moderator(commands.Cog):
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
        c.execute("UPDATE ServerConfig SET AutoRoleId = ? WHERE ServerId = ?",(role, serverId))
        conn.commit()
        await ctx.channel.send(f'**{ctx.guild.name}** sunucusunun oto rolü  **{role}**  ile değiştirildi.')

    @commands.command(aliases=["prefix", "önek", "onek"])
    @commands.has_permissions(administrator=True)
    async def getprefix(self, ctx):
        prefix = get_prefix(ctx, ctx)
        await ctx.send(f"**{ctx.guild.name}** sunucusunun prefix'i  **{prefix}**")

    @commands.command(aliases=["otorol"])
    @commands.has_permissions(manage_roles=True)
    async def getautorole(self, ctx):
        role = get_autorole(ctx, ctx)
        await ctx.send(f"**{ctx.guild.name}** sunucusunun oto rolü  **{role}**")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'*{member.mention}*, *{ctx.message.author.mention}* tarafından banlandı.\n**Sebep:** *{reason}*')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        bans = await ctx.guild.bans()
        for b in bans:
            if b.user.name == member:
                await ctx.guild.unban(b.user, reason=reason)
                await ctx.send(f"*{member}*, *{ctx.message.author.mention}* tarafından ban'ı kaldırıldı.\n**Sebep:** *{reason}*")
                return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'*{member.mention}*, *{ctx.message.author.mention}* tarafından atıldı.\n**Sebep:** *{reason}*')

def setup(client):
    client.add_cog(Moderator(client))
