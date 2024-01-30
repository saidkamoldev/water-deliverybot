import random
from contextlib import suppress

import aiogram.utils.exceptions
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from data.config import load_config
from keyboards.inline.main_menu_inline import start_keyboard
from loader import dp, _
from utils.db_api import db_commands


from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

async def delete_message(message: types.Message):
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()


@dp.message_handler(text=["🔙 Назад", "🔙 orqaga"], state="*")
@dp.message_handler(text="⬅️ Назад", state="*")
async def counter_show(message: types.Message, state: FSMContext):
    await state.finish()
    user_db = await db_commands.select_user(telegram_id=message.from_user.id)
    markup = await start_keyboard(status=user_db["status"])
    await message.answer(_(f"Выберите раздел:"), reply_markup=markup)
    

@dp.callback_query_handler(text="back", state="*")
async def open_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await delete_message(call.message)
    heart = random.choice(['💙', '💚', '💛', '🧡', '💜', '🖤', '❤', '🤍', '💖', '💝'])
    user_db = await db_commands.select_user(telegram_id=call.from_user.id)
    markup = await start_keyboard(status=user_db['status'])
    support = await db_commands.select_user(telegram_id=load_config().tg_bot.support_ids[0])
    fullname = call.from_user.full_name
    try:
        await call.message.edit_text(("Привет, {fullname}!!\n\n"
                           " <b>Добро пожаловать в корпоративный бот компании <b> CROSSGIF </b> \n"
                           "\n\n").format(fullname=fullname),
                                     reply_markup=markup)

    except aiogram.utils.exceptions.BadRequest:
        await delete_message(call.message)

        await call.message.answer(("Привет, {fullname}!!\n\n"
                           "Добро пожаловать в корпоративный бот компании <b> CROSSGIF </b> \n").format(fullname=fullname),
                                     reply_markup=markup)

@dp.callback_query_handler(text="back_with_delete")
async def open_menu(call: CallbackQuery) -> None:
    user_db = await db_commands.select_user(telegram_id=call.from_user.id)
    heart = random.choice(['💙', '💚', '💛', '🧡', '💜', '🖤', '❤', '🤍', '💖', '💝'])
    markup = await start_keyboard(status=user_db['status'])
    support = await db_commands.select_user(telegram_id=load_config().tg_bot.support_ids[0])
    fullname = call.from_user.full_name
    text = _("Привет, {fullname}!!\n\n"
                           "Добро пожаловать в корпоративный бот компании <b> CROSSGIF </b> \n").format(fullname=fullname)
    try:
        await call.message.edit_text(text,
                                     reply_markup=markup)

    except aiogram.utils.exceptions.BadRequest:
        await delete_message(call.message)

        await call.message.answer(text,
                                  reply_markup=markup)


@dp.callback_query_handler(text="back_to_reg_menu")
@dp.callback_query_handler(text="back_to_profile_menu")
async def event_back_handler(call: CallbackQuery) -> None:
    if call.data == "back_to_reg_menu":
        await registration_menu(call, scheduler, send_message_week, load_config, random)
    elif call.data == "back_to_profile_menu":
        telegram_id = call.from_user.id
        await delete_message(call.message)
        user_db = await db_commands.select_user(telegram_id=telegram_id)
        markup = await get_profile_keyboard(verification=user_db["verification"])
        await display_profile(call, markup)




@dp.callback_query_handler(text="go_out", state="cancel_record")
@dp.callback_query_handler(text="event_menu")
async def event_profile_back(call: CallbackQuery, state: FSMContext) -> None:
    await state.finish()
    await delete_message(call.message)
    await view_meetings_handler(call)


@dp.callback_query_handler(text="cancel", state="*")
async def back_push(call: CallbackQuery,state: FSMContext ) -> None:
    await state.finish()
    await delete_message(call.message)
    await call.message.answer("Вы отменили рассылку")

# @dp.callback_query_handler(text="cancel", state="broadcast_get_content")
# async def back_push(call: CallbackQuery,state: FSMContext ) -> None:
#     await state.finish()
#     await delete_message(call.message)
#     await call.message.answer("Вы отменили рассылку")

# @dp.callback_query_handler(text="cancel", state="broadcast_confirming")
# async def back_push(call: CallbackQuery,state: FSMContext ) -> None:
#     await state.finish()
#     await delete_message(call.message)
#     await call.message.answer("Вы отменили рассылку")

