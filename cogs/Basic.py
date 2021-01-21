from discord.ext import commands
import discord
import datetime


class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.send(msg)

    @commands.command(brief='Sunucuya Davet Linki Verir Yoksa Oluşturur',
                      aliases=['davet', 'davetet'])
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(unique=False)
        await ctx.send(link)

    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        async with ctx.typing():
            pass
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

    @commands.command(aliases=["p"])
    async def ping(self, ctx):
        async with ctx.typing():
            pass
        await ctx.send(f'*Ping: **{round(self.client.latency * 1000)}ms***')

    @commands.command(brief='Sunucu Hakkında Bilgiler Verir',
                      aliases=['bilgi', 'serverbilgi'])
    async def server(self, ctx):
        guild = ctx.guild

        voice_channels = len(guild.voice_channels)
        text_channels = len(guild.text_channels)

        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)

        now = datetime.datetime.now()

        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text=now.strftime("%X  •  %x  •  %A"))


        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Voice Channel", value=voice_channels)
        embed.add_field(name="Text Channel", value=text_channels)
        embed.add_field(name="AFK Channel", value=guild.afk_channel, inline=False)
        embed.add_field(name="Server Emoji", value=emoji_string or "None", inline=False)

        async with ctx.typing():
            pass
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Basic(client))
