import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')


client.run('NzMxMjg3MDkyNTAzNzczMjA2.XwkK3w.fwR-g41I3MzomR_nt1HKTpXRCtA')
