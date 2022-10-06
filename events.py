import discord
from discord.ext import commands

from utils import database
import json
import datetime

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = database.DataBase()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.db.create_table()

        for guild in self.bot.guilds:
            for member in guild.members:
                await self.db.insert_new_member(member)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.db.insert_new_member(member)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for member in guild.members:
            await self.db.insert_new_member(member)



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)

        if isinstance(error, commands.UserInputError):
            await ctx.send(embed=discord.Embed(
                description=f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief}): `{ctx.prefix}{ctx.command.usage}`"
            ))




def setup(bot):
    bot.add_cog(Events(bot))
