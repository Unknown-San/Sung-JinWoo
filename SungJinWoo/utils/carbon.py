"""@Kaizuryu"""

from io import BytesIO
from SungJinWoo import aiohttpsession

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "SungJinWoo_Carbon.png"
    return image
