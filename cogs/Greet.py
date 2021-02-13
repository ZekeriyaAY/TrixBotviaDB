import discord
from discord.ext import commands
import sqlite3

conn = sqlite3.connect('Database.db')
c = conn.cursor()

class Greet(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["hoşgeldin", "hoşgeldinaçkapat"])
    @commands.has_permissions(administrator=True)
    async def greet(self, ctx, onoff):
        serverId = str(ctx.guild.id)
        c.execute("SELECT GreetStatus FROM GreetConfig WHERE ServerId = ?", (serverId,))
        status = c.fetchall()
        status = status[0][0]

        if onoff == 'on':
            if status == 'on':
                embed = discord.Embed(
                    description=f'**{ctx.guild.name}** sunucusunun hoş geldin mesaj özelliği zaten ***açık***.',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                c.execute("UPDATE GreetConfig SET GreetStatus = 'on' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(
                    description=f'**{ctx.guild.name}** sunucusunun hoş geldin mesaj özelliği ***açıldı***.',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            await ctx.send(f'**{ctx.guild.name}** sunucusunun hoş geldin mesaj özelliği ***{status}***.')

        elif onoff == 'off':
            if status == 'on':
                c.execute("UPDATE GreetConfig SET GreetStatus = 'off' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(
                    description=f'**{ctx.guild.name}** sunucusunun hoş geldin mesaj özelliği ***kapatıldı***.',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                embed = discord.Embed(
                    description=f'**{ctx.guild.name}** sunucusunun hoş geldin mesaj özelliği zaten ***kapalı***.',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            await ctx.send(f'**{ctx.guild.name}** sunucusunun hoş geldin mesaj özelliği ***{status}***.')
        else:
            await ctx.send(f'HOŞ GELDİN MESAJ KULLANIM MESAJI OLACAK')

    @commands.command(aliases=["hoşgeldindm", "hoşgeldindmaçkapat"])
    @commands.has_permissions(administrator=True)
    async def greetdm(self, ctx, onoff):
        serverId = str(ctx.guild.id)
        c.execute("SELECT GreetDMStatus FROM GreetConfig WHERE ServerId = ?", (serverId,))
        status = c.fetchall()
        status = status[0][0]

        if onoff == 'on':
            if status == 'on':
                embed = discord.Embed(
                    description=f'**{ctx.guild.name}** sunucusunun dm hoş geldin mesaj özelliği zaten ***açık***.',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                c.execute("UPDATE GreetConfig SET GreetDMStatus = 'on' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(
                    description=f'**{ctx.guild.name}** sunucusunun dm hoş geldin mesaj özelliği ***açıldı***.',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            await ctx.send(f'**{ctx.guild.name}** sunucusunun dm hoş geldin mesaj özelliği ***{status}***.')

        elif onoff == 'off':
            if status == 'on':
                c.execute("UPDATE GreetConfig SET GreetDMStatus = 'off' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(
                    description=f'**{ctx.guild.name}** sunucusunun dm hoş geldin mesaj özelliği ***kapatıldı***.',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                embed = discord.Embed(
                    description=f'**{ctx.guild.name}** sunucusunun dm hoş geldin mesaj özelliği zaten ***kapalı***.',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            await ctx.send(f'**{ctx.guild.name}** sunucusunun dm hoş geldin mesaj özelliği ***{status}***.')
        else:
            await ctx.send(f'DM HOŞ GELDİN MESAJ KULLANIM MESAJI OLACAK')

def setup(client):
    client.add_cog(Greet(client))