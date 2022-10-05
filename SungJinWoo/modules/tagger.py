"""@Kaizuryu"""

from telethon.tl.types import ChannelParticipantsAdmins

from SungJinWoo import telethn, BOT_NAME
from SungJinWoo.events import register as SungJinWoo



@SungJinWoo(pattern="^/tagall ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = f"Hi Friends I'm {BOT_NAME} Let's be friends?"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


@SungJinWoo(pattern="^/users ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Users : "
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


__mod_name__ = "Tagger"
__help__ = """
 ⫸ /tagall: Mention All Members
Exp:- /tagall <Text> or <reply>

Alternative command: /mentionall

Note:- This `/tagall` Command can mention members upto 10,000 in groups and can mention members upto 200 in channels !
"""
