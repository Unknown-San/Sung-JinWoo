"""@Kaizuryu"""

from SungJinWoo.events import register 
import requests

@register(pattern="[/!]dare")
async def dare(event):
  gay = requests.get("https://api.truthordarebot.xyz/v1/dare").json()
  dare = gay["question"] 
  BRUH = "{}"
  await event.reply(BRUH.format(dare)) 
  
  
@register(pattern="[/!]truth")
async def truth(event):
  gae = requests.get("https://api.truthordarebot.xyz/v1/truth").json()
  truth = gae["question"] 
  BRAH = "{}"
  
  await event.reply(BRAH.format(truth)) 
  
  # thanks stb gae
