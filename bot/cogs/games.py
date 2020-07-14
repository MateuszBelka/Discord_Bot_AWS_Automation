# Authors:   Emil Andrzejewski
# Created:  14-Jul-2020

from discord.ext import commands
from gaw.controller import GuessAWordGame

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def gaw(self, ctx):
        pass

    @gaw.command(name="start")
    async def gaw_start(self, ctx):
        guild = ctx.guild
        author = ctx.author
        players = list()

        game = GuessAWordGame()
        await game.start_game(guild, author, players)

    @gaw.command(name="g")
    async def gaw_guess(self, ctx):
        pass

def setup(client):
    client.add_cog(Games(client))