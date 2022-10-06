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

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command()
    async def serverinfo(self, ctx):

        text_channel_server = len(ctx.message.guild.channels)
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        staff_roles = ["Owner", "Head Dev", "Dev", "Head Admin", "Admins", "Moderators", "Community Helpers", "Members"]
        
        embed2 = discord.Embed(timestamp=ctx.message.created_at, color=0xFF0080)
        embed2.add_field(name='Название сервера', value=f"{ctx.guild.name}", inline=False)
        embed2.add_field(name='Создатель сервера', value="<@!403875492496670732>", inline=False)
        embed2.add_field(name='Уровень верификации', value="medium", inline=False)
        embed2.add_field(name='Высшая роль', value=ctx.guild.roles[-1], inline=False)

        for r in staff_roles:
            role = discord.utils.get(ctx.guild.roles, name=r)
            if role:
                members = '\n'.join([member.name for member in role.members]) or "None"
                embed2.add_field(name=role.name, value=members)

        embed2.add_field(name='✅Количество ролей', value=str(role_count), inline=False)
        embed2.add_field(name="🚶Количество участников ", value=ctx.guild.member_count, inline=False)
        embed2.add_field(name="💬Текстовые каналы:", value=len(ctx.message.guild.channels), inline=False)
        embed2.add_field(name="🔊Голосовые каналы:", value=len(ctx.message.guild.voice_channels), inline=True)
        embed2.set_thumbnail(url=ctx.guild.icon_url)
        embed2.add_field(name="🚀Бустов:", value=f'{str(ctx.guild.premium_subscription_count)}', inline=False)
        embed2.add_field(name='Создан:', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    
        await ctx.message.delete()
        await ctx.send(embed=embed2)





def setup(bot):
    bot.add_cog(fun(bot))