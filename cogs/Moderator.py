from discord.ext import commands
import json

from discord.utils import get

from main import get_prefix, get_autorole, get_autorole_int


class Moderator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["prefixDeğiştir", "prefixdeğiştir", "prefixdeğiş", "prefixayarla"])
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        with open("./jsons/prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open("./jsons/prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        await ctx.channel.send(f'**{ctx.guild.name}** sunucusunun prefix(önek)i  **{prefix}**  ile değiştirildi.')

    @commands.command(aliases=["otoRolDeğiştir", "otoroldeğiştir", "otoroldeğiş", "otorolayarla"])
    @commands.has_permissions(manage_roles=True)
    async def changeautorole(self, ctx, role):
        trash = "<>@&"
        int_role = role
        for char in trash:
            int_role = int_role.replace(char, "")

        with open("./jsons/auto_roles_int.json", "r") as f:
            roles = json.load(f)
        roles[str(ctx.guild.id)] = int(int_role)
        with open("./jsons/auto_roles_int.json", "w") as f:
            json.dump(roles, f, indent=4)

        with open("./jsons/auto_roles.json", "r") as f:
            roles = json.load(f)
        roles[str(ctx.guild.id)] = role
        with open("./jsons/auto_roles.json", "w") as f:
            json.dump(roles, f, indent=4)
        await ctx.channel.send(f'**{ctx.guild.name}** sunucusunun oto rolü  **{role}**  ile değiştirildi.')

    @commands.command(aliases=["prefix", "önek", "onek"])
    async def getprefix(self, ctx):
        prefix = get_prefix(ctx, ctx)
        await ctx.send(f"**{ctx.guild.name}** sunucusunun prefix'i  **{prefix}**")

    @commands.command(aliases=["otorol"])
    async def getautorole(self, ctx):
        role_id = get_autorole_int(ctx, ctx)
        role = ctx.guild.get_role(role_id=role_id)
        await ctx.send(f"**{ctx.guild.name}** sunucusunun oto rolü  **{role.mention}**")

    @commands.command()
    async def oi(self, member):
        role_id = get_autorole_int(member, member)
        role = get(member.guild.roles, id=role_id)
        await member.add_roles(role)
        await member.send(role.mention)


def setup(client):
    client.add_cog(Moderator(client))
