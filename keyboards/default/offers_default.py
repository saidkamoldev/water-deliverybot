from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import _


async def chose_offer():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=_("💦 Вода TozaSuv"))
    btn2 = KeyboardButton(text=_("🚰 Куллеры TozaSuv"))
    btn3 = KeyboardButton(text=_("🗜 Помпы для воды"))
    btn4 = KeyboardButton(text=_("🔙 Назад"))

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    return markup

async def chose_kuler():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=_("💦 10kg"))
    btn2 = KeyboardButton(text=_("🚰 20kg"))
    btn3 = KeyboardButton(text=_("🗜 30kg"))
    btn4 = KeyboardButton(text=_("🗜 30kg"))
    btn5 = KeyboardButton(text=_("🔙 Назад"))

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)
    return markup

async def chose_type():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=_("💦 Toza Suv 5л"))
    btn2 = KeyboardButton(text=_("💦 Toza Suv 10л"))
    btn3 = KeyboardButton(text=_("💦 Toza Suv 18.5л"))
    btn4 = KeyboardButton(text=_("💦 Toza Suv 18.5л"))
    btn5 = KeyboardButton(text=_("🔙 Назад"))

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)
    return markup



async def select_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text=_("Пропустить ➡️"))
    markup.row(btn1)
    return markup


async def dostavka_location():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=("📍 Локаия 1"))
    btn2 = KeyboardButton(text=("📍 Локаия 2"))
    btn3 = KeyboardButton(text=("⬅️ Назад"))

    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    return markup

async def payments_type():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=_("💸 Наличными"))
    btn2 = KeyboardButton(text=_("💳 Click UP"))
    btn3 = KeyboardButton(text=_("💳 Терминал"))
    btn4 = KeyboardButton(text=_("⬅️ Назад"))

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    return markup

async def address_send_offer():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text=_("📍 Отправить гео-локацию "), request_location=True)
    btn2 = KeyboardButton(text=_("Пропустить ➡️"))
    btn3 = KeyboardButton(text=_("⬅️ Назад"))

    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    return markup



