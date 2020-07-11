import discord
import os
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
load_dotenv(find_dotenv())
token = os.environ.get("TOKEN")

@client.event
async def on_ready():
    print('Bot is ready.')


client.run(token)
