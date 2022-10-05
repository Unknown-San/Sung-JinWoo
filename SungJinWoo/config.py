"""@Kaizuryu"""

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SungJinWoo/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):

    ##dont change
    LOGGER=True
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY="./"
    DEL_CMDS=False
    BAN_STICKER="kans" 
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="SungJinWoo"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot"

    #you can change these 
    INFOPIC=True #picture while doing /info
    STRICT_GBAN=True
    API_ID=681 ##api id from my.telegram.org
    APP_ID=6281 #same as API_ID
    API_HASH="45aabfacadsdsds" ##api hash from my.telegram.org
    APP_HASH="45aabfadsdsd" #same as API_HASH
    BL_CHATS=[1] #chats to be blacklisted
    MONGO_DB_URL="mongodb+srv://mesdsdwhidsdsgodb.net/?retryWrites=true&w=majority" ##mongo database link (necessary)
    DB_URL2="mongodb+srv://meowhisswswuj7.mongodb.net/?retryWrites=true&w=majority" #mongo db (not necessary)
    DB_URL="postgresql://wdsdsw@ldsas/wasassddb" #postgres sql database link
    REDIS_URL="redis://dsds3@reddsdsuth-1-1.ec2.cloud.redislabs.com:154dsd/Arssddsdsb" #redis database url from redislabs.com
    TOKEN="54dssdV8e59Odo" #bot token from @BotFather
    DEV_USERS=[5306064258] #developers id
    DRAGONS=[9656] #sudo users id
    DEMONS=[1909] #support user ids
    TIGERS=[1] #commas for multiple ids
    WOLVES=[2112, 1212] #commas for multiple ids 
    DONATION_LINK="https://www.paypal.me/PaulSonOfLars" #u can change with yours
    EVENT_LOGS=-100159 #channel id for gban logs
    JOIN_LOGGER=-1001523  #log channel/group id
    OWNER_ID=5306064258 #owner id in integer
    ERROR_LOGS=-1001 #support group id
    BOT_NAME="SungJinWoo" #your bot name
    ARQ_API_KEY="SLSFXSsdUXNSMH-ARQ" #ARQ api key from @ARQRobot
    ARQ_API_URL="arq.hamker.dev" #arq link
    SUPPORT_CHAT="Ignidsn" #support group username without @
    OWNER_USERNAME="arsshh" #owner username without @
    UPDATES_CHANNEL="Igsd" #Updates/News Channel username without @
    BOT_USERNAME="SungJinWoo_Robot" #bot username without @
    REM_BG_API_KEY="K2dsdsYma6cZx" #not necessary
    GENIUS_API_TOKEN="e-8UdRQNrIssPyM" # api token from genius.com (not necessary)
    TIME_API_KEY="QLLLDV7SWFD3" #not necessary
    SPAMWATCH_API="J968E_20LgxrKjsdN24cqYtD~gNRTbU" #spamwatch api token from @SpamWatchBot
    WALL_API="6950f5ds6a3" #wall api (not necessary)


class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True