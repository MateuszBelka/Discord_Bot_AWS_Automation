# Author:   Mateusz Belka
# Created:  12-Jul-2020
import time
import boto3
import os
import discord
from mcstatus import MinecraftServer

import cogs.aws
from util import messages, aws_instance_state


def get_instance_from_channel(channel):
    instance_name = ""
    for supported_channel in cogs.aws.Aws.supported_channels:
        if channel.name == supported_channel:
            instance_name = cogs.aws.Aws.channel_game_map[supported_channel]

    instance_id = os.environ.get("INSTANCE_ID_{}".format(instance_name.upper()))

    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)  # Set new instance to get updated info about it's status
    return instance


def get_state(channel):
    instance = get_instance_from_channel(channel)
    return instance.state['Name']


async def server_state_change_update(channel, final_state):
    interval = 5
    time_limit = 60

    await messages.purge(channel)

    if final_state == "stopped":
        await channel.send("Turning the {} server **OFF**!".format(cogs.aws.Aws.channel_game_map[channel.name]))
    elif final_state == "running":
        await channel.send("Turning the {} server **ON**!".format(cogs.aws.Aws.channel_game_map[channel.name]))

    message_content = "..."
    await channel.send(message_content)
    last_messageID = channel.last_message_id
    last_message = await discord.TextChannel.fetch_message(channel, last_messageID)
    for i in range(0, time_limit):
        message_content += "."
        await last_message.edit(content=message_content)

        time.sleep(1)
        if i % interval == 0:

            state = get_state(channel)
            if state == final_state:
                await messages.purge(channel)
                await messages.aws_server_status_message(channel)
                break
            elif i == time_limit - 1:
                await messages.purge(channel)
                await messages.perror(channel, "{} server status did not change to **{}** in time".format(
                    cogs.aws.Aws.channel_game_map[channel.name], final_state.upper()))


# Currently supporting only minecraft server
async def turn_off_mcserver_check_loop(channel):
    timeout_check_interval_sec = 300
    turn_off_server = False

    time.sleep(60)  # Extra 60 seconds to allow server to start running
    while True:
        print()
        print("Checking Minecraft Server inactivity status")

        await countdown(timeout_check_interval_sec, channel)

        server_status = get_state(channel).upper()
        if server_status != "RUNNING":
            break

        server_ip = get_instance_from_channel(channel).public_ip_address
        server = MinecraftServer.lookup(server_ip)
        status = server.status()
        if status.players.online == 0:
            turn_off_server = True

        if turn_off_server:
            print("Turning the server off due to lack of activity")
            await aws_instance_state.turn_off_instance(channel, cogs.aws.Aws.channel_instanceId_map[channel.name])
            break


async def countdown(t, channel):
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    await channel.send(
        "{} server inactivity check in: **{}**".format(cogs.aws.Aws.channel_game_map[channel.name], timer))
    last_messageID = channel.last_message_id
    last_message = await discord.TextChannel.fetch_message(channel, last_messageID)

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        await last_message.edit(
            content="{} server inactivity check in: **{}**".format(cogs.aws.Aws.channel_game_map[channel.name], timer))

        time.sleep(1)
        t -= 1

    await last_message.delete()
