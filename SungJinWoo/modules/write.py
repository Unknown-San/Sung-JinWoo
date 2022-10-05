"""@Kaizuryu"""

from SungJinWoo.events import register
from io import BytesIO
from requests import get
from telethon import events

@register(pattern="^/write")
async def writer(m: events.NewMessage):
    if not m.reply_to_msg_id:
        text: str = (
            m.text.split(None, 1)[1]
            if len(m.text) < 3
            else m.text.split(None, 1)[1].replace(" ", "%20")
        )
        var: str = await m.reply("`Waitoo...`")
        with BytesIO(get(f"https://apis.xditya.me/write?text={text}").content) as file:
            file.name: str = "image.jpg"
            await m.reply(file=file)
        await var.delete()
        
    else:
        reply: str = (await m.get_reply_message()).text
        text = reply.split(" ")[1].replace(" ", "%20")
        var: str = await m.reply("`Waitoo...`")
        with BytesIO(get(f"https://apis.xditya.me/write?text={text}").content) as file:
            file.name: str = "image.jpg"
            await m.reply(file=file)
        await var.delete()


__mod_name__ = "Hand Write"

__help__ = """
Writes the given text on white page with a pen 🖊

/write <text> *:* Writes the given text.
 """