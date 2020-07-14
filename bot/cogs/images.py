# Authors:   Emil Andrzejewski
# Created:  14-Jul-2020
import random
import aiohttp
from discord.ext import commands
import discord
from dotenv import load_dotenv, find_dotenv
import os

import praw

load_dotenv(find_dotenv())
REDDIT_APP_ID = os.environ.get("REDDIT_APP_ID")
REDDIT_APP_SECRET = os.environ.get("REDDIT_APP_SECRET")
REDDIT_ENABLED_MEME_SUBREDDITS = os.environ.get("REDDIT_ENABLED_MEME_SUBREDDITS")

class images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_SECRET, user_agent="shr1mpBot:%s:1.0" %REDDIT_APP_ID)

    # MEMIKI Z REDDITA
    @commands.command()
    async def memik(self, ctx, subreddit: str = ""):
        async with ctx.channel.typing():
            if self.reddit:
                #start working
                chosen_subreddit = 'dankmemes'
                if subreddit:
                    if subreddit in REDDIT_ENABLED_MEME_SUBREDDITS:
                        chosen_subreddit = subreddit
                    else:
                        await ctx.send(f'Ten subreddit nie jest dostepny... Wybierz z tych: {REDDIT_ENABLED_MEME_SUBREDDITS}')
                        return

                submissions = self.reddit.subreddit(chosen_subreddit).hot()

                post_to_pick = random.randint(1,10)
                for i in range(0, post_to_pick):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.url)

            else:
                await ctx.send('Cos nie dziala... skontaktuj sie z administratorem.')

    # ZDJECIA KOTOW
    @commands.command(brief="Randomowe zdjecie kota")
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
    @commands.command(brief="Randomowe zdjecie psa")
    async def piesek(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Hau hau")
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="https://random.dog/")

                    await ctx.send(embed=embed)

    # ZDJECIA LISOW
    @commands.command(brief="Randomowe zdjecie lisa")
    async def lisek(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Floof")
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="https://randomfox.ca/")

                    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(images(bot))