import requests
import random
from typing import Tuple, NoReturn
from aiogram.dispatcher import FSMContext

import numpy as np
from aiogram.types import CallbackQuery
from aiogram import types
from keyboards.inline.main_menu_inline import start_keyboard
from utils.db_api import db_commands
from states.reg_state import RegData

async def back(call: CallbackQuery) -> NoReturn:
        await call.message.delete()
        telegram_id = call.from_user.id
        user_db = await db_commands.select_user(telegram_id=telegram_id)
        markup = await start_keyboard(status=user_db['status'])   
        await call.message.answer("Меню 📙", reply_markup=markup)


async def back_admin_func(call: CallbackQuery,  state: FSMContext) -> NoReturn:
        await call.message.delete()
        await state.finish()
        await call.message.answer("Отмена рассылки")

