
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

class message(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print("message Cog Ready!")

  #this will increase the user's xp everytime they message
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot:
      return
    if message.content.startswith("m."):
      return
    if message.author.id == 690246409613737986:
      return
    def check(m):
      return m.author == message.author and m.channel == message.channel

    try:
      msg = await self.bot.wait_for("message", timeout=2.0, check=check)
      if msg:
        return
    except asyncio.TimeoutError:
      pass
    with open('message.json', 'r') as f:
        data = json.load(f)
    if str(message.author.id) in data:
        data[str(message.author.id)]['count'] += 1
    else:
        data[str(message.author.id)] = {}
        data[str(message.author.id)]['count'] = 1
    with open('message.json', 'w') as f:
        json.dump(data, f)
        #если у человека count = 10 то мы отправляем в чат что у него 10 сообещний
    with open('message.json', 'r') as f:
        data = json.load(f)
        #каждые 10 count мы пишем сколько набрал сообщений человек
        if data[str(message.author.id)]['count'] % 10 == 0:
            channel = self.bot.get_channel(1024734194817044611)
            banner = Image.open(random.choice(["mine.png", "message1.png", "message2.png", "message3.png", "message4.png", "dosh2.png"]))
            draw = ImageDraw.Draw(banner)
            font = ImageFont.truetype("minecraft.ttf", 15)
            # писать текст сколько всего участников на сервере
            draw.text((60, 35), f"{message.author.name} набрал {data[str(message.author.id)]['count']} сообщений", (255, 255, 255), font=font)
            #получить список участнико
            banner.save("message.png")
            await channel.send(file=discord.File("message.png"))
    with open('message.json', 'r') as f:
        data = json.load(f)
    if data[str(message.author.id)]['count'] == 300:
      #изменять значение в dosh.json 300message вместо nahalo.jpg на almaz.jpg
        with open('dosh.json', 'r') as f:
            data = json.load(f)
        if str(message.author.id) in data:
            data[str(message.author.id)]['300message'] = "lapus.jpg"
        else:
            data[str(message.author.id)]['300message'] = "lapus.jpg"
        with open('dosh.json', 'w') as f:
            json.dump(data, f)
        with open('dosh2.json', 'r') as f:
            data2 = json.load(f)
        if str(message.author.id) in data2:
            data2[str(message.author.id)]['dosh2'] += 1
        else:
            data2[str(message.author.id)] = {}
            data2[str(message.author.id)]['dosh2'] = 0
        with open('dosh2.json', 'w') as f:
            json.dump(data2, f)
        with open('dosh.json', 'r') as f:
            data = json.load(f)
    if data[str(message.author.id)]['count'] == 500:
      #изменять значение в dosh.json 300message вместо nahalo.jpg на almaz.jpg
        with open('dosh.json', 'r') as f:
            data = json.load(f)
        if str(message.author.id) in data:
            data[str(message.author.id)]['500message'] = "isumrud.jpg"
        else:
            data[str(message.author.id)]['500message'] = "isumrud.jpg"
        with open('dosh.json', 'w') as f:
            json.dump(data, f)
        with open('dosh2.json', 'r') as f:
            data2 = json.load(f)
        if str(message.author.id) in data2:
            data2[str(message.author.id)]['dosh2'] += 1
        else:
            data2[str(message.author.id)] = {}
            data2[str(message.author.id)]['dosh2'] = 0
        with open('dosh2.json', 'w') as f:
            json.dump(data2, f)
    with open('levels.json', 'r') as f:
        data = json.load(f)
    if data[str(message.guild.id)][str(message.author.id)]['xp'] == 475:
        with open('dosh.json', 'r') as f:
            data = json.load(f)
        if str(message.author.id) in data:
            data[str(message.author.id)]['5lvl'] = "5lvl.jpg"
        else:
            data[str(message.author.id)] = {}
            data[str(message.author.id)]['5lvl'] = "5lvl.jpg"
        with open('dosh.json', 'w') as f:
            json.dump(data, f)
        with open('dosh2.json', 'r') as f:
            data2 = json.load(f)
        if str(message.author.id) in data2:
            data2[str(message.author.id)]['dosh2'] += 1
        else:
            data2[str(message.author.id)] = {}
            data2[str(message.author.id)]['dosh2'] = 0
        with open('dosh2.json', 'w') as f:
            json.dump(data2, f)
    if data[str(message.guild.id)][str(message.author.id)]['xp'] == 1475:
        with open('dosh.json', 'r') as f:
            data = json.load(f)
        if str(message.author.id) in data:
            data[str(message.author.id)]['5lvl'] = "15lvl.jpg"
        else:
            data[str(message.author.id)] = {}
            data[str(message.author.id)]['5lvl'] = "15lvl.jpg"
        with open('dosh.json', 'w') as f:
            json.dump(data, f)
        with open('dosh2.json', 'r') as f:
            data2 = json.load(f)
        if str(message.author.id) in data2:
            data2[str(message.author.id)]['dosh2'] += 1
        else:
            data2[str(message.author.id)] = {}
            data2[str(message.author.id)]['dosh2'] = 0
        with open('dosh2.json', 'w') as f:
            json.dump(data2, f)






  @commands.command(name="message")
  async def message(self, ctx):
    #выдать всем пользователем сервера 0 count в message.json
    with open('message.json', 'r') as f:
        data = json.load(f)
    for member in ctx.guild.members:
        data[str(member.id)] = {}
        data[str(member.id)]['count'] = 0
    with open('message.json', 'w') as f:
        json.dump(data, f)
    await ctx.send("Всем пользователям было выдано 0 count")



  @commands.command(name="profile")
  async def profile(self, ctx, member: discord.Member = None):
    if ctx.channel.id == 1024734194817044611 or ctx.channel.id == 1024734194817044611 or ctx.channel.id == 1024734194817044611 or ctx.channel.id == 1025433152082161715:
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
      await ctx.message.delete()

  @commands.command(name="alldosh")
  async def alldosh(self, ctx):
    #добавить всем пользователей в dosh2.json с текстом dosh2 и значением 0
    with open('dosh2.json', 'r') as f:
        data = json.load(f)
    for member in ctx.guild.members:
      if str(member.id) not in data:
        data[str(member.id)] = {}
        data[str(member.id)]['dosh2'] = 0
    with open('dosh2.json', 'w') as f:
        json.dump(data, f)
  
  @commands.command(name="vudad")
  async def vudad(self, ctx):
    #изменять значение в dosh.json 300message вместо nahalo.jpg на almaz.jpg
    with open('dosh.json', 'r') as f:
        data = json.load(f)
    data[str(ctx.author.id)]['300message'] = "almaz.jpg"
    with open('dosh.json', 'w') as f:
        json.dump(data, f)

  
  @commands.command(name="test222")
  async def test222(self, ctx, member: discord.Member = None):
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
        color2 = (0,0,0)
      if color == "black":
        color2 = (255,255,255)
      if color == "green":
        color2 = (0,128,0)
      if color == "pink":
        color2 = (255,20,147)
      if color == "reset":
        color2 = (93,26,116)


      draw.rectangle(((280, 141), (267, 151)), fill=(color2))
      draw.rectangle(((312, 141), (298, 151)), fill=(color2))
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
      await ctx.message.delete()
  

def setup(client):
  client.add_cog(message(client))


