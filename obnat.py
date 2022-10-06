from random import random
from threading import local
import time

from discord_slash import SlashCommand
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
import ipc
import json
import requests
import timestamp
from discord.ext import commands
from discord_slash import SlashCommand, cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import os

intents = discord.Intents.all()
intents.members = True
intents.messages = True

client = commands.Bot(command_prefix = '-', intents=intents, help_command=None, case_insensitive=True)
slash = SlashCommand(client)

class obnat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command()
    async def обнять(self,ctx, member: discord.Member = None):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
  
        randomgifs = [
            "https://media.discordapp.net/attachments/943974690186219610/971874580874555452/hug_063.gif",
            "https://images-ext-1.discordapp.net/external/EgBCjeXRvSvd9AtbC0NCpz7Dn5pYJaQkxU9_DqDj7mg/https/i.imgur.com/O6qhsfp.gif",
            "https://images-ext-2.discordapp.net/external/G6BgoEmy5gmSX6Syif-VMPD28dMMHzwI-KWapxbC9eI/https/i.imgur.com/RWTBzWm.gif",
            "https://images-ext-2.discordapp.net/external/lHIPfEX7nL_Ufg1Zfaoi33o-tD9qP8_y8_YNKdEaxLE/https/i.imgur.com/xJlv3OX.gif",
            "https://images-ext-2.discordapp.net/external/IM_IQ_M5PIRO7oianl0iqYjeINxAxwgY46lmF7mgewc/https/i.imgur.com/edYHVXC.gif",
            "https://images-ext-2.discordapp.net/external/Zj8S0BgVbb2X1o9wAGdvXKPyLBSPXqyVdgp_qEWXaJQ/https/i.imgur.com/7jf6ihH.gif",
            "https://images-ext-2.discordapp.net/external/msx7P85NiPrcq1nSfcSOJX8XL5tm4DVUGXmDw0dycdk/https/i.imgur.com/LSFissS.gif"
        ]
        if member == None:
            await ctx.send(embed = discord.Embed(description = '@Укажите участника', color=0xFF0080))
            return
        await ctx.message.delete()
        embed=discord.Embed(color = random.choice(colors), timestamp=ctx.message.created_at)
        embed.set_author(name=f"{ctx.author} Обнял пользователя {member}",icon_url=member.avatar_url)
        randomgif = random.choice(randomgifs)
        embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url = randomgif)
        await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(obnat(bot))