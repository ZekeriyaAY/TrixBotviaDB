import discord
from discord.ext import commands
import sqlite3

from Utility import get_prefix

conn = sqlite3.connect('Database.db')
c = conn.cursor()

class Leave(commands.Cog):
    def __init__(self, client):
        self.client = client
    """ EKLENEN MESAJDA ÖZEL EMOJİLERDE SORUN YAŞIYOR 
    @commands.command(aliases=["chngleavemsg", "hoşçakalmesajıdeğiştir", "hoscakalmesajıdegistir"])
    @commands.has_permissions(manage_channels=True)
    async def changeleavemsg(self, ctx, *, msg):
        serverId = str(ctx.guild.id)
        c.execute("UPDATE LeaveConfig SET LeaveMsg = ? WHERE ServerId = ?", (msg, serverId))
        conn.commit()

        embed = discord.Embed(title=":white_check_mark: HOŞÇA KAL MESAJI DEĞİŞTİ :white_check_mark:",
                              description=f'**Giden üyeleri duyurulacak mesaj: *{msg}***',
                              color=discord.Color.green())
        await ctx.send(embed=embed)
    
        
        c.execute("SELECT LeaveMsg FROM LeaveConfig WHERE ServerId = ?", (serverId,))
        mesag = c.fetchall()
        await ctx.send(mesag[0][0])
    """

    @commands.command(aliases=["chngleavechnl", "hoşçakalkanalıdeğiştir", "hoscakalkanalidegistir"])
    @commands.has_permissions(manage_channels=True)
    async def changeleavechnl(self, ctx, chnl):
        serverId = str(ctx.guild.id)
        c.execute("UPDATE LeaveConfig SET LeaveChannelId = ? WHERE ServerId = ?", (chnl, serverId))
        conn.commit()

        embed = discord.Embed(title=":white_check_mark: HOŞÇA KAL MESAJ KANALI DEĞİŞTİ :white_check_mark:",
                              description=f'**Giden üyeleri duyurulacak kanal: *{chnl}***',
                              color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.command(aliases=["hoşçakal", "hoscakal"])
    @commands.has_permissions(manage_channels=True)
    async def leave(self, ctx, onoff):
        serverId = str(ctx.guild.id)
        c.execute("SELECT LeaveStatus FROM LeaveConfig WHERE ServerId = ?", (serverId,))
        status = c.fetchall()
        status = status[0][0]

        if onoff == 'on' or onoff == 'aç':
            if status == 'on':
                embed = discord.Embed(title=":grey_question: HOŞÇA KAL MESAJI AÇIK :grey_question:",
                    description=f'Hoşça kal mesaj özelliği zaten ***AÇIK***',
                    color=discord.Color.gold())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                c.execute("UPDATE LeaveConfig SET LeaveStatus = 'on' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: HOŞÇA KAL MESAJI AÇILDI :white_check_mark:",
                    description=f'Hoşça kal mesaj özelliği ***AÇILDI***',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
        elif onoff == 'off' or onoff == 'kapat':
            if status == 'on':
                c.execute("UPDATE LeaveConfig SET LeaveStatus = 'off' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: HOŞÇA KAL MESAJI KAPATILDI :white_check_mark:",
                    description=f'Hoşça kal mesaj özelliği ***KAPATILDI***',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                embed = discord.Embed(title=":grey_question: HOŞÇA KAL MESAJI KAPALI :grey_question:",
                    description=f'Hoşça kal mesaj özelliği zaten ***KAPALI***',
                    color=discord.Color.gold())
                await ctx.send(embed=embed)
                return
        else:
            embed = discord.Embed(title=":grey_question: HATALI ARGÜMAN KULLANIMI :grey_question:",
                                  color=discord.Color.gold())
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoşça kal mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}leave on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}leave off/kapat`***')
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoşça kal dm mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}leavedm on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}leavedm off/kapat`***')
            await ctx.send(embed=embed)

    @commands.command(aliases=["hoşçakaldm", "hoscakaldm"])
    @commands.has_permissions(manage_channels=True)
    async def leavedm(self, ctx, onoff):
        serverId = str(ctx.guild.id)
        c.execute("SELECT LeaveDMStatus FROM LeaveConfig WHERE ServerId = ?", (serverId,))
        status = c.fetchall()
        status = status[0][0]

        if onoff == 'on' or onoff == 'aç':
            if status == 'on':
                embed = discord.Embed(title=":grey_question: HOŞÇA KAL DM MESAJI AÇIK :grey_question:",
                                      description=f'Hoşça kal dm mesaj özelliği zaten ***AÇIK***',
                                      color=discord.Color.gold())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                c.execute("UPDATE LeaveConfig SET LeaveDMStatus = 'on' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: HOŞÇA KAL DM MESAJI AÇILDI :white_check_mark:",
                                      description=f'Hoşça kal dm mesaj özelliği ***AÇILDI***',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
                return
        elif onoff == 'off' or onoff == 'kapat':
            if status == 'on':
                c.execute("UPDATE LeaveConfig SET LeaveDMStatus = 'off' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: HOŞÇA KAL DM MESAJI KAPATILDI :white_check_mark:",
                                      description=f'Hoşça kal dm mesaj özelliği ***KAPATILDI***',
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                embed = discord.Embed(title=":grey_question: HOŞÇA KAL DM MESAJI KAPALI :grey_question:",
                                      description=f'Hoşça kal dm mesaj özelliği zaten ***KAPALI***',
                                      color=discord.Color.gold())
                await ctx.send(embed=embed)
                return
        else:
            embed = discord.Embed(title=":grey_question: HATALI ARGÜMAN KULLANIMI :grey_question:",
                                  color=discord.Color.gold())
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoşça kal mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}leave on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}leave off/kapat`***')
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoşça kal dm mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}leavedm on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}leavedm off/kapat`***')
            await ctx.send(embed=embed)

    @leave.error
    @leavedm.error
    async def leave_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            serverId = str(ctx.guild.id)
            c.execute("SELECT LeaveStatus FROM LeaveConfig WHERE ServerId = ?", (serverId,))
            status = c.fetchall()
            status = status[0][0]
            c.execute("SELECT LeaveDMStatus FROM LeaveConfig WHERE ServerId = ?", (serverId,))
            statusDM = c.fetchall()
            statusDM = statusDM[0][0]

            embed = discord.Embed(title=":question: HOŞÇA KAL MESAJ/DM MESAJ KULLANIMI :question:",
                                  color=discord.Color.gold())
            if status == 'on':
                embed.add_field(name="Hoşça Kal Mesaj Özelliği", value="***`AÇIK`***")
            elif status == 'off':
                embed.add_field(name="Hoşça Kal Mesaj Özelliği", value="***`KAPALI`***")
            if statusDM == 'on':
                embed.add_field(name="Hoşça Kal DM Mesaj Özelliği", value="***`AÇIK`***")
            elif statusDM == 'off':
                embed.add_field(name="Hoşça Kal DM Mesaj Özelliği", value="***`KAPALI`***")
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoşça kal mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}leave on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}leave off/kapat`***')
            embed.add_field(name=":heavy_minus_sign:", value=f'**Hoşça kal dm mesaj özelliğini;**', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}leavedm on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}leavedm off/kapat`***')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Leave(client))