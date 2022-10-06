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

class moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command()
    async def ip(self, ctx, arg):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://ipwhois.app/json/{arg}'
) as r:
                data = await r.json()

        user_ip = data['ip']
        user_continent = data['continent']
        user_city = data['city']
        user_code = data['country_code']
        user_flag = data['country_flag']
        user_stol = data['country_capital']
        user_codep = data['country_phone']
        user_region = data['region']
        user_country = data['country']
        user_time = data['timezone_gmt']
        user_val = data['currency']
        user_val_s = data['currency_code']
        user_org = data['org']
        user_timezone = data['timezone']

        all_info = f'\nIP : {user_ip}\nГород : {user_city}\nРегион : {user_region}\nСтолица страны : {user_stol}\nКод телефона : {user_codep}\nКод страны : {user_code}\nСтрана : {user_country}\nВалюта : {user_val}\nВалюта (короткая) : {user_val_s}\nПровайдер : {user_org}\nЗона : {user_timezone}'

        flag = f'{user_flag}'

        embed = discord.Embed(title = 'IP инфо', description = f'{all_info}')
        embed.set_thumbnail(url = f'{flag}')
        await ctx.author.send(embed=embed)

def setup(bot):
    bot.add_cog(moderation(bot))