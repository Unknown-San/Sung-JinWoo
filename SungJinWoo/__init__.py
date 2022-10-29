"""@Kaizuryu"""

import logging
import os
import sys
import time
import spamwatch
import httpx
import telegram.ext as tg
from redis import StrictRedis

from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import MemorySession
from motor import motor_asyncio
from odmantic import AIOEngine
from pymongo import MongoClient
from Python_ARQ import ARQ
from aiohttp import ClientSession
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
from telegraph import Telegraph
from telegram import Chat
import pymongo

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.",
    )
    sys.exit(1)

ENV = bool(os.environ.get("ENV", True))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", 5531584953))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER",  -1001892260605)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "XtheAnonymous")

    try:
        DRAGONS = {int(x) for x in os.environ.get("DRAGONS", "").split()}
        DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "").split()}
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = {int(x) for x in os.environ.get("DEMONS", "").split()}
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = {int(x) for x in os.environ.get("WOLVES", "").split()}
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = {int(x) for x in os.environ.get("TIGERS", "").split()}
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get("INFOPIC", True))  # Info Pic (use True[Value] If You Want To Show In /info.)
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)  # G-Ban Logs (Channel) (-100)
    ERROR_LOGS = os.environ.get("ERROR_LOGS", None)  # Error Logs (Channel Ya Group Choice Is Yours) (-100)
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    ARQ_API_URL = os.environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = os.environ.get("ARQ_API_KEY", None)
    #URL="https://meow.herokuapp.com"
    PORT = int(os.environ.get("PORT", 8443)) 
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", 4665778)  # Bot Owner's API_ID (From:- https://my.telegram.org/auth)
    API_HASH = os.environ.get("API_HASH", "10e3ed833b0d09699973420d45359409")  # Bot Owner's API_HASH (From:- https://my.telegram.org/auth)
    DB_URL = os.environ.get('DB_URI','postgres://kukypeqz:xfHycQJ0uugi60F8Tdjc9pAST6d7YPzq@peanut.db.elephantsql.com/kukypeqz')  # Any SQL Database Link (RECOMMENDED:- PostgreSQL & elephantsql.com)
    DB_URL2 = os.environ.get("DATABASE_URL2")
    DONATION_LINK = os.environ.get("DONATION_LINK")  # Donation Link (ANY)
    LOAD = os.environ.get("LOAD", "").split()  # Don't Change
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()  # Don't Change
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))  # Don't Change
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))  # Use `True` Value
    WORKERS = int(os.environ.get("WORKERS", 8))  # Don't Change
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")  # Don't Change
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)  # Don't Change
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")  # Don't Change
    # CASH_API_KEY = os.environ.get("CASH_API_KEY", None)  # From:- https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)  # From:- https://timezonedb.com/api
    WALL_API = os.environ.get("WALL_API", None)  # From:- https://wall.alphacoders.com/api.php
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)  # From:- https://www.remove.bg/
   # OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", "")  # From:- https://openweathermap.org/api
    #GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)  # From:- http://genius.com/api-clients
    MONGO_DB_URL = os.environ.get("MONGO_DB_URL", "mongodb+srv://ok:lol@cluster1.udhzs7r.mongodb.net/?retryWrites=true&w=majority")  # MongoDB URL (From:- https://www.mongodb.com/)
    REDIS_URL = os.environ.get("REDIS_URL", None)  # REDIS URL (From:- Heraku & Redis)
    BOT_ID = int(os.environ.get("BOT_ID", 5417821247))  # Telegram Bot ID (EXP:- 1241223850)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "@SungJinSupport")  # Support Chat Group Link (Use @AnimeCorps || Dont Use https://t.me/AnimeCorps)
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "@SungJinUpdates")  # Updates channel for bot (Use @TheSoloMonarch instead of t.me//example)
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)  # Use @SpamWatchSupport
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)  # From https://t.me/SpamWatchBot
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@SungJinRobot")  # Bot Username
    # Telethon Based String Session (2nd ID) [ From https://repl.it/@SpEcHiDe/GenerateStringSession ]
    APP_ID = os.environ.get("APP_ID", None)  # 2nd ID
    APP_HASH = os.environ.get("APP_HASH", None)  # 2nd ID
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", True)  # Heroku App Name
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", True)  # Heroku API [From https://dashboard.heroku.com/account]
    # YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", True)
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)  # Don't Change
    BOT_NAME = os.environ.get("BOT_NAME", True)  # Name Of your Bot.4
    BOT_API_URL = os.environ.get('BOT_API_URL', "https://api.telegram.org/bot")
    MONGO_DB = "SungJinWoo"
    GOOGLE_CHROME_BIN = "/usr/bin/google-chrome"
    CHROME_DRIVER = "/usr/bin/chromedriver"
    
    try:
        BL_CHATS = {int(x) for x in os.environ.get("BL_CHATS", "").split()}
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

else:
    from SungJinWoo.config import Development as Config

    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = Config.JOIN_LOGGER
    OWNER_USERNAME = Config.OWNER_USERNAME
    ALLOW_CHATS = Config.ALLOW_CHATS
    try:
        DRAGONS = {int(x) for x in Config.DRAGONS or []}
        DEV_USERS = {int(x) for x in Config.DEV_USERS or []}
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = {int(x) for x in Config.DEMONS or []}
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = {int(x) for x in Config.WOLVES or []}
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = {int(x) for x in Config.TIGERS or []}
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    INFOPIC = Config.INFOPIC
    EVENT_LOGS = Config.EVENT_LOGS 
    ERROR_LOGS = Config.ERROR_LOGS
    WEBHOOK = Config.WEBHOOK
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    BOT_API_URL = Config.BOT_API_URL
    ARQ_API_URL = Config.ARQ_API_URL
    ARQ_API_KEY = Config.ARQ_API_KEY
    DB_URL = Config.DB_URL
    DB_URL2 =Config.DB_URL2
    DONATION_LINK = Config.DONATION_LINK
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
   # CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    WALL_API = Config.WALL_API
    MONGO_DB_URL = Config.MONGO_DB_URL
    MONGO_DB = Config.MONGO_DB
    REDIS_URL = Config.REDIS_URL
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    UPDATES_CHANNEL = Config.UPDATES_CHANNEL
    SPAMWATCH_SUPPORT_CHAT = "SpamWatchSupport"
    SPAMWATCH_API = Config.SPAMWATCH_API
    REM_BG_API_KEY = Config.REM_BG_API_KEY
  #  OPENWEATHERMAP_ID = Config.OPENWEATHERMAP_ID
    APP_ID = Config.APP_ID
    APP_HASH = Config.APP_HASH
    BOT_ID = Config.BOT_ID
    BOT_USERNAME = Config.BOT_USERNAME
    BOT_NAME = Config.BOT_NAME
    ALLOW_EXCL = Config.ALLOW_EXCL
    DEL_CMDS = Config.DEL_CMDS
   # GENIUS_API_TOKEN = Config.GENIUS_API_TOKEN
    # YOUTUBE_API_KEY = Config.YOUTUBE_API_KEY

    try:
        BL_CHATS = {int(x) for x in Config.BL_CHATS or []}
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")
        

DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(5306064258)

REDIS = StrictRedis.from_url(REDIS_URL, decode_responses=True)

try:
    REDIS.ping()
    LOGGER.info("Your redis server is now alive!")

except BaseException:
    raise Exception("Your redis server is not alive, please check again.")

finally:
   REDIS.ping()
   LOGGER.info("Your redis server is now alive!")


if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("[ERROR]: SpamWatch API key Is Missing! Recheck Your Config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("[ERROR]: Can't connect to SpamWatch!")


# Credits Logger
print("[SungJinWoo] SungJin Is Starting. | Kaizuryu Project | Licensed Under MIT.")
print("[SungJinWoo] Kawaii ! Successfully Connected With Kaizuryu HQ")
print("[SungJinWoo] Project Maintained By: @TheShadowArsenal")


print("[SungJinWoo]: Telegraph Installing")
telegraph = Telegraph()
print("[SungJin]: Telegraph Account Creating")
telegraph.create_account(short_name='SungJinWoo')
updater = tg.Updater(token=TOKEN, base_url=BOT_API_URL, workers=WORKERS, request_kwargs={"read_timeout": 10, "connect_timeout": 10}, use_context=True)           
print("[SungJin]: TELETHON CLIENT STARTING")
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)

dispatcher = updater.dispatcher
print("[SungJin]: PYROGRAM CLIENT STARTING")
session_name = TOKEN.split(":")[0]
pgram = Client(
    session_name,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
)
print("[SungJin]: Connecting To Kaizuryu HQ")
mongodb = MongoClient(MONGO_DB_URL, 27017)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URL)
db = motor[MONGO_DB]
engine = AIOEngine(motor, MONGO_DB)
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
print("[SungJin]: Connecting To Kaizuryu HQ • PostgreSQL Database")
#ubot = TelegramClient(StringSession(STRING_SESSION), APP_ID, APP_HASH)
print("[SungJin]: Connecting To Kaizuryu (t.me/Kaizuryu)")
timeout = httpx.Timeout(40)
http = httpx.AsyncClient(http2=True, timeout=timeout)


async def get_entity(client, entity):
    entity_client = client
    if not isinstance(entity, Chat):
        try:
            entity = int(entity)
        except ValueError:
            pass
        except TypeError:
            entity = entity.id
        try:
            entity = await client.get_chat(entity)
        except (PeerIdInvalid, ChannelInvalid):
            for pgram in apps:
                if pgram != client:
                    try:
                        entity = await pgram.get_chat(entity)
                    except (PeerIdInvalid, ChannelInvalid):
                        pass
                    else:
                        entity_client = pgram
                        break
            else:
                entity = await pgram.get_chat(entity)
                entity_client = pgram
    return entity, entity_client


apps = [pgram]
DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from SungJinWoo.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
