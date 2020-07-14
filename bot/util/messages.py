# Authors:   Mateusz Belka, Emil Andrzejewski
# Created:  11-Jul-2020
from aws import util


async def clear(ctx, number):
    # Clears 'number' of messages in the channel that the command has been sent
    await ctx.channel.purge(limit=number)


async def reset_channel(ctx):
    name = ctx.channel.name
    guild = ctx.channel.guild

    await delete_channel(ctx)
    await create_new_channel(name, guild)


async def delete_channel(ctx):
    await ctx.channel.delete()


async def create_new_channel(name, guild):
    await guild.create_text_channel(name)


async def perror(ctx, msg):
    final_msg = "ERROR: " + msg + "!"
    await ctx.send(final_msg)


async def clear_factorio_text_channel_known_client(client):
    channel_name = "bot-factorio"
    factorioChannel = None
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.name == channel_name:
                factorioChannel = channel
                break
        if factorioChannel is not None:
            await purge(factorioChannel)
        else:
            await create_new_channel(channel_name, guild)
    return factorioChannel


async def factorio_status_message_known_client(client):
    factorio_channel = await clear_factorio_text_channel_known_client(client)
    if factorio_channel is not None:
        print("Factorio server is {}!".format(util.get_state().upper()))
        await factorio_channel.send("Factorio server is **{}**!".format(util.get_state().upper()))


async def factorio_status_message_known_channel(channel):
    if channel is not None:
        print("Factorio server is {}!".format(util.get_state().upper()))
        await channel.send("Factorio server is **{}**!".format(util.get_state().upper()))


async def purge(channel):
    await channel.purge()
