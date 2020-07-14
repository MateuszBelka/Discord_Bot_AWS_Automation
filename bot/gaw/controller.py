# Authors:   Emil Andrzejewski
# Created:  14-Jul-2020
import random
from .model import GuessAWord

games = {

}

class GuessAWordGame:

    current_game = None

    # Zwraca objekt
    def fetch_game(self):
        return self.current_game

    def get_game(self, channel_id):
        self.current_game = None
        for g in games.keys():
            if channel_id == g:
                self.current_game = games[g]

    def guess(self, channel_id, guess):
        self.get_game(channel_id)
        if self.current_game is None:
            return None
        # zaczynamy gre
        return self.current_game.guess(guess)

    def new_round(self, channel):
        self.current_game = None
        new_game = self.create_game_instance(channel.id, channel.name)
        self.save(new_game)
        self.get_game(channel.id)

    # Tworzy instancje gry i zwraca jej obiekt
    def create_game_instance(self, channel_id, channel_name):
        random_instance = self.get_random_word()
        new_game = GuessAWord(random_instance['word'], random_instance['category'])
        new_game.channel_id = channel_id
        new_game.channel_name = channel_name
        return new_game

    ########################################################################

    # Startuje gre, dodaje graczy, ustawia uprawnienia
    async def start_game(self, guild, author, players):

        channel_name = f'gaw-game-{author.name.lower()}'
        existing_channel = self.get_channel_by_name(guild, channel_name)

        if existing_channel is None:
            channel = await self.create_channel(guild, channel_name)
            await self.set_permissions(guild, channel, players)

            new_game = self.create_game_instance(channel.id, channel.name)

            self.save(new_game)
            self.get_game(channel.id)

            return channel

        return None

    #########################################################################

    # Zapisuje gre do listy
    def save(self, game):
        games[game.channel_id] = game

    # Usuwa gre z listy i kanal
    async def destroy(self, guild, channel_id):
        games.pop(channel_id)
        await self.delete_channel(guild, channel_id)

    # Usuwa kanal
    async def delete_channel(self, guild, channel_id):
        channel = guild.get_channel(channel_id)
        await channel.delete()

    # Ustawia uprawnienia dla kanalu
    async def set_permissions(self, guild, channel, players):
        await channel.set_permissions(guild.default_role,
        view_channel=False, send_messages=False)

        for p in players:
            await channel.set_permissions(p,
            view_channel=True, send_messages=True)

    # Tworzy nowy kanal w kategorii "Gry"
    async def create_channel(self, guild, channel_name):
        category = self.get_category_by_name(guild, 'Gry')
        await guild.create_text_channel(channel_name,  category=category)
        channel = self.get_channel_by_name(guild, channel_name)
        return channel

    # Zwraca objekt kanal uzywajac nazwy kanalu
    def get_channel_by_name(self, guild, channel_name):
        channel = None
        for c in guild.channels:
            if c.name == channel_name.lower():
                channel = c
                break
        return channel

    # Zwraca objekt kategoria uzywajac nazwy kategorii
    def get_category_by_name(self, guild, category_name):
        category = None
        for c in guild.categories:
            if (c.name==category_name):
                category = c
                break
        return category

    # Losuje randomowe slowo z listy
    def get_random_word(self):
        return random.choice([
        {
            'word': "Jezyk",
            'category': "Anatomia"
        },
        {
            'word': "Serce",
            'category': "Anatomia"
        },
        {
            'word': "Paznokiec",
            'category': "Anatomia"
        },
        {
            'word': "Krew",
            'category': "Anatomia"
        },
        {
            'word': "Kciuk",
            'category': "Owoce"
        },
        {
            'word': "Arbuz",
            'category': "Owoce"
        },
        {
            'word': "Jablko",
            'category': "Owoce"
        },
        {
            'word': "Wisnia",
            'category': "Owoce"
        },
        {
            'word': "Brzoskwinia",
            'category': "Owoce"
        },
        {
            'word': "Grejpfrut",
            'category': "Owoce"
        },
        {
            'word': "Niebieski",
            'category': "Kolor"
        },
        {
            'word': "Bialy",
            'category': "Kolor"
        },
        {
            'word': "Czerwony",
            'category': "Kolor"
        },
        {
            'word': "Zielony",
            'category': "Kolor"
        },
        {
            'word': "Czarny",
            'category': "Kolor"
        },
        {
            'word': "Malpa",
            'category': "Zwierzeta"
        },
        {
            'word': "Kon",
            'category': "Zwierzeta"
        },
        {
            'word': "Krokodyl",
            'category': "Zwierzeta"
        },
        {
            'word': "Hipopotam",
            'category': "Zwierzeta"
        },
        {
            'word': "Zaba",
            'category': "Zwierzeta"
        }
    ])
