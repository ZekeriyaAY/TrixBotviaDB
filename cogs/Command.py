import discord
from discord.ext import commands


class Command(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["yeniyil","yy","yeniyıl"])
    async def herkesebendenyeniyıl(self, ctx):
        embed = discord.Embed(title=f'Koca Yürekli *{ctx.author.name}*  Herkese Yeni Yıl Diledi',
                            colour=discord.Color.red())
        embed.set_image(url='https://reactiongifs.me/wp-content/uploads/2013/12/christmas-is-coming-candice-swanepoel-victorias-secret-angel.gif')
        await ctx.send(embed=embed)

    @commands.command(aliases=["raki","rakı"])
    async def herkesebendenrakı(self, ctx):
        embed = discord.Embed(title=f'Koca Yürekli *{ctx.author.name}*  Herkese Rakı Ismarladı',
                            colour=discord.Color.green())
        embed.set_image(url='https://cdn.discordapp.com/attachments/748893012427538473/760225241561170030/unknown.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=["çay","cay"])
    async def herkesebendençay(self, ctx):
        embed = discord.Embed(title=f'Koca Yürekli *{ctx.author.name}*  Herkese Çay Ismarladı',
                            colour=discord.Color.green())
        embed.set_image(url='https://i.sozcu.com.tr/wp-content/uploads/2018/08/iecrop/cay_16_9_1533630396.jpg')
        await ctx.send(embed=embed)

    @commands.command(aliases=["nude"])
    async def herkesebendennude(self, ctx):
        embed = discord.Embed(title=f'Koca Yürekli *{ctx.author.name}*  Herkese Nude Yolladı',
                            colour=discord.Color.purple())
        embed.set_image(url='https://i.ytimg.com/vi/-9BSbY8fUWY/maxresdefault.jpg')
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Command(client))