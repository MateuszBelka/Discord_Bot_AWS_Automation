# Authors:   Mateusz Belka, Emil Andrzejewski
# Created:  11-Jul-2020
from aws import util
import discord

def help_embed():
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )
    embed.set_author(name='Getting Started')
    embed.add_field(name='$help', value='Placeholder', inline=False)
    embed.add_field(name='$shrimp', value='Placeholder', inline=False)
    embed.add_field(name='$przepowiednia', value='Placeholder', inline=False)
    embed.add_field(name='$8ball', value='Placeholder', inline=False)
    embed.add_field(name='$factorio_on', value='Placeholder', inline=False)
    embed.add_field(name='$factorio_off', value='Placeholder', inline=False)
    embed.add_field(name='$factorio_status', value='Placeholder', inline=False)
    embed.add_field(name='$clear {integer}', value='Placeholder', inline=False)
    embed.add_field(name='$nuke', value='Placeholder', inline=False)

    return embed

async def clear(ctx, number):
    # Clears 'number' of messages in the channel that the command has been sent
    await ctx.channel.purge(limit=number)


async def reset_channel(ctx, discord):
    # If you decide to use this function, make sure to catch the return object, because ctx will not longer work
    author = ctx.message.author.name
    array = ["Regis", "futomak"]
    if author in array:  # todo: For actual bot set this to some rank
        name = ctx.channel.name
        guild = ctx.channel.guild

        await delete_channel(ctx)
        return await create_new_channel(name, guild, discord)
    else:
        await perror(ctx, "Only Regis and futomak can use this command")


async def delete_channel(ctx):
    await ctx.channel.delete()


async def create_new_channel(name, guild, discord):
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(send_messages=False)
        # todo: Add more limitations on shrimp server
    }
    return await guild.create_text_channel(name, overwrites=overwrites)


async def perror(ctx, msg):
    final_msg = "ERROR: " + msg + "!"
    await ctx.send(final_msg)


async def clear_factorio_text_channel(client):
    channel_name = "bot-factorio"
    factorioChannel = None
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.name == channel_name:  # todo: Update the name to whatever will be chosen on shrimp
                factorioChannel = channel
                break
        if factorioChannel is not None:
            await purge(factorioChannel)
        else:
            await create_new_channel(channel_name, guild, discord)
    return factorioChannel  # todo: Currently doesn't support multiple guilds


async def factorio_welcome_message(channel):
    await channel.send("Factorio server is **{}**!".format(util.get_state().upper()))


async def purge(channel):
    await channel.purge()
