import random

from .model import GuessAWord

games = {

}

class GuessAWordGame:

    async def start_game(self, guild, author, players):
        channel_name = f'gaw-game-{author.name}'

        await self.create_channel(guild, channel_name)

    async def create_channel(self, guild, channel_name):
        await guild.create_text_channel(channel_name)

    def get_random_word(self):
        return random.choice('discord', 'bot', 'python', 'dev')