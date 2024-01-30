from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentType, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.markdown import quote_html
from loguru import logger

from loader import dp, _
from states.reg_state import RegData
from utils.db_api import db_commands
from functions.get_data_func import get_data
from utils.misc.profanityFilter import censored_message
from aiogram.types import Contact
import re
from keyboards.inline.main_menu_inline import start_keyboard
from states.reg_state import RegData
from keyboards.default.params_default import address_send
from keyboards.inline.main_menu_inline import main_keyboard


def is_valid_phone_number(phone_number: str) -> bool:
    """
    Проверяет, что номер телефона соответствует допустимому формату.
    Допустимый формат: содержит только цифры и знак "+", длина не более 13 символов.
    """
    if not phone_number:
        return False

    # Проверяем формат номера с использованием регулярного выражения
    pattern = r'^\+?[0-9]+$'
    if re.match(pattern, phone_number) and len(phone_number) <= 13:
        return True
    return False

# Обрабатываем нажатия кнопок для изменения языка
@dp.callback_query_handler(text="Russian")
@dp.callback_query_handler(text="Uzbek")
async def change_language(call: CallbackQuery, state: FSMContext):
    telegram_id = call.from_user.id
    language = call.data

    # Обновляем язык пользователя в базе данных

    if language == "Russian":
        button_send_number = KeyboardButton('Отправить номер 📲', request_contact=True)
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_send_number)

        await call.message.answer("Отправьте или введите свой номер телефона 👇  в виде:\n<b>+998 ** *** ****</b>", reply_markup=keyboard)
        await db_commands.update_user_data(telegram_id=telegram_id, language="ru")

    elif language == "Uzbek":
        button_send_number = KeyboardButton('Raqamni uzatish 📲', request_contact=True)
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_send_number)

        await call.message.answer("Telefon raqamingizni quyidagi tarzda 👇 yuboring yoki kiriting:\n<b>+998 ** *** ****</b> ", reply_markup=keyboard)
        await db_commands.update_user_data(telegram_id=telegram_id, language="uz")


    await RegData.Phone.set()

@dp.message_handler(content_types=[ContentType.CONTACT, ContentType.TEXT], state=RegData.Phone)
async def commentary_reg(message: types.Message, state: FSMContext):
    user_db = await db_commands.select_user(telegram_id=message.from_user.id)
    markup = await start_keyboard(status=user_db["status"])
    telegram_id = message.from_user.id

    if message.content_type == ContentType.CONTACT:
        contact = message.contact
        phone_number = contact.phone_number
    elif message.content_type == ContentType.TEXT:
        phone_number = message.text

    # Проверяем формат номера
    if is_valid_phone_number(phone_number):
        censored = censored_message(phone_number)
        await db_commands.update_user_data(phone=quote_html(censored), telegram_id=message.from_user.id)
        user_data = await get_data(telegram_id)

        await message.answer(_(f"Отправьте свою гео-локцию, с помощью кнопки"), reply_markup=await address_send())
        await RegData.Location.set()
    else:
        await message.answer(_("Неверный формат номера. Пожалуйста, введите корректный номер телефона."))

@dp.message_handler(content_types=[ContentType.LOCATION], state=RegData.Location)
async def commentary_reg(message: types.Message, state: FSMContext):
    location = message.location
    await message.answer(_(f"Авторизация прошла успешно! Поздравляем! 🎉"), reply_markup=ReplyKeyboardRemove())
    await message.answer(_(f"Выберите раздел ниже ⤵️"), reply_markup=await main_keyboard())
    await db_commands.update_user_data(status=True, telegram_id=message.from_user.id)
    await db_commands.update_user_data(location=location, telegram_id=message.from_user.id)
    await state.finish()


