# Author:   Mateusz Belka
# Created:  11-Jul-2020
#
# Clears messages in the channel that the command has been sent


async def clear(ctx, number):
    await ctx.channel.purge(limit=number + 1)

    debug_msg = "Cleared {}".format(number)
    if number == 1:
        debug_msg += " message!"
    else:
        debug_msg += " messages!"
    print(debug_msg)