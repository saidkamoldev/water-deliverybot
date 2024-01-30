
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _

async def address_send():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text=_("📍 Отправить гео-локацию "), request_location=True)
    btn3 = KeyboardButton(text=_("⬅️ Назад"))

    markup.row(btn1)
    markup.row(btn3)
    return markup


async def language_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    ru = InlineKeyboardButton(text=("🇷🇺 Русский"))
    uz = InlineKeyboardButton(text=("🇺🇿 Uzbek"))
    markup.add(uz, ru)
    return markup


async def chose_offer():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=_("🚙 Доставка"))
    btn2 = KeyboardButton(text=_("🏃 Самовывоз"))
    btn3 = KeyboardButton(text=_("⬅️ Назад"))
    markup.row(btn1, btn2)
    markup.row(btn3)
    return markup


async def params_keyboards():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=_("🇺🇿🇷🇺 Изменить язык "))
    btn3 = KeyboardButton(text=_("🔙 Назад"))
    btn4 = KeyboardButton(text=_("🔑 Повторная  авторизация"))
    markup.add(btn1,btn4)

    markup.add(btn3)
    return markup

async def filials_keyboards():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=_("📍 Первая локация "))
    btn2 = KeyboardButton(text=_("📍 Вторая локация"))
    btn3 = KeyboardButton(text=_("🔙 Назад"))
    markup.add(btn1,btn2)
    markup.add(btn3)
    return markup


async def about_keyboards() -> InlineKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=_("🤳 Соц сети "))
    btn2 = KeyboardButton(text=_("🚛 Доставка "))
    btn3 = KeyboardButton(text=_("🚀 Гарантия "))
    btn4 = KeyboardButton(text=_("🔙 Назад"))
    # btn4 = InlineKeyboardButton(text=("Повторная авторизация 🔑"), callback_data="disable")
    markup.add(btn1,btn2)
    markup.add(btn3, btn4)
    return markup

async def back_keyboard() -> InlineKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=_("🔙 Назад"))
    # btn4 = InlineKeyboardButton(text=("Повторная авторизация 🔑"), callback_data="disable")
    markup.add(btn1)
    return markup

