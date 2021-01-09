import json
from discord.ext import commands
from discord.utils import get
from main import get_autorole_int


class Event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        await ctx.send(f'Yanlış veya eksik komut kullandınız.'
                       f'\nLütfen **>help** komutundan kontrol edin veya yetkili birine başvurun.'
                       f'\n**Hata:** *{ex}*')

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('./jsons/prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = "+"
        with open('./jsons/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        everyoneRoleId = guild.roles[0].id
        with open('./jsons/auto_roles.json', 'r') as f:
            roles = json.load(f)
        roles[str(guild.id)] = everyoneRoleId
        with open('./jsons/auto_roles.json', 'w') as f:
            json.dump(roles, f, indent=4)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        role_id = get_autorole_int(member, member)
        role = get(member.guild.roles, id=role_id)
        print(role_id)
        print(role)
        await member.add_roles(role)


def setup(client):
    client.add_cog(Event(client))
