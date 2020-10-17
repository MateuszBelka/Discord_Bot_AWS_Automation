# Authors:   Mateusz Belka, Emil Andrzejewski
# Created:  11-Jul-2020
from cogs.aws import Aws
from util import aws


async def clear(channel, number):
    # Clears 'number' of messages in the channel that the command has been sent
    await channel.purge(limit=number)


async def reset_channel(channel):
    name = channel.name
    guild = channel.guild

    await delete_channel(channel)
    await create_new_channel(name, guild)


async def delete_channel(channel):
    await channel.delete()


async def create_new_channel(name, guild):
    return await guild.create_text_channel(name)


async def perror(channel, msg):
    final_msg = "ERROR: " + msg + "!"
    await channel.send(final_msg)


async def aws_all_servers_status(client):
    awsChannel = None
    for guild in client.guilds:
        if (guild.name == "SHR1MP") or (guild.name == "shr1mpBot test"):
            for aws_channel_name in Aws.supported_channels:
                for guild_channel in guild.channels:
                    if guild_channel.name == aws_channel_name:
                        awsChannel = guild_channel
                        break

                if awsChannel is not None:
                    await purge(awsChannel)
                else:
                    awsChannel = await create_new_channel(aws_channel_name, guild)

                await aws_server_status_message(awsChannel)
                awsChannel = None


async def aws_server_status_message(channel):
    await purge(channel)
    if channel is not None and channel.name in Aws.supported_channels:
        print("{} server status: {}!".format(Aws.channel_game_map[channel.name], aws.get_state(channel).upper()))
        await channel.send("**Commands Available on this channel:** ($help for more)\n"
                           "$server {start, on}, {stop, off}, status, reboot\n"
                           "-------------------\n")
        await channel.send("{} server status: **{}**!".format(Aws.channel_game_map[channel.name], aws.get_state(channel).upper()))
        await channel.send("{} server's public ip: **{}**".format(Aws.channel_game_map[channel.name], aws.get_instance_from_channel(channel).public_ip_address))


async def purge(channel):
    await channel.purge()
