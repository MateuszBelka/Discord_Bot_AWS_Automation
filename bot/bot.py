import platform

import discord
from discord.ext import commands
from util import privileges
from settings import *

from util import messages

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('DM me $help'))
    print('Logged in as')
    print('Name: {}'.format(client.user.name))
    print('ID: {}'.format(client.user.id))
    print('------------')
    await messages.aws_all_servers_status(client)


@client.event
async def on_member_join(member):
    print(f'{member} joined the SHR1MP Clan!')


@client.event
async def on_member_remove(member):
    print(f'{member} left the SHR1MP Clan...')


# Error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await messages.perror(ctx, "Additional argument is required")
    elif isinstance(error, commands.MissingPermissions):
        await messages.perror(ctx, "You don't have permissions to use this command")
    elif isinstance(error, commands.CommandNotFound):
        await messages.perror(ctx, "Invalid command used")


##############################################################################

@client.command()
async def stats(ctx):
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))
    await ctx.send(f'Liczba osób na serwerze: {memberCount} :CattoBlush: Korzystam z Pythona '
                   f'{pythonVersion} i Discorda {dpyVersion}.')


@client.command()
async def shrimp(ctx):
    await ctx.send(f'shromp (latency: {round(client.latency * 1000)} ms)')


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number: int):
    await messages.clear(ctx, number + 1)


# Error handling for clear (when there will be no specified int value given)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('This command requires additional information.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permissions to use this command")


@client.command()
@commands.check(privileges.nuke_priv)
async def nuke(ctx):
    await messages.reset_channel(ctx)


# @client.command()
# async def automemeoff():
# unload(automeme)
# return True

# LOADING / UNLOADING COGS

@client.command()
async def load(extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(extension):
    client.unload_extension(f'cogs.{extension}')
    return True


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

###########################################################

client.run(TOKEN)
