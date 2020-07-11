from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os
from util import messages
from InputHandler import onReactionAdd


client = commands.Bot(command_prefix='!')
load_dotenv(find_dotenv())
TOKEN = os.environ.get("TOKEN")


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_reaction_add(reaction, user):
    await onReactionAdd.send_confirmation_msg(reaction, user)


@client.command(pass_context=True)
async def clear(ctx, number: int):
    await messages.clear(ctx, number)


client.run(TOKEN)
