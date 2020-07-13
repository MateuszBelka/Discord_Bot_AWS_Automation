# Authors:   Emil Andrzejewski
# Created:  14-Jul-2020
import aiohttp
from discord.ext import commands
import discord

class images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ZDJECIA KOTOW
    @commands.command()
    async def kotek(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Miau")
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat/")

                    await ctx.send(embed=embed)

    # ZDJECIA PSOW
    @commands.command()
    async def piesek(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Hau hau")
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="https://random.dog/")

                    await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(images(bot))