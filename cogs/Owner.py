import os
from discord.ext import commands
import discord
from Utility import get_prefix


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        self.client.unload_extension(f'cogs.{cog}')
        embed = discord.Embed(description=f'***{cog}** Cog Unloaded*',
                              color=discord.Color.green())
        await ctx.send(embed=embed)


    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        self.client.load_extension(f'cogs.{cog}')
        embed = discord.Embed(description=f'***{cog}** Cog Loaded*',
                              color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        self.client.reload_extension(f'cogs.{cog}')
        embed = discord.Embed(description=f'***{cog}** Cog Reloaded*',
                              color=discord.Color.green())
        await ctx.send(embed=embed)

    @unload.error
    @load.error
    @reload.error
    async def cog_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=":grey_question: COG KULLANIMI :grey_question:",
                                  color=discord.Color.orange())
            embed.add_field(name="Devre Dışı Bırakmak için", value=f'**`{get_prefix(ctx, ctx)}unload [cog_adı]`**')
            embed.add_field(name="Yüklemek için", value=f'**`{get_prefix(ctx, ctx)}load [cog_adı]`**')
            embed.add_field(name="Tekrar Kurmak için", value=f'**`{get_prefix(ctx, ctx)}reload [cog_adı]`**')

            cog_list = ""
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py') and filename != '__init__.py':
                    cog_list += f' {filename[:-3]}\n'
            embed.add_field(name="Cog Listesi", value=cog_list)
            loaded_cog_list = ""
            for cog in self.client.extensions:
                loaded_cog_list += f' {cog[5:]}\n'
            embed.add_field(name="Yüklü Cog Listesi", value=loaded_cog_list)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.ExtensionAlreadyLoaded):
            embed = discord.Embed(title=":grey_question: COG ZATEN YÜKLÜ :grey_question:",
                                  color=discord.Color.orange())
            embed.add_field(name="Hata Mesajı", value=f'*{error}*')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.ExtensionNotLoaded):
            embed = discord.Embed(title=":question: COG YÜKLÜ DEĞİL :question:",
                                  color=discord.Color.red())
            embed.add_field(name="Hata Mesajı", value=f'*{error}*')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.NoEntryPointError):
            embed = discord.Embed(title=":question: COG NO ENTRY POINT ERROR :question:",
                                  color=discord.Color.red())
            embed.add_field(name="Hata Mesajı", value=f'*{error}*')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.ExtensionFailed):
            embed = discord.Embed(title=":question: COG EXTENSION FAILED :question:",
                                  color=discord.Color.red())
            embed.add_field(name="Hata Mesajı", value=f'*{error}*')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.ExtensionNotFound):
            embed = discord.Embed(title=":question: COG BULUNAMADI :question:",
                                  color=discord.Color.red())
            cog_list = ""
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py') and filename != '__init__.py':
                    cog_list += f' {filename[:-3]}\n'
            embed.add_field(name="Cog Listesi", value=cog_list)
            embed.add_field(name="Hata Mesajı", value=f'*{error}*', inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=":question: COG ERROR :question:",
                                  color=discord.Color.red())
            embed.add_field(name="Hata Mesajı", value=f'*{error}*')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Owner(client))
