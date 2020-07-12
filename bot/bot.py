import boto3
import os

from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

from AWS import factorio_server, util
from util import messages


load_dotenv(find_dotenv())
TOKEN = os.environ.get("token")
INSTANCE_ID = os.environ.get("instance_id")
AWS_ACCESS_KEY_ID = os.environ.get("aws_access_key_id")
AWS_SECRET_ACCESS_KEY = os.environ.get("aws_secret_access_key")

client = commands.Bot(command_prefix='!')  # When typing bot commands, always start with '!'

ec2 = boto3.resource('ec2')
instance = ec2.Instance(INSTANCE_ID)


@client.event
async def on_ready():
    print('Logged in as')
    print('Name: {}'.format(client.user.name))
    print('ID: {}'.format(client.user.id))
    print('Factorio server status: {}!'.format(util.get_state()))
    print('------------')


@client.command()
async def factorio_on(context):
    if util.get_state() == "stopped":
        await factorio_server.turn_on_instance(context, instance)
    elif util.get_state() == "running":
        await context.channel.send("Factorio server is already on!")
    else:
        await messages.print_error(context, "Server is either being turned off or on right now. Wait")


@client.command()
async def factorio_off(context):
    if util.get_state() == "running":
        await factorio_server.turn_off_instance(context, instance)
    elif util.get_state() == "stopped":
        await context.channel.send("Factorio server is already off!")
    else:
        await messages.print_error(context, "Server is either being turned off or on right now. Wait")


@client.command()
async def factorio_status(context):
    await util.send_state_message(context)


@client.command(pass_context=True)
async def clear(context, number: int):
    await messages.clear(context, number)


client.run(TOKEN)
