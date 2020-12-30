import discord
from discord.ext import commands
import json



class AdminCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["prefixDeğiştir","prefixdeğiştir","prefixdeğiş"])
    @commands.has_permissions(administrator = True)
    async def changeprefix(self, ctx, prefix):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open("prefixes.json","w") as f:
            json.dump(prefixes,f)
        await ctx.channel.send(f'**{ctx.guild.name}** sunucusunun prefix(önek)i  **{prefix}**  ile değiştirildi.')

    @commands.command(aliases=["otoRolDeğiştir","otoroldeğiştir","otoroldeğiş"])
    @commands.has_permissions(administrator = True)
    async def changeautorole(self, ctx, role):
        with open("autoroles.json", "r") as f:
            roles = json.load(f)
        roles[str(ctx.guild.id)] = role
        with open("autoroles.json","w") as f:
            json.dump(roles,f)
        await ctx.channel.send(f'**{ctx.guild.name}** sunucusunun oto rolü  **{role}** ile değiştirildi.')

    @commands.command(aliases=["prefix"])
    @commands.has_permissions(administrator = True)
    async def getprefix(self, ctx):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        print(prefixes[str(ctx.guild.id)])


def setup(client):
    client.add_cog(AdminCog(client))