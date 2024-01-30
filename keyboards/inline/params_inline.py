
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


async def params_keyboards() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text=_("🇺🇿🇷🇺 Изменить язык "), callback_data="sheets")
    btn3 = InlineKeyboardButton(text=_("🔙 Назад"), callback_data="back")
    btn4 = InlineKeyboardButton(text=_("Выйти  🔑"), callback_data="disable")
    markup.add(btn1,btn4)

    markup.add(btn3)
    return markup

async def filials_keyboards() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text=_("📍 Первая локация "), callback_data="location1")
    btn2 = InlineKeyboardButton(text=_("📍 Вторая локация"), callback_data="location2")
    btn3 = InlineKeyboardButton(text=_("🔙 Назад"), callback_data="back")
    # btn4 = InlineKeyboardButton(text=("Повторная авторизация 🔑"), callback_data="disable")
    markup.add(btn1,btn2)
    markup.add(btn3)
    return markup


