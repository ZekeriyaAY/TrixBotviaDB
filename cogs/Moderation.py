from discord.ext import commands
import discord
from Utility import get_prefix, get_autorole



class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


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
    client.add_cog(Moderation(client))
