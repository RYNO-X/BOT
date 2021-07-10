from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())

class Config(object):
    API_ID = os.environ.get("API_ID", default=None)
    API_HASH = os.environ.get("API_HASH", default=None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", default=None)
    REDIS_URI = os.environ.get("REDIS_URI", default=None)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", default=None)
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")

XXX = "1024855816"