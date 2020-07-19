# Author:   Mateusz Belka
# Created:  13-Jul-2020
import os
import boto3
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

from aws import factorio_server, util
from util import messages


async def server_status(ctx):
    channel = ctx.channel
    await messages.factorio_status_message_known_channel(channel)


class Factorio(commands.Cog):

    def __init__(self, client):
        self.client = client

        load_dotenv(find_dotenv())
        self.ec2 = boto3.resource('ec2')
        self.instance = self.ec2.Instance(os.environ.get("INSTANCE_ID"))

    # Commands
    @commands.command()
    async def factorio(self, ctx, *cmds):
        if 'on' in cmds or 'start' in cmds:
            print("Turning factorio server ON!")
            await self.server_start(ctx)
        elif 'off' in cmds or 'stop' in cmds:
            print("Turning factorio server OFF!")
            await self.server_stop(ctx)
        elif 'status' in cmds:
            print("Checking factorio server status!")
            await server_status(ctx)
        else:
            await messages.perror(ctx, "Try: $factorio on, start, off, stop, status. You need to use of those arguments in combination with $factorio")

    async def server_start(self, ctx):
        if util.get_state() == "stopped":
            await factorio_server.turn_on_instance(ctx, self.instance)
        elif util.get_state() == "running":
            await ctx.send("Factorio server is already **ONLINE**!")
        else:
            await messages.perror(ctx, "Server is either being turned off or on right now. Wait")

    async def server_stop(self, ctx):
        if util.get_state() == "running":
            await factorio_server.turn_off_instance(ctx, self.instance)
        elif util.get_state() == "stopped":
            await ctx.send("Factorio server is already **OFFLINE**!")
        else:
            await messages.perror(ctx, "Server is either being turned off or on right now. Wait")


def setup(client):
    client.add_cog(Factorio(client))
