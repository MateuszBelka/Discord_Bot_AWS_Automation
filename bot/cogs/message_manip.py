# Authors:   Emil Andrzejewski
# Created:  16-Jul-2020

from functions import text_to_owo

from discord.ext import commands

class Message_manip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def owo(self, ctx):
        owo_text = text_to_owo(ctx.message.content)
        if owo_text.startswith('$owo'):
            owo_text = owo_text[4:]
        await ctx.send(owo_text)

def setup(bot):
    bot.add_cog(Message_manip(bot))