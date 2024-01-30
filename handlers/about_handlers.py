from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentType, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.markdown import quote_html
from loguru import logger

from loader import dp, _, bot
from states.reg_state import RegData
from utils.db_api import db_commands
from functions.get_data_func import get_data
from utils.misc.profanityFilter import censored_message
from aiogram.types import Contact
import re
from states.states import Feedback

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.main_menu_inline import main_keyboard
from keyboards.default.params_default import about_keyboards


@dp.message_handler(text=["💼 О компании", "💼 Kompaniya haqida"])
async def feedback_func(message: types.Message):
    await message.answer(_("Выберите раздел ниже"), reply_markup=await about_keyboards())


@dp.message_handler(text=["🤳 Соц сети", "🤳 Ijtimoiy tarmoqlar"])
async def feedback_func(message: types.Message):
    await message.answer(_("Наши 🤳 Соц сети"))


@dp.message_handler(text=["🚛 Доставка", "🚛 Yetkazib berish"])
async def feedback_func(message: types.Message):
    await message.answer(_("Как работает наша 🚛 Доставка"))


@dp.message_handler(text=["🚀 Гарантия", ""])
async def feedback_func(message: types.Message):
    await message.answer(_("Наша гарантия 🚀 Гарантия"))




