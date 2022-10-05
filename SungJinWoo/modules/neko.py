"""@Kaizuryu"""

import html
import random

from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import SungJinWoo.modules.nekostrings as nekostrings
from SungJinWoo import dispatcher
from SungJinWoo.modules.disable import DisableAbleCommandHandler
from SungJinWoo.modules.helper_funcs.extraction import extract_user



@run_async
def nyaa(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message or message

    curr_user = html.escape(message.from_user.first_name)
    if user_id := extract_user(message, args):
        neko_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(neko_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    nyaa_type = random.choice(("Text", "Gif"))
    if nyaa_type == "Gif":
        try:
            temp = random.choice(nekostrings.NEKO_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            nyaa_type = "Text"

    if nyaa_type == "Text":
        temp = random.choice(nekostrings.NEKO_TEXT)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)




@run_async
def meow(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message or message

    curr_user = html.escape(message.from_user.first_name)
    if user_id := extract_user(message, args):
        meow_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(neko_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    meow_type = random.choice(("Text", "Gif"))
    if meow_type == "Gif":
        try:
            temp = random.choice(nekostrings.CATTO_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            nyaa_type = "Text"

    if meow_type == "Text":
        temp = random.choice(nekostrings.CATTO_TEXT)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

__help__ = """
 • /nyaa*:* Use this to get cute Neko/Catto Gifs!
 • /meow*:* Works same as above!
"""


NYAA_HANDLER = DisableAbleCommandHandler("nyaa", nyaa)
MEOW_HANDLER = DisableAbleCommandHandler("meow", meow)


dispatcher.add_handler(NYAA_HANDLER)
dispatcher.add_handler(MEOW_HANDLER)

__mod_name__ = "Neko"

__command_list__ = [
       "nyaa", "meow"
]
__handlers__ = [
       NYAA_HANDLER, MEOW_HANDLER
]
