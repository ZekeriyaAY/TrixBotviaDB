from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, cog: str):
        try:
            self.client.unload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'HATA: {e}')
            return
        await ctx.send(f'{cog} Cog Unloaded')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, cog: str):
        try:
            self.client.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'HATA: {e}')
            return
        await ctx.send(f'{cog} Cog Loaded')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, cog: str):
        try:
            self.client.reload_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'HATA: {e}')
            return
        await ctx.send(f'{cog} Cog Reloaded')


def setup(client):
    client.add_cog(Admin(client))
