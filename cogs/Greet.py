import discord
from discord.ext import commands
import sqlite3

from Utility import get_prefix

conn = sqlite3.connect('Database.db')
c = conn.cursor()

class Greet(commands.Cog):
    def __init__(self, client):
        self.client = client
    """ EKLENEN MESAJDA ÖZEL EMOJİLERDE SORUN YAŞIYOR 
    @commands.command(aliases=["chnggreetmsg", "hoşgeldinmesajıdeğiştir", "hosgeldinmesajıdegistir"])
    @commands.has_permissions(manage_channels=True)
    async def changegreetmsg(self, ctx, *, msg):
        serverId = str(ctx.guild.id)
        c.execute("UPDATE GreetConfig SET GreetMsg = ? WHERE ServerId = ?", (msg, serverId))
        conn.commit()

        embed = discord.Embed(title=":white_check_mark: HOŞ GELDİN MESAJI DEĞİŞTİ :white_check_mark:",
                              description=f'**Yeni gelen üyeleri duyurulacak mesaj: *{msg}***',
                              color=discord.Color.green())
        await ctx.send(embed=embed)
    
        
        c.execute("SELECT GreetMsg FROM GreetConfig WHERE ServerId = ?", (serverId,))
        mesag = c.fetchall()
        await ctx.send(mesag[0][0])
    """

    @commands.command(aliases=["chnggreetchnl", "hoşgeldinkanalıdeğiştir", "hosgeldinkanalidegistir"])
    @commands.has_permissions(manage_channels=True)
    async def changegreetchnl(self, ctx, chnl):
        serverId = str(ctx.guild.id)
        c.execute("UPDATE GreetConfig SET GreetChannelId = ? WHERE ServerId = ?", (chnl, serverId))
        conn.commit()

        embed = discord.Embed(title=":white_check_mark: HOŞ GELDİN MESAJ KANALI DEĞİŞTİ :white_check_mark:",
                              description=f'**Yeni gelen üyeleri duyurulacak kanal: *{chnl}***',
                              color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.command(aliases=["hoşgeldin", "hosgeldin"])
    @commands.has_permissions(manage_channels=True)
    async def greet(self, ctx, onoff):
        serverId = str(ctx.guild.id)
        c.execute("SELECT GreetStatus FROM GreetConfig WHERE ServerId = ?", (serverId,))
        status = c.fetchall()
        status = status[0][0]

        if onoff == 'on' or onoff == 'aç':
            if status == 'on':
                embed = discord.Embed(title=":grey_question: HOŞ GELDİN MESAJI AÇIK :grey_question:",
                    description=f'Hoş geldin mesaj özelliği zaten ***AÇIK***',
                    color=discord.Color.gold())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                c.execute("UPDATE GreetConfig SET GreetStatus = 'on' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: HOŞ GELDİN MESAJI AÇILDI :white_check_mark:",
                    description=f'Hoş geldin mesaj özelliği ***AÇILDI***',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
        elif onoff == 'off' or onoff == 'kapat':
            if status == 'on':
                c.execute("UPDATE GreetConfig SET GreetStatus = 'off' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: HOŞ GELDİN MESAJI KAPATILDI :white_check_mark:",
                    description=f'Hoş geldin mesaj özelliği ***KAPATILDI***',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                embed = discord.Embed(title=":grey_question: HOŞ GELDİN MESAJI KAPALI :grey_question:",
                    description=f'Hoş geldin mesaj özelliği zaten ***KAPALI***',
                    color=discord.Color.gold())
                await ctx.send(embed=embed)
                return
        else:
            embed = discord.Embed(title=":grey_question: HATALI ARGÜMAN KULLANIMI :grey_question:",
                                  color=discord.Color.gold())
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoş geldin mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}greet on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}greet off/kapat`***')
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoş geldin dm mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}greetdm on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}greetdm off/kapat`***')
            await ctx.send(embed=embed)

    @commands.command(aliases=["hoşgeldindm", "hosgeldindm"])
    @commands.has_permissions(manage_channels=True)
    async def greetdm(self, ctx, onoff):
        serverId = str(ctx.guild.id)
        c.execute("SELECT GreetDMStatus FROM GreetConfig WHERE ServerId = ?", (serverId,))
        status = c.fetchall()
        status = status[0][0]

        if onoff == 'on' or onoff == 'aç':
            if status == 'on':
                embed = discord.Embed(title=":grey_question: HOŞ GELDİN DM MESAJI AÇIK :grey_question:",
                                      description=f'Hoş geldin dm mesaj özelliği zaten ***AÇIK***',
                                      color=discord.Color.gold())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                c.execute("UPDATE GreetConfig SET GreetDMStatus = 'on' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: HOŞ GELDİN DM MESAJI AÇILDI :white_check_mark:",
                                      description=f'Hoş geldin dm mesaj özelliği ***AÇILDI***',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
                return
        elif onoff == 'off' or onoff == 'kapat':
            if status == 'on':
                c.execute("UPDATE GreetConfig SET GreetDMStatus = 'off' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: HOŞ GELDİN DM MESAJI KAPATILDI :white_check_mark:",
                                      description=f'Hoş geldin dm mesaj özelliği ***KAPATILDI***',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                embed = discord.Embed(title=":grey_question: HOŞ GELDİN DM MESAJI KAPALI :grey_question:",
                                      description=f'Hoş geldin dm mesaj özelliği zaten ***KAPALI***',
                                      color=discord.Color.gold())
                await ctx.send(embed=embed)
                return
        else:
            embed = discord.Embed(title=":grey_question: HATALI ARGÜMAN KULLANIMI :grey_question:",
                                  color=discord.Color.gold())
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoş geldin mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}greet on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}greet off/kapat`***')
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoş geldin dm mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}greetdm on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}greetdm off/kapat`***')
            await ctx.send(embed=embed)

    @greet.error
    @greetdm.error
    async def greet_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            serverId = str(ctx.guild.id)
            c.execute("SELECT GreetStatus FROM GreetConfig WHERE ServerId = ?", (serverId,))
            status = c.fetchall()
            status = status[0][0]
            c.execute("SELECT GreetDMStatus FROM GreetConfig WHERE ServerId = ?", (serverId,))
            statusDM = c.fetchall()
            statusDM = statusDM[0][0]

            embed = discord.Embed(title=":question: HOŞ GELDİN MESAJ/DM MESAJ KULLANIMI :question:",
                                  color=discord.Color.gold())
            if status == 'on':
                embed.add_field(name="Hoş Geldin Mesaj Özelliği", value="***`AÇIK`***")
            elif status == 'off':
                embed.add_field(name="Hoş Geldin Mesaj Özelliği", value="***`KAPALI`***")
            if statusDM == 'on':
                embed.add_field(name="Hoş Geldin DM Mesaj Özelliği", value="***`AÇIK`***")
            elif statusDM == 'off':
                embed.add_field(name="Hoş Geldin DM Mesaj Özelliği", value="***`KAPALI`***")
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoş geldin mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}greet on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}greet off/kapat`***')
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoş geldin dm mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}greetdm on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}greetdm off/kapat`***')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Greet(client))