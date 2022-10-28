"""@Kaizuryu"""

from telethon import events, Button, custom
from SungJinWoo.events import register
from SungJinWoo import telethn as tbot
SungJinWoo = "https://telegra.ph/file/bb2ac197bafa9619450b1.jpg"
@register(pattern=("/alive"))
async def awake(event):
  STB = event.sender.first_name
  STB = "**I m SungJinWoo** \n\n" + "**I'm Working Properly**\n\n"
  STB += "**Python Version : 3.9.7**\n\n"
  STB += "**python-Telegram-Bot : 13.7**\n\n"
  BUTTON = [[Button.url("Support", "https://t.me/{SUPPORT_CHAT}"), Button.url("Updates", "https://t.me/{UPDATES_CHANNEL}")]]
  await tbot.send_file(event.chat_id, SungJinWoo, caption=STB,  buttons=BUTTON)

  # thanks to stb the gay
