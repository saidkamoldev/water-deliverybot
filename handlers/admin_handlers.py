from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.markdown import escape_md, quote_html
from loguru import logger
from utils.db_api import db_commands
import requests
from aiogram.types import CallbackQuery, ContentType, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from filters.is_admin_filter import IsAdmin
from functions.admin_func  import generate_password
from functions.back_functions import back_admin_func
import json
import random
from functions.get_data_func import get_data

from typing import Tuple, NoReturn

from keyboards.default.admin_default import admin_keyboard
from keyboards.inline.admin_inline import  confirm_with_button_keyboard, add_buttons_keyboard, tech_works_keyboard
from keyboards.inline.cancel_inline import cancel_keyboard
from loader import dp, bot
from datetime import date
from time import sleep  
import time
from states.states import NewItem, Purchace, Mailing
import secrets
import string
from states.states import Admin
current_datetime = date.today()

@dp.message_handler(IsAdmin(), Command("admin"))
async def admin_start(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)
    await state.finish()
    await message.reply(text=("Вы вошли на админ панел"), reply_markup=await admin_keyboard())
    

@dp.message_handler(IsAdmin(), text="Посчитать людей")
async def counter_show(message: types.Message):
    users = await db_commands.count_users()

    await message.answer(text=("Количество людей внутри бота: {users}\n").format(users=users))  

@dp.message_handler(IsAdmin(), text="ID фото")
async def counter_show(message: types.Message):
    await message.answer("Отпрвьте мне фотографию")
    await Admin.Photo.set()

    
@dp.message_handler(IsAdmin(), content_types=types.ContentType.PHOTO, state=Admin.Photo)
async def counter_show(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await message.answer(f"Ид этого фото  - {photo}")
    await state.finish()



@dp.message_handler(IsAdmin(), text="Рассылка")
async def broadcast_get_text(message: types.Message, state: FSMContext) -> None:
    await message.reply(text=("Пришлите текст для рассылки либо фото с текстом для рассылки! Чтобы отредактировать, "
                               "используйте встроенный редактор телеграма!\n"),
                        reply_markup=await cancel_keyboard())
    await state.set_state("broadcast_get_content")


@dp.message_handler(IsAdmin(), content_types=["text"], state="broadcast_get_content")
async def get_text_for_confirm(message: types.Message, state: FSMContext) -> None:
    text = message.md_text
    escape_md(text)
    await bot.send_message(chat_id=message.from_user.id, text=text,
                           parse_mode="MarkdownV2", reply_markup=await add_buttons_keyboard())
    await state.update_data(text=text)
    await state.set_state("broadcast_confirming")


@dp.callback_query_handler(state="broadcast_confirming")
async def broadcast_confirming(call: CallbackQuery, state: FSMContext) -> None:
    await call.message.edit_text(text=("Начинаю рассылку!"))
    chats = await db_commands.select_all_users()
    count = 0
    async with state.proxy() as data:
        text = data["text"]
        if call.data == "confirm_send":
            for i in chats:
                try:
                    await bot.send_message(chat_id=i.get('telegram_id'),
                                           text=text, parse_mode="MarkdownV2")
                    count += 1
                    await sleep(1)
                except Exception as err:
                    logger.error(
                        ("Сообщение не дошло в чат {chat} Причина: \n{err}").format(err=err,
                                                                                     chat=(i.get('telegram_id'))))

            await call.message.edit_text(
                text=("Рассылка проведена успешно! Ее получили: {count} чатов!\n").format(count=count))
            await state.reset_state(with_data=True)
        elif call.data == "add_buttons":
            await call.message.edit_text(text=("Пришлите мне название кнопки!"))
            await state.set_state("get_button_name")


@dp.message_handler(IsAdmin(), state="get_button_name")
async def get_button_name(message: types.Message, state: FSMContext) -> None:
    button_name = message.text
    await state.update_data(button_name=button_name)
    await message.reply(text=("Название кнопки принято! Теперь отправьте мне ссылку для этой кнопки!"))
    await state.set_state("get_button_url")


@dp.message_handler(IsAdmin(), state="get_button_url")
async def get_button_url(message: types.Message, state: FSMContext) -> None:
    button_url = message.text
    await state.update_data(button_url=button_url)
    async with state.proxy() as data:
        text = data["text"]
        button_name = data["button_name"]

    markup = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton(text=button_name, url=button_url)
    markup.add(btn)
    try:
        await message.answer(text=("Вот так будет выглядеть сообщение: \n\n"
                                    "{text}\n\n").format(text=text), reply_markup=markup,
                             parse_mode="Markdown")
        await message.answer(text=("Вы подтверждаете отправку?"),
                             reply_markup=await confirm_with_button_keyboard())
        await state.set_state("confirm_with_button_no_photo")
    except Exception as err:
        logger.error(err)
        await message.answer(text=("Произошла ошибка! Скорее всего, неправильно введена ссылка! "
                                    "Попробуйте еще раз."))


@dp.callback_query_handler(state="confirm_with_button_no_photo")
async def confirm_with_button_no_photo(call: CallbackQuery, state: FSMContext) -> None:
    chats = await db_commands.select_all_users()
    count = 0

    async with state.proxy() as data:
        text = data["text"]
        button_name = data["button_name"]
        button_url = data["button_url"]

        markup = InlineKeyboardMarkup(row_width=1)
        btn = InlineKeyboardButton(text=button_name, url=button_url)
        markup.add(btn)
        await call.message.edit_text(text=("Начинаю рассылку!"))
        for i in chats:
            try:
                await bot.send_message(chat_id=i.get('telegram_id'), reply_markup=markup,
                                       text=text, parse_mode="MarkdownV2")
                count += 1
                await sleep(1)
            except Exception as err:
                logger.error(
                    ("Сообщение не дошло в чат {chat} Причина: \n{err}").format(err=err,
                                                                                 chat=(i.get('telegram_id'))))

            await call.message.edit_text(
                text=("Рассылка проведена успешно! Ее получили: {count} чатов!\n").format(count=count))
        await state.reset_state(with_data=True)


@dp.message_handler(IsAdmin(), content_types=["photo"], state="broadcast_get_content")
async def get_photo_for_confirm(message: types.Message, state: FSMContext) -> None:
    text = message.md_text
    escape_md(text)
    quote_html(text)
    photo = message.photo[-1].file_id
    await message.answer_photo(caption=("Вот сообщение: \n\n{text}\n\n Вы подтверждаете отправку? "
                                         "Или хотите что-то добавить?").format(text=text),
                               photo=photo,
                               reply_markup=await add_buttons_keyboard(),
                               parse_mode="Markdown")
    await state.update_data(text=text)
    await state.update_data(photo=photo)
    await state.set_state("broadcast_confirming_photo")


@dp.callback_query_handler(state="broadcast_confirming_photo")
async def broadcast_confirming_photo(call: CallbackQuery, state: FSMContext) -> None:
    chats = await db_commands.select_all_users()
    count = 0
    async with state.proxy() as data:
        text = data["text"]
        photo = data["photo"]

        if call.data == "confirm_send":
            await call.message.answer(text="Начинаю рассылку!")
            for i in chats:
                try:
                    await bot.send_photo(chat_id=i.get('telegram_id'),
                                         caption=text, photo=photo, parse_mode="MarkdownV2")
                    count += 1
                    await sleep(1)
                except Exception as err:
                    logger.error(
                        ("Сообщение не дошло в чат {chat} Причина: \n{err}").format(err=err,
                                                                                     chat=(i.get('telegram_id'))))

                await call.message.edit_text(
                    text=("Рассылка проведена успешно! Ее получили: {count} чатов!\n").format(count=count))
            await state.reset_state(with_data=True)
        elif call.data == "add_buttons":
            await call.message.answer(text="Пришлите мне название кнопки!")
            await state.set_state("get_button_name_photo")


@dp.message_handler(IsAdmin(), state="get_button_name_photo")
async def get_button_name_photo(message: types.Message, state: FSMContext) -> None:
    button_name = message.text
    await state.update_data(button_name=button_name)
    await message.reply(text="Название кнопки принято! Теперь отправьте мне ссылку для этой кнопки!")
    await state.set_state("get_button_url_photo")


@dp.message_handler(IsAdmin(), state="get_button_url_photo")
async def get_button_url(message: types.Message, state: FSMContext) -> None:
    button_url = message.text
    await state.update_data(button_url=button_url)
    async with state.proxy() as data:
        text = data["text"]
        photo = data["photo"]
        button_name = data["button_name"]

    markup = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton(text=button_name, url=button_url)
    markup.add(btn)
    try:
        await message.answer(text=("Вот так будет выглядеть сообщение: \n\n"
                                    "{text}\n\n").format(text=text), reply_markup=markup,
                             parse_mode="Markdown")
        await message.answer(text=("Вы подтверждаете отправку?"),
                             reply_markup=await confirm_with_button_keyboard())
        await state.set_state("confirm_with_button_photo")
    except Exception as err:
        logger.error(err)
        await message.answer(text=("Произошла ошибка! Скорее всего, неправильно введена ссылка! "
                                    "Попробуйте еще раз."))


@dp.callback_query_handler(state="confirm_with_button_photo")
async def confirm_with_button_no_photo(call: CallbackQuery, state: FSMContext) -> None:
    chats = await db_commands.select_all_users()
    count = 0

    async with state.proxy() as data:
        text = data["text"]
        photo = data["photo"]
        button_name = data["button_name"]
        button_url = data["button_url"]

        markup = InlineKeyboardMarkup(row_width=1)
        btn = InlineKeyboardButton(text=button_name, url=button_url)
        markup.add(btn)
        await call.message.edit_text(text=("Начинаю рассылку!"))
        for i in chats:
            try:
                await bot.send_photo(chat_id=i.get('telegram_id'), photo=photo, reply_markup=markup,
                                     caption=text, parse_mode="MarkDown")
                count += 1
                await sleep(1)
            except Exception as err:
                logger.error(
                    ("Сообщение не дошло в чат {chat} Причина: \n{err}").format(err=err,
                                                                                 chat=(i.get('telegram_id'))))

            await call.message.edit_text(
                text=("Рассылка проведена успешно! Ее получили: {count} чатов!\n").format(count=count))
        await state.reset_state(with_data=True)

@dp.message_handler(IsAdmin(), text="Сообщение по id")
async def message_by_id_init(message: types.Message, state: FSMContext):
    await message.reply(text=_("Отправьте мне id получателя!"))
    await state.set_state("get_id_receiver")


@dp.message_handler(state="get_id_receiver")
async def get_id_receiver(message: types.Message, state: FSMContext):
    chat_id = message.text
    await state.update_data(chat_id=chat_id)
    await message.reply(text=_("ID принят! Теперь введите текст!"))
    await state.set_state("get_text_for_send")


@dp.message_handler(state="get_text_for_send")
async def get_text_for_send(message: types.Message, state: FSMContext):
    text = message.md_text
    escape_md(text)
    async with state.proxy() as data:
        chat_id = data["chat_id"]
        try:
            await bot.send_message(chat_id=chat_id, text=text, parse_mode="MarkDown")
            await message.reply(text=_("Сообщение успешно отправлено!"))
        except Exception as err:
            await message.reply(text=("Произошла нижеследующая ошибка!\n\n"
                                      "{err}").format(err=err))
            logger.error(err)

        await state.reset_state(with_data=True)

@dp.message_handler(IsAdmin(), text="Тех.Работа")
async def tech_works_menu(message: types.Message) -> None:
    settings = await db_commands.select_setting(message.from_user.id)
    tech_works = settings.get("technical_works")
    await message.answer(text=("Чтобы включить/выключить технические работы, нажмите на кнопку ниже"),
                         reply_markup=await tech_works_keyboard(tech_works))


@dp.callback_query_handler(text="set_up_tech_work")
async def set_up_tech_works(call: CallbackQuery) -> None:
    await db_commands.update_setting(telegram_id=call.from_user.id, technical_works=True)
    await call.message.edit_text(("Технические работы включены"))


@dp.callback_query_handler(text="disable_tech_work")
async def set_up_tech_works(call: CallbackQuery) -> None:
    await db_commands.update_setting(telegram_id=call.from_user.id, technical_works=False)
    await call.message.edit_text(("Технические работы выключены"))


