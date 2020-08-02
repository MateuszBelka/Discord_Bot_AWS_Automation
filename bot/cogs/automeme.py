# Authors:   Emil Andrzejewski
# Created:  16-Jul-2020

from discord.ext import commands
import praw
import aiohttp
import os
from dotenv import load_dotenv, find_dotenv
import random
import time
from discord.ext import tasks
from bot import unload

load_dotenv(find_dotenv())
REDDIT_APP_ID = os.environ.get("REDDIT_APP_ID")
REDDIT_APP_SECRET = os.environ.get("REDDIT_APP_SECRET")
REDDIT_ENABLED_MEME_SUBREDDITS = os.environ.get("REDDIT_ENABLED_MEME_SUBREDDITS")

start_time = time.time()
repeat = 300.0

class Automeme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_SECRET, user_agent="shr1mpBot:%s:1.0" % REDDIT_APP_ID)

    # AUTO MEMIK
    @commands.command()
    async def automemik(self, ctx):
        async with ctx.channel.typing():
            if self.reddit:
                # start working
                chosen_subreddit = 'dankmemes'

                submissions = self.reddit.subreddit(chosen_subreddit).hot()

                post_to_pick = random.randint(1, 10)

                while True:
                    for i in range(0, post_to_pick):
                        submission = next(x for x in submissions if not x.stickied)
                    await ctx.send(submission.url)
                    time.sleep(repeat - ((time.time() - start_time) % repeat))
                    # Pathological solution rn - you cannot use other commands when this one is used.
                    # todo: Implement a solution which would allow this code to run in the background

def setup(bot):
    bot.add_cog(Automeme(bot))