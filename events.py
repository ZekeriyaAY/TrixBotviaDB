import discord
from discord.ext import commands
import json


class EventsCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = '>'
        with open('prefixes.json', 'w') as f:
            json.dump(prefixes,f)


        with open('autoroles.json', 'r') as f:
            roles = json.load(f)
        everyoneRole = guild.roles[0].id
        roles[str(guild.id)] = everyoneRole.id
        with open('autoroles.json', 'w') as f:
            json.dump(roles,f)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        pass

def setup(client):
    client.add_cog(EventsCog(client))