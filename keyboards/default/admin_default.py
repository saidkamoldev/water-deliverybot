from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from loader import _


async def admin_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text=("Рассылка"))
    btn2 = KeyboardButton(text=("Посчитать людей"))
    btn3 = KeyboardButton(text=("ID фото"))

    markup.row(btn1, btn2)
    markup.row(btn3)
    return markup

