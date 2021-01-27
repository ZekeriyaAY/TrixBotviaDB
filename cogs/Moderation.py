from discord.ext import commands
import discord
from Utility import get_prefix, get_autorole



class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["prefix", "önek", "onek"])
    @commands.has_permissions(administrator=True)
    async def getprefix(self, ctx):
        prefix = get_prefix(ctx, ctx)
        await ctx.send(f"**{ctx.guild.name}** sunucusunun prefix'i  **{prefix}**")

    @commands.command(aliases=["otorol"])
    @commands.has_permissions(manage_roles=True)
    async def getautorole(self, ctx):
        role = get_autorole(ctx, ctx)
        await ctx.send(f"**{ctx.guild.name}** sunucusunun oto rolü  **{role}**")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(
            description=f":white_check_mark: *{member.mention}*, *{ctx.message.author.mention}* tarafından **banlandı**. :hammer:"
                        f'\n***Sebep:*** **`{reason}`**',
            colour=discord.Color.green())
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @ban.error
    async def ban_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description=f':warning: **`Üyeleri Engelle` yetkisine sahip değilsin.** :warning: *{ctx.author.mention}*',
                colour=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, discord.Forbidden):
            embed = discord.Embed(
                description=f':warning: Bot, **sunucu sahibini** veya **kendinden daha yetkili** birini banlama yetkisine **sahip değil.** :warning:'
                            f'\n*{ctx.author.mention} Bunun için botun rolünü en üste alın.*',
                colour=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                description=f':interrobang: **Eksik Argüman** :interrobang: *{ctx.author.mention}*',
                colour=discord.Color.red())
            embed.add_field(name="Kullanım şekli:", value=f'**`{get_prefix(ctx, ctx)}ban [Üye] (Sebep)`**',
                            inline=False)
            embed.add_field(name="Argümanlar:",
                            value=f'**`Üye`**: *Banlamak istediğin üyeyi etiketle* [**@Üye**]'
                                  f'\n**`Sebep`**: *Banlama sebebin (**Zorunlu değil**)*')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(
                description=f':warning: *Üye **bulunamadı.*** :warning: *{ctx.author.mention}*',
                colour=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f':interrobang: **Hatalı Ban Komutu Kullanımı** :interrobang: *{ctx.author.mention}*',
                colour=discord.Color.red())
            embed.add_field(name="Kullanım şekli:", value=f'**`{get_prefix(ctx, ctx)}ban [Üye] (Sebep)`**',
                            inline=False)
            embed.add_field(name="Argümanlar:",
                            value=f'**`Üye`**: *Banlamak istediğin üyeyi etiketle* [**@Üye**]'
                                  f'\n**`Sebep`**: *Banlama sebebin (**Zorunlu değil**)*')
            await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        bans = await ctx.guild.bans()
        for b in bans:
            if b.user.name == member:
                await ctx.guild.unban(b.user, reason=reason)
                embed = discord.Embed(
                    description=f":white_check_mark: *{member.mention}*, *{ctx.message.author.mention}* tarafından **ban'ı kaldırıldı**. :confetti_ball:"
                                f'\n***Sebep:*** **`{reason}`**',
                    colour=discord.Color.green())
                await ctx.send(embed=embed)
                return
        embed = discord.Embed(
            description=f':warning: **`{member}`** adında **banlanmış üye bulunamadı!** :warning: *{ctx.author.mention}*',
            colour=discord.Color.red())
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @unban.error
    async def unban_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description=f':warning: **`Üyeleri Engelle` yetkisine sahip değilsin.** :warning: *{ctx.author.mention}*',
                colour=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                description=f':interrobang: **Eksik Argüman** :interrobang: *{ctx.author.mention}*',
                colour=discord.Color.red())
            embed.add_field(name="Kullanım şekli:", value=f'**`{get_prefix(ctx, ctx)}unban [Üye] (Sebep)`**',
                            inline=False)
            embed.add_field(name="Argümanlar:", value=f'**`Üye`**: *Banı kaldırmak istediğin üyenin adı* [**Üye~~#1234~~**]'
                                                      f'\n**`Sebep`**: *Banı kaldırma sebebin (**Zorunlu değil**)*')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f':interrobang: **Hatalı Unban Komutu Kullanımı** :interrobang: *{ctx.author.mention}*',
                colour=discord.Color.red())
            embed.add_field(name="Kullanım şekli:", value=f'**`{get_prefix(ctx, ctx)}unban [Üye] (Sebep)`**',
                            inline=False)
            embed.add_field(name="Argümanlar:",
                            value=f'**`Üye`**: *Banı kaldırmak istediğin üyenin adı* [**Üye~~#1234~~**]'
                                  f'\n**`Sebep`**: *Banı kaldırma sebebin (**Zorunlu değil**)*')
            await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(
            description=f':white_check_mark: *{member.mention}*, *{ctx.message.author.mention}* tarafından **atıldı**. :hammer:'
                        f'\n***Sebep:*** **`{reason}`**',
            colour=discord.Color.green())
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @kick.error
    async def kick_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description=f':warning: **`Üyeleri At` yetkisine sahip değilsin.** :warning: *{ctx.author.mention}*',
                colour=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, discord.Forbidden):
            embed = discord.Embed(
                description=f':warning: Bot, **sunucu sahibini** veya **kendinden daha yetkili** birini atma yetkisine **sahip değil.** :warning:'
                            f'\n*{ctx.author.mention} Bunun için botun rolünü en üste alın.*',
                colour=discord.Color.red())
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                description=f':interrobang: **Eksik Argüman** :interrobang: *{ctx.author.mention}*',
                colour=discord.Color.red())
            embed.add_field(name="Kullanım şekli:", value=f'**`{get_prefix(ctx, ctx)}kick [Üye] (Sebep)`**', inline=False)
            embed.add_field(name="Argümanlar:", value=f'**`Üye`**: *Atmak istediğin üyeyi etiketle* [**@Üye**]'
                                                      f'\n**`Sebep`**: *Atma sebebin (**Zorunlu değil**)*')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(
                description=f':warning: *Üye **bulunamadı.*** :warning: *{ctx.author.mention}*',
                colour=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f':interrobang: **Hatalı Kick Komutu Kullanımı** :interrobang: *{ctx.author.mention}*',
                colour=discord.Color.red())
            embed.add_field(name="Kullanım şekli:", value=f'**`{get_prefix(ctx, ctx)}kick [Üye] (Sebep)`**', inline=False)
            embed.add_field(name="Argümanlar:", value=f'**`Üye`**: *Atmak istediğin üyeyi etiketle* [**@Üye**]'
                                                      f'\n**`Sebep`**: *Atma sebebin (**Zorunlu değil**)*')
            await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(client):
    client.add_cog(Moderation(client))