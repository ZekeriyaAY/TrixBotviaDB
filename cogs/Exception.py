from discord.ext import commands
from Utility import get_prefix


class Exception(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Eksik değişken var.")
        else:
            await ctx.send(f'Lütfen **{get_prefix(ctx, ctx)}help** komutundan kontrol edin veya yetkili birine başvurun.'
                           f'\n**Hata:** *{error}*')

def setup(client):
    client.add_cog(Exception(client))
