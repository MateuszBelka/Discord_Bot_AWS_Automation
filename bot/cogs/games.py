# Authors:   Emil Andrzejewski
# Created:  14-Jul-2020
import random

import discord
from discord.ext import commands

from gaw.controller import GuessAWordGame


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def gaw(self, ctx):
        ctx.gaw_game = GuessAWordGame()

    @gaw.command(name="start")
    async def gaw_start(self, ctx, *members: discord.Member):
        guild = ctx.guild
        author = ctx.author
        players = list()

        for m in members:
            players.append(m)

        channel = await ctx.gaw_game.start_game(guild, author, players) # Zapisuje boola z funkcji start_game w zmiennej result
        # Uzywamy boola do nastepnych dzialan$
        if channel is None:
            await ctx.send("Taka gra juz istnieje! Aby stworzyc nowa gre zamknij istniejaca.")
        else:
            game = ctx.gaw_game.fetch_game()
            await ctx.send("Aby zaczac gre wejdz w nowo stworzony kanal.")
            await channel.send("Kategoria: %s, Dlugosc slowa: %s" % (game.category, len(game.word)))

    @gaw.command(name="g")
    async def gaw_guess(self, ctx, guess: str):
        channel = ctx.channel
        author = ctx.author
        result, hint = ctx.gaw_game.guess(channel.id, guess)

        if result is None:
            await ctx.send('Nie mozesz grac na tym kanale.')
        elif result is True:
            await ctx.send('%s wygrales!' % author.name)
            # nastepna runda
            ctx.gaw_game.new_round(channel)
            new_round = ctx.gaw_game.fetch_game()
            await channel.send("Kategoria: %s, Dlugosc slowa: %s" % (new_round.category, len(new_round.word)))
        elif result is False and hint != "":
            await ctx.send('%s byles bardzo blisko!' % author.name)

    @gaw.command(name="end")
    async def gaw_end(self, ctx):
        guild = ctx.guild
        channel = ctx.channel
        await ctx.gaw_game.destroy(guild, channel.id)


    # 8 BALL
    @commands.command(aliases=['8ball', 'przepowiednia'])
    async def _8ball(self, ctx, *, question):
        responses = ['+1 byczku',
                     '+0.7 byczku',
                     'Si si toro',
                     'To jest niemożliwe do przewidzenia',
                     'Ooooj tak',
                     'Nie ma chuja',
                     'Ta ta jasne',
                     'We zapytaj jeszcze raz',
                     'Matematyczna szansa',
                     'Prędzej Duda przestanie być prezydentem',
                     'Zapytaj czy mnie to obchodzi',
                     'Głupie pytanie',
                     'Tak, a ja jestem papieżem',
                     'Zrób to, co zrobiłby jezus - umrzyj w wieku 33 lat',
                     'Przestań pytać czy Tom Cruise jest gejem i sprawdź to samemu',
                     'Trump wykorzystuje mnie przy podejmowaniu decyzji o wszczęciu wojny']
        await ctx.send(f'{random.choice(responses)}')

def setup(client):
    client.add_cog(Games(client))