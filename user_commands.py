from turtle import color
import discord
from discord.ext import commands
from dislash import SlashClient, ActionRow, Button
from discord_components import DiscordComponents, Select, SelectOption, Button,ButtonStyle
import random
from utils import database
import asyncio


class UserCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = database.DataBase()



    @commands.command(name="баланс" )
    async def user_balance(self, ctx, member: discord.Member=None):
        balance = await self.db.get_data(ctx.author)
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
        embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤБаланс {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ  У вас на руках: {balance['balance']}:coin:", inline=False)
        embed.add_field(name="————————————————————————————", value=f"ㅤ")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.has_permissions(administrator=True)
    @commands.command(
        name="наградить",
        aliases=["award"],
        brief="Наградить пользователя суммой денег",
        usage="award <@user> <amount>"
    )
    async def award_user(self, ctx, member: discord.Member, amount: int):
        if amount < 1:
            await ctx.send("Сумма не должна быть меньше 1")
            await ctx.message.delete()
        else:
            await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount, member.id, ctx.guild.id])
            await ctx.message.add_reaction("💖")
            await ctx.message.delete()
    @commands.has_permissions(administrator=True)
    @commands.command(
        name="забрать",
        aliases=["take", "отнять"],
        brief="Забрать сумму денег у пользователя",
        usage="take <@user> <amount (int or all)>"
    )
    async def take_cash(self, ctx, member: discord.Member, amount):
        if amount == "all":
            await self.db.update_member("UPDATE users SET balance = ? WHERE member_id = ? AND guild_id = ?", [0, member.id, ctx.guild.id])
        elif int(amount) < 1:
            await ctx.send("Сумма не должна быть меньше 1")
            await ctx.message.delete()
        else:
            await self.db.update_member("UPDATE users SET balance = balance - ? WHERE member_id = ? AND guild_id = ?", [amount, member.id, ctx.guild.id])

        await ctx.message.add_reaction("💖")
        await ctx.message.delete()

    @commands.command(name="перевести")
    async def pay_cash(self, ctx, member: discord.Member=None):
        msg = await ctx.send("Укажите участника для перевода")
        #ждать сообщение пользователя упомянув другого
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            member = await self.bot.wait_for('message', check=check, timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Время ожидания вышло")
            return
        member = member.mentions[0]
        await ctx.send(f"Укажите сумму для перевода {member.mention}")
#ждать сообщение пользователя сколько денег надо перевести
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            amount = await self.bot.wait_for('message', check=check, timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Время ожидания вышло")
            return
        amount = amount.content
        if amount == "all":
            await self.db.update_member("UPDATE users SET balance = ? WHERE member_id = ? AND guild_id = ?", [0, member.id, ctx.guild.id])
        elif int(amount) < 1:
            await ctx.send("Сумма не должна быть меньше 1")
            await ctx.message.delete()
        else:
            #забрать деньги кто хочет перевести и отдать их кого упомянули
            await self.db.update_member("UPDATE users SET balance = balance - ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])
            await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount, member.id, ctx.guild.id])
        await ctx.message.add_reaction("💖")
        await ctx.message.delete()


    @commands.command(
        name="+репутация",
        aliases=["+rep", "реп", "репутация"],
        brief="Респект пользователю",
        usage="rep <@user>"
    )
    async def reputation(self, ctx, member: discord.Member):
        if member.id == ctx.author.id:
            await ctx.send("Нельзя выдать репутацию себе")
            await ctx.message.delete()
        else:
            await self.db.update_member("UPDATE users SET reputation = reputation + ? WHERE member_id = ? AND guild_id = ?", [1, member.id, ctx.guild.id])
            await ctx.message.add_reaction("💖")
            await ctx.message.delete()

    @commands.command(
        name="лидеры",
        aliases=["leaders", "leadersboard", "лидер"],
        brief="Таблица лидеров"
    )
    async def server_leadersboard(self, ctx):
        embed = discord.Embed(title="Топ 10 сервера")
        counter = 0

        data = await self.db.get_data(ctx.guild.id, all_data=True, filters="ORDER BY balance DESC LIMIT 10")
        for row in data:
            counter += 1
            embed.add_field(
                name=f"#{counter} | `{self.bot.get_user(row['member_id'])}`",
                value=f"Баланс: {row['balance']}",
                inline=False
            )

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.command(name="ограбить")
    async def random_earn_money(self, ctx):
        amount = random.randint(100, 500)
        await self.db.update_member("UPDATE users SET balance = balance + ? WHERE member_id = ? AND guild_id = ?", [amount, ctx.author.id, ctx.guild.id])
        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="ㅤ",description=f"————————————————————————————", color=color)
        embed.add_field(name=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤБаланс {ctx.author}", value=f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤВы ограбили банк на: {amount}:coin:", inline=False)
        embed.add_field(name="————————————————————————————", value=f"ㅤ")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(name="sdfsdfsd", aliases=["sdfsdfsdf", "sdfsdfsdfsd"])
    async def hel312312312312p(self, ctx):
#   First page of embeds **make sure to call each embed a different name**
         embed = discord.Embed(title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤКоманды", description="**ㅤㅤㅤㅤㅤㅤㅤ ᠌ ᠌ㅤ  ㅤㅤㅤПрефикс бота:**  __.__", color=0xFF0080)
         embed.add_field(name="**——————————————————————————————————**", value="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Заработок**__", inline=False)
         embed.add_field(name="> Заработать", value="`Заработать деньги`")
         embed.add_field(name="> Казино", value="`Играть в казино`")
         embed.add_field(name="> Удача", value="`Испытать удачу`")
         embed.add_field(name="> Ограбить", value="`Ограбить банк`")
         embed.add_field(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Деньги**__", value="ㅤ", inline=False)
         embed.add_field(name="> Снять", value="`Снять деньги с банка`")
         embed.add_field(name="> Банк", value="`Получить баланс в банке`")
         embed.add_field(name="> Баланс", value="`Показать баланс пользователя`", inline=True)
         embed.add_field(name="> Перевести", value="`Перевести деньги пользователю`", inline=True)
         embed.add_field(name="> Репутация", value="`Респект пользователю`", inline=True)
         embed.add_field(name="> Лидеры", value="`Таблица лидеров`", inline=True)
         embed.add_field(name="> Положить", value="`Положить деньги в банк`")
         embed.add_field(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Магазин**__", value="ㅤ", inline=False)
         embed.add_field(name="> Купить-роль", value="`Купить роль в магазине`")
         embed.add_field(name="> Магазин-ролей", value="`Посмотреть список ролей в магазине`")
         embed.add_field(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Админ-команды**__", value="ㅤ", inline=False)
         embed.add_field(name="> Наградить", value="`Наградить пользователя суммой денег`", inline=True)
         embed.add_field(name="> Забрать", value="`Забрать сумму денег у пользователя`", inline=True)
         embed.add_field(name="> Добавить-роль", value="`Добавить роль в магазин`")
         embed.add_field(name="> Удалить-роль", value="`Удалить роль с магазина`", inline=False)
         embed.add_field(name=" ㅤ", value="**——————————————————————————————————**")
         await ctx.send(embed=embed)
         await ctx.message.delete()

    @commands.command(name="хелп", aliases=["help", "помощь"])
    async def help(self, ctx):
#   First page of embeds **make sure to call each embed a different name**
         embed = discord.Embed(title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤКоманды", description="**ㅤㅤㅤㅤㅤㅤㅤ ᠌ ᠌ㅤ  ㅤㅤㅤПрефикс бота:**  __-__", color=0xFF0080)
         embed.add_field(name="**——————————————————————————————————**", value="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Заработок**__", inline=False)
         embed.add_field(name="> Заработать", value="`Заработать деньги`")
         embed.add_field(name="> Казино", value="`Играть в казино`")
         embed.add_field(name="> Удача", value="`Испытать удачу`")
         embed.add_field(name="> Ограбить", value="`Ограбить банк`")
         embed.add_field(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Деньги**__", value="ㅤ", inline=False)
         embed.add_field(name="> Снять", value="`Снять деньги с банка`")
         embed.add_field(name="> Банк", value="`Получить баланс в банке`")
         embed.add_field(name="> Баланс", value="`Показать баланс пользователя`", inline=True)
         embed.add_field(name="> Перевести", value="`Перевести деньги пользователю`", inline=True)
         embed.add_field(name="> Репутация", value="`Респект пользователю`", inline=True)
         embed.add_field(name="> Лидеры", value="`Таблица лидеров`", inline=True)
         embed.add_field(name="> Положить", value="`Положить деньги в банк`")
         embed.add_field(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Магазин**__", value="ㅤ", inline=False)
         embed.add_field(name="> Купить-роль", value="`Купить роль в магазине`")
         embed.add_field(name="> Магазин-ролей", value="`Посмотреть список ролей в магазине`")
         embed.add_field(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Админ-команды**__", value="ㅤ", inline=False)
         embed.add_field(name="> Наградить", value="`Наградить пользователя суммой денег`", inline=True)
         embed.add_field(name="> Забрать", value="`Забрать сумму денег у пользователя`", inline=True)
         embed.add_field(name="> Добавить-роль", value="`Добавить роль в магазин`")
         embed.add_field(name="> Удалить-роль", value="`Удалить роль с магазина`", inline=False)
         embed.add_field(name=" ㅤ", value="**——————————————————————————————————**")
   
         emMod = discord.Embed(title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤКоманды", description="**ㅤㅤㅤㅤㅤㅤㅤㅤ ᠌ ᠌ㅤ  ㅤㅤㅤПрефикс бота:**  __-__", color=0xFF0080)
         emMod.add_field(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Фан-команды**__", value="ㅤ", inline=False)
         emMod.add_field(name="> обнять", value="`Обнять человека.`")
         emMod.add_field(name="> Трахнуть", value="`Трахнуть человека.`")
         emMod.add_field(name="> Наказать", value="`Наказать человека.`", inline=True)
         emMod.add_field(name="> Грусть", value="`Погрустить.` ", inline=True)
         emMod.add_field(name="> Поцеловать", value="`Поцеловать челока.", inline=True)
         emMod.add_field(name="> аватар", value="`Показать аватарку человека.`", inline=True)
         emMod.add_field(name="> инфа", value="`Показать информацию о пользователе.`")
         emMod.add_field(name="> инфасервер", value="`Показать информацию о сервере.`")
         emMod.add_field(name="> 8ball", value="`Шар судьбы.`", inline=True)
         emMod.add_field(name="> кнб", value="`Сыграть в камень ножницы бумага.` ", inline=True)
         emMod.add_field(name="> Крестики", value="`Показать информацию о сервере.`")
         emMod.add_field(name="> rep", value="`Выдать репутацию человеку.`", inline=True)
         emMod.add_field(name="> top", value="`Посмотреть топ по репутациям.`", inline=True)
         emMod.add_field(name="> кнб", value="`Сыграть в крестики нолики (@упомянуть себя @упомянуть друга)` ", inline=True)
         emMod.add_field(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Music-команды**__", value="ㅤ", inline=False)
         emMod.add_field(name="> play", value="`Воспроизвести музыку.`")
         emMod.add_field(name="> stop", value="`Остановить музыку.`")
         emMod.add_field(name="> pause", value="`Поставить музыку на паузу.`", inline=True)
         emMod.add_field(name="> resume", value="`Продолжить музыку.` ", inline=True)
         emMod.add_field(name="> skip", value="`Пропустить трэк`", inline=True)
         emMod.add_field(name="> queue", value="`Посмотреть очередь трэков.`", inline=True)
         emMod.add_field(name="> Join", value="`Бот присоедениться к вам в гс.`")
         emMod.add_field(name="> repeat", value="`Повторить музыку 2 раза.`")
         emMod.add_field(name="> remove", value="`Удалить музыку из очереди (+remove номер музыки в очереди (+queue).)`", inline=True)
         emMod.add_field(name="> disconnect", value="`чистить очередь музыки и удалить бота из гс` ", inline=True)
         emMod.add_field(name="**——————————————————————————————————**", value="ㅤ",inline=False)

         emMod2 = discord.Embed(title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤКоманды", description="**ㅤㅤㅤㅤㅤㅤㅤㅤ ᠌ ᠌ㅤ  ㅤㅤㅤПрефикс бота:**  __-__", color=0xFF0080)
         emMod2.add_field(name="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__**Модератор-команды**__", value="ㅤ", inline=False)
         emMod2.add_field(name="> clear", value="`Очистить чат от сообещний -clear число`")
         emMod2.add_field(name="> ban", value="`Забанить человека -ban @ (время 1с, 1м, 1ч, 1д) (причина)`")
         emMod2.add_field(name="> mute", value="`Замьютить человека -mute @ (время 1с, 1м, 1ч, 1д) (причина).`", inline=True)
         emMod2.add_field(name="> unmute", value="`Размьютить человека.` ", inline=True)

   
#   Group all the embeds to a single phrase to call on later
         contents = [
           embed,
           emMod,
           emMod2
         ]
#   Pages: How many pages you want
#   Cur_page: Tells you what your current page is. **1 = when command is called it starts on 1**
#   message: sends the above and embeds in a message **Make sure embed=contents** 
         pages = 3
         cur_page = 1
         message = await ctx.send(
                       content=f"Page {cur_page}/{pages}",
                       embed=contents[cur_page - 1]
         )
   
   
#   Tells bot to add the following reaction emojis to above message just sent
         await message.add_reaction("◀️")
         await message.add_reaction("▶️")
   
#   Check function so only the command caller can interact with the embed
         def check(reaction, user):
             return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
   
   
         while True:
             try:
#   **timeout=None** No time limit if no reaction
#   **timeout=60** If no reaction after 60 seconds message will delete 
                 reaction, user = await self.bot.wait_for("reaction_add", timeout=None, check=check)
   
   
                 if str(reaction.emoji) == "▶️" and cur_page != pages:
                     cur_page += 1
                     await message.edit(
                         content=f"Page {cur_page}/{pages}**",
                         embed=contents[cur_page - 1]
                     )
                     await message.remove_reaction(reaction, user)
   
                 elif str(reaction.emoji) == "◀️" and cur_page > 1:
                     cur_page -= 1
                     await message.edit(
                         content=f"Page {cur_page}/{pages}**",
                         embed=contents[cur_page - 1]
                     )
                     await message.remove_reaction(reaction, user)
   
                 else:
                     await message.remove_reaction(reaction, user)
   
             except asyncio.TimeoutError:
                 await message.delete()
                 break

        









def setup(bot):
    bot.add_cog(UserCommands(bot))
