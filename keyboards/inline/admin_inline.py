from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# TODO: поменять названия кнопок
async def add_buttons_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text=("Подвердить отправку"), callback_data="confirm_send")
    btn2 = InlineKeyboardButton(text=("Добавить кнопку"), callback_data="add_buttons")
    btn3 = InlineKeyboardButton(text=("Отменить"), callback_data="cancel")

    markup.add(btn1, btn2, btn3)
    return markup

async def offer_confirm_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text=("Доставлен"), callback_data="confirm_send")
    btn2 = InlineKeyboardButton(text=("Ожидание"), callback_data="add_buttons")
    btn3 = InlineKeyboardButton(text=("Отменить"), callback_data="cancel")

    markup.add(btn1, btn2, btn3)
    return markup


async def confirm_with_button_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text=("Подвердить отправку"), callback_data="confirm_send_with_button")
    btn2 = InlineKeyboardButton(text=("Отменить"), callback_data="cancel")
    markup.add(btn1, btn2)
    return markup


async def tech_works_keyboard(tech_works: bool) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    set_up_tech_work = InlineKeyboardButton(text=_("Включить"), callback_data="set_up_tech_work")
    disable_technical_work = InlineKeyboardButton(text=_("Выключить"), callback_data="disable_tech_work")
    if tech_works:
        markup.add(disable_technical_work)
        return markup
    else:
        markup.add(set_up_tech_work)
        return markup
