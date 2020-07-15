# Authors:   Emil Andrzejewski
# Created:  15-Jul-2020
from discord.ext import commands
import discord
import json
import random

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def insult(self, ctx, member: discord.Member = None):
        insult = await self.random_mama_joke()
        await ctx.send(f'{member}, {insult}')

    async def random_mama_joke(self):
        twoja_stara = ["Twoja stara prasuje trawnik czajnikiem",
                       "Twoja stara jeździ windą po lesie",
                       "Twoja stara kroi chleb łokciem",
                       "Twoja stara ciągnie rzepę w familiadzie",
                       "Twoja stara gryzie zęby",
                       "Twoja stara pierze komputer czajnikiem",
                       "Twoja stara grabi liście ołówkiem",
                       "Twoja stara mieszka pod Łodzią",
                       "Twoja stara ma stragan na allegro",
                       "Twoja stara jest taka gruba, że jak spada z łóżka to po obydwu stronach na raz !!!",
                       "Twoja stara mieszka pod Łodzią",
                       "Twoja stara ma stragan na allegro",
                       "Twoja stara jest taka gruba, że jak spada z łóżka to po obydwu stronach na raz !!!",
                       "Twoja stara robi kompoty z ziemniaków!!!",
                       "Twoja stara ugniata ziemniaki poduszką !!!",
                       "Twoja stara jak wychodziła za mąż to miała welon z koca !!!",
                       "Twoja stara czesze się schabowym!!!",
                       "Twoja stara klaszcze czołem",
                       "Twoja stara ubija ziemniaki czołem",
                       "Twoja stara jest taka gruba , ze jak chodziła do szkoły to siedziała obok wszystkich",
                       "Twoja stara jest tak tania ze zrobili ja w Chinach",
                       "Twoja stara prowadzi audycje u Rydzyka",
                       "Twoja stara to ksiądz",
                       "Twoja stara jest kolporterem metra",
                       "Twoja stara skręca pejsy żydom",
                       "Twoja stara potrafi znaleźć trufle",
                       "Twoja stara przeszła simsy",
                       "Twoja stara jest obojniakiem",
                       "Stara twojej starej to twój stary",
                       "Twoja stara chodzi boso",
                       "Twoja stara nie ma brwi",
                       "Twoja stara to Elżbieta Zapędowska",
                       "Twoja stara śpiewa do zupy",
                       "Twoja stara ma jądro",
                       "Twoja stara to zbyń",
                       "Twoja stara gra w teletubisiach",
                       "Twoja stara gra na skrzypcach",
                       "Twoja stara gwiżdże w Kanikulach",
                       "Twoja stara robi techno",
                       "Twoja stara kupuje skype",
                       "Twoja stara robi kontrolę biletów bez uprawnień",
                       "Twoja stara jest łysa",
                       "Twoja stara nie oglądała pokemonów",
                       "Twoja stara grała brzydulę Betty",
                       "Twoja stara słucha mandaryny",
                       "Twoja stara jest papieżem",
                       "Twoja stara skacze",
                       "Twoja stara ma dwie śledziony",
                       "Twoja stara się nie depiluje",
                       "Twoja stara to tablica",
                       "Twoja stara uczy matmy",
                       "Twoja stara je zupę wiatrakiem",
                       "Twoja stara śpi na ścianie",
                       "Twoja stara lepi garnki",
                       "Twoja stara sika do wiadra",
                       "Twoja stara pije deszczówkę",
                       "Twoja stara cię lubi",
                       "Twoja stara pije oranżadę tesco",
                       "Twoja stara mieszka w Lidlu",
                       "Twoja stara je chrzan",
                       "Twoja stara cię nie lubi",
                       "Twoja stara czesze kotlety",
                       "Twoja stara ma na imię Alik",
                       "Twoja stara nie ma ucha",
                       "Twoja stara ma sklep z wazeliną",
                       "Twoja stara to Pudzian",
                       "Twój stary to Andrzej Lepper",
                       "Twoja Stara sprząta po imprezach",
                       "Twoja stara zapowiada przystanki w metrze",
                       "Twoja stara You Can Dance",
                       "Twoja stara przegrała rozprawę w Annie Marii Wesołowskiej",
                       "Twoja stara robi oświetlenie w milionerach",
                       "Twoja stara lubi Magdę Mołek",
                       "Twoja stara masturbuje się kaszanką",
                       "Twoja stara can''t dance",
                       "Twoja stara zawsze gotowa",
                       "Twoja stara ma już dość",
                       "Twoja stara myje owoce w hortexie",
                       "Twoja stara jeździ czołgiem po stodole",
                       "Twoja stara nie ma znaku zodiaku",
                       "Twoja stara goli paznokcie szklanką",
                       "Twoja stara nie ma deski w kiblu",
                       "Twoja stara wróży z kropel moczu",
                       "Piotr Rubik klaszcze twoją starą",
                       "Twoja stara wciąga prześcieradło dupą",
                       "Twoja stara nosi prąd w wiaderku",
                       "Twoja stara dostaje prezenty na dzień ojca",
                       "Twoja stara nie ma dupy",
                       "Twoja stara zjada ciastka okiem",
                       "Twoja stara sika na rabarbar",
                       "Twoja stara goli czoło",
                       "Twoja stara wpierdala suchy chleb dla konia",
                       "Twoja stara kąpie bobry",
                       "Twoja stara ma tylko dwie kalorie",
                       "Twoja stara jeździ komunikacją warszawską na bilety z łodzi",
                       "Twoja stara trzy po trzy",
                       "Twoja stara moczy fiuta w miednicy",
                       "Twoja stara pali jointy nosem",
                       "Twoja stara wciąga tytoń dupą"]

        random_stara = random.choice(twoja_stara)
        return random_stara

def setup(bot):
    bot.add_cog(NSFW(bot))