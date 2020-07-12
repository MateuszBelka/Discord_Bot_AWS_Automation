# Author:   Mateusz Belka
# Created:  12-Jul-2020
import time
import boto3
import os

from util import messages


async def send_state_message(context):
    await context.channel.send("Factorio server is {}!".format(get_state()))


def get_state():
    instance_id = os.environ.get("INSTANCE_ID")

    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)    # Set new instance to get updates info about it's status
    return instance.state['Name']


async def server_state_change_update(context, intermediate_state, final_state):
    interval = 5
    time_limit = int(60 / interval)

    if final_state == "stopped":
        await context.channel.send("Turning off the server!")
    elif final_state == "running":
        await context.channel.send("Turning on the server!")

    for i in range(0, time_limit):
        time.sleep(interval)

        state = get_state()
        print("Factorio server status: {}".format(state))

        if state == final_state:
            await messages.clear(context, i - 1)
            await context.channel.send("Factorio server status is now: {}!".format(final_state.capitalize()))
            break
        elif i == time_limit - 1:
            await messages.clear(context, i - 1)
            await messages.print_error(context, "Factorio server status did not change to {} in time".format(final_state.capitalize()))
        else:
            if state == intermediate_state:
                await context.channel.send("...")
            else:
                await messages.print_error(context, "Unexpected instance state")
