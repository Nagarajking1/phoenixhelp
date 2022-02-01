import json
import os


def get_user_list(config, key):
    with open('{}/MashaRoBot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
  
    TEMP_DOWNLOAD_DIRECTORY = 'None'
    API_ID = 6246021
    API_HASH = "112a701ebaf8995ce35ba7ae4433eb4b"
    TOKEN = "2084060024:AAG2qH4BL9PXPKFnvmuIxwDjcKFJG-jLXEQ"
    OWNER_ID = 1417352329 
    OWNER_USERNAME = "jaihindupuram_king"
    SUPPORT_CHAT = 'PHOENIX_CHAT_TAMIL'
    JOIN_LOGGER = -1001547905195
    EVENT_LOGS =  -1001547905195

    ALLOW_CHATS = "True"
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "snRLLgUwXrwWw_2Qy8nmUbkmKfLf9IHH4rbNGM3PrWSk4XNt7EY~FgzJcEcAXcnL"  
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_ID = "2084060024"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 100  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAACAgUAAxkBAAEDyBVh-NMeDTdzKypJrfCYKTJAGOyLuwACTAUAAu-r0VW1EtKPPK-RqiME'  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'AS5LYK9Z7227QYCJ'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'QM8PH28330UD'  # Get your API key from https://timezonedb.com/api
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = '1bf1e6aecf90a6861d4d5876daefdb87c718a73f4b3168dce7cc86823ae89537e1212ebfb2bbd859ddb1cc7fce78f113130289273859cac0f4d4763f67de3fc6'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
