from random import random
from threading import local
import time


from discord_components import DiscordComponents, Select, SelectOption, Button,ButtonStyle
from datetime import date, datetime, timedelta
import datetime
import sqlite3
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import CommandNotFound
from discord import FFmpegPCMAudio
from discord import Status
from asyncio import sleep
import random
from discord import utils



import DateTime
import asyncio
from PIL import Image, ImageFont, ImageDraw
import io
import requests
import io
from discord.ext import commands,tasks
from PIL import Image, ImageDraw, ImageFont
discordintents = discord.Intents(messages=True, guilds=True)
from io import BytesIO
client = discord.Client()
from dislash import SlashClient, ActionRow, Button
import ipc
import json
import requests
import timestamp
from discord.ext import commands
from discord_slash import SlashCommand, cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import os
from discord.ext import commands
from dislash import InteractionClient, SelectMenu, SelectOption
from dislash import SlashClient, ActionRow, Button
import discord as ds
import json

intents = discord.Intents.all()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix = '-', intents=intents, help_command=None, case_insensitive=True)
slash = SlashCommand(client)

class kiss(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command()
    async def поцеловать(self, ctx, member: discord.Member = None):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
  
        randomgifs = [
            "https://images-ext-1.discordapp.net/external/LbvbptPGA0pEm7S5qMgWsyX1TFg_V3F4lvdWG8XUj1I/https/i.imgur.com/Ui0Gy9z.gif",
            "https://images-ext-1.discordapp.net/external/q0qLf9Qtjnp5McTDAojwv6wL9Xyi7KXajA82YfUtmWY/https/i.imgur.com/fSCM7Wu.gif",
            "https://images-ext-2.discordapp.net/external/8W78jkO-sBo2s23sZeXMPrzJRLXjeTbMLPIkPX-8Bzw/https/i.imgur.com/x2gEP9W.gif",
            "https://images-ext-1.discordapp.net/external/E-bP2MnAHfdIexUV79D1DMgxc6O72g3zxoEpcDFHH7U/https/i.imgur.com/pKwOitS.gif",
            "https://c.tenor.com/Daj-Pn82PagAAAAM/gif-kiss.gif"
        ]
        if member == None:
            await ctx.send(embed = discord.Embed(description = '@Укажите участника', color=0xFF0080))
            return
        await ctx.message.delete()
        embed=discord.Embed(color = random.choice(colors), timestamp=ctx.message.created_at)
        embed.set_author(name=f"{ctx.author} Поцеловал пользователя {member}",icon_url=member.avatar_url)
        randomgif = random.choice(randomgifs)
        embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url = randomgif)
        await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(kiss(bot))