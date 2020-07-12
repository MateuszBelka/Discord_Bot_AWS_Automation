# Author:   Mateusz Belka
# Created:  12-Jul-2020
import time
import boto3
import os
import discord

from util import messages


async def send_state_message(channel, prefix):
    await channel.send("{} server is {}!".format(prefix, get_state()))


def get_state():
    instance_id = os.environ.get("INSTANCE_ID")

    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)    # Set new instance to get updated info about it's status
    return instance.state['Name']


async def server_state_change_update(context, intermediate_state, final_state, prefix):
    interval = 5
    time_limit = int(60 / interval)

    if final_state == "stopped":
        await context.send("Turning **OFF** the server!")
    elif final_state == "running":
        await context.send("Turning **ON** the server!")

    for i in range(0, time_limit):
        time.sleep(interval)

        state = get_state()
        if state == final_state:
            # await messages.clear(context, i - 1)
            await messages.reset_channel(context, discord)
            await context.send("{} server status is now: **{}**!".format(prefix, final_state.upper()))
            break
        elif i == time_limit - 1:
            # await messages.clear(context, i - 1)
            await messages.reset_channel(context, discord)
            await messages.print_error(context, "{} server status did not change to **{}** in time".format(prefix, final_state.upper()))
        else:
            if state == intermediate_state:
                await context.send("...")
            else:
                await messages.print_error(context, "Unexpected instance state")
