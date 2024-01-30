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

from keyboards.default.params_default import chose_offer

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


@dp.message_handler(text=["📍 Первая локация", "📍 Birinchi manzil"])
async def location_send(message: types.Message):

    latitude = 39.74030752056112
    longitude = 64.49503124187741

    await bot.send_location(message.chat.id, latitude, longitude)
    await message.answer(_(f"Первая локация"))


@dp.message_handler(text=["📍 Вторая локация", "📍 Ikkinchi manzil"])
async def location_send(message: types.Message):

    latitude = 39.74030752056112
    longitude = 64.49503124187741

    await bot.send_location(message.chat.id, latitude, longitude)
    await message.answer(_(f"Первая локация"))
