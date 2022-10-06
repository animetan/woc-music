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

class ball(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name = "8ball111")
    async def _8ball11(self,ctx, *, question):
       responses = [
       'Это точно.',
        'Это определенно так.',
        'Без сомнения.',
        'Да - определенно.',
        'Вы можете положиться на это.',
        'Скорее всего.',
        'Хорошая перспектива.',
        'Да',
        'Знаки указывают на да.',
        'Ответить туманно, попробуйте еще раз.',
        'Спросить позже.',
        'Лучше не говорить вам сейчас.',
        'Невозможно предсказать сейчас.',
        'Сконцентрируйтесь и спросите еще раз',
        "Не рассчитывайте на это.",
        'Мой ответ - нет' ,
        'Мои источники говорят нет',
        'Перспектива не очень хорошая.',
        'Очень сомнительно.'
         ]
       responses = random.choice(responses)
       embed = discord.Embed(title=f"Вопрос от: {ctx.author.name}: {question}",color=0xFF0080)
       embed.add_field(name="Ответ:", value=responses, inline=False)
       embed.set_footer(text=f"{ctx.author}",icon_url=ctx.author.avatar_url)
       embed.timestamp = datetime.datetime.utcnow()
       await ctx.send(embed=embed)
       await ctx.message.delete()



def setup(bot):
    bot.add_cog(ball(bot))