"""@Kaizuryu"""

# thanks to inrajith for meow meow meow
import os

from pyrogram import filters
from pyrogram.types import Message
from SungJinWoo.core.sections import section

from SungJinWoo import pgram
from telegram import ParseMode


async def get_chat_info(chat, already=False):
    if not already:
        chat = await pgram.get_chat(chat)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    type_ = chat.type
    is_scam = chat.is_scam
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    link = f"[Link](t.me/{username})" if username else "Null"
    total = ""
    for m in await pgram.get_chat_members(chat.id, filter="administrators"):
        total += f"• [{m.user.first_name}](tg://user?id={m.user.id})\n"
    dc_id = chat.dc_id
    photo_id = chat.photo.big_file_id if chat.photo else None
    body = {
        "ID:": chat_id,
        "DC:": dc_id,
        "Type:": type_,
        "Name:": [title],
        "Username:": [("@" + username) if username else "Null"],
        "Mention:": [link],
        "Members:": members,
        "Scam:": is_scam,
        "Restricted:": is_restricted,
        "\nDescription:\n\n": [description],
        "\nAdmins List:\n" : [total],
        
    }
    caption = section("Chat Info:\n", body)
    return [caption, photo_id]



@pgram.on_message(filters.command("ginfo"))
async def chat_info_func(_, message: Message):
    try:
        if len(message.command) > 2:
            return await message.reply_text(
                "**Usage:**/ginfo [USERNAME|ID]"
            )

        if len(message.command) == 1:
            chat = message.chat.id
        elif len(message.command) == 2:
            chat = message.text.split(None, 1)[1]

        m = await message.reply_text("Processing")
        

        info_caption, photo_id = await get_chat_info(chat)
        if not photo_id:
            return await m.edit(info_caption, disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)

        photo = await pgram.download_media(photo_id)
        await message.reply_photo(photo, caption=info_caption, quote=False, parse_mode=ParseMode.MARKDOWN)

        await m.delete()
        os.remove(photo)
    except Exception as e:
        await m.edit(e),
        parse_mode=ParseMode.MARKDOWN