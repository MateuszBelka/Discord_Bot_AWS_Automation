import boto3
import os

from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

from AWS import factorio_server
from util import messages


load_dotenv(find_dotenv())
TOKEN = os.environ.get("TOKEN")
INSTANCE_ID = os.environ.get("TOKEN")
BOT_NAME = "shr1mpBot"
is_factorio_server_on = None

client = commands.Bot(command_prefix='!')  # When typing bot commands, always start with '!'
ec2 = boto3.client('ec2')
instance = ec2.Instance(INSTANCE_ID)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')


@client.command()
async def factorio_start(context):
    global is_factorio_server_on
    if not is_factorio_server_on:
        await factorio_server.turn_on_instance(instance, context)
        is_factorio_server_on = True
    else:
        await context.channel.send("Factorio server is already on!")


@client.command()
async def factorio_stop(context):
    global is_factorio_server_on
    if is_factorio_server_on:
        await factorio_server.turn_off_instance(instance, context)
        is_factorio_server_on = False
    else:
        await context.channel.send("Factorio server is already off!")



@client.command()
async def factorio_status(context):
    channel = context.channel
    await channel.send("Factorio server is ONLINE" if is_factorio_server_on else "Factorio server is OFFLINE")


@client.command(pass_context=True)
async def clear(context, number: int):
    await messages.clear(context, number)


client.run(TOKEN)
