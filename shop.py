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
    @commands.has_permissions(administrator=True)
    @commands.command(
        name="добавить-роль",
        aliases=["add", "add-shop", "добавить"],
        brief="Добавить новую роль в магазин",
        usage="add <@role> <cost>"
    )
    async def add_role_to_shop(self, ctx, role: discord.Role, cost: int=0):
        if cost < 0:
            await ctx.send("Сумма не должна быть меньше 0")
        else:
            await self.db.insert_new_role(role, cost)
            await ctx.message.add_reaction("💖")
            await ctx.message.delete()
    @commands.has_permissions(administrator=True)
    @commands.command(
        name="удалить-роль",
        aliases=["remove", "rm-role", "remove-role", "удалить"],
        brief="Удалить роль из магазина",
        usage="remove <@role>"
    )
    async def remove_role(self, ctx, role: discord.Role):
        if ctx.guild.get_role(role.id) is None:
            await ctx.send("Роли не существует")
        else:
            await self.db.delete_role_from_shop(role)
            await ctx.message.add_reaction("💖")
            await ctx.message.delete()


    @commands.command(
        name="купить-роль",
        aliases=["buy", "buy-role", "купить"],
        brief="Купить роль",
        usage="buy <@role>"
    )
    async def buy_role(self, ctx, role: discord.Role):
        if ctx.guild.get_role(role.id) is None:
            await ctx.send("Роли не существует")
            await ctx.message.delete()
        elif role in ctx.author.roles:
            await ctx.send("У вас уже имеется такая роль")
            await ctx.message.delete()
        else:
            role_data = await self.db.get_shop_data(role)
            balance = await self.db.get_data(ctx.author)

            if balance["balance"] < role_data["cost"]:
                await ctx.send("Недостаточно средств")
                await ctx.message.delete()
            elif balance["balance"] <= 0:
                await ctx.send("Недостаточно средств")
                await ctx.message.delete()
            else:
                await self.db.update_member("UPDATE users SET balance = balance - ? WHERE member_id = ? AND guild_id = ?", [role_data["cost"], ctx.author.id, ctx.guild.id])

                await ctx.author.add_roles(role)
                await ctx.message.add_reaction("💖")
                await ctx.message.delete()
    @commands.has_permissions(administrator=True)
    @commands.command(
        name="магазин-ролей",
        aliases=["shop", "roles-shop", "магазин"],
        brief="Магазин ролей"
    )
    async def view_shop(self, ctx):
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
        embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤМагазин ролей", value=f"————————————————————————————", inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)


        data = await self.db.get_shop_data(ctx.guild.id, all_data=True)
        for row in data:
            if ctx.guild.get_role(row["role_id"]) is not None:
                embed.add_field(
                    name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤСтоимость: {row['cost']}",
                    value=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤРоль: {ctx.guild.get_role(row['role_id']).mention}",
                    inline=False
                )
                embed.add_field(name="————————————————————————————", value=f"ㅤ")


        await ctx.send(embed=embed)
        await ctx.message.delete()



    @commands.cooldown(1, 10800, commands.BucketType.user)
    @commands.command(name="казино")
    async def casino(self, ctx, amount: int):
        emojis = [
            "💎",
            "🍇",
            "🍒",
        ]
        emojis2 = [
            "🍒",
            "🍇",
            "💎",
        ]
        emojis3 = [
            "🍇",
            "💎",
            "🍒",
        ]
        emojis2 = random.choice(emojis)
        emojis33 = random.choice(emojis2)
        emojis44 = random.choice(emojis3)
        msg = await ctx.send(f"{emojis2} {emojis33} {emojis44}")
        await asyncio.sleep(0)
        emojis11 = random.choice(emojis)
        emojis12 = random.choice(emojis2)
        emojis13 = random.choice(emojis3)
        await ctx.send(f"{emojis11} {emojis12} {emojis13}")
        #если выпадает 2 одинаковых эмодзи выдавать деньги
        if emojis11 == emojis12 and emojis11 == emojis13:
            amount2 = random.randint(100, 300)
            await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount2, ctx.author.id, ctx.guild.id])
            color = random.randint(0, 0xffffff)
            embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
            embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤКазино с {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤВы выиграли {amount}:coin:", inline=False)
            embed.add_field(name="————————————————————————————", value=f"ㅤ")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif emojis11 == emojis12 or emojis11 == emojis13 or emojis12 == emojis13:
            amount3 = random.randint(400, 700)
            await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount3, ctx.author.id, ctx.guild.id])
            color = random.randint(0, 0xffffff)
            embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
            embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤКазино с {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤВы выиграли {amount3}:coin:", inline=False)
            embed.add_field(name="————————————————————————————", value=f"ㅤ")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            color = random.randint(0, 0xffffff)
            embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
            embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤКазино с {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤВы проиграли:coin:", inline=False)
            embed.add_field(name="————————————————————————————", value=f"ㅤ")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
   

#команда чтобы положить в банк деньги
    @commands.command(
        name="положить",
        aliases=["deposit", "депозит", "положить-деньги"],
        brief="Положить деньги в банк",
        usage="положить <сколько положить>"
    )
    async def deposit(self, ctx, amount: int):
        bank = await self.db.get_data(ctx.author)
        if bank['balance'] < amount:
            color = random.randint(0, 0xffffff)
            embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
            embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ{ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤНедостаточно средств на руках", inline=False)
            embed.add_field(name="————————————————————————————", value=f"ㅤ")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.message.delete()
        else:
         await self.db.update_member("UPDATE users SET balance = balance - ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])
         await self.db.update_member("UPDATE users SET bank = bank + ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])
         color = random.randint(0, 0xffffff)
         embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
         embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤБанк {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ Вы положили: {amount}:coin:", inline=False)
         embed.add_field(name="————————————————————————————", value=f"ㅤ")
         embed.set_thumbnail(url=ctx.author.avatar_url)
         await ctx.send(embed=embed)
         await ctx.message.delete()


    @commands.command(name = "банк")
    async def bank(self, ctx):
        bank = await self.db.get_data(ctx.author)
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
        embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤБанк {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ  У вас в банке: {bank['bank']}:coin:", inline=False)
        embed.add_field(name="————————————————————————————", value=f"ㅤ")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await ctx.message.delete()



#команду могут использовать только админы
    @commands.command(
        name="снять",
        aliases=["withdraw", "вывести", "снять-деньги"],
        brief="Снять деньги с банка",
        usage="withdraw <amount>"
    )
    async def withdraw(self, ctx, amount: int):
        bank = await self.db.get_data(ctx.author)
        if bank['bank'] < amount:
            color = random.randint(0, 0xffffff)
            embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
            embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ{ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤНедостаточно средств на руках", inline=False)
            embed.add_field(name="————————————————————————————", value=f"ㅤ")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.message.delete()
        else:
            await self.db.update_member("UPDATE users SET bank = bank - ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])
            await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])
            color = random.randint(0, 0xffffff)
            embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
            embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤБанк {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ Вы сняли: {amount}:coin:", inline=False)
            embed.add_field(name="————————————————————————————", value=f"ㅤ")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.message.delete()



    
    @commands.command()
    async def rps(self, ctx, member: discord.Member=None, amount: int=None):
        if amount is None:
            await ctx.send("Укажите сумму")
        if member is None:
            member = ctx.author
        balance = await self.db.get_data(ctx.author)
        if balance['balance'] < amount:
            await ctx.send("У вас недостаточно средств в банке")
            return
            #проверять деньги пользователя которого упомянули
        balance = await self.db.get_data(member)
        if balance['balance'] < amount:
            await ctx.send(f"У {member} Недостаточно средств.")
            return
        if member is None:
            member = ctx.author
        if member == ctx.author:
            await ctx.send("Вы не можете играть с собой")
        else:
            #ждать сообщения пользователя
            msg = await ctx.send(f"{member}, выберите один из трех вариантов: камень, ножницы или бумага")
            #ждать ответа пользователя
            try:
                answer = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("Время вышло")
                return
            #проверка ответа пользователя
            if answer.content.lower() == "||камень||":
                #записывать в test.json
                with open("test.json", "r") as f:
                    data = json.load(f)
                data[ctx.author.id] = "||камень"
                with open("test.json", "w") as f:
                    json.dump(data, f)
            if answer.content.lower() == "||бумага||":
                #записывать в test.json
                with open("test.json", "r") as f:
                    data = json.load(f)
                data[ctx.author.id] = "бумага"
                with open("test.json", "w") as f:
                    json.dump(data, f)
            if answer.content.lower() == "||ножницы||":
                #записывать в test.json
                with open("test.json", "r") as f:
                    data = json.load(f)
                data[ctx.author.id] = "ножницы"
                with open("test.json", "w") as f:
                    json.dump(data, f)
                await ctx.send(f"{member}, выберите один из трех вариантов: камень, ножницы или бумага")
                try:
                    answer = await self.bot.wait_for('message', check=lambda m: m.author == member, timeout=30)
                except asyncio.TimeoutError:
                    await ctx.send("Время вышло")
                    return
                #проверять что ответил пользователь которого упомянули
                if answer.content.lower() == "камень":
                    await answer.delete()
                    with open("test.json", "r") as f:
                        data = json.load(f)
                    data[member.id] = "камень"
                    with open("test.json", "w") as f:
                        json.dump(data, f)
                    await ctx.send("Ничья")
                elif answer.content.lower() == "ножницы":
                    
                    await answer.delete()
                    with open("test.json", "r") as f:
                        data = json.load(f)
                    data[member.id] = "ножницы"
                    with open("test.json", "w") as f:
                        json.dump(data, f)
                    await ctx.send("Вы победили")
                    await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])
                elif answer.content.lower() == "бумага":
                   
                    await answer.delete()
                    with open("test.json", "r") as f:
                        data = json.load(f)
                    data[member.id] = "бумага"
                    with open("test.json", "w") as f:
                        json.dump(data, f)
                    await ctx.send(f"{member} Вы проиграли")

                    await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount, member.id, ctx.guild.id])
                    await self.db.update_member("UPDATE users SET balance = balance - ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])


                else:
                    await ctx.send("Неверный ответ")
                    await answer.delete()


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




def setup(bot):
    bot.add_cog(Shop(bot))
