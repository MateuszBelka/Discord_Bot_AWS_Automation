# Author:   Mateusz Belka
# Created:  12-Jul-2020


async def send_state_message(context, instance):
    if get_state(instance) is "running":
        await context.channel.send("Factorio server is running!")
    else:
        await context.channel.send("Factorio server is NOT running!")


def get_state(instance):
    return instance.state['Name']