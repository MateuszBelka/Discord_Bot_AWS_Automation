# Author:   Mateusz Belka
# Created:  11-Jul-2020
#
#


async def send_confirmation_msg(reaction, user):
    # Temporary method responsible for testing if bot can respond to discord reactions being added

    channel = reaction.message.channel
    await channel.send('{} has added {} to the message {}'.format(user.name, reaction.emoji, reaction.message.content))
    print("Message sent!")
