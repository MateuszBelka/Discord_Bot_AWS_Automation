import time

import boto3
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

from aws import factorio_server, util
from util import messages

load_dotenv(find_dotenv())
TOKEN = os.environ.get("TOKEN")
INSTANCE_ID = os.environ.get("INSTANCE_ID")

client = commands.Bot(command_prefix='!')  # When typing bot commands, always start with '!'
client.remove_command('help')

ec2 = boto3.resource('ec2')
instance = ec2.Instance(INSTANCE_ID)


@client.event
async def on_ready():
    print('Logged in as')
    print('Name: {}'.format(client.user.name))
    print('ID: {}'.format(client.user.id))
    print('Factorio server status: {}!'.format(util.get_state()))
    print('------------')
    factorio_channel = await messages.clear_factorio_text_channel(client)
    await messages.factorio_welcome_message(factorio_channel)
    await factorio_channel.send(embed=messages.help_embed())


@client.event
async def on_member_join(member):
    print(f'{member} joined the SHR1MP Clan!')
    # print jest do terminala a nie do discorda
    # ciebie interesuje chyba context.send(string)


@client.event
async def on_member_remove(member):
    print(f'{member} left the SHR1MP Clan...')
    # print jest do terminala a nie do discorda
    # ciebie interesuje chyba context.send(string)


@client.command()
async def help(context):
    author = context.message.author
    await author.send(embed=messages.help_embed())
    await messages.clear(context, 1)


@client.command()
async def shrimp(ctx):
    await ctx.send(f'shromp (latency: {round(client.latency * 1000)} ms)')


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
async def factorio_on(context):
    if util.get_state() == "stopped":
        await factorio_server.turn_on_instance(context, instance)
    elif util.get_state() == "running":
        await context.send("Factorio server is already **ONLINE**!")
    else:
        await messages.print_error(context, "Server is either being turned off or on right now. Wait")


@client.command()
async def factorio_off(context):
    if util.get_state() == "running":
        await factorio_server.turn_off_instance(context, instance)
    elif util.get_state() == "stopped":
        await context.send("Factorio server is already **OFFLINE**!")
    else:
        await messages.print_error(context, "Server is either being turned off or on right now. Wait")


@client.command()
async def factorio_status(context):
    channel = context.channel
    await messages.purge(channel)
    await util.send_state_message(channel, "Factorio")


@client.command(pass_context=True)
async def clear(context, number: int):
    await messages.clear(context, number + 1)


@client.command()
async def nuke(context):
    return await messages.reset_channel(context, discord)


client.run(TOKEN)
