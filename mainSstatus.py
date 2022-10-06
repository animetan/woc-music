 
from asyncio import TimeoutError
import asyncio
import time
import discord
import os
import json
import io
import datetime
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_components import DiscordComponents, Select, SelectOption, Button, ButtonStyle
from discord_slash import SlashCommand, cog_ext, SlashContext
from dislash import SlashClient, ActionRow, Button
from dislash import InteractionClient, SelectMenu, SelectOption
from dislash import SlashClient, ActionRow, Button
from mcstatus import JavaServer
from PIL import Image, ImageDraw, ImageFont
from discord_slash.utils.manage_commands import create_option, create_choice
import random
import ffmpeg
from discord.ext import commands
from mcstatus import JavaServer
import discord
import requests
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import CommandNotFound
from discord import FFmpegPCMAudio
from discord import Status
from youtube_dl import YoutubeDL
from discord.ext import commands, tasks

discordintents = discord.Intents(messages=True, guilds=True)
from io import BytesIO
from asyncio import sleep
import pytz
client = discord.Client()
import ipc

intents = discord.Intents.all()
intents.members = True
intents.messages = True
client = InteractionClient
discordintents = discord.Intents(messages=True, guilds=True)

print("i online")






client = commands.Bot(command_prefix='m.',
                      intents=intents,
                      help_command=None,
                      case_insensitive=True)
slash = SlashCommand(client,sync_commands=True, sync_on_cog_reload=True, override_type = True)
DiscordComponents(client)
from discord.ext.tasks import loop
import datetime

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@loop(seconds=1)
async def task():
    nowtime = str(datetime.datetime.now().time().strftime("%H.%M.%S"))
    if nowtime == "18.00.00":
      channel = client.get_channel(961668931934879794)
      await channel.send("ауе")
            # your task

task.start()

@client.command()
async def time(ctx):
  moscow_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
  # если moscow_time = 12:45 то мы пишем в чат 
  if moscow_time.hour == 12 and moscow_time.minute == 54:
    await ctx.send("ауе")
    
@client.command()
async def sredbal(ctx):
    #открыть bal.josn
    with open("bal.json", "r") as f:
        users = json.load(f)
    #брать значения со второй строки и высчитывать средний бал из них
    bal = list(users.values())
    sredbal = sum(bal) / len(bal)
    #считать сколько цифр 2 в bal.json
    count2 = bal.count(2)
    #считать сколько цифр 3 в bal.json
    count3 = bal.count(3)
    #считать сколько цифр 4 в bal.json
    count4 = bal.count(4)
    #считать сколько цифр 5 в bal.json
    count5 = bal.count(5)
    #считать сколько цифр 1 в bal.json
    count1 = bal.count(1)
    #вывести средний бал и количество каждой оценки
    await ctx.send(f'Средний балл: {sredbal}\nОценка 1: {count1}\nОценка 2: {count2}\nОценка 3: {count3}\nОценка 4: {count4}\nОценка 5: {count5}\n')

@client.command()
async def iamge(ctx):
    banner = Image.open("mine.png")
    draw = ImageDraw.Draw(banner)
    font = ImageFont.truetype("minecraft.ttf", 15)
    # писать текст сколько всего участников на сервере
    draw.text((60, 35), f"AnimeTan получил новый уровень - 1", (255, 255, 255), font=font)
    #получить список участнико
    banner.save("mine2.png")
    #отправлять файл
    await ctx.send(file=discord.File('mine2.png'))

@client.event
async def on_message(message):
        #записывать 1 сообщение = 1 число и добавлять к этому числу число сообщений в message.json
    with open('message.json', 'r') as f:
        data = json.load(f)
    if str(message.author.id) in data:
        data[str(message.author.id)]['count'] += 1
    else:
        data[str(message.author.id)] = {}
        data[str(message.author.id)]['count'] = 1
    with open('message.json', 'w') as f:
        json.dump(data, f)

    await client.process_commands(message)


@client.event
async def on_command_error(ctx, error):
    embed = discord.Embed(
        title=":warning: Использована неизвестная команда.",
        description=
        "Пожалуйста, напишите `m.help` для списка команд и соответствующего использования. {error}",
        color=0xFF0080)
    await ctx.send(embed=embed,delete_after=10.0)
    print('Ошибка выполнения команды: ', error)


@client.command()
async def cities(ctx):
    with open('words.json', "r") as f:
        cities = json.load(f)
    await ctx.send(f'Всего городов: {len(cities)}')

# ------------------------------------- - ------------------------------------ #



# ------------------------------------- infoserver ------------------------------------ #
# on ready

@slash.slash(
    name="профиль",
    description="Профиль пользователя.",
    guild_ids=[786301738155245578],
    options=[
        create_option(
            name="member",
            description="Да, профиль",
            option_type=
            6,  #check out the docs (link is provided in readme.md file) to know more about different types of options

            required=False)
    ])
async def profile2(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.author

    with open('dosh.json', 'r') as f:
        data4 = json.load(f)
    if str(member.id) not in data4:
      data4[str(member.id)] = {}
      data4[str(member.id)]['300message'] = "nahalo.jpg"
      data4[str(member.id)]['500message'] = "nahalo.jpg"
      data4[str(member.id)]['800message'] = "nahalo.jpg"
      data4[str(member.id)]['5lvl'] = "nahalo.jpg"
      data4[str(member.id)]['20lvl'] = "nahalo.jpg"
      data4[str(member.id)]['50lvl'] = "nahalo.jpg"
    with open('dosh.json', 'w') as f:
        json.dump(data4, f)

    with open('message.json', 'r') as f:
      data = json.load(f)
      if str(member.id) not in data:
        data[str(member.id)]['count'] = 0
      with open('message.json', 'w') as f:
        json.dump(data, f, indent=4)

    with open("levels.json", "r") as f:
      data2 = json.load(f)


      level = data2[str(ctx.guild.id)][str(member.id)]['level']
      xp = data2[str(ctx.guild.id)][str(member.id)]['xp']
      xp_needed = int(level+(level*100))
      xp_left = xp_needed-xp



      #создать картинку
      #брать из skin.json какую картинку поставил человек и ставить её
      with open('skin.json', 'r') as f:
        data3 = json.load(f)
        if str(member.id) not in data3:
          skin = "profile.jpg"
        else:
          skin = data3[str(member.id)]['skin']
      banner = Image.open(f"skin/{skin}")
      foreground = Image.open("message.png")
      #создать кисть
      draw = ImageDraw.Draw(banner)
        #если id человека есть в dosh.json то мы выполняем код
      dosh = data4[str(member.id)]['300message']
      #если member.id есть в data4 то мы выполняем код
      if str(member.id) in data4:
    
        im2 = Image.open(f'{data4[str(member.id)]["300message"]}')

        banner.paste(im2, (150, 810))
      if str(member.id) in data4:
    
        im3 = Image.open(f'{data4[str(member.id)]["500message"]}')

        banner.paste(im3, (250, 810))
      if str(member.id) in data4:
    
        im4 = Image.open(f'{data4[str(member.id)]["5lvl"]}')

        banner.paste(im4, (350, 810))
      if str(member.id) in data4:
    
        im5 = Image.open(f'{data4[str(member.id)]["15lvl"]}')

        banner.paste(im5, (450, 810))
      if str(member.id) in data4:
    
        im5 = Image.open(f'{data4[str(member.id)]["50lvl"]}')

        banner.paste(im5, (550, 810))

      with open('dosh2.json', 'r') as f:
        data5 = json.load(f)

      font = ImageFont.truetype("minecraft.ttf", 40)
      card = Image.new("RGBA", (220, 220), (255, 255, 255))
      img = Image.open("message.png").convert("RGBA")
      x, y = img.size
      card.paste(img, (0, 0, x, y), img)

      with open('glass.json', 'r') as f:
        data6 = json.load(f)

        #брать из glass.json цвет который написан там и ставить его в fill
        color = data6[str(member.id)]['color']
        #если member.id есть в data6 то мы выполняем код
      if color == "belie":
        color2 = (255,255,255)
        draw.rectangle(((280, 141), (267, 151)), fill=(color2))
        draw.rectangle(((312, 141), (298, 151)), fill=(color2))
      if color == "black":
        color2 =  (0,0,0)
        draw.rectangle(((280, 141), (267, 151)), fill=(color2))
        draw.rectangle(((312, 141), (298, 151)), fill=(color2))
      if color == "green":
        color2 = (0,128,0)
        draw.rectangle(((280, 141), (267, 151)), fill=(color2))
        draw.rectangle(((312, 141), (298, 151)), fill=(color2))
      if color == "pink":
        color2 = (255,20,147)
        draw.rectangle(((280, 141), (267, 151)), fill=(color2))
        draw.rectangle(((312, 141), (298, 151)), fill=(color2))
      if color == "reset":
        color2 = (93,26,116)
        draw.rectangle(((280, 141), (267, 151)), fill=(color2))
        draw.rectangle(((312, 141), (298, 151)), fill=(color2))
      if color == "adminglaza":
        color2 = (93,26,116)




      
      if len(str(member.display_name)) > 8:
        draw.text((200, 48), f"{str(member.display_name)[:8]}", (255, 255, 255), font=font)
        draw.text((504, 230), f"Уровень: {level}", (0, 0, 0), font=font)
        draw.text((504, 300), f"Открыто ачивок: {data5[str(member.id)]['dosh2']}", (0,0,0), font=font)
        draw.text((504, 160), f"Сообщений: {data[str(member.id)]['count']}", (0,0,0), font=font)
      else:
        draw.text((200, 48), f"{str(member.display_name)}", (255, 255, 255), font=font)
        draw.text((504, 230), f"Уровень: {level}", (0, 0, 0), font=font)
        draw.text((504, 300), f"Открыто ачивок: {data5[str(member.id)]['dosh2']}", (0,0,0), font=font)
        draw.text((504, 160), f"Сообщений: {data[str(member.id)]['count']}", (0,0,0), font=font)
      #сохраняем картинку
      banner.save("profile.png")
      #отправляем картинку
      await ctx.send(file=discord.File("profile.png"))



# ------------------------------------- - ------------------------------------ #



# ------------------------------------- аватар ------------------------------------ #

# ------------------------------------- - ------------------------------------ #

# ------------------------------------- инфа ------------------------------------ #

# ------------------------------------- - ------------------------------------ #

@client.command()
async def deleteall(ctx, role):
    for member in ctx.guild.members:
        await member.remove_roles(role)
# ---------------------------------- play, p --------------------------------- #



#на определённую ошибку отправлять сообщение
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=discord.Embed(
            title=":warning: Использована неизвестная команда.",
            description=
            "Пожалуйста, напишите `m.help` для списка команд и соответствующего использования.",
            delete_after=10.0,
            color=0xFF0080))
        print(error)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            embed=discord.Embed(title=":angry: Вы не в голосовом канале!",
                                delete_after=10.0,
                                color=0xFF0080))
        print(error)
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(embed=discord.Embed(
            title=":no_entry_sign: У меня нет прав для этой команды!",
            delete_after=10.0,
            color=0xFF0080))
        print(error)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
            title=":no_entry_sign: Команда на время выполняется!",
            delete_after=10.0,
            color=0xFF0080))
    elif isinstance(error, commands.CheckFailure):
        await ctx.send(embed=discord.Embed(
            title=":no_entry_sign: У вас нет прав для этой команды!",
            delete_after=10.0,
            color=0xFF0080))
        print(error)
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send(embed=discord.Embed(
            title=":no_entry_sign: Ошибка выполнения команды!",
            delete_after=10.0,
            color=0xFF0080))
        print(error)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(
            title=":no_entry_sign: Команда на время выполняется!",
            delete_after=10.0,
            color=0xFF0080))
        print(error)


# -------------------------------- remove, rm -------------------------------- #


@commands.has_any_role("Основатель", "Модератор", "Тех.администратор","Старший модератор","Модератор (Исп.срок)")
@client.command(name="поиск")
async def search(ctx, word):
    with open('words.json', "r") as f:
        prefixes = json.load(f)

    if not str(word) in prefixes:
        return await ctx.send(f'Город "{word}" не найден',delete_after = 10)

    embed = discord.Embed(description=f"""**Город {word} найден**""",color=0xFF0080)
    embed.add_field(name="Его создатель", value=f"<@{prefixes[word]}>", inline=False)
    embed.set_footer(
                text="С уважением, администрация World of Colonization",
                icon_url=
                "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
            )
    await ctx.send(embed=embed,delete_after = 10)
    await ctx.message.delete()
  
@commands.has_any_role("Основатель", "Тех.администратор","Старший модератор")
@client.command("админ")
async def admin(ctx):
  embed=discord.Embed(description="""
  **Список админских команд**
  
  **m.поиск** - Cмотрит список городов которые уже созданы.
  **m.город** - Посмотреть какой район есть у города, кто одобрил и сколько чанков выдал.
  **m.одобрить** - Одобрить район человеку, (Использование - m.одобрить и нажимаем на кнопку ответить, также как и с m.gorot2 только в конце написать сколько чанков выдано m.одобрить Количество чанков, m.одобрить 10)
  **m.gorot2** - Написать сообщение о создании города (Использование - m.gorot2 и нажимаем на кнопку ответить, человеку пишет текст и выдаёт роль)

  Каждый раз когда одобряете район, вы должны прописывать m.одобрить чтобы занести в базу данных город.
  """,color=0xFF0080)
  embed.set_image(
        url=
        "https://media.discordapp.net/attachments/683979559577714728/1013438736840785920/unknown.png"
    )
  embed.set_footer(
                text="Администрация World of Colonization",
                icon_url=
                "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
            )
  await ctx.send(embed=embed)
@commands.has_any_role("Основатель", "Модератор", "Тех.администратор","Старший модератор","Модератор (Исп.срок)")
@client.command(name="123123213123")
async def dobav(ctx, word, word2, word3):
# записывать 1 значение и 2 значение и человека который вызвал команду в test.json
    with open('test.json', 'r') as file:
        data = json.load(file)
    if word in data:
      if word2 in data[word]:
        embed=discord.Embed(title=f'Район "{word2}" уже одобрен!',
                                      color=0x00FF00)
        embed.set_footer(
                text="Администрация World of Colonization",
                icon_url=
                "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
            )
        await ctx.send(embed=embed,delete_after = 10)
      else:
        data[word].append(word2)
        data[word].append(word3)
        data[word].append(f"<@{ctx.author.id}>")
        embed=discord.Embed(title=f"Район добавлен!", description=f"Город: {word}",color=0x00FF00)
        embed.set_footer(
                text="Администрация World of Colonization",
                icon_url=
                "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
            )
        await ctx.send(embed=embed)
        await ctx.message.delete()

    else:
        data[word] = [word2, word3, f"<@{ctx.author.id}>"]
    with open('test.json', 'w') as file:
        json.dump(data, file)

@commands.has_any_role("Основатель", "Модератор", "Тех.администратор","Старший модератор","Модератор (Исп.срок)")
@client.command(name="Город")
async def gorot1231(ctx, word):
    # искать в test.json значение которое указал участник и показывать все данные в этом значении
    with open('test.json', 'r') as file:
        data = json.load(file)
    if word in data:
        embed=discord.Embed(title=f"Информация по городу {word}", description=f"{data[word]}",color=0x00FF00)
        embed.set_footer(
                text="Администрация World of Colonization",
                icon_url=
                "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
            )
        await ctx.send(embed=embed)
        await ctx.message.delete()
    else:
        embed=discord.Embed(title=f"У города {word} ещё не проверяли чанки.",color=0xFF0000)
        embed.set_footer(
                text="Администрация World of Colonization",
                icon_url=
                "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
            )
        await ctx.send(embed=embed)


# ------------------------------------- - ------------------------------------ #
# ------------------------------------- channel ------------------------------------

# ------------------------------------- 8ball ------------------------------------

# ------------------------------------- - ------------------------------------


# ------------------------------------- 8ball ------------------------------------
@client.command(name="8ball")
async def _8ball(ctx, *, question):
    if ctx.channel.id != 1024734194817044611:
        embed = discord.Embed(
            title="Ошибка :angry:",
            description=
            f"Мой создатель запретил тут использовать эту команду :(",
            color=0xFF0080)
        embed.set_footer(text=f'{ctx.message.author}',
                         icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
    else:
        if question == None:
            await ctx.send("Вы не ввели вопрос", delete_after=10.0)
            return
        responses = [
            'Это точно.', 'Это определенно так.', 'Без сомнения.',
            'Да - определенно.', 'Вы можете положиться на это.',
            'Скорее всего.', 'Хорошая перспектива.', 'Да',
            'Знаки указывают на да.', 'Ответить туманно, попробуйте еще раз.',
            'Спросить позже.', 'Лучше не говорить вам сейчас.',
            'Невозможно предсказать сейчас.',
            'Сконцентрируйтесь и спросите еще раз', "Не рассчитывайте на это.",
            'Мой ответ - нет', 'Мои источники говорят нет',
            'Перспектива не очень хорошая.', 'Очень сомнительно.'
        ]
        responses = random.choice(responses)
        embed = discord.Embed(
            title=f"Вопрос от: {ctx.author.name}: {question}", color=0xFF0080)
        embed.add_field(name="Ответ:", value=responses, inline=False)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()


# ------------------------------------- - ------------------------------------


@client.command()
async def moderation(ctx):
    embed = discord.Embed(
        title=
        "**Приветствуем тебя на проекте World of Colonization, дорогой любитель политических серверов!**",
        description="Коротко о сервере:",
        color=0xFF0080)
    embed.add_field(name="- Действия происходят в XVI веке",
                    value="-",
                    inline=False)
    embed.add_field(
        name=
        "- Карта представляет собой необитаемый континент в Тихом океане, на который приплывают колонизаторы(игроки).",
        value="-",
        inline=False)
    embed.set_thumbnail(
        url=
        "https://sun9-17.userapi.com/impg/jz1svf1aosSnhI-1iixA0jQ1ejD-MpoMlpTXAA/slU9VrxjuRE.jpg?size=1665x895&quality=96&sign=9aa57997c122a0b23f84e2e9d9876f86&type=album"
    )
    embed.add_field(
        name=
        "- Игрок появляется недалеко от сейф-зоны - горной деревушке, где стоят **торговцы** и игрок может получить **квесты**.",
        value="-",
        inline=False)
    embed.add_field(
        name=
        "Далее игрок либо создает свой город, подав тикет, либо присоединяется к существующему. ",
        value=
        "В первом случае игрок подает тикет в отдельном канале, пишет заявку, описанную ниже и ожидает ответа администрации. ",
        inline=False)
    embed.add_field(
        name=
        "Если вам одобрят город - прилетит админ и выдаст право на основание города.",
        value=
        "Если же вы захотите вступить в существующий город - просто свяжитесь с его главой и попросите его принять вас.",
        inline=False)
    embed.add_field(
        name=
        "- Карту, а также расположение городов вы можете наблюдать на динамической карте - ",
        value="http://indieplay.ru:29854/",
        inline=False)
    embed.add_field(
        name=
        "- На карте **ресурсов в два с половиной раза меньше**, чем обычно. ",
        value=
        "Но присутствуют крупные залежи, о которых вы сможете узнать в ходе прохождения квестов",
        inline=False)
    embed.add_field(
        name=
        "- Каждый день, **в 18:00 по МСК **проходит **ивент**. Суть ивента удержать три точки (или большинство точек)",
        value=
        "Ивент проходит 20 минут и по окончанию будут оглашены победители и выданы **награды**. ",
        inline=False)
    embed.set_footer(text="World of Colonization",
                     icon_url="https://i.ibb.co/pZjPKbB/unknown.png")
    embed.set_image(
        url=
        'https://sun9-17.userapi.com/impg/jz1svf1aosSnhI-1iixA0jQ1ejD-MpoMlpTXAA/slU9VrxjuRE.jpg?size=1665x895&quality=96&sign=9aa57997c122a0b23f84e2e9d9876f86&type=album'
    )
    await ctx.send(embed=embed)


@client.command()
async def moderation1(ctx):
    embed = discord.Embed()
    embed.add_field(
        name=
        "7 апреля, в 18:00 начинается закрытый бета-тест. Всех желающих приглашаем принять участие в тестировании геймплея! Тест продлится от двух до четырех дней, затем прогресс сбросится, произойдет вайп.",
        value=
        "Всем участникам бета-теста будет выдан бонус при открытии. Для подачи заявки нужно написать свой ник Streamcraft ",
        inline=False,
        color=0xFF0080)
    embed.add_field(
        name="- В Discord специальном канале (https://discord.gg/Hv2nxRSEKH). ",
        value=
        "Надеемся вместе с вами мы выявим основные критические ошибки, недоработки и подготовим сервер к открытию! (ссылка на Streamcraft - https://streamcraft.net) ",
        inline=True)
    embed.set_footer(text="С уважением, администрация World of Colonization")
    await ctx.send(embed=embed)


@client.command()
async def test(ctx):
    embed = discord.Embed(
        title=
        """World of colonization готовится принять первых колонизаторов уже в эту пятницу!
Кратко напомним вам что мы из себя представляем:""",
        color=0xFF0080)
    embed.add_field(
        name=
        "WOC – это выживание с элементами политики. Здесь ты можешь создать свой город или присоединиться к другим. Развивай его и приведи свой народ к победе. Из достоинств сервера можно выделить: ",
        value="""
 - Продвинутая экономика
 - Улучшенная боевая система
- Мушкеты и полевые пушки
- Настоящие плавучие корабли
- Система прокачки города
- Квесты, которые иногда помогут отвлечься от градостроения
- Ежедневное событие по захвату точек
- Красивый текстурпак, подчеркивающий средневековую атмосферу
- Политическая система
- Уникальный континент
- Онлайн карта 
  """)
    embed.add_field(name="Открытие сервера: 22.04.22 в 18:00 МСК",
                    value="Сайт - https://streamcraft.net/",
                    inline=False)
    embed.set_image(
        url=
        "https://sun9-7.userapi.com/s/v1/ig2/OiqGCgTf38NfYuvb7qJ6MZ9tDM-oauR10vufBQe1yAeHP_KQfDYHTgxdRpxBu-6aocrLj8-gMmVY94Fuv1g5xx8h.jpg?size=1280x720&quality=95&type=album"
    )
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def test2(ctx):
    embed = discord.Embed(description="""
 
 **Сервер доступен, можно начинать приключения.**
В лаунчере **StreamCraft** выбирайте **WOC**, не забудьте в настройках лаунчера выделить побольше оперативной памяти.
**Не пропускайте диалоги с NPC**, прописывайте **/kit start**, кооперируйтесь с другими игроками!
 
 """,
                          color=0xFF0080)
    embed.set_image(
        url=
        "https://sun9-84.userapi.com/s/v1/ig2/pKd8IYZ_HwA-hOtY9hO8aD5uVmO7U4vVBLp5Hw3z9urCRGOgDQzzF_n1pom0Z38WTNdRaUkRxC56UcTQ5gW1FRu7.jpg?size=1280x720&quality=95&type=album"
    )
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()

@commands.has_any_role("Основатель","Тех.администратор","Старший модератор")
@client.command()
async def vadim(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description="""
 
Наблюдаются технические неполадки и некорректная работа сервера. Администрация работает над устранением неполадок.
 
 """,
                          color=0xFF0080)
    embed.set_image(
        url=
        "https://media.discordapp.net/attachments/811324049224630323/967427138280120330/unknown.png"
    )
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send("||@everyone||",embed=embed)

@client.command()
async def test1312312(ctx):
  channel = client.get_channel(961668931934879794)
  msg_id = 988401138976051260
  msg = await channel.fetch_message(msg_id)
  embed = discord.Embed(description="""
 
**4. Игровой чат**
4.1 Запрещено писать в чат рекламы не по назначению, а также общение через рекламный чат.(Пример 1: # Продам гараж. Пример 2: # Толик привет! Как у тебя дела. За такое администрация будет давать вам мут)
4.2 NonRP оскорбления запрещены и сильно наказываются администрацией сервера.
Пример нарушения: [Глобальный чат] ! Долб#б, что ты делаешь. (Такое оскорбление будет наказываться) (Оскорбление в локальном чате в рамках рп наказываться не будет.) Пример нарушения: Вы пришли к человеку в приват и начали его просто так оскорблять. Пример без нарушения: Вы глава города увидели что ваш горожанин ничего не делает и сказали ему:"Алло, долб#б, давай работай")
4.3 Запрещено оскорблять в любом из чатов родных.
 
 """,color=0xFF0080)
  await msg.edit(content=embed)
  
@commands.has_any_role("Основатель","Тех.администратор","Старший модератор")
@client.command()
async def vadim2(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description="""
 
Администрация приносит свои извинения за то, что сервер длительное время был не доступен. Сейчас доступ восстановлен, приятной игры.
Ежедневный ивент по захвату точек будет запущен в 21:00 по МСК.
 
 """,
                          color=0xFF0080)
    embed.set_image(
        url=
        "https://media.discordapp.net/attachments/811324049224630323/967430393311686676/unknown.png"
    )
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send("||@everyone||",embed=embed)
 


@client.command()
async def gorott(ctx):
    embed = discord.Embed(description="""
 
**Ваш город готов, и вот короткий список начальных команд:**
**Имейте ввиду, каждые 24 часа со счета вашего города будет списываться 10 реалов. **
/t - Информация о городе.
/towny map - Карта чанков для привата.
/town add/kick <Ник> - Добавить/кикнуть игрока.
/town claim - Захватить чанк в котором стоишь.
/plot unclaim - уменьшить территорию Вашего участка.
/towny - Подсказки с командами.
/t deposit/withdraw <Сумма> - положить/снять в/с города.
/t invite - пригласить участника в город.
/town withdraw [количество] - снять деньги со счета города.
/town set taxes [количество] - установить налог, который будет ежедневно собираться с жителей.
/plot toggle mobs  [on/off] - включить / отключить враждебных мобов на участке.
/t rank add [Ник] assistant. - добавить ассистента.
/t toggle pvp off - Отключить ПВП.
 
 """,
                          color=0xFF0080)
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def ivent(ctx):
    embed = discord.Embed(description="""
Вся символика и упоминания запрещённых в России организаций должны быть стёрты с сервера в течение дня.
 """,
                          color=0xFF0080)
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def poc(ctx):
    await ctx.send("@everyone")
    embed = discord.Embed(description="""
В центре континента, в славном городе **Midburg** развернул свою лавку местный торговец. Говорят, привез с большой земли новые семена...
 """,
                          color=0xFF0080)
    embed.set_image(
        url=
        "https://sun1-86.userapi.com/s/v1/ig2/fpasYeOcX8UHPkOUYl8HyKU0VBiBGZ2wR5pSJBRI850yCO4kjejwZx1jiz7MvJScqQ3MMW_x8wHPZT0MzIouUbJc.jpg?size=1920x987&quality=96&type=album"
    )
    embed.set_footer(
        text="Слухи с просторов Ганории... ",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
@commands.has_guild_permissions(administrator=True)
async def on(ctx):
    embed = discord.Embed(color=0xFF0080)
    embed.set_image(
        url=
        "https://sun9-86.userapi.com/s/v1/ig2/JlDLProhY9y4r1wcfKm64C15V13fsFT-w8YIQCcG1i7_6HKFcH3HW1N7SQP4CSbkok3JIfDCNWpZeMcm2w3hoqxV.jpg?size=1280x720&quality=96&type=album"
    )
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
@commands.has_guild_permissions(administrator=True)
async def off(ctx):
    embed = discord.Embed(color=0xFF0080)
    embed.set_image(
        url=
        "https://sun9-43.userapi.com/s/v1/ig2/x8KXJh64K4adnLARgNLFrU9OZSQIjUERKAtxOglheHFXaiq_RhxqzDVqa4fHYfUaM98kqBeNKb73c7woerAf-7k_.jpg?size=1280x720&quality=96&type=album"
    )
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()

@commands.has_any_role("Основатель", "Модератор", "Тех.администратор","Старший модератор")
@client.command()
async def moder(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description="""
 
==================================================
**Non rp chat **- Это **чат**, в котором игроки могут общаться на расстоянии на свою тематику, **т.е не в рамках рп.**
**Rp Chat** - Это чат, для общения по **ролям**, т.е рп чат заменяет для вас** голосовой чат**
и конечно-же в РП есть свои правила,которыми вы должны следовать,для того что-бы вас поняли те,с кем вы ролите.
**Заходя на сервер, вы автоматически соглашаетесь со списком правил снизу.**
==================================================
**ПРАВИЛА ПОВЕДЕНИЯ НА СЕРВЕРЕ**
**1. Общие положения и правила**
1.1. **Помните - незнание правил сервера не освобождает от ответственности!**
1.2. Администрация не несёт ответственности за взломанные аккаунты. Любое действие злоумышленника от вашего игрового аккаунта будет принято, как ваше.
1.3 Вы несёте полную ответственность за свой аккаунт и будете получать наказание за нарушения совершенные на нём.
(Даже если это сделал ваш брат, внук или домашний питомец)
1.4. Администрация абсолютна. Любое принятое администратором решение, до момента его оспаривания, будет считаться истинно-правильным.
1.5. Запрещено использование, а также хранение любых читов, модов, ресурспаков, программ, скриптов и модификаций, дающих преимущество над другими игроками, в том числе встроенного в периферию (клавиатуру/мышку), а также любых технических модификаций или нестандартных методов использования периферии.  
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(PermaBan)↑**__
1.6. Запрещено использование и сокрытие от администрации багов сервера, а также обход игровых ограничений любым путем.  
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(На усмотрение администрации)↑**__
1.7. Запрещено использование недоработок/уязвимостей в правилах сервера. (Если вы нашли недоработку/уязвимость на сервере - просьба сообщить администрации.)  
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(На усмотрение администрации)↑**__
1.8. Запрещена провокация или подталкивание к нарушению правил сервера игроков. Правило не распространяется на общение между игроками в любых модерируемых зонах. Данное правило не освобождает спровоцированного от ответственности.  
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(На усмотрение администрации)↑**__
1.9. Запрещены деструктивные действия по отношению к проекту: неконструктивная критика, призывы покинуть проект, попытки нарушить развитие проекта, атаки на ресурсы проекта или любые другие действия, способные привести к помехам в игровом процессе. __**(PermaBan)**__
1.10. Запрещены попытки нанесения урона экономике сервера. 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __ **↑(1 warn)↑**__
1.11. В зависимости от ситуации наказания могут пересматриваться администрацией.
За нарушения любого из правил в этом блоке следует наказание в виде временной или перманентной блокировки аккаунта.
 
 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed = discord.Embed(description="""
 
**2. Правила поведения**
2.1. Запрещены угрозы, оскорбления, провокации в отношении реальной жизни игрока. 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**(За слабое оскорбление будет слабое наказание. За сильное - сильное наказание) (Пример сильного - Дол#аёб, еб#ан, иди работай давай) (Пример слабого - Ты тупой, дебил, иди работай давай) (Правило не действует если человек это делает в РП, т.е если допустим глава города сказал своему жителю, Алло, дол#аёб иди работай, за это не даём наказание, если челвоек написал в ooc такое, то мут) (Слабое = tempmute 30m. Сильное = tempmute 2h)**__
2.2. Запрещена реклама любых сторонних ресурсов.  
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(PermaBan)↑**__
2.3. Запрещён флуд и спам в чате. (Спамом или флудом считается повторение одного и того же сообщения от трёх раз) 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(TempMute - 30m)↑**__
2.4. Запрещено распространение дезинформации о проекте. 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(1 warn)↑**__
2.5. Распространение вредоносного ПО или ссылок запрещено. 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(PermaBan)↑**__
2.6. Ник игрока не должен состоять из оскорблений или плохих слов. (Если администратор видит, что в вашем нике присутствуют оскорбления или плохие слова, ваш ник изменяется на тот, который вы предложите)
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑За нарушение любого из правил в этом блоке следует наказание в виде мута от получаса до суток.↑**__
 
 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed = discord.Embed(description="""
 
**3. Игровой процесс**
3.1. Игрок не может иметь больше одного аккаунта. 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(Блокировка всех аккаунтов, кроме основного)↑**__
3.2. Запрещена порча ландшафта. Что является порчей ландшафта, решает администратор. 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(1 warn)↑**__
3.3. Выпрашивать у Администрации ресурсы или права запрещено. 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(TempMute 30m)↑**__
3.4. Запрещено мешать игровому процессу, к примеру помехи строительству или РП-ситуациям.  
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(Кик с сервера/временная блокировка аккаунта)↑**__
3.5. Гриферство запрещено.
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(Warn (Кол-во по усмотрению администрации))↑**__
3.6. Внедрение в город с целью гриферства запрещено. (Когда человек присоединяется к городу чтобы уничтожить постройки и/или украсть ресурсы.) 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(Warn (Кол-во по усмотрению администрации))↑**__
3.7 Запрещаются многочисленные убийства беззащитных игроков рядом с точкой их возрождения.  
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(1 warn))↑**__
3.8 Запрещается закрывать на продолжительное время игроков в привате. | Максимум на сколько можно закрыть это - 30 минут 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(1 warn)↑**__
3.9 Запрещается использование афк-рыбалки. | 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(1 пред дальше 1 warn)↑**__
3.10 Запрещается использование алмазных арбалетов. |  
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(1 пред дальше 1 warn)↑**__
3.11 Минимальное расстояние между приватами должно быть 5 чанков. 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(Снос чанка)↑**__
3.12 Запрещены постройки:
1) Преимущественно построенные из одного или двух типов блоков (булыжник, доски, земля и прочее).
2) В виде коробок или напоминающие коробки, а также состоящие из множества коробок.
3) Постройки в воздухе, без опоры, которые выглядят неестественно.
4) Портящие красоту окружающего ландшафта или не вписывающиеся в него.
5) Конструкции (механизмы/фермы и прочее), создающие нагрузку на сервер ("клок"-генераторы, "мигалки", фермы с большим количеством животных) 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ **↑(Снос постройки)↑**
3.13 Запрещена автоматизация производства.
Администрация оставляет за собой право сноса построек без уведомления игроков.
__**(Наказание — снос постройки + варн(предупреждение) по причине 3.2.)**__
Примечание: постройка может быть снесена или продана администрацией, если владельцы региона отсутствовали более 1 месяца.

 
 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed = discord.Embed(description="""
 
**4. Игровой чат**
4.1 Запрещено писать в чат рекламы не по назначению, а также общение через рекламный чат.(Пример 1: # Продам гараж. Пример 2: # Толик привет! Как у тебя дела. За такое администрация будет давать вам мут) 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __ **↑(tempmute 1h)↑**__ 
4.2 NonRP оскорбления запрещены и сильно наказываются администрацией сервера.
Пример нарушения: [Глобальный чат] ! Долб#б, что ты делаешь. (Такое оскорбление будет наказываться) (Оскорбление в локальном чате в рамках рп наказываться не будет.) Пример нарушения: Вы пришли к человеку в приват и начали его просто так оскорблять. Пример без нарушения: Вы глава города увидели что ваш горожанин ничего не делает и сказали ему:"Алло, долб#б, давай работай") 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(1 warn)↑**__
4.3 Запрещено оскорблять вне зависимости от чата родных.
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __ **↑(1 warn)↑**__
4.4 Запрещены вне зависимости от чата любые упоминание родных. 
 ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ  ᅠ __**↑(1 warn)↑**__

 
 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed = discord.Embed(description="""
 
** Выдача наказаний**
/tempmute - временный мут (Пример: /tempmute animetan 1h 4.1)
/mute - мут навсегда (Пример: /mute animetan 4.1 )
/tempban - бан на время (Пример: /ban animetan 1h 4.1)
/ban - бан навсегда (Пример: /ban animetan 4.1)

 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed.set_footer(
        text="С уважением, администрация World of Colonizationn",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)




@client.command()
async def obnova(ctx):
    embed = discord.Embed(description="""
 
**ОБНОВЛЕНИЕ 1.0**
**"Обман и сила - орудие злых"**
**Удалено:**
-Epic fight(мод на боевую систему)
-Corpse(мод на трупы)
-Максимальный уровень зачарований уменьшен.
-Зачарование огненная стрела
-Северное сияние
-Бонус чанки за нацию
**Добавлено:**
-Anti x-ray
-Anti-Cheat
-Автоматизированная система воин (смотрите обновленную статью)
-Добавлен в продажу у NPC кварц
-Добавлено на скупку у NPC баранина
-Появление сообщения из чата над игроком
-Кнопки-подсказки в группе ВКонтакте
-Система спасения. Теперь, при смерти, в течении минуты, игрока может поднять союзник, а враг - добить. Чтобы поднять союзника нужно подойти к нему и зажать ПКМ до заполнения индикатора.
-Команда /t spawn теперь доступна (цена 15 реалов)
-Ник теперь можно посмотреть нажав ПКМ по игроку
**Изменено:**
-Глобальный чат больше недоступен игрокам
-Теперь, при основании, город будет иметь не 16, а 32 чанка.
-Скорректированы цены на куплю/продажу у NPC
-Всадники получают бонус +5 к урону
-Уведомление о кике/бане видят все игроки
-Статья "Районы и чанки города"
-Статья "Основы и суть сервера"
-Статья "Война"
-Правила сервера
**Планы на ближайшее будущее:**
-Восстановить профессии
-Восстановить алкоголь
-Работа над оптимизацией и повышением стабильности сервера
-Борьба с читерами
-Многочисленные корректировки в геймплее и экономике
-Корректировки в механике войны
 
 """,
                          color=0xFF0080)
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    embed.set_image(
        url=
        "https://sun9-7.userapi.com/s/v1/ig2/gsWpxFYHHpCFxJ8fHsgcqnwGem8o3ifPsCmlJStlutMrWHxHDlKjwia5_bjBEkZXC-9KLW99ESPD0cEuMB_q-qa-.jpg?size=1280x720&quality=95&type=album"
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def wetgfwetgwtginfo(ctx):
    embed = discord.Embed(description="""
 
**Основные команды для управления городом:**
/t - Информация о городе.
/towny map - Карта чанков для привата.
/town add/kick <Ник> - Добавить/кикнуть игрока.
/town claim - Захватить чанк в котором стоишь.
/plot unclaim - уменьшить территорию Вашего участка.
/towny - Подсказки с командами.
/t deposit [Сумма] - положить деньги в город.
/t invite - пригласить участника в город.
/town withdraw [количество] - снять деньги со счета города.
/t rank add [Ник] assistant - добавить ассистента.
/t set taxes [количество] - установить налог, который будет ежедневно собираться с жителей.
/tset plottax [количество] - установить налог, который будет ежедневно собираться с жителей, имеющих собственные участки.
/t set plotprice [количество] - установить стоимость покупки собственного участка.
/t toggle explosion on/off - включить / отключить TNT в городе.
/t toggle open on/off - включить / отключить вступление в Ваш город без приглашения.
Городские участки:
/plot - информация о команде.
/plot claim - выделить собственный участок в городе.
/plot toggle mobs [on/off] - включить / отключить враждебных мобов на участке.
Уменьшение участков:
/plot unclaim - уменьшить территорию Вашего участка.
Продаж участков:
/plot forsale - выделить участок на продажу.
/plot forsale [цена] - установить цену участка.
Снятие с продажи участков:
/plot notforsale - снять участок с продажи.
Указание типа участков:
/plot set reset - сбросить на обычный участок.
/plot set arena - изменить участок на арену с PvP.
Настройка допуска на участок:
/plot set perm on / off - включить / отключить изменения настроек на участке.
/plot set perm [категория] on / off - разрешить / запретить некой категории изменять что-либо на участке.
/plot set perm [действие] on / off - разрешить / запретить всем действие.
/plot set perm [категория] [действие] on / off - разрешить / запретить указанной категории указанное действие.
/plot set perm perm reset - вернуть стандартные настройки на участке.
Дополнительно:
/towny top land [all/resident/town] - ֪список больших городов по размерам.
/towny top residents [all/town/nation] - список активных жителей.
/towny time - определить время плагина. (важно знать, чтобы быть в курсе когда собирают налоги)
Нации:
/nation - информация о Вашей нации.
/nation ? - информация о команде.
/nation list - список наций.
/nation leave - убрать Ваш город из нации.
/nation [название] - информация о конкретной нации.
/nation online - показать игроков из нации, которые находятся на сервере.
/nation withdraw [количество] - снять деньги из банка нации.
/nation deposit [количество] - положить деньги в банк нации.
/nation new [название] - создать нацию.
/nation assistant add [ник] - назначить ассистента нации.
/nation assistant remove [ник] - разжаловать ассистента нации.
/nation add [название] - добавить город в нацию.
/nation kick [название] - убрать город из нации.
/nation delete - удалить нацию.
/nation ally add [название] - добавить нацию в альянс.
/nation ally remove [название] - убрать нацию из альянса.
/nation enemy add [название] - добавить нацию в список врагов.
/nation enemy remove [название] - убрать нацию из списка врагов.
/nation set king [ник] - назначить игрока новым королем нации.
/nation set capital [город] - назначить столицу нации.
/nation set name [название] - изменить название нации.
/nation set taxes [количество] - установить размер налога с городов в банк нации.
/nation toggle neutral on/off - вкличить/отключить военное положение.(на нашем сервере стоит 100 реалов)
/tr survey — захватить ресурс (ресурс должен находится на территории города, а игрок, прописывающий команду, на чанке с ресурсом)
/tr towncollect — собрать ресурс (ресурс можно собирать раз в 24 часа КАЖДОМУ горожанину, находясь при этом на территории города)
/tr nationcollect — собрать ресурс нации (для участников нации)
/tr survey — улучшить ресурс до следующего уровня (находясь на чанке с ресурсом, при захвате ресурса ему присваивается 1 уровень)
Аванпост:
/town claim outpost
***Реал - игровая валюта сервера.**
 
 """,
                          color=0xFF0080)
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    await ctx.message.delete()

@commands.has_any_role("Основатель", "Модератор", "Тех.администратор","Старший модератор")
@client.command()
async def egsgsgeshosnova(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description="""
 
**Коротко о сервере:**
События сервера разворачиваются на вымышленных, малозаселенных островах в эпоху колонизации. (18 век)
Вы прибываете на континент в составе одного из пассажирских рейсов, которые приплывают сюда регулярно вместе с добровольцами. На новом материке Европейцам была обещана бесплатная земля.
Король приказал в кратчайшие сроки исследовать и заселить материк настолько, насколько это возможно. Европейцы то приплыть успели, чего не скажешь о законах… Их здесь нет!
У нас есть собственная [карта](https://woc-map.streamcraft.net/), где спавн руд уменьшен в 2.5 раза, однако это компенсируется системой ресурсов.
- Каждый день, в 18:00 по МСК проходит ивент. Суть ивента удержать три точки (или большинство точек)
Ивент проходит 20 минут и по окончанию будут оглашены победители и выданы награды.
 
 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed = discord.Embed(description="""
 
==================================================
**Non rp chat **- Это **чат**, в котором игроки могут общаться на расстоянии на свою тематику, **т.е не в рамках рп.**
**Rp Chat** - Это чат, для общения по **ролям**, т.е рп чат заменяет для вас** голосовой чат**
и конечно-же в РП есть свои правила,которыми вы должны следовать,для того что-бы вас поняли те,с кем вы ролите.
**Заходя на сервер, вы автоматически соглашаетесь со списком правил снизу.**
==================================================
**ПРАВИЛА ПОВЕДЕНИЯ НА СЕРВЕРЕ**
**1. Общие положения и правила**
1.1. **Помните - незнание правил сервера не освобождает от ответственности!**
1.2. Администрация не несёт ответственности за взломанные аккаунты. Любое действие злоумышленника от вашего игрового аккаунта будет принято, как ваше.
1.3 Вы несёте полную ответственность за свой аккаунт и будете получать наказание за нарушения совершенные на нём.
(Даже если это сделал ваш брат, внук или домашний питомец)
1.4. Администрация абсолютна. Любое принятое администратором решение, до момента его оспаривания, будет считаться истинно-правильным.
1.5. Запрещено использование, а также хранение любых читов, модов, ресурспаков, программ, скриптов и модификаций, дающих преимущество над другими игроками, в том числе встроенного в периферию (клавиатуру/мышку), а также любых технических модификаций или нестандартных методов использования периферии.
1.6. Запрещено использование и сокрытие от администрации багов сервера, а также обход игровых ограничений любым путем.
1.7. Запрещено использование недоработок/уязвимостей в правилах сервера. (Если вы нашли недоработку/уязвимость на сервере - просьба сообщить администрации.)
1.8. Запрещена провокация или подталкивание к нарушению правил сервера игроков. Правило не распространяется на общение между игроками в любых модерируемых зонах. Данное правило не освобождает спровоцированного от ответственности.
1.9. Запрещены деструктивные действия по отношению к проекту: неконструктивная критика, призывы покинуть проект, попытки нарушить развитие проекта, атаки на ресурсы проекта или любые другие действия, способные привести к помехам в игровом процессе.
1.10. Запрещены попытки нанесения урона экономике сервера.
1.11. В зависимости от ситуации наказания могут пересматриваться администрацией.
За нарушения любого из правил в этом блоке следует наказание в виде временной или перманентной блокировки аккаунта.
 
 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed = discord.Embed(description="""
 
**2. Правила поведения**
2.1. Запрещены угрозы, оскорбления, провокации в отношении реальной жизни игрока. (За слабое оскорбление будет слабое наказание. За сильное - сильное наказание)
2.2. Запрещена реклама любых сторонних ресурсов.
2.3. Запрещён флуд и спам в чате. (Спамом или флудом считается повторение одного и того же сообщения от трёх раз)
2.4. Запрещено распространение дезинформации о проекте.
2.5. Распространение вредоносного ПО или ссылок запрещено.
2.6. Ник игрока не должен состоять из оскорблений или плохих слов. (Если администратор видит, что в вашем нике присутствуют оскорбления или плохие слова, ваш ник изменяется на тот, который вы предложите)
**За нарушение любого из правил в этом блоке следует наказание в виде мута от получаса до суток.**
 
 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed = discord.Embed(description="""
 
**3. Игровой процесс**
3.1. Игрок не может иметь больше одного аккаунта. | Блокировка всех аккаунтов, кроме основного.
3.2. Запрещена порча ландшафта. Что является порчей ландшафта, решает администратор. | 1 warn.
3.3. Выпрашивать у Администрации ресурсы или права запрещено. | Мут
3.4. Запрещено мешать игровому процессу, к примеру помехи строительству или РП-ситуациям. | Кик с сервера/временная блокировка аккаунта.
3.5. Гриферство запрещено. | Warn (Кол-во по усмотрению администрации)
3.6. Внедрение в город с целью гриферства запрещено. (Когда человек присоединяется к городу чтобы уничтожить постройки и/или украсть ресурсы.) | Warn (Кол-во по усмотрению администрации)
3.7 Запрещаются многочисленные убийства беззащитных игроков рядом с точкой их возрождения.
3.8 Запрещается закрывать на продолжительное время игроков в привате. | Максимум на сколько можно закрыть это - 30 минут
3.9 Запрещается использование афк-рыбалки. | 1 пред дальше 1 warn
3.10 Запрещается использование алмазных арбалетов. | 1 пред дальше 1 warn
3.11 Минимальное расстояние между приватами должно быть 5 чанков.
3.12 Запрещены постройки:
1) Преимущественно построенные из одного или двух типов блоков (булыжник, доски, земля и прочее).
2) В виде коробок или напоминающие коробки, а также состоящие из множества коробок.
3) Постройки в воздухе, без опоры, которые выглядят неестественно.
4) Портящие красоту окружающего ландшафта или не вписывающиеся в него.
5) Конструкции (механизмы/фермы и прочее), создающие нагрузку на сервер ("клок"-генераторы, "мигалки", фермы с большим количеством животных)
3.13 Запрещена автоматизация производства.
Администрация оставляет за собой право сноса построек без уведомления игроков.
Наказание — снос постройки + варн(предупреждение) по причине 3.2.
Примечание: постройка может быть снесена или продана администрацией, если владельцы региона отсутствовали более 1 месяца.

 
 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed = discord.Embed(description="""
 
**4. Игровой чат**
4.1 Запрещено писать в чат рекламы не по назначению, а также общение через рекламный чат.(Пример 1: # Продам гараж. Пример 2: # Толик привет! Как у тебя дела. За такое администрация будет давать вам мут)
4.2 NonRP оскорбления запрещены и сильно наказываются администрацией сервера.
Пример нарушения: [Глобальный чат] ! Долб#б, что ты делаешь. (Такое оскорбление будет наказываться) (Оскорбление в локальном чате в рамках рп наказываться не будет.) Пример нарушения: Вы пришли к человеку в приват и начали его просто так оскорблять. Пример без нарушения: Вы глава города увидели что ваш горожанин ничего не делает и сказали ему:"Алло, долб#б, давай работай")
4.3 Запрещено оскорблять вне зависимости от чата родных. (1 warn)
4.4 Запрещены вне зависимости от чата любые упоминание родных. (1 warn)

 
 """,
                          color=0xFF0080)
    await ctx.send(embed=embed)
    embed = discord.Embed(description="""
 
**5. Донат**
5.1. Жертвуя на развитие проекта в качестве благодарности вы можете получить "привилегию или иной бонус" в зависимости от суммы пожертвования.
5.2 *Донат это не покупка чего либо, а добровольное пожертвование за которое вы получаете "спасибо" от streamcraft в виде привилегии или иного бонуса.
5.3 Никаких претензий относительно сохранности, качества, гарантий мы не принимаем. Никаких гарантий мы не даем.
5.4 Возврат ресурсов, которые Вы приобрели за Ваши средства, осуществляется в течение 14 дней после покупки и только в том случае, если они были утрачены вследствие ошибки со стороны сервера (баг или откат).
(Если Вы случайно купили привилегию не на тот сервер и ещё не забирали киты в игре, то обратитесь в течение 24 часов в группу streamcraft ВКонтакте, Ваша донат-группа будет перенесена на нужный Вам сервер.
На момент вайпа если у Вас остаётся 14 или больше дней до истечения донат-группы, то все киты (наборы ресурсов /cart) возвращаются в полном объёме (либо автоматически, либо через группу streamcraft ВКонтакте).
5.5 Вернуть средства возможно только в случае ошибки при совершении платежа, для этого необходимо написать на электронную почту frostboolio@gmail.com с предоставлением квитанции об оплате, суммы, даты и времени проведения Вашей транзакции.
 
 """,
                          color=0xFF0080)
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)





@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None:
        if after.channel.id == 967505478345191474:
            category = after.channel.category
            
            channel2 = await member.guild.create_voice_channel(
                name     = f' || { member.display_name } Канал', 
                category = category
            )
            
            await channel2.set_permissions(member, connect = True, manage_channels = True, administrator = True, manage_permissions = True, )
            await member.move_to(channel2)

            def check(x, y, z): return len(channel2.members) == 0
            
            await client.wait_for('voice_state_update', check = check)
            await channel2.delete()



@client.command()
async def info1(ctx):
    embed = discord.Embed(color=0xFF0080)
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    embed.set_image(
        url=
        "https://sun9-north.userapi.com/sun9-85/s/v1/ig2/uoQTOP73GYscgL6GFHTw81RX-6f1F2MfVk8bj9sVB9952ABtQL622ZFIFvpEgXduA0ePqhj_O4wILXoG0mNvzsVd.jpg?size=2560x1440&quality=96&type=album"
    )
    await ctx.send("||@everyone||", embed=embed)
    await ctx.message.delete()

@commands.has_any_role("Основатель", "Модератор", "Тех.администратор","Старший модератор")
@client.command()
async def fdgdfgdfgdfinfo2(ctx):
    await ctx.message.delete()
    embed = discord.Embed(description="""
 
У нас есть группа ВКонтакте, где публикуются эксклюзивные материалы по проекту. Сейчас, к примеру, там вышел пост с подборкой скриншотов локаций Парфея.
https://vk.com/worldofcolonization

 
 """,
                          color=0xFF0080)
    embed.set_footer(
        text=" С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    #mbed.set_image(
     #   url=
     #   "https://sun9-35.userapi.com/impg/Fw5GHyxt5HNaKtfLTJBYcTuyLQce8UD85Lr28g/ftJIOgY4igo.jpg?size=990x991&quality=96&sign=0c3ba4ab561f151cecdb9349b4ad5a96&type=album"
   # )

    await ctx.send("||@everyone||", embed=embed)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    await client.process_commands(message)
    
    if message.author == client.user:
        return
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('1'):
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('2'):
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('3'):
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('4'):
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('5'):
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('6'): 
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('7'):
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('8'):
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('9'):
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)
    if message.channel.type == discord.ChannelType.private:
     if message.content.startswith('0'):
        embed = discord.Embed(title='———————————————————', color=0x00ff00)
        embed.add_field(name='ᅠ ᅠᅠ ᅠᅠ  ᅠᅠ  Ошибка', value='Вы отправили сообщение не тому боту, отправьте его в личные сообщения бота на скриншоте (World of Colonization#3630)', inline=False)
        embed.add_field(name='——————————————————————', value='ᅠ')
        embed.set_image(url='https://media.discordapp.net/attachments/961668931934879794/988821845639852032/unknown.png')
        await message.channel.send(embed=embed)


@client.command()
async def fgdfgfdginfo3(ctx):
    await ctx.send("https://discord.gg/hN8KanNU?event=1005123391000432701")
    await ctx.message.delete()

@commands.has_any_role("Основатель", "Модератор", "Тех.администратор","Старший модератор","Модератор (Исп.срок)")
@client.command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="",
                          description=f"Удалил `{amount}` Сообщений!")
    embed.set_author(name=f"Запросил: {ctx.author.name}")
    embed.set_footer(
        text=f"Запросил: {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=ctx.author.avatar_url)
    massage = await ctx.send(embed=embed)


@slash.slash(
    name="Топ",
    description="Топ 5 лидеров по лвл и сообщениям.",
    guild_ids=[786301738155245578],
    options=[])
async def top2221(ctx):
    with open("levels.json", "r") as f:
      data = json.load(f)
    if str(ctx.guild.id) in data:
      if data[str(ctx.guild.id)]:
        data = data[str(ctx.guild.id)]
        data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['level'], reverse=True)}
        top = []
        for i in data:
          top.append(i)
        top = top[:5]
        top.reverse()
        top_5 = []
        for i in top:
          top_5.append(ctx.guild.get_member(int(i)))
        top_5.reverse()
        top_5 = top_5[:5]
        banner = Image.open("kniga.png")
        draw = ImageDraw.Draw(banner)
        font = ImageFont.truetype("minecraft.ttf", 20)
        # писать текст сколько всего участников на сервере
        draw.text((60, 150), f"Топ 5 участников по уровню", (0, 0, 0), font=font)
        #если у человека ник больше 5 символов то мы берём только 5 символов в его нике
        #если у человека ник меньше 5 символов то мы добавляем пробелы в конец его ника
        # если у человека нет ника то мы пропускаем его
        for i in range(5):
          if top_5[i] is None:
            continue
          if len(top_5[i].display_name) > 9:
            draw.text((60, 200+50*i), f"{i+1}. {top_5[i].display_name[:5]}", (0, 0, 0), font=font)
            draw.text((60+200, 200+50*i), f"{data[str(top_5[i].id)]['level']} уровень", (0,0,0), font=font)
          else:
            draw.text((60, 200+50*i), f"{i+1}. {top_5[i].display_name}", (0, 0, 0), font=font)
            draw.text((60+200, 200+50*i), f"{data[str(top_5[i].id)]['level']} уровень", (0,0,0), font=font)
        #брать из message.json брать сообщения участника и создать топ 5 участников по уровню вставлять текст в картинку pillow
        with open('message.json', 'r') as f:
            data = json.load(f)
            #сортировать список по count
            data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['count'], reverse=True)}
            #вывести топ 5
            top = list(data.items())[:5]
            # писать текст сколько всего участников на сервере
            draw.text((60, 450), f"Топ 5 по сообщениям", (0,0,0), font=font)
            #если у человека имя больше 9 символов то мы пишем только 5 символов
            #если у человека имя меньше 9 символов то мы добавляем пробелы в конец его имени
            # если у человека нет имени то мы пропускаем его
            for i in range(5):
              member = ctx.guild.get_member(int(top[i][0]))
              if member is None:
                continue
              if len(member.display_name) > 9:
                draw.text((60, 500+50*i), f"{i+1}. {member.display_name[:5]}", (0, 0, 0), font=font)
                draw.text((60+200, 500+50*i), f"{top[i][1]['count']} сообщений", (0,0,0), font=font)
              else:
                draw.text((60, 500+50*i), f"{i+1}. {member.display_name}", (0, 0, 0), font=font)
                draw.text((60+200, 500+50*i), f"{top[i][1]['count']} сообщений", (0,0,0), font=font)
            #сохранить картинку
            banner.save("top.png", "PNG")
            #отправить картинку
            await ctx.send(file=discord.File("top.png"))


@client.group(invoke_without_command=True)
async def help(ctx):
    if ctx.channel.id != 1024734194817044611:
        embed = discord.Embed(
            title="Ошибка :angry:",
            description=
            f"Мой создатель запретил тут использовать эту команду :(",
            color=0xFF0080)
        embed.set_footer(text=f'{ctx.message.author}',
                         icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
    else:
        embed = discord.Embed(
            title=
            "Так же можно использовать slash команды, напишите / и у вас появиться список всех команд ",
            color=0xff00ff)
        embed.set_author(name="Основные команды:")
        embed.add_field(name="😄 Fun ",
                        value="""`m.top - топ 5 лидеров` 
`m.profile - посмотреть свой профиль`
**Остальные функции можно найти в канале <#1025120273458012220>**
""",
                        inline=False)
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=512"
        )
        embed.set_footer(
            text="World Of Colanization © 2022",
            icon_url=
            "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
        )
        await ctx.send(embed=embed)
        await ctx.message.delete()



@client.event
async def on_select_option(interaction):
    await interaction.respond(type=6)
    if interaction.values[0] == "option1":
        e1 = discord.Embed(title=" Economy команды",
                           color=0xFF0080,
                           description="""
   
      ```             m.rank``` Посмотреть свою или чужую стастистику.
      ```             m.top``` Посмотреть лидеров по уровню.

    """)
        await interaction.send(embed=e1)
    elif interaction.values[0] == "option2":
        e3 = discord.Embed(title="Fun команды",
                           color=0xFF0080,
                           description="""
      ```       аватар``` Показать аватарку человека. @ или /
      ```       8ball``` Шар судьбы, (m.8ball вопрос)
      ```       m.юзер``` Посмотреть информацию о человеке. (m.юзер @)
      ```       m.top2``` Посмотреть информацию топ по печенькам.
      ```       Печеньки``` Вы можете выдать печеньки человеку поставив реакцию 🍪на особщение пользователя . (Посмотреть сколько у вас печенек m.инфа)
    """)
        await interaction.send(embed=e3)
    elif interaction.values[0] == "option4":
        embed = discord.Embed(
            title=
            "Вы можете получить подробную справочную информацию для каждой команды, нажав на селектор и выбрав нужную категорию.",
            color=0xff00ff)
        embed.set_author(name="Основные команды:")
        embed.add_field(name="🪙 Economy ",
                        value="`m.rank`  `m.top`  ",
                        inline=False)
        embed.add_field(name="😄  Fun ",
                        value="`m.avatar` `m.юзер` `m.8ball` `Печеньки (читать в селекторе)`",
                        inline=False)
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=512"
        )
        embed.set_footer(
            text="World Of Colanization © 2022",
            icon_url=
            "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
        )
        await interaction.send(embed=embed)


@client.command(name="avatar")
async def avatar(ctx, *, member: discord.Member = None):
    if ctx.channel.id != 986013528047624253:
        embed = discord.Embed(
            title="Ошибка :angry:",
            description=
            f"Мой создатель запретил тут использовать эту команду :(",
            color=0xFF0080)
        embed.set_footer(text=f'{ctx.message.author}',
                         icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
    else:
        if member == None:
            embed = discord.Embed(
                description=f'**Запросил: {ctx.author.name}**',
                icon_url=ctx.author.avatar_url,
                color=0xFF0080)
            embed.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return
        userAvatarUrl = member.avatar_url
        await ctx.message.delete()
        embed = discord.Embed(description=f'**Запросил: {ctx.author.name}**',
                              icon_url=ctx.author.avatar_url,
                              color=0xFF0080)
        embed.add_field(name=" Аватар:", value=member.mention, inline=False)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)




@client.command(aliases = ['userinfo', 'uinfo', 'юзер', 'инфо'])
async def user(ctx,member:discord.Member = None):

    with open('rep3.json', 'r') as f:
        rep = json.load(f)

    with open("levels.json", "r") as f:
        data = json.load(f)
    if str(ctx.guild.id) in data:
        if str(ctx.author.id) in data[str(ctx.guild.id)]:
            xp = data[str(ctx.guild.id)][str(ctx.author.id)]['xp']
            lvl = data[str(ctx.guild.id)][str(ctx.author.id)]['level']

  
    if member==None:
        member=ctx.author

    rlist = []
    for role in member.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)




    datetime.datetime(2013, 10, 4, 23, 27, 14, 678151)
    py_dt = member.joined_at
    epoch = round(py_dt.timestamp())

    py_dt1 = member.created_at
    epoch1 = round(py_dt1.timestamp())
  
    b = ", ".join(rlist)
    date_format = "%a, %b %d, %Y @ %I:%M %p" 
    if member == None:
        member = ctx.author
    if member.nick == None:
        nick = member.name
    else:
        nick = member.nick
    emb = discord.Embed(title = f'**Информация о {member.name}**',description = f'''
Никнейм на сервере: {nick}
Айди: {member.id}

**Аватар:** [[клик]({member.avatar_url})]
**Тег:** {member.discriminator}
**Всего ролей:** {len(rlist)}
{''.join([b])}
**Гл.Роль:** {member.top_role.mention}

**Печеньки🍪:**  {rep[str(member.id)]}
**Уровень** {lvl}
    
**Дата создания аккаунта:** <t:{epoch1}:D> <t:{epoch1}:R>
**Дата входа на сервер:** <t:{epoch}:D> <t:{epoch}:R>
                        ''',color=0xFF0080 )
    emb.set_footer(text=f'Запросил - {ctx.author}',
  icon_url=ctx.author.avatar_url,)
    emb.timestamp = datetime.datetime.utcnow()
    emb.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed = emb,delete_after=120.0)
    await ctx.message.delete()
    

@slash.slash(name="инфа",
             description="Информация о пользователе",
             options=[
               create_option(
                 name="member",
                 description="Да, инфа и что",
                 option_type=6,  #check out the docs (link is provided in readme.md file) to know more about different types of options
                 required=True
               )
             ])
async def user(ctx,member:discord.Member = None):

    with open('rep3.json', 'r') as f:
        rep = json.load(f)

    with open("levels.json", "r") as f:
        data = json.load(f)
    if str(ctx.guild.id) in data:
        if str(ctx.author.id) in data[str(ctx.guild.id)]:
            xp = data[str(ctx.guild.id)][str(ctx.author.id)]['xp']
            lvl = data[str(ctx.guild.id)][str(ctx.author.id)]['level']
  
    if member==None:
        member=ctx.author

    rlist = []
    for role in member.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)





    datetime.datetime(2013, 10, 4, 23, 27, 14, 678151)
    py_dt = member.joined_at
    epoch = round(py_dt.timestamp())

    py_dt1 = member.created_at
    epoch1 = round(py_dt1.timestamp())
  
    b = ", ".join(rlist)
    date_format = "%a, %b %d, %Y @ %I:%M %p" 
    if member == None:
        member = ctx.author
    if member.nick == None:
        nick = member.name
    else:
        nick = member.nick
    emb = discord.Embed(title = f'**Информация о {member.name}**',description = f'''
Никнейм на сервере: {nick}
Айди: {member.id}

**Аватар:** [[клик]({member.avatar_url})]
**Тег:** {member.discriminator}
**Всего ролей:** {len(rlist)}
{''.join([b])}
**Гл.Роль:** {member.top_role.mention}

**Печеньки🍪:**  {rep[str(member.id)]}
**Уровень** {lvl}
                        
**Дата создания аккаунта:** <t:{epoch1}:D> <t:{epoch1}:R>
**Дата входа на сервер:** <t:{epoch}:D> <t:{epoch}:R>
                        ''',color=0xFF0080 )
    emb.set_footer(text=f'Запросил - {ctx.author}',
  icon_url=ctx.author.avatar_url,)
    emb.timestamp = datetime.datetime.utcnow()
    emb.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed = emb,delete_after=120.0)

@commands.has_permissions(administrator=True)
@client.command()
async def rep_all(ctx):
    with open('rep.json', 'r') as f:
        prefixes = json.load(f)

    for member in ctx.guild.members:
        if not str(member.id) in prefixes:
            prefixes[str(member.id)] = 0
            with open('rep.json', "w") as f:
                json.dump(prefixes, f, indent=4)
        else:
            prefixes[str(member.id)] += 0
            with open('rep.json', "w") as f:
                json.dump(prefixes, f, indent=4)

    with open('rep.json', 'w') as f:
        json.dump(prefixes,f)

    embed = discord.Embed(title="Репутация", description = f'Все пользователи занесены в бд!', timestamp = ctx.message.created_at)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command(pass_context=True)
async def gorot(ctx, member: discord.Member, nick):
    await member.edit(nick=f"{member.name} ({nick})")
    embed = discord.Embed(description="""
 
**Ваш город готов, и вот короткий список начальных команд:**
**Имейте ввиду, каждые 24 часа со счета вашего города будет списываться 10 реалов. **
/t - Информация о городе.
/towny map - Карта чанков для привата.
/town add/kick <Ник> - Добавить/кикнуть игрока.
/town claim - Захватить чанк в котором стоишь.
/plot unclaim - уменьшить территорию Вашего участка.
/towny - Подсказки с командами.
/t deposit/withdraw <Сумма> - положить/снять в/с города.
/t invite - пригласить участника в город.
деньги со счета города.
/town set taxes [количество] - установить налог, который будет ежедневно собираться с жителей.
/plot toggle mobs  [on/off] - включить / отключить враждебных мобов на участке.
/t rank add [Ник] assistant. - добавить ассистента.
/tr survey — захватить ресурс (ресурс должен находится на территории города, а игрок, прописывающий команду, на чанке с ресурсом)
/tr towncollect — собрать ресурс (ресурс можно собирать раз в 24 часа КАЖДОМУ горожанину, находясь при этом на территории города)
/tr nationcollect — собрать ресурс нации (для участников нации)
/tr survey — улучшить ресурс до следующего уровня (находясь на чанке с ресурсом, при захвате ресурса ему присваивается 1 уровень)
 
 """,
                          color=0xFF0080)
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    role = discord.utils.get(member.guild.roles, name='Правитель')
    await member.add_roles(role)
    await ctx.message.delete()



@client.command()
async def embed(ctx, link, *, arg):
    if "https://" in link:
        embed = discord.Embed(description=f"""{arg}""", color=0xff00ff)
        embed.set_image(url=f"{link}")
        embed.set_footer(
            text="С уважением, администрация World of Colonization",
            icon_url=
            "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
        )
        await ctx.send(embed=embed)
        await ctx.message.delete()
    else:
        embed = discord.Embed(description=f"""{arg}""", color=0xff00ff)
        embed.set_footer(
            text="С уважением, администрация World of Colonization",
            icon_url=
            "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
        )
        await ctx.send(embed=embed)
        await ctx.message.delete()



@client.command()
async def role(ctx):
    await ctx.send("""||@everyone||
https://www.youtube.com/watch?v=U3bIpK_JcOk&ab_channel=Larkin
    """)
    await ctx.message.delete()

@client.command()
async def top2(ctx):
    if ctx.channel.id != 986013528047624253:
        embed = discord.Embed(
            title="Ошибка :angry:",
            description=
            f"Мой создатель запретил тут использовать эту команду :(",
            color=0xFF0080)
        embed.set_footer(text=f'{ctx.message.author}',
                         icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
        return
    with open('rep3.json', 'r') as f:
        rep3 = json.load(f)
    rep3 = sorted(rep3.items(), key=lambda x: x[1], reverse=True)
    embed = discord.Embed(title="Топ по печенькам🍪", color=0xFF0080)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    for i in range(5):
        member = client.get_user(int(rep3[i][0]))
        embed.add_field(name=f'{i+1} место', value=f'{member.mention} - {rep3[i][1]}', inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()

guild_ids = [786301738155245578]

@slash.slash(
    name="gorot",
    description="Аватар пользователя.",
    guild_ids=guild_ids,
    options=[
        create_option(
            name="member",
            description="Да, пользователь",
            option_type=
            6,  #check out the docs (link is provided in readme.md file) to know more about different types of options
            required=True),
        create_option(
            name="nick",
            description="Да, ник",
            option_type=
            3,  #check out the docs (link is provided in readme.md file) to know more about different types of options
            required=False),

    ])
async def gorot22(ctx, *, member: discord.Member = None, nick):
    await member.edit(nick=f"{member.name} ({nick})")
    embed = discord.Embed(description="""
 
**Ваш город готов, и вот короткий список начальных команд:**
**Имейте ввиду, каждые 24 часа со счета вашего города будет списываться 10 реалов. **
/t - Информация о городе.
/towny map - Карта чанков для привата.
/town add/kick <Ник> - Добавить/кикнуть игрока.
/town claim - Захватить чанк в котором стоишь.
/plot unclaim - уменьшить территорию Вашего участка.
/towny - Подсказки с командами.
/t deposit/withdraw <Сумма> - положить/снять в/с города.
/t invite - пригласить участника в город.
деньги со счета города.
/town set taxes [количество] - установить налог, который будет ежедневно собираться с жителей.
/plot toggle mobs  [on/off] - включить / отключить враждебных мобов на участке.
/t rank add [Ник] assistant. - добавить ассистента.
/t toggle pvp off - Отключить ПВП.
/tr survey — захватить ресурс (ресурс должен находится на территории города, а игрок, прописывающий команду, на чанке с ресурсом)
/tr towncollect — собрать ресурс (ресурс можно собирать раз в 24 часа КАЖДОМУ горожанину, находясь при этом на территории города)
/tr nationcollect — собрать ресурс нации (для участников нации)
/tr survey — улучшить ресурс до следующего уровня (находясь на чанке с ресурсом, при захвате ресурса ему присваивается 1 уровень)
 
 """,
                          color=0xFF0080)
    embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
    await ctx.send(embed=embed)
    role = discord.utils.get(member.guild.roles, name='Правитель')
    await member.add_roles(role)

@slash.slash(name="top2",
                description="Таблица лидеров по печенькам.🍪",
                options=[
                ])
async def rep33(ctx):
    with open('rep3.json', 'r') as f:
        rep = json.load(f)
    embed = discord.Embed(title="Топ по печенькам🍪", description="Топ по печенькам🍪", color=0xFF0080)
    embed.timestamp = datetime.datetime.utcnow()
    for key, value in sorted(rep.items(), key=lambda item: item[1], reverse=True):
        member = client.get_user(int(key))
        embed.add_field(name=f"", value=f"{value}", inline=False)
    await ctx.send(embed=embed)

@commands.cooldown(1, 60, commands.BucketType.user)
@client.command()
async def rep(ctx, member: discord.Member):
    if ctx.channel.id != 961668931934879794:
        embed = discord.Embed(
            title="Ошибка :angry:",
            description=
            f"Мой создатель запретил тут использовать эту команду :(",
            color=0xFF0080)
        embed.set_footer(text=f'{ctx.message.author}',
                         icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
        return
    with open('rep.json', 'r') as f:
        rep = json.load(f)
#нельзя выдавать себе репутацию
    if member.id == ctx.author.id:
        await ctx.send("Ты не можешь выдать себе печеньки🍪")
        return
    if str(ctx.author.id) in rep:
        embed = discord.Embed(title="Ошибка :angry:", description=f" Вы уже выдавали этому пользователю печеньку🍪!", color=0xFF0080)
        embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed, delete_after=5.0)
        await ctx.message.delete()
    else:
        rep[str(ctx.author.id)] = str(member.id)
        with open('rep.json', 'w') as f:
            json.dump(rep, f)
        embed = discord.Embed(title="Успех :white_check_mark:", description=f" Вы  {member.mention} выдали печенюку🍪", color=0xFF0080)
        embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed,delete_after=5.0)
        await ctx.message.delete()
        with open('rep3.json', "r") as f:
            prefixes = json.load(f)

        if not str(member.id) in prefixes:
             prefixes[str(member.id)] = 1
             with open('rep3.json', "w") as f:
                json.dump(prefixes, f, indent=4)
        else:
             prefixes[str(member.id)] += 1
             with open('rep3.json', "w") as f:
                 json.dump(prefixes, f, indent=4)

        with open('rep3.json', 'w') as f:
             json.dump(prefixes,f)

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🍪":
        if user.id == client.user.id:
            return
  #выдавать репутацию человеку на чьё сообщение было поставлена реакция
        with open('rep.json', 'r') as f:
            rep = json.load(f)
        if str(user.id) in rep:
            embed = discord.Embed(title="Ошибка :angry:", description=f" Вы уже выдавали этому пользователю печеньку🍪!", color=0xFF0080)
            embed.set_footer(text=f'{user}', icon_url=f'{user.avatar_url}')
            await reaction.message.channel.send(embed=embed,delete_after=5.0)
            await reaction.remove(user)
            return
        else:
            rep[str(user.id)] = str(reaction.message.author.id)
            with open('rep.json', 'w') as f:
                json.dump(rep, f)
            embed = discord.Embed(title="Успех :white_check_mark:", description=f" Вы выдали печенюку🍪 {reaction.message.author.mention}", delete_after=5.0,color=0xFF0080)
            embed.set_footer(text=f'{user}', icon_url=f'{user.avatar_url}')
            await reaction.message.channel.send(embed=embed,delete_after=5.0)
            with open('rep3.json', "r") as f:
                prefixes = json.load(f)

            if not str(reaction.message.author.id) in prefixes:
                    prefixes[str(reaction.message.author.id)] = 1
                    with open('rep3.json', "w") as f:
                        json.dump(prefixes, f, indent=4)
            else:
                    prefixes[str(reaction.message.author.id)] += 1
                    with open('rep3.json', "w") as f:
                        json.dump(prefixes, f, indent=4)

@client.event
async def on_message_delete(message):
    if message.author.bot:
        return
    if message.content.startswith('m.'):
        return
    if not message.attachments:
        log = client.get_channel(989147411236655134)
        #если участник удалил сообщение другого участника писать об этом
        e = discord.Embed(title=f'{message.author.display_name} удалил сообщение', timestamp = message.created_at, color=0xff0000)
        e.add_field(name='Сообщение:', value=f'{message.content}', inline=False)
        e.add_field(name='Канал:', value=f'{message.channel.mention}', inline=False)
        e.add_field(name='Участник:', value=f'{message.author.mention}', inline=False)
        e.set_thumbnail(url=message.author.avatar_url)
        return await log.send(embed=e)

    files = []
    for file in message.attachments:
        fp = io.BytesIO()
        await file.save(fp = f'log.jpg')

    log = client.get_channel(989147411236655134)
    e = discord.Embed(title=f'{message.author.display_name} удалил сообщение:',color=0xff0000)
    e.add_field(name='Канал:', value=f'{message.channel.mention}', inline=False)
    e.add_field(name='Участник:', value=f'{message.author.mention}', inline=False)
    e.set_thumbnail(url=message.author.avatar_url)
    file = discord.File(f"log.jpg",filename=f"log.jpg")
    e.set_image(url=f"attachment://log.jpg")
    await log.send(file=file,embed=e)

@client.event
async def on_message_edit(before, after):
    z = client.get_channel(989147411236655134)
    if before.author.bot:
        return
    guild = before.guild
    embed = discord.Embed(title = f"{before.author} Отредактировал свое сообщение", description = f"До: **{before.content}**\nПосле: **{after.content}**\nАвтор: {before.author.mention}\nКанал: {before.channel.mention}", color = discord.Colour.blue())
    embed.timestamp = datetime.datetime.utcnow()
    await z.send(embed = embed)

@client.event
async def on_member_update(before, after):
    z = client.get_channel(989147411236655134)
    if len(before.roles) > len(after.roles):
        role = next(role for role in before.roles if role not in after.roles)
        embed = discord.Embed(title = f"{before} Роль была удалена", description = f"роль {role.name} удалена у  {before.mention}.", color = discord.Colour.red())
        
    elif len(after.roles) > len(before.roles):
        role = next(role for role in after.roles if role not in before.roles)
        embed = discord.Embed(title = f"{before} Получил новую роль", description = f"Роль {role.name} добавлена у  {before.mention}.", color = discord.Colour.green())
        
    elif before.nick != after.nick:
        embed = discord.Embed(title = f"{before} Ник изменен", description = f"До: **{before.nick}**\nПосле: **{after.nick}**", color = discord.Colour.blue())
    else:
        return
    async for event in before.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update):
     embed.set_thumbnail(url=before.avatar_url)
     embed.timestamp = datetime.datetime.utcnow()
     await z.send(embed = embed)

@client.event
async def on_member_join(member):
        with open("words.json", "r") as f:
            words = json.load(f)
        banner = Image.open("banner.jpeg")
        draw = ImageDraw.Draw(banner)
        font = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 70)
        font2 = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 50)
        # писать текст сколько всего участников на сервере
        draw.text((130, 300), f"{len(words)}", (255, 255, 255), font=font)
        draw.text((130, 400), f"{len(member.guild.members)}",  (255, 255, 255), font=font)
        draw.text((670, 420), f"{status.players.online}/100",  (255, 255, 255), font=font2)
        banner.save("banner2.jpg")
        with open("banner2.jpg", 'rb') as pfp:
            await member.guild.edit(banner=pfp.read())
        channel = client.get_channel(1025788640330268803)
        embed = discord.Embed(title = f"{member} Зашёл на сервер", description = f"Всего участников на сервере: {len(member.guild.members)}", color=0x80ff00)
        embed.set_thumbnail(url = member.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed = embed)





@client.event
async def on_member_remove(member):
        with open("words.json", "r") as f:
            words = json.load(f)
        banner = Image.open("banner.jpeg")
        draw = ImageDraw.Draw(banner)
        font = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 70)
        font2 = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 50)
        # писать текст сколько всего участников на сервере
        draw.text((130, 300), f"{len(words)}", (255, 255, 255), font=font)
        draw.text((130, 400), f"{len(member.guild.members)}",  (255, 255, 255), font=font)
        draw.text((670, 420), f"{status.players.online}/100",  (255, 255, 255), font=font2)
        banner.save("banner2.jpg")
        with open("banner2.jpg", 'rb') as pfp:
            await member.guild.edit(banner=pfp.read())
        channel = client.get_channel(1025788640330268803)
        embed = discord.Embed(title = f"{member} Покинул сервер", description = f"Всего участников на сервере: {len(member.guild.members)}", color = discord.Colour.red())
        embed.set_thumbnail(url = member.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed = embed)

@client.event
async def on_ready():
    while True:
        for guild in client.guilds:
            server = JavaServer.lookup("65.109.22.206:3502")
            status = server.status()
            with open('online.json', 'r') as f:
                data2 = json.load(f)
                data2["online"] = status.players.online
            with open('online.json', 'w') as f:
                json.dump(data2, f)
            with open("online.json", "r") as f:
                online = json.load(f)
            if online["online"] == status.players.online:
                pass
            else:
              with open("words.json", "r") as f:
                  words = json.load(f)
              server = JavaServer.lookup("65.109.22.206:3502")
              status = server.status()
              banner = Image.open("banner.jpeg")
              draw = ImageDraw.Draw(banner)
              font = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 70)
              font2 = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 50)
              # писать текст сколько всего участников на сервере
              draw.text((130, 300), f"{len(words)}", (255, 255, 255), font=font)
              #получить список участников
              draw.text((130, 400), f"{len(guild.members)}",  (255, 255, 255), font=font)
              draw.text((670, 420), f"{status.players.online}/100",  (255, 255, 255), font=font2)
              #записывать в online.json status.players.online
              banner.save("banner2.jpg")
              with open("banner2.jpg", 'rb') as pfp:
                  await guild.edit(banner=pfp.read())
              await asyncio.sleep(15)
        for guild in client.guilds:
              with open("words.json", "r") as f:
                  words = json.load(f)
              server = JavaServer.lookup("65.109.22.206:3502")
              status = server.status()
              banner = Image.open("banner.jpeg")
              draw = ImageDraw.Draw(banner)
              font = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 70)
              font2 = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 50)
              # писать текст сколько всего участников на сервере
              draw.text((130, 300), f"{len(words)}", (255, 255, 255), font=font)
              #получить список участников
              draw.text((130, 400), f"{len(guild.members)}",  (255, 255, 255), font=font)
              draw.text((670, 420), f"{status.players.online}/100",  (255, 255, 255), font=font2)
              banner.save("banner2.jpg")
              with open("banner2.jpg", 'rb') as pfp:
                  await guild.edit(banner=pfp.read())
              await asyncio.sleep(15)



@client.command()
async def online(ctx):
  await ctx.send(f"{status.players.online}")

@client.command()
async def obnovit(ctx):

    with open("words.json", "r") as f:
        words = json.load(f)
    banner = Image.open("banner.jpeg")
    draw = ImageDraw.Draw(banner)
    font = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 70)
    font2 = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 50)
    # писать текст сколько всего участников на сервере
    draw.text((130, 300), f"{len(words)}", (255, 255, 255), font=font)
    draw.text((130, 400), f"{len(ctx.guild.members)}",  (255, 255, 255), font=font)
    draw.text((670, 420), f"{status.players.online}/100",  (255, 255, 255), font=font2)
    banner.save("banner2.jpg")
    with open("banner2.jpg", 'rb') as pfp:
        await ctx.guild.edit(banner=pfp.read())





@client.command()
async def dfafwawsfwqagagaw(ctx):
    embed = discord.Embed(description="""
Приветствуем в нашем составе администрации.
Расскажем основную информацию:
что требуется от вас, проверять тикеты в дискорде, помогать игрокам, **не страдать фигней, никому ничего не выдавать, себе тоже ничего не выдавать. и быть адекватным**
За любое нарушение от модератора = 1 warn
За грубое нарушение такое как выдача игрокам, что либо = по усмотрению старшей администрации

——————————————————————————————————————
При создании города не должно быть в названии больших букв, пробелов, цифр, также название городов должно быть адекватное, допустим DotaGrad, такое название мы отклоняем.
Примеры
Нельзя:
- MoScOw
- Mos12ow

Можно:

-Mosow
-Saint_Peterburg

——————————————————————————————————————
Команды, чтобы создать город:

/ta new Название города
/ta set mayor (город) (ник человека) - без скобок
——————————————————————————————————————

Когда отвечаем в тикете человеку, здороваемся, не привет, а здравствуйте.
Тикеты удалять через 6ч после ответа, если человек уже видел что вы ему отправили то можно сразу закрывать и удалять

——————————————————————————————————————

При создании города:
Проверяем в канале<#868520809105330266> командой m.поиск НазваниеГорода нет ли такого города, если есть пишем игроку чтобы он поменял название, если нету, то тепаемся на координаты которые указал игрок и пишем: /t new названиеГорода. Дальше /ta set mayour названиеГорода НикЧеловека.
Дальше нажимаем ответить на сообщение игрока, где находится название города и пишем в чат дс m.gorot2


Если есть вопросы их можно задать в канале <#868520809105330266>

——————————————————————————————————————

При проверках района:
Человек создаёт тикет, мы смотрим какой район нужно проверить, тепаемся на координаты которые указал игрок, смотрим район, в районе не должно быть коробок, постройка должна быть красивая и большая
Дальше в тикете если район принят пишем команду в дискорде m.одобрить КоличествоЧанков и нажимаем на кнопку ответить, если район не принят то в чат дискорд пишем почему.

——————————————————————————————————————
Все админские команды в дискорде можно посмотреть в канале: <#1013437440444350534>

Желаем удачи и терпения на посту модератора.
    """,color=0xFF0080)
    embed.set_footer(
                      text="Администрация World of Colonization",
                      icon_url=
                      "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
                  )
    await ctx.send(embed=embed)

@client.command()
async def rulesmoder(ctx):
    embed = discord.Embed(title="Правила модераторов",description="""
1. **Модератор обязан соблюдать речевые нормы, быть общительным, грамотным, воспитанным, вежливым и толерантным по отношению ко всем игрокам проекта.**

``Модератор не имеет права игнорировать игроков по их проблемам и обязан помогать им в пределах своих возможностей. Если по какой-то причине выполнить просьбу игрока не представляется возможным, то модератор должен написать игроку об этом.``

2. **Модератор обязан соблюдать все правила проекта.**

3. **Модератор не имеет права злоупотреблять или использовать свои полномочия во вред другим игрокам или серверу в целом, либо в пользу себя, друзей или третьих лиц.**

4. **Модератор не имеет права устраивать обмен, торговлю и снабжать игроков ресурсами, если они были изъяты у другого игрока или же были добыты с помощью возможностей, доступных только модератору.**

``В ходе обычного развития модератору разрешается обмениваться и торговать с обычными игроками, но только ресурсами, которые добыты во время игрового процесса.``

5. **Модератору запрещено разглашать посторонним лицам информацию, не предназначенную для игроков.**

``Любая информация о грядущих изменениях/нововведениях, содержание всевозможных конференций, групп и личных сообщений модераторов и Администрации.``

    """,color=0xFF0080)
    embed.set_footer(
                      text="Администрация World of Colonization",
                      icon_url=
                      "https://cdn.discordapp.com/avatars/1014579843310047373/ed32de15c1c0bbc4cca8fd1627581978.png"
                  )
    await ctx.send(embed=embed)

async def send_if(ctx, check, message):
    if check:
        await ctx.send(message)
        
async def is_connected(ctx, user_connected = True, send_assert = False):
    if user_connected and not ctx.author.voice:
        await send_if(ctx, send_assert, ':angry: Вы не в голосовом канале!')
        return False

    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        
        if user_connected and voice.channel != ctx.message.author.voice.channel:
            await send_if(ctx, send_assert, ':angry: Вы находитесь не на том же голосовом канале, что и бот!')
            return False
        
        return True

    await send_if(ctx, send_assert, ':confused: бот не находится на голосовом канале. Сначала используйте `!join`.')
    return False
# ------------------------------------- - ------------------------------------ #

# ------------------------------------- infoserver ------------------------------------ #



# ------------------------------------- - ------------------------------------ #


# ------------------------------------- аватар ------------------------------------ #



# ------------------------------------- - ------------------------------------ #


# ------------------------------------- инфа ------------------------------------ #

music_queues = {}
null_music_data = {'source' : None, 'title' : 'Null', 'requestor' : None}
currently_playing = {}

def play_next_in_queue(ctx, guild_id):
    queue = music_queues[guild_id]
    
    if queue != []:
        voice = ctx.guild.voice_client
        music_data = queue.pop(0)
        
        global currently_playing 
        currently_playing[guild_id] = music_data
        
        voice.play(music_data['source'], after=lambda x=0: play_next_in_queue(ctx, guild_id))
    else:
        currently_playing[guild_id] = null_music_data

# ------------------------------------- - ------------------------------------ #


# ---------------------------------- play, p --------------------------------- #
def fformat(dur):
    hours, rem = divmod(dur, 3600)
    minutes, seconds = divmod(rem, 60)
    return '{:0>2}h:{:0>2}m:{:02}s'.format(int(hours),int(minutes),seconds)
    
async def fplay(ctx, url):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await ctx.message.delete()
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
    else:
        await ctx.message.delete()
        await ctx.send(':angry: Вы не в голосовом канале!')
  
  
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True', 'default_search':'ytsearch'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)
  
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)

        o_url = url
        if 'entries' in info:
            url = info['entries'][0]['formats'][0]['url']
            duration = fformat(int(info['entries'][0]['duration']))
            short_url = info['entries'][0]['webpage_url']
        elif 'formats' in info:
            url = info['formats'][0]['url']
            duration = None
            short_url = None
            
    title = info.get('title') or info['entries'][0]['title']
    
    source = (FFmpegPCMAudio(url, **FFMPEG_OPTIONS))
    guild_id = ctx.message.guild.id
   
    music_data = {
        'source' : source,
        'title' : str(title),
        'requestor' : ctx.message.author
    }
   
    embed = discord.Embed(title=f':headphones: Опа,смотри что играет:',description=f'```css\n{str(title)}\n```',colour = discord.Colour.magenta(), url = (short_url and url) or o_url)
    if duration:
        embed.add_field(name='Время прослушивания :clock1:', value=str(duration))
    embed.add_field(name='Запросил:', value=ctx.author.mention, inline=True)
    embed.set_image(url=info.get('thumbnail') or info['entries'][0]['thumbnail'])

    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label = 'Включить repeat',
            emoji = "🔁",
            custom_id = 'repeat'
        ),
        Button(
            style = ButtonStyle.gray,
            label = 'Выключить repeat',
            emoji = "🔁",
            custom_id = 'repeat2'
        ),
        Button(
            style = ButtonStyle.gray,
            label = 'Пауза',
            emoji = "⏸",
            custom_id = 'pause'
        ),
        Button(
            style = ButtonStyle.gray,
            label = 'Снять с паузы',
            emoji = "▶",
            custom_id = 'pause2'
        ),
    )
    await ctx.send(embed = embed, components = [row])  
    
    if voice.is_playing():
        embed.title = 'В очереди: '
        if guild_id in music_queues:
            music_queues[guild_id].append(music_data)
        else:
            music_queues[guild_id] = [music_data]
    else:
        global currently_playing
        currently_playing[guild_id] = music_data
        voice.play(FFmpegPCMAudio(url, **FFMPEG_OPTIONS), after=lambda x=0: play_next_in_queue(ctx, ctx.message.guild.id))




    

@client.command(pass_context = True)
async def play2(ctx, *, url):
    await fplay(ctx, url)
@client.command(pass_context = True)
async def p(ctx, *, url):
    await fplay(ctx, url)
# ------------------------------------- - ------------------------------------ #

# -------------------------------- remove, rm -------------------------------- #
async def fremove(ctx, index=0):
    if await is_connected(ctx, user_connected=True, send_assert=True):
        if ctx.message.guild.id in music_queues:
            local_queue = music_queues[ctx.message.guild.id]
            index = int(index)
            index = (index == -1 and len(local_queue) - 1) or (index-1)            
            
            if index < 0 or index >= len(local_queue):
                await ctx.send(':warning: Индекс очереди вне допустимого диапазона. \n\nСначала используйте `+queue`, чтобы найти правильный индекс очереди. Индекс очереди -1 удалит из очереди последнюю добавленную песню.')
            else:
                music_data = local_queue[index]
                if music_data:
                    local_queue.pop(index)
                    await ctx.send('Удаленно: ' + music_data['title'] + ' из очереди!')    

@client.command(pass_context = True)
async def remove(ctx, index):
    await fremove(ctx, index)
@client.command(pass_context = True)
async def rm(ctx, index):
    await fremove(ctx, index)
# ------------------------------------- - ------------------------------------ #

# --------------------------------- pause, ps -------------------------------- #
async def fpause(ctx):
    if await is_connected(ctx, user_connected=True, send_assert=True):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.send(':pause_button: Приостановлено: ' + currently_playing[ctx.message.guild.id]['title'])
        else:
            await ctx.send(':confused: Не понимаю, что ты хочешь остановить?') 
            
@client.command(pass_context = True)
async def pause2(ctx):
    await ctx.message.delete()
    await fpause(ctx)
@client.command(pass_context = True)
async def ps(ctx):
    await fpause(ctx)
    await ctx.message.delete()
# ------------------------------------- - ------------------------------------ #

# --------------------------------- resume, r -------------------------------- #
async def fresume(ctx):
    if await is_connected(ctx, user_connected=True, send_assert=True):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            await ctx.send(':play_pause: Возобновлено: ' + currently_playing[ctx.message.guild.id]['title'])
        else:
            await ctx.send(':confused: Звук не поставлен на паузу..?')

@client.command(pass_context = True)
async def resume(ctx):
    await fresume(ctx)
    await ctx.message.delete()
@client.command(pass_context = True)
async def rs(ctx):
    await fresume(ctx)
    await ctx.message.delete()
# ------------------------------------- - ------------------------------------ #
@client.command()
async def repeat(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():

            await voice.move_to(channel)
        else:
            voice = await channel.connect()
    else:

        await ctx.send(':angry: Вы не в голосовом канале!')
  
    guild_id = ctx.message.guild.id
    if guild_id in music_queues and music_queues[guild_id] != []:
        queue = music_queues[guild_id]
        music_data = queue.pop(0)
        queue.insert(0, music_data)
        await ctx.send(f':repeat: повторяю {music_data["title"]}')
    elif guild_id in currently_playing and currently_playing[guild_id] != null_music_data:
        music_data = currently_playing[guild_id]
        if guild_id in music_queues:
            music_queues[guild_id].insert(0, music_data)
        else:
            music_queues[guild_id] = [music_data]
        await ctx.send(f':repeat: повторяю {music_data["title"]}')
    else:
        await ctx.send(':confused: ничего не играет')

@client.command()
async def repeatoff(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():

            await voice.move_to(channel)
        else:
            voice = await channel.connect()
    else:

        await ctx.send(':angry: Вы не в голосовом канале!')
  
    guild_id = ctx.message.guild.id
    if guild_id in music_queues and music_queues[guild_id] != []:
        queue = music_queues[guild_id]
        music_data = queue.pop(0)
        await ctx.send(f':repeat: Повтор выключен')
    elif guild_id in currently_playing and currently_playing[guild_id] != null_music_data:
        music_data = currently_playing[guild_id]
        if guild_id in music_queues:
            music_queues[guild_id].insert(0, music_data)
        else:
            music_queues[guild_id] = [music_data]
        await ctx.send(f':repeat: Повтор выключен ')
    else:
        await ctx.send(':confused: ничего не играет')

@client.command()
async def osenka(ctx):
    #сделать оценку вайпа с кнопкой
    embed = discord.Embed(title="""
    Третий сезон подходит к концу""", description="Администрация World Of Colonization вводит систему оценки сезонов, теперь, в конце каждого вайпа игроки будут оценивать сезон по пятибальной шкале", color=0xeee657)
    embed.add_field(name="Пожалуйста, оцените третий сезон", value="1 - очень плохо, 2 - плохо, 3 - нормально, 4 - хорошо, 5 - отлично", inline=False)
    embed.set_footer(text="С уважением, администрация World of Colonization",icon_url="https://cdn.discordapp.com/avatars/1014579843310047373/ed32de15c1c0bbc4cca8fd1627581978.png?size=4096")
    embed.set_image(
        url=
        'https://media.discordapp.net/attachments/1017393296273838150/1022856394099134584/unknown-.jpg'
    )
    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label= "⭐",
            custom_id = 'bal1'
        ),
        Button(
            style = ButtonStyle.gray,
            label=  "⭐⭐",
            custom_id = 'bal2'
        ),
        Button(
            style = ButtonStyle.gray,
            label=  "⭐⭐⭐",
            custom_id = 'bal3'
        ),
        Button(
            style = ButtonStyle.gray,
            label="⭐⭐⭐⭐",
            custom_id = 'bal4'
        ),
        Button(
            style = ButtonStyle.gray,
            label="⭐⭐⭐⭐⭐",
            custom_id = 'bal5'
        ),
    )
    await ctx.send(embed = embed, components = [row])
    await ctx.message.delete()

@client.command()
async def set(ctx):
    if ctx.channel.id != 1025120273458012220:
        embed = discord.Embed(
            title="Ошибка :angry:",
            description=
            f"Мой создатель запретил тут использовать эту команду :(",
            color=0xFF0080)
        embed.set_footer(text=f'{ctx.message.author}',
                         icon_url=f'{ctx.message.author.avatar_url}')
        await ctx.send(embed=embed, delete_after=10.0)
        await ctx.message.delete()
    else:
      embed = discord.Embed(title="""
      Выберете свой сет на скин""", description="Нажмите на нужную вам кнопку и сет поставиться", color=0xeee657)
      embed.set_footer(text="С уважением, администрация World of Colonization",icon_url="https://cdn.discordapp.com/avatars/1014579843310047373/ed32de15c1c0bbc4cca8fd1627581978.png?size=4096")
      embed.set_image(
          url=
          'https://media.discordapp.net/attachments/868520809105330266/1025008837046042654/unknown.png?width=710&height=671'
      )
      row = ActionRow(
          Button(
              style = ButtonStyle.gray,
              label= "Кожаный сет",
              custom_id = 'kosh'
          ),
          Button(
              style = ButtonStyle.gray,
              label=  "Железный сет",
              custom_id = 'shelesh'
          ),
          Button(
              style = ButtonStyle.gray,
              label=  "Золотой сет",
              custom_id = 'zolotoi'
          ),
          Button(
              style = ButtonStyle.gray,
              label="Алмазный сет",
              custom_id = 'almaz'
          ),
          Button(
              style = ButtonStyle.gray,
              label="Убрать сет",
              custom_id = 'ybrat'
          ),
      )
      await ctx.send(embed = embed, components = [row])
      await ctx.message.delete()

@client.command()
async def glass(ctx):
    emb = discord.Embed(title="Нажмите на нужную вам кнопку, чтобы поставить цвет глаз",color=0xFF0080)
    emb.set_footer(text="С уважением, администрация World of Colonization",icon_url="https://cdn.discordapp.com/avatars/955189437275467798/9949d32ffa9b2776d8788a422f6a184d.png?size=4096")
    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label = 'Белые глаза',
            custom_id = 'belie',
        ),
        Button(
            style = ButtonStyle.gray,
            label = 'Чёрные глаза',
            custom_id = 'black'
        ),
        Button(
            style = ButtonStyle.gray,
            label = 'Зелёные глаза',
            custom_id = 'green'
        ),
        Button(
            style = ButtonStyle.gray,
            label = 'Розовые глаза',
            custom_id = 'pink'
        ),
        Button(
            style = ButtonStyle.gray,
            label = 'Сбросить цвет глаз',
            custom_id = 'reset'
        ),
    )
    await ctx.send(embed = emb, components = [row])
    await ctx.message.delete()

@client.command()
async def shlaba(ctx):
      embed = discord.Embed(title="""
      Выберете свою шляпу""", description="Нажмите на нужную вам кнопку и  поставиться", color=0xeee657)
      embed.set_footer(text="С уважением, администрация World of Colonization",icon_url="https://cdn.discordapp.com/avatars/1014579843310047373/ed32de15c1c0bbc4cca8fd1627581978.png?size=4096")
      embed.set_image(
          url=
          'https://media.discordapp.net/attachments/961668931934879794/1025487394348220538/unknown.png?width=710&height=671'
      )
      row = ActionRow(
          Button(
              style = ButtonStyle.gray,
              label= "Надеть шляпу фермера",
              custom_id = 'fermer'
          ),
          Button(
              style = ButtonStyle.gray,
              label= "Надеть шляпу ведьмы",
              custom_id = 'vedma'
          ),
          Button(
              style = ButtonStyle.gray,
              label= "Надеть корону",
              custom_id = 'korona'
          ),
          Button(
              style = ButtonStyle.gray,
              label= "Снять шляпу",
              custom_id = 'snat'
          )
      )
      await ctx.send(embed = embed, components = [row])
      await ctx.message.delete()

@client.event
async def on_button_click(inter):


    

    guild = client.get_guild(inter.guild.id)
    if inter.component.id == "snat":
      #в skin.json брать id человека и ставить значение profile.jpg
      with open("skin.json", "r") as f:
        data = json.load(f)
      data[str(inter.user.id)] = {}
      data[str(inter.author.id)]["skin"] = "profile.jpg"
      with open("skin.json", "w") as f:
        json.dump(data, f)
      await inter.respond(content="Вы успешно сняли шляпу")  
    if inter.component.id == "fermer":
      with open('buy.json', 'r') as f:
        buy = json.load(f)
      #проверять если человек в buy.json если нету добавляем
      if str(inter.author.id) not in buy:
        buy[str(inter.author.id)] = {}
        buy[str(inter.author.id)]["hat"] = 0
        buy[str(inter.author.id)]["hat2"] = 0
        buy[str(inter.author.id)]["hat3"] = 0
        with open('buy.json', 'w') as f:
          json.dump(buy, f)
      if buy[str(inter.author.id)]["hat"] == 0:
      #вы уверены что хотите купить шляпу
        row = ActionRow(
            Button(
                style = ButtonStyle.green,
                label= "Подтвердить",
                custom_id = 'fermer2'
            ),
            Button(
                style = ButtonStyle.red,
                label= "Отмена",
                custom_id = 'no'
            ),
        )
        emb = discord.Embed(title="Вы уверены что хотите купить шляпу фермера",color=0xFF0080)
        emb.add_field(name='Стоимость шляпы:', value='150 сообщений', inline = False)
        emb.set_footer(text="С уважением, администрация World of Colonization",icon_url="https://cdn.discordapp.com/avatars/955189437275467798/9949d32ffa9b2776d8788a422f6a184d.png?size=4096")
        channel = client.get_channel(1025120273458012220)
        await channel.send(embed = emb, components = [row], delete_after=10.0)
        await inter.respond(content="Подтвердите покупку")
      else:
        #в skin.json брать id человека и если он уже покупал шляпу то пишем что шляпа есть
        with open("buy.json", "r") as f:
          buy2 = json.load(f)
        #брать из значение hat слово и писать его
        if buy2[str(inter.author.id)]["hat"] == "fermer":
          with open('skin.json', 'r') as f:
            users2 = json.load(f)
          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoshshlaba.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profile.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilefermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profileshele.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profileshelezofermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profilezoloto.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilezolotofermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profilealmaz.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilealmazfermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          else:
            await inter.respond(content="У вас уже надета эта шляпа или у вас уже стоит другая")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)
        if buy2[str(inter.author.id)]["hat2"] == "vedma":
          with open('skin.json', 'r') as f:
            users2 = json.load(f)
          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilevedmakosh.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)

          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoshshlaba.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profile.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilefermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profileshele.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profileshelezofermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profilezoloto.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilezolotofermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profilealmaz.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilealmazfermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          else:
            await inter.respond(content="У вас уже надета эта шляпа или у вас уже стоит другая")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)
              

        with open('skin.json', 'w') as f:
            json.dump(users2, f)




    if inter.component.id == "no":
      channel = client.get_channel(1025120273458012220)
      await channel.purge(limit=1)
      await inter.respond(content = "Хорошо, покупка отмененна")
    if inter.component.id == "fermer2":
      with open('skin.json', 'r') as f:
        users2 = json.load(f)
      if users2[str(inter.author.id)]['skin'] != 'profile.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      else:
        with open('skin.json', 'r') as f:
          users2 = json.load(f)
      with open('message.json', 'r') as f:
        users = json.load(f)
#если участника нету в message.json то мы записываем его id и выдаём 0 сообщений
      if not str(inter.author.id) in users:
        users[str(inter.author.id)] = {}
        users[str(inter.author.id)]['count'] = 0
      if users[str(inter.author.id)]['count'] < 149:
        await inter.respond(content="Недостаточно сообщение, нужное количество - 150 сообщений")
        channel = client.get_channel(1025120273458012220)
        await channel.purge(limit=1)
      if users[str(inter.author.id)]['count'] > 149:
        users[str(inter.author.id)]['count'] -= 150
        with open('message.json', 'w') as f:
          json.dump(users, f)

          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoshshlaba.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)

          if users2[str(inter.author.id)]['skin'] == 'profile.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilefermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profileshele.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profileshelezofermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profilezoloto.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilezolotofermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
          if users2[str(inter.author.id)]['skin'] == 'profilealmaz.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilealmazfermer.jpg'
            await inter.respond(content="Вы успешно надели шляпу фермера")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)

#записывать в buy.json какую шляпу купил участник
        with open("buy.json", "r") as f:
          buy2 = json.load(f)
        buy2[str(inter.author.id)]["hat"] = "fermer"
        await inter.respond(content="Вы успешно купили шляпу фермера")
        with open("buy.json", "w") as f:
          json.dump(buy2, f)


        with open('skin.json', 'w') as f:
            json.dump(users2, f)

    if inter.component.id == "korona":
      with open('buy.json', 'r') as f:
        buy = json.load(f)
      #проверять если человек в buy.json если нету добавляем
      if str(inter.author.id) not in buy:
        buy[str(inter.author.id)] = {}
        buy[str(inter.author.id)]["hat"] = 0
        buy[str(inter.author.id)]["hat2"] = 0
        buy[str(inter.author.id)]["hat3"] = 0
        with open('buy.json', 'w') as f:
          json.dump(buy, f)
      if buy[str(inter.author.id)]["hat3"] == 0:
      #вы уверены что хотите купить шляпу
        row = ActionRow(
            Button(
                style = ButtonStyle.green,
                label= "Подтвердить",
                custom_id = 'fermer4'
            ),
            Button(
                style = ButtonStyle.red,
                label= "Отмена",
                custom_id = 'no4'
            ),
        )
        emb = discord.Embed(title="Вы уверены что хотите купить корону",color=0xFF0080)
        emb.add_field(name='Стоимость шляпы:', value='250 сообщений', inline = False)
        emb.set_footer(text="С уважением, администрация World of Colonization",icon_url="https://cdn.discordapp.com/avatars/955189437275467798/9949d32ffa9b2776d8788a422f6a184d.png?size=4096")
        channel = client.get_channel(1025120273458012220)
        await channel.send(embed = emb, components = [row], delete_after=10.0)
        await inter.respond(content="Подтвердите покупку")
      else:
        #в skin.json брать id человека и если он уже покупал шляпу то пишем что шляпа есть
        with open("buy.json", "r") as f:
          buy2 = json.load(f)
        #брать из значение hat слово и писать его
        if buy2[str(inter.author.id)]["hat3"] == "korona":
          with open('skin.json', 'r') as f:
            users2 = json.load(f)
          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronakosh.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profile.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekorona.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profileshele.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronashelezo.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profilezoloto.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronazoloto.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profilealmaz.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronaalmaz.jpg'
            await inter.respond(content="Вы успешно надели корону")
          else:
            await inter.respond(content="У вас уже надета эта шляпа или у вас уже стоит другая")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)
        if buy2[str(inter.author.id)]["hat3"] == "korona":
          with open('skin.json', 'r') as f:
            users2 = json.load(f)
          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilevedmakosh.jpg'
            await inter.respond(content="Вы успешно надели корону")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)

          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronakosh.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profile.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekorona.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profileshele.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronashelezo.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profilezoloto.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronazoloto.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profilealmaz.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronaalmaz.jpg'
            await inter.respond(content="Вы успешно надели корону")
          else:
            await inter.respond(content="У вас уже надета эта шляпа или у вас уже стоит другая")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)
              

        with open('skin.json', 'w') as f:
            json.dump(users2, f)




    if inter.component.id == "no4":
      channel = client.get_channel(1025120273458012220)
      await channel.purge(limit=1)
      await inter.respond(content = "Хорошо, покупка отмененна")
    if inter.component.id == "fermer4":
      with open('skin.json', 'r') as f:
        users2 = json.load(f)
      if users2[str(inter.author.id)]['skin'] == 'profilekoshshlaba.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilefermer.jpg':
        await inter.respond(content="Вы успешно купили шляпу, осталось её надеть")
      if users2[str(inter.author.id)]['skin'] == 'profilevedma.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilevedmakosh.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profileshelezovedma.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilealmazvedma.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilezolotovedma.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilealmazfermer.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profileshelezofermer.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilezolotofermer.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilekorona.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilekoronakosh.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilekoronashelezo.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilekoronazoloto.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilekoronaalmaz.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      else:
        with open('skin.json', 'r') as f:
          users2 = json.load(f)
      with open('message.json', 'r') as f:
        users = json.load(f)
      if not str(inter.author.id) in users:
        users[str(inter.author.id)] = {}
        users[str(inter.author.id)]['count'] = 0
      #брать кол-во count если меньше 100 то мы пишем что мало count
      if users[str(inter.author.id)]['count'] < 249:
        await inter.respond(content="Недостаточно сообщение, нужное количество - 250 сообщений")
        channel = client.get_channel(1025120273458012220)
        await channel.purge(limit=1)
      if users[str(inter.author.id)]['count'] > 249:
        users[str(inter.author.id)]['count'] -= 250
        with open('message.json', 'w') as f:
          json.dump(users, f)

          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronakosh.jpg'
            await inter.respond(content="Вы успешно надели корону")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)

          if users2[str(inter.author.id)]['skin'] == 'profile.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekorona.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profileshele.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronashelezo.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profilezoloto.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilekoronazoloto.jpg'
            await inter.respond(content="Вы успешно надели корону")
          if users2[str(inter.author.id)]['skin'] == 'profilealmaz.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilkoronaalmaz.jpg'
            await inter.respond(content="Вы успешно надели корону")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)

#записывать в buy.json какую шляпу купил участник
        with open("buy.json", "r") as f:
          buy2 = json.load(f)
        buy2[str(inter.author.id)]["hat3"] = "korona"
        await inter.respond(content="Вы успешно купили корону")
        with open("buy.json", "w") as f:
          json.dump(buy2, f)


        with open('skin.json', 'w') as f:
            json.dump(users2, f)

    if inter.component.id == "vedma":
      with open('buy.json', 'r') as f:
        buy = json.load(f)
      #проверять если человек в buy.json если нету добавляем
      if str(inter.author.id) not in buy:
        buy[str(inter.author.id)] = {}
        buy[str(inter.author.id)]["hat"] = 0
        buy[str(inter.author.id)]["hat2"] = 0
        buy[str(inter.author.id)]["hat3"] = 0
        with open('buy.json', 'w') as f:
          json.dump(buy, f)
      if buy[str(inter.author.id)]["hat2"] == 0:
      #вы уверены что хотите купить шляпу
        row = ActionRow(
            Button(
                style = ButtonStyle.green,
                label= "Подтвердить",
                custom_id = 'fermer3'
            ),
            Button(
                style = ButtonStyle.red,
                label= "Отмена",
                custom_id = 'no3'
            ),
        )
        emb = discord.Embed(title="Вы уверены что хотите купить шляпу ведьмы",color=0xFF0080)
        emb.add_field(name='Стоимость шляпы:', value='150 сообщений', inline = False)
        emb.set_footer(text="С уважением, администрация World of Colonization",icon_url="https://cdn.discordapp.com/avatars/955189437275467798/9949d32ffa9b2776d8788a422f6a184d.png?size=4096")
        channel = client.get_channel(1025120273458012220)
        await channel.send(embed = emb, components = [row], delete_after=10.0)
        await inter.respond(content="Подтвердите покупку")
      else:
        #в skin.json брать id человека и если он уже покупал шляпу то пишем что шляпа есть
        with open("buy.json", "r") as f:
          buy2 = json.load(f)
        if buy2[str(inter.author.id)]["hat2"] == "vedma":
          with open('skin.json', 'r') as f:
            users2 = json.load(f)
          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilevedmakosh.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)

          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilevedmakosh.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
          if users2[str(inter.author.id)]['skin'] == 'profile.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilevedma.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
          if users2[str(inter.author.id)]['skin'] == 'profileshele.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profileshelezovedma.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
          if users2[str(inter.author.id)]['skin'] == 'profilezoloto.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilezolotovedma.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
          if users2[str(inter.author.id)]['skin'] == 'profilealmaz.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilealmazvedma.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
          else:
            await inter.respond(content="У вас уже надета эта шляпа или у вас уже стоит другая")
            
          with open('skin.json', 'w') as f:
              json.dump(users2, f)
              

        with open('skin.json', 'w') as f:
            json.dump(users2, f)

    if inter.component.id == "no3":
      channel = client.get_channel(1025120273458012220)
      await channel.purge(limit=1)
      await inter.respond(content = "Хорошо, покупка отмененна")
    if inter.component.id == "fermer3":
      with open('skin.json', 'r') as f:
        users2 = json.load(f)
      if users2[str(inter.author.id)]['skin'] == 'profilekoshshlaba.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilefermer.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilevedma.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilevedmakosh.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profileshelezovedma.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilealmazvedma.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilezolotovedma.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilealmazfermer.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profileshelezofermer.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilezolotofermer.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilekoronakosh.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilekoronashelezo.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilekoronazoloto.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      if users2[str(inter.author.id)]['skin'] == 'profilekoronaalmaz.jpg':
        await inter.respond(content="Сначала снимите шляпу")
      else:
        with open('skin.json', 'r') as f:
          users2 = json.load(f)
      with open('message.json', 'r') as f:
        users = json.load(f)
      if not str(inter.author.id) in users:
        users[str(inter.author.id)] = {}
        users[str(inter.author.id)]['count'] = 0
      #брать кол-во count если меньше 100 то мы пишем что мало count
      if users[str(inter.author.id)]['count'] < 149:
        await inter.respond(content="Недостаточно сообщений, нужное количество - 150 сообщений")
        channel = client.get_channel(1025120273458012220)
        await channel.purge(limit=1)
      if users[str(inter.author.id)]['count'] > 149:
        users[str(inter.author.id)]['count'] -= 150
        with open('message.json', 'w') as f:
          json.dump(users, f)

          if users2[str(inter.author.id)]['skin'] == 'profilekosh.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilevedmakosh.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
            with open('skin.json', 'w') as f:
              json.dump(users2, f)

          if users2[str(inter.author.id)]['skin'] == 'profile.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilevedma.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
          if users2[str(inter.author.id)]['skin'] == 'profileshele.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profileshelezovedma.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
          if users2[str(inter.author.id)]['skin'] == 'profilezoloto.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilezolotovedma.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")
          if users2[str(inter.author.id)]['skin'] == 'profilealmaz.jpg':
            #изменять в значении skin на profilekoshshlaba
            users2[str(inter.author.id)]['skin'] = 'profilealmazvemda.jpg'
            await inter.respond(content="Вы успешно надели шляпу ведьмы")

            with open('skin.json', 'w') as f:
              json.dump(users2, f)

#записывать в buy.json какую шляпу купил участник
        with open("buy.json", "r") as f:
          buy2 = json.load(f)
        buy2[str(inter.author.id)]["hat2"] = "vedma"
        await inter.respond(content="Вы успешно купили шляпу ведьмы")
        with open("buy.json", "w") as f:
          json.dump(buy2, f)


        with open('skin.json', 'w') as f:
            json.dump(users2, f)
    if inter.component.id == "prosmotr":
      with open('dosh.json', 'r') as f:
          data4 = json.load(f)
      if str(inter.author.id) not in data4:
        data4[str(inter.author.id)] = {}
        data4[str(inter.author.id)]['300message'] = "nahalo.jpg"
        data4[str(inter.author.id)]['500message'] = "nahalo.jpg"
        data4[str(inter.author.id)]['800message'] = "nahalo.jpg"
        data4[str(inter.author.id)]['5lvl'] = "nahalo.jpg"
        data4[str(inter.author.id)]['15lvl'] = "nahalo.jpg"
        data4[str(inter.author.id)]['50lvl'] = "nahalo.jpg"
      with open('dosh.json', 'w') as f:
          json.dump(data4, f)

      with open('message.json', 'r') as f:
        data = json.load(f)
        if str(inter.author.id) not in data:
          data[str(inter.author.id)]['count'] = 0
        with open('message.json', 'w') as f:
          json.dump(data, f, indent=4)

      with open("levels.json", "r") as f:
        data2 = json.load(f)


        level = data2[str(inter.guild.id)][str(inter.author.id)]['level']
        xp = data2[str(inter.guild.id)][str(inter.author.id)]['xp']
        xp_needed = int(level+(level*100))
        xp_left = xp_needed-xp



        #создать картинку
        #брать из skin.json какую картинку поставил человек и ставить её
        with open('skin.json', 'r') as f:
          data3 = json.load(f)
          if str(inter.author.id) not in data3:
            skin = "profile.jpg"
          else:
            skin = data3[str(inter.author.id)]['skin']
        banner = Image.open(f"skin/{skin}")
        foreground = Image.open("message.png")
        #создать кисть
        draw = ImageDraw.Draw(banner)
          #если id человека есть в dosh.json то мы выполняем код
        dosh = data4[str(inter.author.id)]['300message']
        #если inter.author.id есть в data4 то мы выполняем код
        if str(inter.author.id) in data4:
        
          im2 = Image.open(f'{data4[str(inter.author.id)]["300message"]}')

          banner.paste(im2, (150, 810))
        if str(inter.author.id) in data4:
        
          im3 = Image.open(f'{data4[str(inter.author.id)]["500message"]}')

          banner.paste(im3, (250, 810))
        if str(inter.author.id) in data4:
        
          im4 = Image.open(f'{data4[str(inter.author.id)]["5lvl"]}')

          banner.paste(im4, (350, 810))
        if str(inter.author.id) in data4:
        
          im5 = Image.open(f'{data4[str(inter.author.id)]["15lvl"]}')

          banner.paste(im5, (450, 810))
        if str(inter.author.id) in data4:
        
          im5 = Image.open(f'{data4[str(inter.author.id)]["50lvl"]}')

          banner.paste(im5, (550, 810))

        with open('dosh2.json', 'r') as f:
          data5 = json.load(f)

        font = ImageFont.truetype("minecraft.ttf", 40)
        card = Image.new("RGBA", (220, 220), (255, 255, 255))
        img = Image.open("message.png").convert("RGBA")
        x, y = img.size
        card.paste(img, (0, 0, x, y), img)

      with open('glass.json', 'r') as f:
        data6 = json.load(f)

        #брать из glass.json цвет который написан там и ставить его в fill
        color = data6[str(inter.author.id)]['color']
        #если member.id есть в data6 то мы выполняем код
      if color == "belie":
        color2 = (255,255,255)
      if color == "black":
        color2 =  (0,0,0)
      if color == "green":
        color2 = (0,128,0)
      if color == "pink":
        color2 = (255,20,147)
      if color == "reset":
        color2 = (93,26,116)


      draw.rectangle(((280, 141), (267, 151)), fill=(color2))
      draw.rectangle(((312, 141), (298, 151)), fill=(color2))
        
      if len(str(inter.author.display_name)) > 8:
          draw.text((200, 48), f"{str(inter.author.display_name)[:8]}", (255, 255, 255), font=font)
          draw.text((504, 230), f"Уровень: {level}", (0, 0, 0), font=font)
          draw.text((504, 300), f"Открыто ачивок: {data5[str(inter.author.id)]['dosh2']}", (0,0,0), font=font)
          draw.text((504, 160), f"Сообщений: {data[str(inter.author.id)]['count']}", (0,0,0), font=font)
      else:
          draw.text((200, 48), f"{str(inter.author.display_name)}", (255, 255, 255), font=font)
          draw.text((504, 230), f"Уровень: {level}", (0, 0, 0), font=font)
          draw.text((504, 300), f"Открыто ачивок: {data5[str(inter.author.id)]['dosh2']}", (0,0,0), font=font)
          draw.text((504, 160), f"Сообщений: {data[str(inter.author.id)]['count']}", (0,0,0), font=font)
        #сохраняем картинку
      banner.save("profile.png")
        #отправляем картинку
      await inter.respond(file=discord.File("profile.png"))
    if inter.component.id == "belie":
        with open('glass.json', 'r') as f:
            glass = json.load(f)
        if str(inter.user.id) not in glass:
            glass[str(inter.user.id)] = {}
            glass[str(inter.user.id)]['color'] = "belie"
        await inter.respond(content = f"Вы поставили белый цвет глаз")
        glass[str(inter.user.id)]['color'] = "belie"
        with open('glass.json', 'w') as f:
            json.dump(glass, f)
    if inter.component.id == "black":
        with open('glass.json', 'r') as f:
            glass = json.load(f)
        if str(inter.user.id) not in glass:
            glass[str(inter.user.id)] = {}
            glass[str(inter.user.id)]['color'] = "black"
        await inter.respond(content = f"Вы поставили чёрный цвет глаз")
        glass[str(inter.user.id)]['color'] = "black"
        with open('glass.json', 'w') as f:
            json.dump(glass, f)
    if inter.component.id == "green":
        with open('glass.json', 'r') as f:
            glass = json.load(f)
        if str(inter.user.id) not in glass:
            glass[str(inter.user.id)] = {}
            glass[str(inter.user.id)]['color'] = "green"
        await inter.respond(content = f"Вы поставили зелёный цвет глаз")
        glass[str(inter.user.id)]['color'] = "green"
        with open('glass.json', 'w') as f:
            json.dump(glass, f)
    if inter.component.id == "pink":
        with open('glass.json', 'r') as f:
            glass = json.load(f)
        if str(inter.user.id) not in glass:
            glass[str(inter.user.id)] = {}
            glass[str(inter.user.id)]['color'] = "pink"
        await inter.respond(content = f"Вы поставили розовый цвет глаз")
        glass[str(inter.user.id)]['color'] = "pink"
        with open('glass.json', 'w') as f:
            json.dump(glass, f)
    if inter.component.id == "reset":
        with open('glass.json', 'r') as f:
            glass = json.load(f)
        if str(inter.user.id) not in glass:
            glass[str(inter.user.id)] = {}
            glass[str(inter.user.id)]['color'] = "reset"
        await inter.respond(content = f"Вы убрали цвет глаз")
        glass[str(inter.user.id)]['color'] = "reset"
        with open('glass.json', 'w') as f:
            json.dump(glass, f)
    if inter.component.id == "ybrat":
        #убирать участника из skin.json
        with open('skin.json', 'r') as f:
            users = json.load(f)
        if str(inter.user.id) not in users:
            users[str(inter.user.id)] = {}
            users[str(inter.user.id)]['skin'] = "profile.jpg"
        await inter.respond(content = f"Вы убрали сет", type = 6)
        users[str(inter.user.id)]['skin'] = "profile.jpg"
        with open('skin.json', 'w') as f:
            json.dump(users, f)
    if inter.component.id == "kosh":
      #открывать levels.json
      with open("levels.json", "r") as f:
        data2 = json.load(f)


      level = data2[str(inter.guild.id)][str(inter.author.id)]['level']
      if level >= 5:
        with open('skin.json', 'r') as f:
            data = json.load(f)
        data[str(inter.author.id)] = {}
        data[str(inter.author.id)]['skin'] = "profilekosh.jpg"
        with open('skin.json', 'w') as f:
            json.dump(data, f)
        await inter.respond(content="Вы успешно установили сет на кожаный")
      else:
        await inter.respond(content="У вас недостаточно уровня для установки этого сета. Уровень для установки этого сета - 5")
    if inter.component.id == "shelesh":
      #открывать levels.json
      with open("levels.json", "r") as f:
        data2 = json.load(f)

#открывать message.json
      with open("message.json", "r") as f:
        data3 = json.load(f)

        #если у участника меньше 100 сообщенй он не может ставить картинку
      message = data3[str(inter.author.id)]['count']
      if message >= 80:
        level = data2[str(inter.guild.id)][str(inter.author.id)]['level']
        if level >= 10:
          with open('skin.json', 'r') as f:
              data = json.load(f)
          data[str(inter.author.id)] = {}
          data[str(inter.author.id)]['skin'] = "profileshele.jpg"
          with open('skin.json', 'w') as f:
              json.dump(data, f)
          await inter.respond(content="Вы успешно установили сет железный")
        else:
          await inter.respond(content="У вас недостаточно уровня для установки этого сета. Уровень для установки этого сета - 10")
      else:
        await inter.respond(content="У вас недостаточно сообщений для установки этого сета. Сообщений для установки этого сета - 80")
    if inter.component.id == "zolotoi":
      #открывать levels.json
      with open("levels.json", "r") as f:
        data2 = json.load(f)

#открывать message.json
      with open("message.json", "r") as f:
        data3 = json.load(f)

        #если у участника меньше 100 сообщенй он не может ставить картинку
      message = data3[str(inter.author.id)]['count']
      if message >= 150:
        level = data2[str(inter.guild.id)][str(inter.author.id)]['level']
        if level >= 25:
          with open('skin.json', 'r') as f:
              data = json.load(f)
          data[str(inter.author.id)] = {}
          data[str(inter.author.id)]['skin'] = "profilezoloto.jpg"
          with open('skin.json', 'w') as f:
              json.dump(data, f)
          await inter.respond(content="Вы успешно установили сет золотой")
        else:
          await inter.respond(content="У вас недостаточно уровня для установки этого сета. Уровень для установки этого сета - 25")
      else:
        await inter.respond(content="У вас недостаточно сообщений для установки этого сета. Сообщений для установки этого сета - 150")
    if inter.component.id == "almaz":
      #открывать levels.json
      with open("levels.json", "r") as f:
        data2 = json.load(f)

#открывать message.json
      with open("message.json", "r") as f:
        data3 = json.load(f)

        #если у участника меньше 100 сообщенй он не может ставить картинку
      message = data3[str(inter.author.id)]['count']
      if message >= 300:
        level = data2[str(inter.guild.id)][str(inter.author.id)]['level']
        if level >= 40:
          with open('skin.json', 'r') as f:
              data = json.load(f)
          data[str(inter.author.id)] = {}
          data[str(inter.author.id)]['skin'] = "profilealmaz.jpg"
          with open('skin.json', 'w') as f:
              json.dump(data, f)
          await inter.respond(content="Вы успешно установили сет алмазный")
        else:
          await inter.respond(content="У вас недостаточно уровня для установки этого сета. Уровень для установки этого сета - 40")
      else:
        await inter.respond(content="У вас недостаточно сообщений для установки этого сета. Сообщений для установки этого сета - 300")
    if inter.component.id == "attaka":
        await inter.respond(content="Ваш полководец <@290777169431625728>, напишите ему в личные сообщения! ")
    if inter.component.id == "zashit":
        await inter.respond(content="Ваш полководец <@434407635287146519>, напишите ему в личные сообщения! ")
    if inter.component.id == "repeat":
        await repeat(inter)
    if inter.component.id == "repeat2":
        await repeatoff(inter)
    if inter.component.id == "pause":
        await fpause(inter)
    if inter.component.id == "pause2":
        await fresume(inter)
    if inter.component.id == "bal1":
        with open('bal.json', 'r') as f:
            bal = json.load(f)
        if f'{inter.user.id}' not in bal:
            bal[f'{inter.user.id}'] = 1
            await inter.respond(content = 'Мы учтём ваш отзыв и станем лучше!')
        else:
            await inter.respond(content = 'Вы уже голосовали')
        with open('bal.json', 'w') as f:
            json.dump(bal, f)
    if inter.component.id == "bal2":
        with open('bal.json', 'r') as f:
            bal = json.load(f)
        if f'{inter.user.id}' not in bal:
            bal[f'{inter.user.id}'] = 2
            await inter.respond(content = 'Мы учтём ваш отзыв и станем лучше!')
        else:
            await inter.respond(content = 'Вы уже голосовали')
        with open('bal.json', 'w') as f:
            json.dump(bal, f)
    if inter.component.id == "bal3":
        with open('bal.json', 'r') as f:
            bal = json.load(f)
        if f'{inter.user.id}' not in bal:
            bal[f'{inter.user.id}'] = 3
            await inter.respond(content = 'Есть куда стремиться! ')
        else:
            await inter.respond(content = 'Вы уже голосовали')
        with open('bal.json', 'w') as f:
            json.dump(bal, f)
    if inter.component.id == "bal4":
        with open('bal.json', 'r') as f:
            bal = json.load(f)
        if f'{inter.user.id}' not in bal:
            bal[f'{inter.user.id}'] = 4
            await inter.respond(content = ':)')
        else:
            await inter.respond(content = 'Вы уже голосовали')
        with open('bal.json', 'w') as f:
            json.dump(bal, f)
    if inter.component.id == "bal5":
        with open('bal.json', 'r') as f:
            bal = json.load(f)
        if f'{inter.user.id}' not in bal:
            bal[f'{inter.user.id}'] = 5
            await inter.respond(content = 'Дальше - лучше')
        else:
            await inter.respond(content = 'Вы уже голосовали')
        with open('bal.json', 'w') as f:
            json.dump(bal, f)
      
async def fskip(ctx):
    if await is_connected(ctx, user_connected=True, send_assert=True):
        global currently_playing    
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.stop()
            embed = discord.Embed(title="Пропущено: " + currently_playing[ctx.message.guild.id]['title'],color=0xFF0080)
            await ctx.send(embed=embed)
        else:
            currently_playing[ctx.message.guild.id] =  null_music_data
            embed = discord.Embed(title='Нету никакой музыки, которую можно пропустить!',color=0xFF0080)
            await ctx.send(embed=embed)

@client.command()
async def givehat3(ctx):
    with open("buy.json", "r") as file:
        data = json.load(file)
        #занести всех пользователей и выдать им значение hat hat2
        for user in ctx.guild.members:
            data[str(user.id)]["hat"] = 0
            data[str(user.id)]["hat2"] = 0


@client.command()
async def giveall(ctx):
    #открыть skin.json
    with open("skin.json", "r") as file:
        data = json.load(file)
        #занести всех пользователей сервера и написать в skin profile.jpg
        for user in ctx.guild.members:
            data[str(user.id)] = {"skin": "profile.jpg"}
        #записать в skin.json
        with open("skin.json", "w") as file:
            json.dump(data, file)
        await ctx.send("Готово")
        await ctx.message.delete()

@client.command(pass_context = True)
async def skip(ctx):
    await fskip(ctx)
    await ctx.message.delete()
@client.command(pass_context = True)
async def s(ctx):
    await fskip(ctx)
    await ctx.message.delete()
# ------------------------------------- - ------------------------------------ #

# --------------------------------- queue, q --------------------------------- #
async def fqueue(ctx):
    if await is_connected(ctx, user_connected=True, send_assert=True):
        guild_id = ctx.message.guild.id
        if not currently_playing[guild_id] or currently_playing[guild_id] == null_music_data:
            await ctx.send(':cricket: Ничего не играет и не стоит в очереди')
        else:
            embed = discord.Embed(colour = discord.Colour.magenta())
            embed.add_field(name=':microphone: Сейчас играет: ' + currently_playing[guild_id]['title'], value='Запросил: :' + currently_playing[guild_id]['requestor'].mention, inline=False)
            embed.add_field(name='Следующий:', value=':parrot:', inline = False)
            if ctx.message.guild.id in music_queues:
                local_queue = music_queues[ctx.message.guild.id]
                for i in range(len(local_queue)):
                    music_data = local_queue[i]
                    embed.add_field(name=str((i+1))+') ' + music_data['title'], value='Запросил: ' + music_data['requestor'].mention, inline=False)

            await ctx.send(embed = embed)

@client.command(pass_context = True)
async def queue(ctx):
    await fqueue(ctx)  
    await ctx.message.delete()  

@client.command(pass_context = True)
async def q(ctx):
    await fqueue(ctx)
    await ctx.message.delete()
# ------------------------------------- - ------------------------------------ #

# --------------------------------- stop, st --------------------------------- #
async def clear_queue(ctx, clear_active = False):
    if clear_active:
        global currently_playing
        currently_playing[ctx.message.guild.id] = null_music_data
    
    if ctx.message.guild.id in music_queues:
        music_queues[ctx.message.guild.id] = []

    await ctx.send('Очередь очищена!')

async def fstop(ctx):
    if await is_connected(ctx, user_connected=True, send_assert=True):
        await clear_queue(ctx, True)
        await ctx.guild.voice_client.disconnect()

        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()   
            await ctx.send(':stop_button: Перестал играть!')

@client.command(pass_context = True)
async def stop2(ctx):
    await fstop(ctx)
    await ctx.message.delete()
@client.command(pass_context = True)
async def st(ctx):
    await fstop(ctx)
    await ctx.message.delete()
# ------------------------------------- - ------------------------------------ #

# --------------------------------- join, disconnect --------------------------------- #
async def fjoin(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        guild_id = ctx.message.guild.id
        
        #await clear_queue(ctx)
        if voice and voice.is_connected():
            if voice.channel != channel:
                await voice.move_to(channel)
            else:
                await ctx.send(':confused: Бот уже подключен к вашему голосовому каналу.')
                return
        else:
            voice = await channel.connect()      

        currently_playing[guild_id] = null_music_data
        music_queues[guild_id] = []
        await ctx.send(':dancer: Присоединился!')
    else:
        await ctx.send(':angry: Вы в не голосовом канале')

@client.command(pass_context = True)
async def join2(ctx):
    await fjoin(ctx)
    await ctx.message.delete()

FFMPEG_PATH = '/home/runner/yourreplnamehere/node_modules/ffmpeg-static/ffmpeg'

# You must include this line for it to work

discord.opus.load_opus("./libopus.so.0.8.0")

@client.command(pass_context = True)
async def j(ctx):
    await fjoin(ctx)
    await ctx.message.delete()


async def fdisconnect(ctx):
    if await is_connected(ctx, user_connected=True, send_assert=True):
        await clear_queue(ctx, True)
        await ctx.guild.voice_client.disconnect()
        await ctx.send(':smiling_face_with_tear: Вышел')
        
@client.command(pass_context = True)
async def disconnect(ctx):
    await fdisconnect(ctx)
    await ctx.message.delete()
    
@client.command(pass_context = True)
async def d(ctx):
    await fdisconnect(ctx)
    await ctx.message.delete()

@client.command()
async def vopros(ctx):
    emb = discord.Embed(title="Чтобы принять участие в битве, нажмите на одну из предложенных ниже кнопок.",color=0xFF0080)
    emb.set_footer(text="С уважением, администрация World of Colonization",icon_url="https://cdn.discordapp.com/avatars/955189437275467798/9949d32ffa9b2776d8788a422f6a184d.png?size=4096")
    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label = 'Присоединиться к атаке',
            emoji = "⚔️",
            custom_id = 'attaka'
        ),
        Button(
            style = ButtonStyle.gray,
            label = 'Присоединиться к обороне',
            emoji = "🛡",
            custom_id = 'zashit',
        ),
    )
    await ctx.send(embed = emb, components = [row])
    await ctx.message.delete()

@client.command()
async def profilmenu(ctx):
    emb = discord.Embed(title="Нажмите на кнопку чтобы посмотреть свой профиль",color=0xFF0080)
    emb.set_footer(text="С уважением, администрация World of Colonization",icon_url="https://cdn.discordapp.com/avatars/955189437275467798/9949d32ffa9b2776d8788a422f6a184d.png?size=4096")
    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label = 'Посмотреть профиль',
            custom_id = 'prosmotr'
        ),
    )
    await ctx.send(embed = emb, components = [row])
    await ctx.message.delete()

client.run(
    "OTYxMzU2NTg5ODY3MDg1ODU0.G04vQx.EUseSyxcYbnG9_KXLBcck3zqCsapxRKrZVnBeo")
