from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import os
import random

from util import messages

client = commands.Bot(command_prefix='!')  # When typing bot commands, always start with '!'
load_dotenv(find_dotenv())
TOKEN = os.environ.get("TOKEN")
is_factorio_server_on = None


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

@client.event
async def on_member_join(member):
    print(f'{member} joined the SHR1MP Clan!')

@client.event
async def on_member_remove(member):
    print(f'{member} left the SHR1MP Clan...')

@client.command()
async def shrimp(ctx):
    await ctx.send(f'shromp (latency: {round(client.latency*1000)} ms)')

@client.command(aliases=['8ball', 'przepowiednia'])
async def _8ball(ctx, *, question):
    responses = ['+1 byczku',
                 '+0.7 byczku',
                 'Si si toro',
                 'To jest niemozliwe do przewidzenia',
                 'Ooooj tak',
                 'Nie ma chuja',
                 'Ta ta jasne',
                 'We zapytaj jeszcze raz',
                 'Matematyczna szansa']
    await ctx.send(f'{random.choice(responses)}')



@client.command()
async def factorio_start(context):
    global is_factorio_server_on
    is_factorio_server_on = True
    channel = context.channel
    await channel.send("Factorio server has been started!")


@client.command()
async def factorio_stop(context):
    global is_factorio_server_on
    is_factorio_server_on = False
    channel = context.channel
    await channel.send("Factorio server has been stopped!")



@client.command()
async def factorio_status(context):
    channel = context.channel
    await channel.send("Factorio server is " + "ONLINE" if is_factorio_server_on else "OFFLINE")


@client.command(pass_context=True)
async def clear(context, number: int):
    await messages.clear(context, number)


client.run(TOKEN)
