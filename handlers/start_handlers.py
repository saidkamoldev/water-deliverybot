import asyncio
import random

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import BadRequest

from data.config import load_config
from filters import IsPrivate
from handlers.back_handler import delete_message

from keyboards.inline.main_menu_inline import start_keyboard
from loader import dp, scheduler, _
from utils.db_api import db_commands

from keyboards.inline.language_inline import language_keyboard

@dp.message_handler(IsPrivate(), CommandStart())
async def register_user(message: types.Message):
    try:
        if message.from_user.username is not None:
            await db_commands.add_user(name=message.from_user.full_name,
                                       telegram_id=message.from_user.id,
                                       username=message.from_user.username)

        else:
            await db_commands.add_user(name=message.from_user.full_name,
                                       telegram_id=message.from_user.id,
                                       username="None")
    except:
        pass
    # support = await db_commands.select_user(telegram_id=load_config().tg_bot.support_ids[0])
    user_db = await db_commands.select_user(telegram_id=message.from_user.id)
    markup = await start_keyboard(status=user_db["status"])
    fullname = message.from_user.full_name

    heart = random.choice(['💙', '💚', '💛', '🧡', '💜', '🖤', '❤', '🤍', '💖', '💝'])
    await message.answer_photo(photo="AgACAgIAAxkBAAIHNmUf4UFhnZm25H8XV8IVOoRbaEzgAAJuzzEbDAwAAUkd4gs5XoEPDQEAAwIAA3kAAzAE", caption=_("Привет, {fullname} 👋\n\n"
                            "Добро пожаловать в наш бот TozaSuv  \n").format(fullname=fullname),
                                     reply_markup=markup)

