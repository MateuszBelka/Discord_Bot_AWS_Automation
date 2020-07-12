# Author:   Mateusz Belka
# Created:  11-Jul-2020


async def clear(context, number):
    # Clears X messages in the channel that the command has been sent
    await context.channel.purge(limit=number + 1)


async def print_error(context, msg):
    final_msg = "ERROR: " + msg + "!"
    await context.channel.send(final_msg)