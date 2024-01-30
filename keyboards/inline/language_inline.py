from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _


async def language_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    ru = InlineKeyboardButton(text=_("🇷🇺 Русский"), callback_data="Russian")
    uz = InlineKeyboardButton(text=_("🇺🇿 Uzbek"), callback_data="Uzbek")
    markup.add(ru, uz)
    return markup
