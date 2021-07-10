import os
from datetime import datetime
from telethon import TelegramClient
from .config import Config
import time
from redis import ConnectionError, ResponseError, StrictRedis
from logging import DEBUG, INFO, FileHandler, StreamHandler, basicConfig, getLogger
from .config import Config

LOGS = getLogger(__name__)

if os.path.exists("logs.txt"):
    os.remove("logs.txt")

basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=INFO,
    handlers=[FileHandler("logs.txt"), StreamHandler()],
    )

LOGS.info(
    """
                        Booting Up Please Wait
    """
    )

if not Config.API_ID:
    LOGS.info("NO API_ID OR API_HASH FOUND")
    exit(1)


if not Config.BOT_TOKEN:
    LOGS.info("NO Bot Token Found")
    exit(1)

def connect_redis():
    yuvi = Config.REDIS_URI.split(":")
    op = StrictRedis(
        host=yuvi[0],
        port=yuvi[1],
        password=Config.REDIS_PASSWORD,
        charset="utf-8",
        decode_responses=True,
    )
    return op

try:
    db = connect_redis()
    LOGS.info("Connecting Db")
    time.sleep(6)
except ConnectionError as ce:
    LOGS.info(f"Error ~ {ce}")
    exit(1)
except ResponseError as re:
    LOGS.info(f"Error ~ {re}")
    exit(1)
except Exception as ex:
    LOGS.info(f"Error ~ {ex}")
    exit(1)

START_TIME = datetime.now()

try:
    db.ping()
except BaseException:
    ok = []
    LOGS.info("Can't connect to Database.... Restarting....")
    for x in range(1, 6):
        db = connect_redis()
        time.sleep(5)
        try:
            if db.ping():
                ok.append("ok")
                break
        except BaseException:
            LOGS.info(f"Database Connection Failed ...  Trying To Reconnect {x}/5 ..")
    if not ok:
        LOGS.info("Database Connection Failed.....")
        exit()
    else:
        LOGS.info("Reconnected To Server Succesfully")

LOGS.info("Succesfully Established Connection With DataBase.")

bot = TelegramClient('hunter', api_id=str(Config.API_ID), api_hash=Config.API_HASH).start(bot_token=Config.BOT_TOKEN)

PLUGINS = []