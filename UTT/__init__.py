# Feel free to use

from os import system, getenv
from dotenv import load_dotenv
from pyrogram import Client as pClient, filters, enums
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from logging import basicConfig, getLogger, FileHandler, StreamHandler, INFO, ERROR

logger = getLogger(__name__)
getLogger("pyrogram").setLevel(ERROR)
load_dotenv('config.env', override=True)
basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', handlers=[FileHandler('logs.txt'), StreamHandler()], level=INFO)

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
OWNER_ID = getenv("OWNER_ID")
MONGODB_URL = getenv("MONGODB_URL")

if not BOT_TOKEN:
    logger.error("Please fill up BOT_TOKEN variable in config.env file.")
    exit(1)

if not API_ID:
    logger.error("Please fill up API_ID variable in config.env file.")
    exit(1)

if not API_HASH:
    logger.error("Please fill up API_HASH variable in config.env file.")
    exit(1)

if not OWNER_ID:
    logger.error("Please fill up OWNER_ID variable in config.env file.")
    exit(1)

if not MONGODB_URL:
    logger.error("Please fill up MONGODB_URL variable in config.env file.")
    exit(1)

bot = pClient("UTTBot", API_ID, API_HASH, bot_token=BOT_TOKEN, workers=1000, parse_mode=enums.ParseMode.MARKDOWN).start()
bot_start = time()
bot_loop = bot.loop
bot_username = bot.me.username
bot_scheduler = AsyncIOScheduler(event_loop=bot_loop)
