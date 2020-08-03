# Author:   Mateusz Belka
# Created:  12-Jul-2020
import time
import boto3
import os
import discord

import cogs.aws
from util import messages


def get_instance_from_channel(channel):
    instance_name = ""
    for supported_channel in cogs.aws.Aws.supported_channels:
        if channel.name == supported_channel:
            instance_name = cogs.aws.Aws.channel_game_map[supported_channel]

    instance_id = os.environ.get("INSTANCE_ID_{}".format(instance_name.upper()))

    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)    # Set new instance to get updated info about it's status
    return instance


def get_state(channel):
    instance = get_instance_from_channel(channel)
    return instance.state['Name']


async def server_state_change_update(ctx, final_state):
    interval = 5
    time_limit = 60

    if final_state == "stopped":
        await ctx.send("Turning the {} server **OFF**!".format(cogs.aws.Aws.channel_game_map[ctx.channel.name]))
    elif final_state == "running":
        await ctx.send("Turning the {} server **ON**!".format(cogs.aws.Aws.channel_game_map[ctx.channel.name]))

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

            state = get_state(ctx.channel)
            if state == final_state:
                await messages.purge(ctx.channel)
                await messages.aws_server_status_message_known_channel(ctx.channel)
                break
            elif i == time_limit - 1:
                await messages.purge(ctx.channel)
                await messages.perror(ctx, "{} server status did not change to **{}** in time".format(cogs.aws.Aws.channel_game_map[ctx.channel.name], final_state.upper()))
