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

class nakaz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command()
    async def танцевать(self,ctx, member: discord.Member = None):

        colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
  
        randomgifs = [
            "https://c.tenor.com/zlhLMAQCZZsAAAAM/dance-vr.gif",
            "https://c.tenor.com/P7QN5kqyiSQAAAAd/aharen-san-aharen-san-anime.gif",
            "https://c.tenor.com/AD70bmXloTcAAAAM/chika-dance-chika-chika-chika.gif",
            "https://c.tenor.com/gZ9NqWUT7x8AAAAC/anime-tv-show.gif",
            "https://images-ext-1.discordapp.net/external/ZZ-Xu7DH76Mb76_HxgwMQ80FNwwsFD9RR8APaKzvjVs/https/i.imgur.com/NL0apZh.gif"
        ]
        randomgifs2 = [
            "https://c.tenor.com/2vRn7mgoMRMAAAAM/cute-anime-dance.gif",
            "https://c.tenor.com/AD70bmXloTcAAAAM/chika-dance-chika-chika-chika.gif",
            "https://c.tenor.com/z85ySqaD6s0AAAAd/hayasaki.gif"
        ]
        if member == None:
         embed=discord.Embed(color = random.choice(colors), timestamp=ctx.message.created_at)
         embed.set_author(name=f"Опа, смотрите как танцует: {ctx.author}",icon_url=ctx.author.avatar_url)
         randomgifs2 = random.choice(randomgifs2)
         embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
         embed.set_image(url = randomgifs2)
         await ctx.send(embed = embed)
         return
        await ctx.message.delete()
        embed=discord.Embed(color = random.choice(colors), timestamp=ctx.message.created_at)
        embed.set_author(name=f"Опа, смотрите как танцует: {ctx.author} с {member}",icon_url=member.avatar_url)
        randomgif = random.choice(randomgifs)
        embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url = randomgif)
        await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(nakaz(bot))