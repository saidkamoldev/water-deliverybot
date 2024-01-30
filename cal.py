from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.types import CallbackQuery

API_TOKEN = '6913020318:AAErFEShNPRwHm4L2Qo-i1HO6w1V3hnYJUY'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.callback_query_handler(text="subscribe_year")
async def subscribe_1(call: CallbackQuery):
    # Bu funksiya "subscribe_year" so'rovnoma kelganda ishlaydi
    # call obyektida so'rovnoma va foydalanuvchi ma'lumotlari mavjud
    # Ushbu funksiya kerakli vazifani bajaradi
    user_id = call.from_user.id
    await bot.send_message(user_id, "Salom! Siz subscribe_year tugmasini bosdingiz!")

if __name__ == '__main__':
    from aiogram import executor

    # Polling or webhook, depending on the configuration settings
    executor.start_polling(dp, skip_updates=True)
