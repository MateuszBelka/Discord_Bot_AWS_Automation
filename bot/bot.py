import boto3
import os

from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

from AWS import factorio_server
from AWS import util
from util import messages

load_dotenv(find_dotenv())
TOKEN = os.environ.get("TOKEN")
INSTANCE_ID = os.environ.get("INSTANCE_ID")
INSTANCE_REGION = os.environ.get("INSTANCE_REGION")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

client = commands.Bot(command_prefix='!')  # When typing bot commands, always start with '!'

aws_client = boto3.client('ec2',
                          region_name=INSTANCE_REGION,
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
ec2 = boto3.resource('ec2',
                     region_name=INSTANCE_REGION,
                     aws_access_key_id=AWS_ACCESS_KEY_ID,
                     aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
instance = ec2.Instance(INSTANCE_ID)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')


@client.command()
async def factorio_start(context):
    if util.get_state(instance) is not "running":
        await factorio_server.turn_on_instance(instance, context)
    else:
        await context.channel.send("Factorio server is already on!")


@client.command()
async def factorio_stop(context):
    if util.get_state(instance) is "running":
        await factorio_server.turn_off_instance(instance, context)
    else:
        await context.channel.send("Factorio server is already off!")


@client.command()
async def factorio_status(context):
    await util.send_state_message(context, instance)


@client.command(pass_context=True)
async def clear(context, number: int):
    await messages.clear(context, number)


client.run(TOKEN)
