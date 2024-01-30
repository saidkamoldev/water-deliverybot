import logging
import os
import django
from django_project.telegrambot.telegrambot import settings
from django.core.management import call_command

from aiogram import executor

from loader import dp, db, bot
import filters
# from functions.check_balance import check_and_notify
from utils.notify_admins import AdminNotification
import asyncio
import aioschedule
from utils.set_bot_commands import set_default_commands
import datetime
from colorama import init
init()
from colorama import Fore, Back, Style

from django_project.telegrambot.usersmanage.models import User, Offer,TimeBasedModel




# For run dataBase

# $ python django_app.py makemigrations
# $ python django_app.py migrate

async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет о запуске
    await AdminNotification.send(dispatcher)
    logging.info(f'Создаем подключение...')
    await db.create()
    logging.info(f'Подключение успешно!')
    logging.info(f'База загружена успешно!')


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "django_project.telegrambot.telegrambot.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()

    # Очишение базы данных
    call_command('flush', '--noinput')

# async def scheduler():
#     aioschedule.every(2).hours.do(check_and_notify)

#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(5)

# async def on_startup(_):
#     asyncio.create_task(scheduler())

if __name__ == '__main__':
    setup_django()
    import handlers



    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)