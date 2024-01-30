from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



async def cancel_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text=("Отменить"), callback_data="cancel")
    markup.add(btn1)
    return markup

async def back_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text=("Назад"), callback_data="back")
    markup.add(btn1)
    return markup
