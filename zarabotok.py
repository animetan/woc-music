import discord
from discord.ext import commands

from utils import database
import random

from discord.utils import get
from random import random
from threading import local
import time

import random
import string
import requests
from colorama import Fore as c
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
from io import BytesIO
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

class Shop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = database.DataBase()


    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.command(name="заработать")
    async def random_earn_money(self, ctx):
        #рандомно брать слова из созданного списка
        words = ["курьер", "шахтёр", "врачь", "таксист"]
        amount = random.randint(0, 100)
        await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
        embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤБаланс {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤВы заработали {amount} на работе {random.choice(words)}:coin:", inline=False)
        embed.add_field(name="————————————————————————————", value=f"ㅤ")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await ctx.message.delete()




    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.command(
        name="удача",
        aliases=["random-earn", "random-earn-money", "рандомное-заработать-денег"],
        brief="Рандомно заработать деньги",
        usage="random-earn <amount>"
    )
    async def random_earn_money(self, ctx):
        amount = random.randint(20, 100)
        await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
        embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤБаланс {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤ   Вы испытали удачу и нашли: {amount}:coin:", inline=False)
        embed.add_field(name="————————————————————————————", value=f"ㅤ")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Shop(bot))
