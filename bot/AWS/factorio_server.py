# Author:   Mateusz Belka
# Created:  11-Jul-2020


async def turn_off_instance(instance, context):
    if did_instance_stop(instance):
        await context.channel.send("Factorio server has been stopped!")
    else:
        await context.channel.send("Error stopping the Factorio server")


def did_instance_stop(instance):
    try:
        instance.stop(False, False, False)
        return True
    except:
        return False


async def turn_on_instance(instance, context):
    if did_instance_start(instance):
        await context.channel.send("Factorio server has been started!")
    else:
        await context.channel.send("Error starting the Factorio server")


def did_instance_start(instance):
    try:
        instance.start("", False)
        return True
    except:
        return False
