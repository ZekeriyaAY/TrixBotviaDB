import discord
from discord.ext import commands
from Utility import get_prefix


class Exception(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        error = getattr(error, "original", error)
        ignored = (commands.CommandNotFound,)
        if isinstance(error, ignored):
            return
        if isinstance(error, commands.NotOwner):
            embed = discord.Embed(
                description=f':warning: ***Botun sahibi sen değilsin. Sahip: <@!149575209026846721> *** :warning: *{ctx.author.mention}*',
                colour=discord.Color.orange())
            await ctx.send(embed=embed)
        else:
            await ctx.send(f'Lütfen **{get_prefix(ctx, ctx)}help** komutundan kontrol edin veya yetkili birine başvurun.'
                           f'\n**Hata:** *{error}*')

def setup(client):
    client.add_cog(Exception(client))
