
import discord
import json
import asyncio

import datetime
from discord import File
from discord.ext import commands
from typing import Optional
from easy_pil import Editor, load_image_async, Font
import PIL
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
from PIL import Image, ImageDraw, ImageFont
import random

#if you want to give role to the user at any specific level upgrade then you can do like this
#enter the name of the role in a list
level = ["Level-5+", "Level-10+", "Level-15+"]

#указать путь на font





#add the level number at which you want to give the role
level_num = [5, 10, 15]

class Levelsys(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print("Leveling Cog Ready!")

  #this will increase the user's xp everytime they message
  @commands.Cog.listener()
  async def on_message(self, message):

    if message.author.id == 690246409613737986:
      return
    if not message.content.startswith("m."):

      #checking if the bot has not sent the message
      if not message.author.bot:
        with open("levels.json", "r") as f:
          data = json.load(f)
        
        #checking if the user's data is already there in the file or not
        if str(message.guild.id) in data:
          if str(message.author.id) in data[str(message.guild.id)]:
            xp = data[str(message.guild.id)][str(message.author.id)]['xp']
            lvl = data[str(message.guild.id)][str(message.author.id)]['level']
  
            #increase the xp by the number which has 100 as its multiple
            increased_xp = xp+25
            new_level = int(increased_xp/100)
  
            data[str(message.guild.id)][str(message.author.id)]['xp']=increased_xp
  
            with open("levels.json", "w") as f:
              json.dump(data, f)
  
            if new_level > lvl:
              channel = self.bot.get_channel(1024734194817044611)
  
              userr = message or message.author
#открыть шрифт anime.ttf
              font_type = ImageFont.truetype("Borsok.ttf", 40)



              with open("levels.json", "r") as f:
                data = json.load(f)

              with open("userdata.json", "r") as f:
                user_data = json.load(f)



                #с каждым новым уровнем писать в чат
              if str(message.guild.id) in data:
                if str(message.author.id) in data[str(message.guild.id)]:
                  data[str(message.guild.id)][str(message.author.id)]['level'] = new_level
                  banner = Image.open(random.choice(["mine.png", "message1.png", "message2.png", "message3.png", "message4.png", "dosh2.png"]))
                  draw = ImageDraw.Draw(banner)
                  font = ImageFont.truetype("minecraft.ttf", 15)
                  # писать текст сколько всего участников на сервере
                  draw.text((60, 35), f"{message.author.name} получил новый уровень - {new_level}", (255, 255, 255), font=font)
                  #получить список участнико
                  banner.save("mine2.png")
                  #отправлять файл
                if message.author.bot: return

                with open("levels.json", "w") as f:
                  json.dump(data, f)







              await channel.send(file=discord.File('mine2.png'))

  
              data[str(message.guild.id)][str(message.author.id)]['level']=new_level
              data[str(message.guild.id)][str(message.author.id)]['xp']=0
  
              with open("levels.json", "w") as f:
                json.dump(data, f)
              
              for i in range(len(level)):
                if new_level == level_num[i]:
                  await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
  
                  mbed = discord.Embed(title=f"{message.author} Вы получили роль**{level[i]}**!", color = message.author.colour)
                  mbed.set_thumbnail(url=message.author.avatar_url)
                  await message.channel.send(embed=mbed)
            return
  
        if str(message.guild.id) in data:
          data[str(message.guild.id)][str(message.author.id)] = {}
          data[str(message.guild.id)][str(message.author.id)]['xp'] = 0
          data[str(message.guild.id)][str(message.author.id)]['level'] = 1
        else:
          data[str(message.guild.id)] = {}
          data[str(message.guild.id)][str(message.author.id)] = {}
          data[str(message.guild.id)][str(message.author.id)]['xp'] = 0
          data[str(message.guild.id)][str(message.author.id)]['level'] = 1
  
        with open("levels.json", "w") as f:
          json.dump(data, f)

        with open("userdata.json", "r") as f:
          user_data = json.load(f)
  
        if str(message.author.id) in user_data:
          pass
        else:
          #these are the default value for user rank card
          user_data[str(message.author.id)] = {}
          user_data[str(message.author.id)]['card'] = 5
          user_data[str(message.author.id)]['text_color'] = "#D71868"
          user_data[str(message.author.id)]['bar_color'] = "#D71868"
          user_data[str(message.author.id)]['blend'] = 1
  
        with open("userdata.json", "w") as f:
          json.dump(user_data, f)




        if message.channel.type == discord.ChannelType.voice:
          with open("levels.json", "r") as f:
            data = json.load(f)
          
          if str(message.guild.id) in data:
            if str(message.author.id) in data[str(message.guild.id)]:
              xp = data[str(message.guild.id)][str(message.author.id)]['xp']
              lvl = data[str(message.guild.id)][str(message.author.id)]['level']
          
              #increase the xp by the number which has 100 as its multiple
              increased_xp = xp+1
              new_level = int(increased_xp/100)
          
              data[str(message.guild.id)][str(message.author.id)]['xp']=increased_xp
          
              with open("levels.json", "w") as f:
                json.dump(data, f)
              with open('dosh.json', 'r') as f:
                data2 = json.load(f)
#если у участника в levels.json 5 level то мы записываем в dosh.json значение 5lvl.jpg
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 2:
                data2[str(message.author.id)]['5lvl'] = "5lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 10:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "10lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 15:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "15lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 20:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "20lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 25:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "25lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 30:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "30lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 35:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "35lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 40:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "40lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 45:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "45lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 50:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "50lvl.jpg"
              if data[str(message.guild.id)][str(message.author.id)]['level'] == 55:
                data[str(message.guild.id)][str(message.author.id)]['dosh'] = "55lvl.jpg"

  
  @commands.command(name="rank")
  async def rank(self, ctx: commands.Context, user: Optional[discord.Member]):
   if ctx.channel.id != 986013528047624253:
    embed = discord.Embed(title="Ошибка :angry:", description=f"Мой создатель запретил тут использовать эту команду :(", color=0xFF0080)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed,delete_after=10.0)
    await ctx.message.delete()
   else:
    userr = user or ctx.author

#открыть шрифт anime.ttf
    font_type = ImageFont.truetype("Borsok.ttf", 40)



    with open("levels.json", "r") as f:
      data = json.load(f)

    with open("userdata.json", "r") as f:
      user_data = json.load(f)

    xp = data[str(ctx.guild.id)][str(userr.id)]["xp"]
    lvl = data[str(ctx.guild.id)][str(userr.id)]["level"]

    next_level_xp = (lvl+1) * 100
    xp_need = next_level_xp
    xp_have = data[str(ctx.guild.id)][str(userr.id)]["xp"]

    card_num = str(user_data[str(userr.id)]['card'])
    text_color = str(user_data[str(userr.id)]['text_color'])
    bar_color = str(user_data[str(userr.id)]['bar_color'])
    blend = int(user_data[str(userr.id)]['blend'])

    percentage = int(((xp_have * 100)/ xp_need))

    if percentage < 1:
      percentage = 0
    
    ## Rank card
    background = Editor(f"{card_num}.png")
    profile = await load_image_async(str(userr.avatar_url))

    profile = Editor(profile).resize((150, 150)).circle_image()
    
    poppins = Font.poppins(size=50)
    poppins_small = Font.poppins(size=40)

    #you can skip this part, I'm adding this because the text is difficult to read in my selected image
    if blend == 1:
      ima = Editor("zBLACK.png")

    background.rectangle((345, 5), width=160, height=160, fill="#ffffff", radius=100)
    background.paste(profile.image, (350, 10))
    #сделать белый круг



    background.rectangle((30, 220), width=416, height=64, fill="#fff", radius=20)
    background.bar(
        (30, 220),
        max_width=850,
        height=64,
        percentage=percentage,
        fill="#D71868",
        radius=20,
    )
    width, height = (650,350)
    background.text((width/2, height/2), str(userr.name), font=font_type, color="#ffffff")

  
    background.text(
        (200, 220),
        f"Level : {lvl}   "
        + f" XP : {xp} / {(lvl+1) * 100}",
        font=font_type,
        color="#282828",
    )

    card = File(fp=background.image_bytes, filename="zCARD.png")
    await ctx.send(file=card)
    await ctx.message.delete()

  @commands.command(name="asdfgvs")
  async def asdfgvs(self, ctx, range_num=5):
   if ctx.channel.id != 961668931934879794:
    embed = discord.Embed(title="Ошибка :angry:", description=f"Мой создатель запретил тут использовать эту команду :(", color=0xFF0080)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed,delete_after=10.0)
    await ctx.message.delete()
   else:
    with open("levels.json", "r") as f:
      data = json.load(f)

    l = {}
    total_xp = []

    for userid in data[str(ctx.guild.id)]:
      xp = int(data[str(ctx.guild.id)][str(userid)]['xp']+(int(data[str(ctx.guild.id)][str(userid)]['level'])*100))

      l[xp] = f"{userid};{data[str(ctx.guild.id)][str(userid)]['level']};{data[str(ctx.guild.id)][str(userid)]['xp']}"
      total_xp.append(xp)

    total_xp = sorted(total_xp, reverse=True)
    index=1

    mbed = discord.Embed(
      title="📋 Список Лидеров Сервера", description="**ТОП 5 ТЕКСТ :speech_balloon:**", timestamp=ctx.message.created_at, color=discord.Color.blue()
    )

    for amt in total_xp:
      id_ = int(str(l[amt]).split(";")[0])
      level = int(str(l[amt]).split(";")[1])
      xp = int(str(l[amt]).split(";")[2])

      member = await self.bot.fetch_user(id_)

      if member is not None:
        name = member.name
        mbed.add_field(name=f"#{index}. {name}",
        value=f"**Level: {level} | XP: {xp}**", 
        inline=False)
        if index == 1:
          mbed.set_thumbnail(url=member.avatar_url)
        mbed.set_footer(text="World of Colonization")
        if index == range_num:
          break
        else:
          index += 1

    await ctx.send(embed = mbed)
    await ctx.message.delete()

  @commands.command("rank_reset")
  async def rank_reset(self, ctx, user: Optional[discord.Member]):
    member = user or ctx.author

    #this if statement will check that user who's using this command is trying to remove his data or any other user data
    #if she is trying to remove any other user's data then we are going to check that he has a specific role or not (in my case its 'Bot-Mod') so that only admins can remov any users data and not other people can remove other
    if not member == ctx.author:
      role = discord.utils.get(ctx.author.guild.roles, id=966085994724081705)

      if not role in member.roles:
        embed = discord.Embed(title="Ошибка", description=f"Вы можете сбросить только свои данные, для сброса других данных у вас должны быть {role.mention} роль", color=0x00ff00)
        await ctx.send(embed = embed)
        return 
    
    with open("levels.json", "r") as f:
      data = json.load(f)

    del data[str(ctx.guild.id)][str(member.id)]

    with open("levels.json", "w") as f:
      json.dump(data, f)

    await ctx.send(f"{member.mention} Данные Были сброшены")
  
  @commands.command(name="increase_level")
  @commands.has_role("Bot-Mod")
  async def increase_level(self, ctx, increase_by: int, user: Optional[discord.Member]):
    member = user or ctx.author

    with open("levels.json", "r") as f:
      data = json.load(f)
    
    data[str(ctx.guild.id)][str(member.id)]['level'] += increase_by

    with open("levels.json", "w") as f:
      json.dump(data, f)
    
    await ctx.send(f"{member.mention}, Ваш уровень был увеличен на: {increase_by}")

  @commands.command(name="increase_xp")
  @commands.has_role("Bot-Mod")
  async def increase_xp(self, ctx, increase_by: int, user: Optional[discord.Member]):
    member = user or ctx.author

    with open("levels.json", "r") as f:
      data = json.load(f)

    data[str(ctx.guild.id)][str(member.id)]['xp'] += increase_by

    with open("levels.json", "w") as f:
      json.dump(data, f)

    await ctx.send(f"{member.mention}, Получин новый уровень! - {increase_by}")

    with open("test.json", "w") as f:
      json.dump(data, f)


  @commands.command(name="testtest")
  async def testtest(self, ctx: commands.Context, user: Optional[discord.Member]):
   if ctx.channel.id != 961668931934879794:
    embed = discord.Embed(title="Ошибка :angry:", description=f"Мой создатель запретил тут использовать эту команду :(", color=0xFF0080)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed,delete_after=10.0)
    await ctx.message.delete()
   else:
    userr = user or ctx.author

#открыть шрифт anime.ttf
    font_type = ImageFont.truetype("Borsok.ttf", 40)



    with open("levels.json", "r") as f:
      data = json.load(f)

    with open("userdata.json", "r") as f:
      user_data = json.load(f)

    xp = data[str(ctx.guild.id)][str(userr.id)]["xp"]
    lvl = data[str(ctx.guild.id)][str(userr.id)]["level"]

    next_level_xp = (lvl+1) * 100
    xp_need = next_level_xp
    xp_have = data[str(ctx.guild.id)][str(userr.id)]["xp"]

    card_num = str(user_data[str(userr.id)]['card'])
    text_color = str(user_data[str(userr.id)]['text_color'])
    bar_color = str(user_data[str(userr.id)]['bar_color'])
    blend = int(user_data[str(userr.id)]['blend'])

    percentage = int(((xp_have * 100)/ xp_need))

    if percentage < 1:
      percentage = 0
    
    ## Rank card
    background = Editor(f"{card_num}.png")
    profile = await load_image_async(str(userr.avatar_url))

    profile = Editor(profile).resize((150, 150)).circle_image()
    
    poppins = Font.poppins(size=50)
    poppins_small = Font.poppins(size=40)

    #you can skip this part, I'm adding this because the text is difficult to read in my selected image
    if blend == 1:
      ima = Editor("zBLACK.png")

    background.rectangle((345, 5), width=160, height=160, fill="#ffffff", radius=100)
    background.paste(profile.image, (350, 10))
    #сделать белый круг



    background.rectangle((30, 220), width=416, height=64, fill="#fff", radius=20)
    background.bar(
        (30, 220),
        max_width=416,
        height=64,
        percentage=percentage,
        fill="#D71868",
        radius=20,
    )
    width, height = (650,350)
    background.text((width/2, height/2), str(userr.name), font=font_type, color="#ffffff")

  
    background.text(
        (200, 220),
        f"Level : {lvl}   "
        + f" XP : {xp} / {(lvl+1) * 100}",
        font=font_type,
        color="#282828",
    )

    card = File(fp=background.image_bytes, filename="zCARD.png")
    await ctx.send(file=card)
    await ctx.message.delete()




  @commands.command(name="123123")
  async def ffffff(self, ctx, range_num=5):
   if ctx.channel.id != 986013528047624253:
    embed = discord.Embed(title="Ошибка :angry:", description=f"Мой создатель запретил тут использовать эту команду :(", color=0xFF0080)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed,delete_after=10.0)
    await ctx.message.delete()
   else:
    with open("levels.json", "r") as f:
      data = json.load(f)

    l = {}
    total_xp = []

#сортировать по уровеню пользователей
    for guild in data:
      for user in data[guild]:
        l[user] = data[guild][user]["level"]
        total_xp.append(data[guild][user]["xp"])
    l = sorted(l.items(), key=lambda x: x[1], reverse=True)
    total_xp = sorted(total_xp, reverse=True)
    index = 1

    embed = discord.Embed(title="📋 Список Лидеров Сервера", description="**ТОП 5 ТЕКСТ :speech_balloon:**", color=0xFF0080)
    #вывести информацию
    for i in range(range_num):
      user = self.bot.get_user(int(l[i][0]))
      embed.add_field(name=f"#{i+1}. **{user.name}**", value=f"Level: {l[i][1]} XP: {total_xp[i]}", inline=False)
    embed.set_footer(text=f'World of Colonization', icon_url=f'https://cdn.discordapp.com/avatars/961356589867085854/9949d32ffa9b2776d8788a422f6a184d.png?size=4096')
    user2 = self.bot.get_user(int(l[0][0]))
    embed.set_thumbnail(url=f"{user2.avatar_url}")
    await ctx.send(embed=embed)
    await ctx.message.delete()

  @commands.command(name="asfafasf")
  async def safasf(self, ctx, range_num=5):
   if ctx.channel.id != 961668931934879794:
    embed = discord.Embed(title="Ошибка :angry:", description=f"Мой создатель запретил тут использовать эту команду :(", color=0xFF0080)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed,delete_after=10.0)
    await ctx.message.delete()
   else:
    with open("levels.json", "r") as f:
      data = json.load(f)

    l = {}
    total_xp = []


    
    for userid in data[str(ctx.guild.id)]:
      xp = int(data[str(ctx.guild.id)][str(userid)]['level']+(int(data[str(ctx.guild.id)][str(userid)]['level'])*100))


      l[xp] = f"{userid};{data[str(ctx.guild.id)][str(userid)]['level']};{data[str(ctx.guild.id)][str(userid)]['xp']}"
      total_xp.append(xp)


    total_xp = sorted(total_xp, reverse=True)
    index=1

    mbed = discord.Embed(
      title="📋 Список Лидеров Сервера", description="**ТОП 5 ТЕКСТ :speech_balloon:**", timestamp=ctx.message.created_at, color=discord.Color.blue()
    )


    for amt in total_xp:
      id_ = int(str(l[amt]).split(";")[0])
      level = int(str(l[amt]).split(";")[1])
      xp = int(str(l[amt]).split(";")[2])

      member = await self.bot.fetch_user(id_)

      if member is not None:
        name = member.name
        mbed.add_field(name=f"{index}. {name}",
        value=f"**Level: {level} | XP: {xp}**", 
        inline=False)
        if index == 1:
          mbed.set_thumbnail(url=member.avatar_url)
        mbed.set_footer(text="World of Colonization")

        if index == range_num:
          break
        else:
          index += 1

  @commands.command(name="11")
  async def top(self, ctx, range_num=5):
   if ctx.channel.id != 986013528047624253:
    embed = discord.Embed(title="Ошибка :angry:", description=f"Мой создатель запретил тут использовать эту команду :(", color=0xFF0080)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed,delete_after=10.0)
    await ctx.message.delete()
   else:
    with open("levels.json", "r") as f:
      data = json.load(f)

    l = {}
    total_xp = []

    for userid in data[str(ctx.guild.id)]:
      xp = int(data[str(ctx.guild.id)][str(userid)]['level']+(int(data[str(ctx.guild.id)][str(userid)]['level'])*100))

      l[xp] = f"{userid};{data[str(ctx.guild.id)][str(userid)]['level']};{data[str(ctx.guild.id)][str(userid)]['xp']}"
      total_xp.append(xp)

    total_xp = sorted(total_xp, reverse=True)
    index=1

    mbed = discord.Embed(
      title="📋 Список Лидеров Сервера", description="**ТОП 5 ТЕКСТ :speech_balloon:**", timestamp=ctx.message.created_at, color=discord.Color.blue()
    )

    for amt in total_xp:
      id_ = int(str(l[amt]).split(";")[0])
      level = int(str(l[amt]).split(";")[1])
      xp = int(str(l[amt]).split(";")[2])

      member = await self.bot.fetch_user(id_)

      if member is not None:
        name = member.name
        mbed.add_field(name=f"{index}. {name}",
        value=f"**Level: {level} | XP: {xp}**", 
        inline=False)
        if index == 1:
          mbed.set_thumbnail(url=member.avatar_url)
        mbed.set_footer(text="World of Colonization")
        mbed.set_footer(text=f'Запросил - {ctx.author}',
  icon_url=ctx.author.avatar_url)

        if index == range_num:
          break
        else:
          index += 1

    await ctx.send(embed = mbed)

  @commands.command(name="fffffff")
  async def asfasf(self, ctx, range_num=5):
   if ctx.channel.id != 961668931934879794:
    embed = discord.Embed(title="Ошибка :angry:", description=f"Мой создатель запретил тут использовать эту команду :(", color=0xFF0080)
    embed.set_footer(text=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await ctx.send(embed=embed,delete_after=10.0)
    await ctx.message.delete()
   else:
    with open("levels.json", "r") as f:
      data = json.load(f)

    l = {}
    total_xp = []

    for userid in data[str(ctx.guild.id)]:
      xp = int(data[str(ctx.guild.id)][str(userid)]['level']+(int(data[str(ctx.guild.id)][str(userid)]['level'])*100))

      l[xp] = f"{userid};{data[str(ctx.guild.id)][str(userid)]['level']};{data[str(ctx.guild.id)][str(userid)]['xp']}"
      total_xp.append(xp)

    total_xp = sorted(total_xp, reverse=True)
    index=1

    mbed = discord.Embed(
      title="📋 Список Лидеров Сервера", description="**ТОП 5 ТЕКСТ :speech_balloon:**", timestamp=ctx.message.created_at, color=discord.Color.blue()
    )

    for amt in total_xp:
      id_ = int(str(l[amt]).split(";")[0])
      level = int(str(l[amt]).split(";")[1])
      xp = int(str(l[amt]).split(";")[2])

      member = await self.bot.fetch_user(id_)
    if member.id in mbed.fields:
        mbed.remove_field(member.id)
        mbed.add_field(name=f"{index}", value=f"{member.mention} - {level} уровень\nОпыт: {xp}", inline=False)
        index+=1
    await ctx.send(embed=mbed)
  @commands.has_any_role("Основатель", "Модератор", "Тех.администратор","Старший модератор","Модератор (Исп.срок)")
  @commands.command(name='gorot2')
  async def fesfsefe(self, ctx):
      await ctx.message.delete()
      if ctx.message.reference and (msg := ctx.message.reference.resolved) and isinstance(msg, discord.Message):
        msg = msg.content.split("\n")[0]
        #убирать 1.
        msg = msg.replace("1.", "")
        msg = msg.replace("1)", "")
        #убирать 2.
        msg = msg.replace(" ", "")
        #проверяем в msg название, если такое название уже есть в words.json то мы не создаём город
        with open('words.json', 'r') as f:
            words = json.load(f)
        if msg in words:
            embed = discord.Embed(title="Такой город уже существует.",color=0xFF0080)
            embed.set_footer(
                  text="С уважением, администрация World of Colonization",
                  icon_url=
                  "https://cdn.discordapp.com/avatars/1014579843310047373/ed32de15c1c0bbc4cca8fd1627581978.png"
              )
            await ctx.send(embed=embed)
            return
        if ctx.message.reference and (msg := ctx.message.reference.resolved) and isinstance(msg, discord.Message):
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
          msg = msg.content.split("\n")[0]
          #убирать 1.
          msg = msg.replace("1.", "")
          msg = msg.replace("1)", "")
          #убирать 2.
          msg = msg.replace(" ", "")
          member = ctx.guild.get_member(ctx.message.reference.resolved.author.id)
          await member.edit(nick=f'{ctx.message.reference.resolved.author.name} ({msg})ㅤ')
          role = discord.utils.get(member.guild.roles, name='Правитель')
          await member.add_roles(role)
          with open('words.json', 'r') as f:
              words = json.load(f)
          words[msg] = member.id
          with open('words.json', 'w') as f:
              json.dump(words, f)
          with open("words.json", "r") as f:
              words = json.load(f)
          banner = Image.open("banner.jpg")
          draw = ImageDraw.Draw(banner)
          font = ImageFont.truetype("FSElliotPro-HeavyItalic.ttf", 70)
          # писать текст сколько всего участников на сервере
          draw.text((130, 300), f"{len(words)}", (255, 255, 255), font=font)
          # показывать текст сколько всего участников на сервере
          draw.text((130, 400), f"{len(ctx.guild.members)}",  (255, 255, 255), font=font)
          banner.save("banner2.jpg")
          with open("banner2.jpg", 'rb') as pfp:
              #ставить баннер на сервер
              await ctx.guild.edit(banner=pfp.read())


  
  @commands.has_any_role("Основатель", "Модератор", "Тех.администратор","Старший модератор","Модератор (Исп.срок)")
  @commands.command(name='одобрить')
  async def dobav2(self, ctx, word3):
      await ctx.message.delete()
      if ctx.message.reference and (msg2 := ctx.message.reference.resolved) and isinstance(msg2, discord.Message):
          msg2 = msg2.content.split("\n")[3]
          #убирать 1.
          msg2 = msg2.replace("4. ", " ")
          msg2 = msg2.replace("4) ", " ")
          msg2 = msg2.replace("4 ", " ")
          msg2 = msg2.replace("4.", " ")
          msg2 = msg2.replace("4)", " ")
          msg2 = msg2.replace("4", " ")
      if ctx.message.reference and (msg := ctx.message.reference.resolved) and isinstance(msg, discord.Message):
          msg = msg.content.split("\n")[0]
          #убирать 1.
          msg = msg.replace("1.", " ")
          msg = msg.replace("1) ", " ")
          msg = msg.replace("1 ", " ")
          msg = msg.replace("1", " ")
          #убирать 2.
          msg = msg.replace(" ", "")
          with open('test.json', 'r') as file:
              data = json.load(file)
          if msg in data:
            if msg2 in data[msg]:
              embed=discord.Embed(title=f'Район "{msg2}" уже одобрен!',
                                            color=0x00FF00)
              embed.set_footer(
                      text="Администрация World of Colonization",
                      icon_url=
                      "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
                  )
              await ctx.send(embed=embed,delete_after = 10)
            else:
              data[msg].append(msg2)
              data[msg].append(word3)
              data[msg].append(f"<@{ctx.author.id}>")
          else:
              data[msg] = [msg2, word3, f"<@{ctx.author.id}>"]
          with open('test.json', 'w') as file:
              json.dump(data, file)
              embed=discord.Embed(title=f""" —————————————————————————————————
                                              Район {msg2} принят!
                                            Выдано чанков: {word3}
—————————————————————————————————""",color=0x00FF00)
              embed.set_footer(
        text="С уважением, администрация World of Colonization",
        icon_url=
        "https://cdn.discordapp.com/icons/786301738155245578/f628f2d3fb9db349dba7944a6190ea86.webp?size=96"
    )
              await ctx.send(embed=embed)
  @commands.command(name="top")
  async def top(self, ctx):
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
      #брать из levels.json брать уровень участника и создать топ 5 участников по уровню вставлять текст в картинку pillow
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
              await ctx.message.delete()
  @commands.command(name="all")
  async def all(self, ctx):
    #добавить в levels.json всем участникам значение count 0
      with open("levels.json", "r") as f:
        data = json.load(f)
      if str(ctx.guild.id) in data:
        if data[str(ctx.guild.id)]:
          data = data[str(ctx.guild.id)]
          for i in data:
            data[i]["count"] = 1
      with open("levels.json", "w") as f:
        json.dump(data, f, indent=2)
      await ctx.message.delete()
  
  @commands.command(name="12331231")
  async def tesatqawga(self, ctx):
      #сделать топ 5 лидеров людей по сообщениям брать из message.json
      if ctx.author.id == 302050872383242240:
        with open("message.json", "r") as f:
          data = json.load(f)
        if str(ctx.guild.id) in data:
          if data[str(ctx.guild.id)]:
            data = data[str(ctx.guild.id)]
            data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['count'], reverse=True)}
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
            draw.text((60, 450), f"Топ 5 участников по сообщениям", (0, 0, 0), font=font)
            for i in range(5):
              if top_5[i] is None:
                continue
              if len(top_5[i].display_name) > 9:
                draw.text((60, 450+50*i), f"{i+1}. {top_5[i].display_name[:5]}", (0, 0, 0), font=font)
                draw.text((60+200, 450+50*i), f"{data[str(top_5[i].id)]['count']} сообщений", (0,0,0), font=font)
              else:
                draw.text((60, 450+50*i), f"{i+1}. {top_5[i].display_name}", (0, 0, 0), font=font)
                draw.text((60+200, 450+50*i), f"{data[str(top_5[i].id)]['count']} сообщений", (0,0,0), font=font)
            banner.save("banner.png", "PNG")
            await ctx.send(file=discord.File("banner.png"))
            await ctx.message.delete()

  
  @commands.command(name="xp")
  async def rank(self, ctx):
    #выдать всем пользователем сервера 0 xp и 1 level
    with open("levels.json", "r") as f:
      data = json.load(f)
  
    if str(ctx.guild.id) in data:
      pass
    else:
      data[str(ctx.guild.id)] = {}
  
    for member in ctx.guild.members:
      if str(member.id) in data[str(ctx.guild.id)]:
        pass
      else:
        data[str(ctx.guild.id)][str(member.id)] = {}
        data[str(ctx.guild.id)][str(member.id)]['xp'] = 0
        data[str(ctx.guild.id)][str(member.id)]['level'] = 1
  
    with open("levels.json", "w") as f:
      json.dump(data, f)
  
    await ctx.send("Added all members to the level database")

  @commands.command(name="rank")
  async def rank(self, ctx: commands.Context, user: Optional[discord.Member]):
    userr = user or ctx.author

#открыть шрифт anime.ttf
    font_type = ImageFont.truetype("Borsok.ttf", 40)



    with open("levels.json", "r") as f:
      data = json.load(f)

    with open("userdata.json", "r") as f:
      user_data = json.load(f)

    xp = data[str(ctx.guild.id)][str(userr.id)]["xp"]
    lvl = data[str(ctx.guild.id)][str(userr.id)]["level"]

    next_level_xp = (lvl+1) * 100
    xp_need = next_level_xp
    xp_have = data[str(ctx.guild.id)][str(userr.id)]["xp"]

    card_num = str(user_data[str(userr.id)]['card'])
    text_color = str(user_data[str(userr.id)]['text_color'])
    bar_color = str(user_data[str(userr.id)]['bar_color'])
    blend = int(user_data[str(userr.id)]['blend'])

    percentage = int(((xp_have * 100)/ xp_need))

    if percentage < 1:
      percentage = 0
    
    ## Rank card
    background = Editor(f"{card_num}.png")
    profile = await load_image_async(str(userr.avatar_url))

    profile = Editor(profile).resize((150, 150)).circle_image()
    
    poppins = Font.poppins(size=50)
    poppins_small = Font.poppins(size=40)

    #you can skip this part, I'm adding this because the text is difficult to read in my selected image
    if blend == 1:
      ima = Editor("zBLACK.png")

    background.rectangle((345, 5), width=160, height=160, fill="#ffffff", radius=100)
    background.paste(profile.image, (350, 10))
    #сделать белый круг



    background.rectangle((30, 220), width=850, height=40, fill="#fff", radius=20)
    background.bar(
        (30, 220),
        max_width=850,
        height=40,
        percentage=percentage,
        fill="#D71868",
        radius=20,
    )
    width, height = (650,350)
    background.text((width/2, height/2), str(userr.name), font=font_type, color="#ffffff")

  
    background.text(
        (200, 220),
        f"Level : {lvl}   "
        + f" XP : {xp} / {(lvl+1) * 100}",
        font=font_type,
        color="#282828",
    )

    card = File(fp=background.image_bytes, filename="zCARD.png")
    await ctx.send(file=card)
    await ctx.message.delete()

def setup(client):
  client.add_cog(Levelsys(client))


