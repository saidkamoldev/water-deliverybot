from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import _
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_keyboard(status) -> InlineKeyboardMarkup:
    try:
        if not status:
            markup = InlineKeyboardMarkup()
            ru = InlineKeyboardButton(text=_("🇷🇺 Русский"), callback_data="Russian")
            uz = InlineKeyboardButton(text=_("🇺🇿 Uzbek"), callback_data="Uzbek")
            markup.add(ru, uz)
            return markup
        else:
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            offer = KeyboardButton(text=_("🛍 Заказать"))
            settings = KeyboardButton(text=_("⚙️ Настройки"))
            socials = KeyboardButton(text=_("💼 О компании"))
            feedback = KeyboardButton(text=_("📖 Предложение и жалобы"))
            filials = KeyboardButton(text=_("📍 Наши филиалы"))
            support = KeyboardButton(text=_("☎️ Обратная связь"))
            markup.row(offer,filials )
            markup.row(feedback, socials)
            markup.add(support, settings)
            return markup
    except:
        print("error") 

async def main_keyboard() -> InlineKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    offer = KeyboardButton(text=_("🛍 Заказать"))
    settings = KeyboardButton(text=_("⚙️ Настройки"))
    socials = KeyboardButton(text=_("💼 О компании"))
    feedback = KeyboardButton(text=_("📖 Предложение и жалобы"))
    filials = KeyboardButton(text=_("📍 Наши филиалы"))
    support = KeyboardButton(text=_("☎️ Обратная связь"))
    markup.row(offer,filials )
    markup.row(feedback, socials)
    markup.add(support, settings)
    return markup
