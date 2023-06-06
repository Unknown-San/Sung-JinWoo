"""@Kaizuryu"""

import requests
from telethon import events
from SungJinWoo import telethn as meow

@meow.on(events.NewMessage(pattern="^/cosplay"))
async def waifu(event):
  r = requests.get("https://sugoi-api.vercel.app/cosplay").json()['url']
  await event.reply(file=r)
  
@meow.on(events.NewMessage(pattern="^/lewd"))
async def waifu(event):
  r = requests.get("https://sugoi-api.vercel.app/ncosplay").json()['url']
  await event.reply(file=r)

__mod_name__ = "Cosplay"
__help__ = """
Just a weeb type module to get anime cosplay and lewd pictures
- /cosplay
- /lewd
"""
