# Author:   Mateusz Belka
# Created:  12-Jul-2020
import time
import boto3
import os
import discord

from util import messages


async def send_state_message(channel, prefix):
    await channel.send("{} server status: **{}**!".format(prefix, get_state().upper()))


def get_state():
    instance_id = os.environ.get("INSTANCE_ID")

    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)    # Set new instance to get updated info about it's status
    return instance.state['Name']


async def server_state_change_update(ctx, final_state, prefix):
    interval = 5
    time_limit = 60

    if final_state == "stopped":
        await ctx.send("Turning the server **OFF**!")
    elif final_state == "running":
        await ctx.send("Turning the server **ON**!")

    message_content = "..."
    await ctx.send(message_content)
    channel = ctx.channel
    last_messageID = channel.last_message_id
    last_message = await discord.TextChannel.fetch_message(channel, last_messageID)
    for i in range(0, time_limit):
        message_content += "."
        await last_message.edit(content=message_content)

        time.sleep(1)
        if i % interval == 0:

            state = get_state()
            if state == final_state:
                # await messages.clear(ctx, i - 1)
                await messages.purge(ctx.channel)
                await ctx.send("{} server status is now: **{}**!".format(prefix, final_state.upper()))
                break
            elif i == time_limit - 1:
                # await messages.clear(ctx, i - 1)
                await messages.purge(ctx.channel)
                await messages.perror(ctx, "{} server status did not change to **{}** in time".format(prefix, final_state.upper()))
