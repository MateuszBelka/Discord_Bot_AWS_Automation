# Author:   Mateusz Belka
# Created:  11-Jul-2020


async def clear(msg_context, number):
    # Clears X messages in the channel that the command has been sent
    await msg_context.channel.purge(limit=number + 1)

    debug_msg = "Cleared {}".format(number)
    if number == 1:
        debug_msg += " message!"
    else:
        debug_msg += " messages!"
    print(debug_msg)
