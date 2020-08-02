# Author:   Mateusz Belka
# Created:  11-Jul-2020
import cogs.aws
from util import messages, aws


async def turn_off_instance(ctx, instance):
    if did_instance_stop(instance):
        await aws.server_state_change_update(ctx, "stopped")
    else:
        await messages.perror(ctx, "Failed to stop the {} server".format(cogs.aws.Aws.channel_game_map[ctx.channel.name]))


def did_instance_stop(instance):
    try:
        instance.stop()
        return True
    except:
        return False


async def turn_on_instance(ctx, instance):
    if did_instance_start(instance):
        await aws.server_state_change_update(ctx, "running")
    else:
        await messages.perror(ctx, "Failed to start the {} server".format(cogs.aws.Aws.channel_game_map[ctx.channel.name]))


def did_instance_start(instance):
    try:
        instance.start()
        return True
    except:
        return False
