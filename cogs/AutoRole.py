import discord
from discord.ext import commands
import sqlite3
from Utility import get_prefix, get_autorole

conn = sqlite3.connect('Database.db')
c = conn.cursor()

class AutoRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["chngautorole", "otoroldeğiştir", "otoroldegistir"])
    @commands.has_permissions(manage_roles=True)
    async def changeautorole(self, ctx, role):
        serverId = str(ctx.guild.id)
        c.execute("UPDATE AutoRoleConfig SET AutoRoleId = ? WHERE ServerId = ?", (role, serverId))
        conn.commit()

        embed = discord.Embed(title=":white_check_mark: OTO ROL DEĞİŞTİ :white_check_mark:", description=f'**Yeni gelen üyelere otomatik verilecek rol: *{role}***',
                              color=discord.Color.green())
        await ctx.send(embed=embed)

    @commands.command(aliases=["otorol", "otorolonoff", "otorolaçkapat", "otorolackapat"])
    @commands.has_permissions(manage_roles=True)
    async def autorole(self, ctx, onoff):
        serverId = str(ctx.guild.id)
        c.execute("SELECT AutoRoleStatus FROM AutoRoleConfig WHERE ServerId = ?", (serverId,))
        status = c.fetchall()
        status = status[0][0]

        if onoff == 'on' or onoff == 'aç':
            if status == 'on':
                embed = discord.Embed(title=":white_check_mark: OTO ROL AÇIK :white_check_mark:",
                    description=f'Otomatik rol verme özelliği zaten ***AÇIK***',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                c.execute("UPDATE AutoRoleConfig SET AutoRoleStatus = 'on' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: OTO ROL AÇILDI :white_check_mark:",
                    description=f'Otomatik rol verme özelliği ***AÇILDI***',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
        elif onoff == 'off' or onoff == 'kapat':
            if status == 'on':
                c.execute("UPDATE AutoRoleConfig SET AutoRoleStatus = 'off' WHERE ServerId = ?", (serverId,))
                conn.commit()
                embed = discord.Embed(title=":white_check_mark: OTO ROL KAPATILDI :white_check_mark:",
                    description=f'Otomatik rol verme özelliği ***KAPATILDI***',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
            elif status == 'off':
                embed = discord.Embed(title=":white_check_mark: OTO ROL KAPALI :white_check_mark:",
                    description=f'Otomatik rol verme özelliği zaten ***KAPALI***',
                    color=discord.Color.green())
                await ctx.send(embed=embed)
                return
        else:
            embed = discord.Embed(title=":grey_question: HATALI ARGÜMAN KULLANIMI :grey_question:",
                                  description=f'Otomatik rol verme özelliğini',
                                  color=discord.Color.orange())
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}autorole on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}autorole off/kapat`***')
            await ctx.send(embed=embed)

    @autorole.error
    async def autorole_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingRequiredArgument):
            serverId = str(ctx.guild.id)
            c.execute("SELECT AutoRoleStatus FROM AutoRoleConfig WHERE ServerId = ?", (serverId,))
            status = c.fetchall()
            status = status[0][0]

            role = get_autorole(ctx, ctx)

            embed = discord.Embed(title=":question: OTO ROL KULLANIMI :question:",
                                  color=discord.Color.red())
            if status == 'on':
                embed.add_field(name="Rol Verme Sistemi", value="***`AÇIK`***")
            elif status == 'off':
                embed.add_field(name="Rol Verme Sistemi", value="***`KAPALI`***")
            embed.add_field(name="Verilcek Rol", value=f'{role}')
            embed.add_field(name=":heavy_minus_sign:", value=f'***Otomatik rol verme özelliğini;***', inline=False)
            embed.add_field(name="Açmak için", value=f'***`{get_prefix(ctx, ctx)}autorole on/aç`***')
            embed.add_field(name="Kapatmak için", value=f'***`{get_prefix(ctx, ctx)}autorole off/kapat`***')
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(AutoRole(client))