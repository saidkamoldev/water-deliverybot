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
from keyboards.default.params_default import back_keyboard


chat_id = -4079630827

@dp.message_handler(text=["📖 Предложение и жалобы", "📖 Taklif va shikoyatlar"])
async def feedback_func(message: types.Message):
    await message.answer(_("Пожалуйста, напишите свой отзыв в ✍️ письменной форме. И мы свяжемся с Вами в ближайшее время. 😊"), reply_markup=await back_keyboard())
    await Feedback.Commentary.set()

@dp.message_handler(state=Feedback.Commentary)
async def feedback_func(message: types.Message, state: FSMContext):
    feedback = message.text
    await bot.send_message(chat_id, f"{feedback}")
    await message.answer(_("Ваше сообщение принято!"))
    await message.answer(_("Для заказа нажмите 🛍 Заказать."), reply_markup=await main_keyboard())
    await state.reset_state()


