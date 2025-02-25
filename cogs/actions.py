import discord as ds
from discord.ext import commands

class Actions(commands.cog):
    def __init__(self, client):
        self.client = client

    #Evento
    @commands.Cog.listener()
    async def on_ready(self):
        print('Tá rodando liso')

    #Comandos
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

async def setup(client):
    await client.add_cog(Actions(client))