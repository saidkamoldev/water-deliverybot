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
from aiogram.types import CallbackQuery, ContentType, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

from keyboards.inline.language_inline import language_keyboard
from keyboards.inline.cancel_inline import back_keyboard
from keyboards.default.params_default import filials_keyboards, params_keyboards , language_keyboard

@dp.message_handler(text=["📍 Наши филиалы", "📍 Bizning filiallarimiz"])
async def filials_func(message: types.Message):
    await message.answer(_(f"Выберите филиал:"), reply_markup=await filials_keyboards())

@dp.message_handler(text={"☎️ Обратная связь", "☎️ Fikr-mulohaza"})
async def counter_show(message: types.Message):
    await message.answer(_("📲 Единый call-центр: 7777 или (77) 777-77-77"))
    

@dp.message_handler(text=["⚙️ Настройки", "⚙️ Sozlamalar"])
async def counter_show(message: types.Message):
    await message.answer(_("Выберите действие:"), reply_markup=await params_keyboards())


@dp.message_handler(text=["🇺🇿🇷🇺 Изменить язык", "🇺🇿🇷🇺 tilni o`zgartirish"])
async def counter_show(message: types.Message):
    await message.answer(_("Выберите язык::"), reply_markup=await language_keyboard())

@dp.message_handler(text=["🔑 Повторная  авторизация", "🔑 Qayta ro`yxatdan o`tish"])
async def counter_show(message: types.Message):
    await db_commands.delete_user(telegram_id=message.from_user.id)
    await message.answer(("Для повторный  авторизации нажмите на /start"), reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="🇷🇺 Русский")
async def counter_show(message: types.Message):
    await db_commands.update_user_data(telegram_id=message.from_user.id, language="ru")
    await message.answer(_("Выберите действие:"), reply_markup=await params_keyboards())

@dp.message_handler(text="🇺🇿 Uzbek")
async def counter_show(message: types.Message):
    await db_commands.update_user_data(telegram_id=message.from_user.id, language="uz")
    await message.answer(_("Выберите действие:"), reply_markup=await params_keyboards())

