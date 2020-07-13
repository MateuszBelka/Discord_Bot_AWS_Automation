# Author:   Emil Andrzejewski
# Created:  13-Jul-2020
import discord
from discord.ext import commands

class User_management(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Wyjebano {member.mention} za {reason}.')
        await member.send(f'Zostałeś wyjebany z {ctx.guild} za {reason}.')

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Zbanowano {member.mention} za {reason}.')
        await member.send(f'Zostałeś zbanowany z {ctx.guild} za {reason}.')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Odbanowano {user.mention}.')
                await member.send(f'Zostałeś odbanowany z {ctx.guild}.')
                return

def setup(client):
    client.add_cog(User_management(client))