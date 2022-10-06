import discord
from discord.ext import commands


import json
import datetime

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot




 

                      



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)

        if isinstance(error, commands.UserInputError):
            await ctx.send(embed=discord.Embed(
                description=f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief}): `{ctx.prefix}{ctx.command.usage}`"
            ))




def setup(bot):
    bot.add_cog(Events(bot))
