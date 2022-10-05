"""@Kaizuryu"""

import requests
from SungJinWoo.events import register
from telethon import Button

@register(pattern="[/!]ud")
async def ud_(e):
    try:
        text = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await e.reply("Invalid Args")
    results = requests.get(
        f"https://api.urbandictionary.com/v0/define?term={text}").json()
    try:
        reply_txt = f'<bold>{text}</bold>\n\n{results["list"][0]["definition"]}\n\n<i>{results["list"][0]["example"]}</i>'
    except:
        reply_txt = "No results found."
    await e.reply(reply_txt, buttons=Button.url("🔎 Google it!", f"https://www.google.com/search?q={text}"), parse_mode="html")
   
