"""@Kaizuryu"""

import os
import urllib
import random
import requests

from SungJinWoo import telethn as meow
from requests import get
from telethon import events

import logging

logging.basicConfig(level=logging.DEBUG)

MemesReddit = [
    "Animemes", "lostpause", "LoliMemes", "cleananimemes",
    "animememes", "goodanimemes", "AnimeFunny", "dankmemes",
    "teenagers", "shitposting", "Hornyjail", "wholesomememes",
    "cursedcomments"
]

@meow.on(events.NewMessage(pattern="^/memes"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = f"https://meme-api.herokuapp.com/gimme/{memereddit}"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/dank"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/dankmemes"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e) 

@meow.on(events.NewMessage(pattern="^/lolimeme"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/LoliMemes"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)   

@meow.on(events.NewMessage(pattern="^/hornyjail"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/Hornyjail"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/wmeme"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/wholesomememes"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/pewds"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/PewdiepieSubmissions"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/hmeme"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/hornyresistance"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/teen"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/teenagers"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/fbi"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/FBI_Memes"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)

@meow.on(events.NewMessage(pattern="^/shitposting"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/shitposting"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)


@meow.on(events.NewMessage(pattern="^/cursed"))
async def mimi(event):
    try:
        memereddit = random.choice(MemesReddit)
        meme_link = "https://meme-api.herokuapp.com/gimme/cursedcomments"
        q = requests.get(meme_link).json()
        await event.reply(q["title"], file=q["url"])
        
    except Exception as e:
        print(e)

__help__ = """
Memes help you get through tough times, enjoy memes with our funny and horny memes

Usage:
- /memes Will give you mixed memes
- /wmeme Will give you wholesome memes
- /dank Provides dank memes
- /cursed Cursed memes
- /shitposting Random shitposts
- /fbi FBI Memes
- /teen Teenagers meme
- /hmeme Horny Memes
- /pewds Pewdiepie Collection
- /hornyjail Onichan Arrested :p
- /lolimeme Loli Memes (**fbi locating**)
"""

__mod_name__ = "Memes"