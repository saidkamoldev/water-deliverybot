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


@dp.message_handler()
async def feedback_func(message: types.Message):
    await message.answer(_("Команда не доступна, нажмите на /start чтобы увидеть меню"))
