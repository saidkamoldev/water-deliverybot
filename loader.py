from typing import Any

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from data.config import load_config

from functions.language_ware import setup_middleware



from utils.db_api.postgres import Database

bot = Bot(token=load_config().tg_bot.token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()

scheduler = AsyncIOScheduler()


i18n = setup_middleware(dp)
_: Any = i18n.gettext
