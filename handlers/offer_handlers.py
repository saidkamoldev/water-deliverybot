from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentType, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.markdown import quote_html
from loguru import logger

from loader import dp, _, bot
from states.reg_state import RegData
from utils.db_api import db_commands
from functions.get_data_func import get_data
from utils.misc.profanityFilter import censored_message
from aiogram.types import Contact
import re

from keyboards.default.params_default import chose_offer, back_keyboard

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from keyboards.default.offers_default import chose_offer, chose_type, select_keyboard, payments_type, address_send_offer, chose_kuler
from states.states import Order, Kuller
from django_project.telegrambot.usersmanage.models import Offer
from keyboards.inline.main_menu_inline import main_keyboard
# from keyboards.inline.admin_inline import offer_confirm_keyboard
import datetime
import asyncio
import json

home_img = "AgACAgIAAxkBAAIHNmUf4UFhnZm25H8XV8IVOoRbaEzgAAJuzzEbDAwAAUkd4gs5XoEPDQEAAwIAA3kAAzAE"

chat_id = -4079630827


water_quantity = {}
# Константы для состояний
SELECT_WATER, SELECT_QUANTITY = range(2)

@dp.message_handler(text=["🛍 Заказать","🛍 Yektazib berish"])
async def order(message: types.Message):
    await message.answer(_("Выберите раздел ниже ⤵️"), reply_markup=await chose_offer())


@dp.message_handler(text=["🚰 Куллеры TozaSuv", "🚰 Kulerlar TozaSuv"])
async def order(message: types.Message):
    await message.answer(_("Выберите раздел ниже ⤵️"), reply_markup=await chose_kuler())
    await Kuller.ChoseKuller.set()

@dp.message_handler(state=Kuller.ChoseKuller)
async def order(message: types.Message,state: FSMContext):
    product = message.text
    await message.answer((f"{product} suv bu"), reply_markup=await back_keyboard())
    await message.answer_location()
    await state.finish()

@dp.message_handler(text=["🗜 Помпы для воды", "🗜 Suv uchun pompa"])
async def order(message: types.Message):
    await message.answer(_("Выберите раздел ниже ⤵️"), reply_markup=await chose_kuler())
    await Kuller.ChosePompa.set()

@dp.message_handler(state=Kuller.ChosePompa)
async def order(message: types.Message,state: FSMContext):
    product = message.text
    await message.answer((f"{product} Pompa bu"), reply_markup=await back_keyboard())
    await state.finish()


@dp.message_handler(text=["💦 Вода TozaSuv", "💦 Toza TozaSuv"])
async def order_water(message: types.Message):

    await message.answer_photo(photo=home_img,  caption=_(
    "<b>Максимальная Очистка: 🌟</b> TozaSuv - это 9 степеней очистки, чтобы каждая капля воды была чистой и свежей, как утренний роса.\n\n"
    "<b>Озонирование для Здоровья: 💧</b> Мы обогатили TozaSuv озоном, чтобы ваша вода была не только чистой, но и полезной. Это ваш дополнительный заряд энергии и здоровья в каждой бутылке.\n\n"
    "<b>Бесплатная Доставка: 🚚</b> И самое лучшее - мы доставляем TozaSuv прямо к вам! Наслаждайтесь чистой водой, не переживая за доставку."
    "<b>Без Усилий: 🌆</b> Независимо от этажа, TozaSuv легко поднимется к вам. Мы заботимся о вашем комфорте и гарантируем, что вы всегда будете иметь доступ к нашей воде.\n\n"
    "<b>Выберите объем для оформление заказа ⏬</b>"
    ), reply_markup=await chose_type())
    await Order.CategoryChoice.set()

caption = ""
photo = ""
@dp.message_handler(state=Order.CategoryChoice)
async def order_category(message: types.Message, state: FSMContext):
    product = message.text
    offer = Offer()
    offer.product = product

    global caption
    global photo
    if product == _("💦 Toza Suv 5л"):
        caption = _("<b>💦 Toza Suv 5л</b>\n\n"
        "<b>Цена:</b> 10.000 сум \n\n"
        "🌟 Toza Suv - вода высшего качества, которую вы заслуживаете! Насладитесь каждой каплей свежести и чистоты.\n\n"
        "💧 Наша вода прошла 9 степеней очистки, чтобы быть идеально чистой. Это здорово, верно?\n\n"
        "🚚 И вы знаете, что лучшее? Мы бесплатно доставим TozaSuv прямо к вам, чтобы вы могли наслаждаться без забот о доставке.\n\n"
        "🌆 А касательно этажей, независимо от этажа, TozaSuv легко дойдет до вас. Всегда доступно и удобно!\n\n"
        "Попробуйте Toza Suv и почувствуйте разницу! 💦")
        photo = "AgACAgIAAxkBAAIHUGUf6MWiRXQo3Wp38eeUDvgZuP4UAAKXzzEbDAwAAUne6klEjbT_CwEAAwIAA20AAzAE"
    elif product == _("💦 Toza Suv 10л"):
        caption = _("<b>💦 Toza Suv 10л</b>\n\n"
        "<b>Цена:</b> 15.000 сум \n\n"
        "🌟 Toza Suv - вода высшего качества, которую вы заслуживаете! Насладитесь каждой каплей свежести и чистоты.\n\n"
        "💧 Наша вода прошла 9 степеней очистки, чтобы быть идеально чистой. Это здорово, верно?\n\n"
        "🚚 И вы знаете, что лучшее? Мы бесплатно доставим TozaSuv прямо к вам, чтобы вы могли наслаждаться без забот о доставке.\n\n"
        "🌆 А касательно этажей, независимо от этажа, TozaSuv легко дойдет до вас. Всегда доступно и удобно!\n\n"
        "Попробуйте Toza Suv и почувствуйте разницу! 💦")
        photo = "AgACAgIAAxkBAAIHgWUf67Z-czAzMwPCSTIX_db-MRnrAAKmzzEbDAwAAUnb3mJoYQp06gEAAwIAA3gAAzAE"
    elif product == _("💦 Toza Suv 18.5л"):
        caption = _("<b>💦 Toza Suv 18.5л</b>\n\n"
        "<b>Цена:</b> 20.000 сум \n\n"
        "🌟 Toza Suv - вода высшего качества, которую вы заслуживаете! Насладитесь каждой каплей свежести и чистоты.\n\n"
        "💧 Наша вода прошла 9 степеней очистки, чтобы быть идеально чистой. Это здорово, верно?\n\n"
        "🚚 И вы знаете, что лучшее? Мы бесплатно доставим TozaSuv прямо к вам, чтобы вы могли наслаждаться без забот о доставке.\n\n"
        "🌆 А касательно этажей, независимо от этажа, TozaSuv легко дойдет до вас. Всегда доступно и удобно!\n\n"
        "Попробуйте Toza Suv и почувствуйте разницу! 💦")
        photo = "AgACAgIAAxkBAAIHhWUf6-HW01vRc2YjEZUAAb2hnB9_0QACqM8xGwwMAAFJdac72UJJgkkBAAMCAAN4AAMwBA"
    elif product == _("💦 Toza Suv 19л"):
        caption = _("<b>💦 Toza Suv 19л</b>\n\n"
        "<b>Цена:</b> 25.000 сум \n\n"
        "🌟 Toza Suv - вода высшего качества, которую вы заслуживаете! Насладитесь каждой каплей свежести и чистоты.\n\n"
        "💧 Наша вода прошла 9 степеней очистки, чтобы быть идеально чистой. Это здорово, верно?\n\n"
        "🚚 И вы знаете, что лучшее? Мы бесплатно доставим TozaSuv прямо к вам, чтобы вы могли наслаждаться без забот о доставке.\n\n"
        "🌆 А касательно этажей, независимо от этажа, TozaSuv легко дойдет до вас. Всегда доступно и удобно!\n\n"
        "Попробуйте Toza Suv и почувствуйте разницу! 💦")
        photo = "AgACAgIAAxkBAAIHiWUf7ATjTatlAAGyupVF5m3Dx9YWKQACq88xGwwMAAFJxso1ey1PousBAAMCAAN4AAMwBA"
    user_id = message.from_user.id
    water_quantity[user_id] = 0

    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton("-", callback_data='decrease'),
        types.InlineKeyboardButton("0", callback_data='quantity'),
        types.InlineKeyboardButton("+", callback_data='increase'),
    ]
    keyboard.row(*buttons)
    keyboard.add(types.InlineKeyboardButton("Выбрать воду", callback_data='select_water'))
    await message.answer(_("Выберите сколько хотели бы заказать "), reply_markup=await back_keyboard())
    await message.reply_photo(photo=photo, caption=caption, reply_markup=keyboard)
    await Order.ChoiseQuality.set()
    await state.update_data(offer=offer)


@dp.callback_query_handler(lambda c: c.data in ['decrease', 'quantity', 'increase'], state=Order.ChoiseQuality)
async def handle_quantity_callback(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    data = callback_query.data

    if data == 'decrease':
        water_quantity[user_id] -= 1
    elif data == 'increase':
        water_quantity[user_id] += 1

    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton("-", callback_data='decrease'),
        types.InlineKeyboardButton(str(water_quantity[user_id]), callback_data='quantity'),
        types.InlineKeyboardButton("+", callback_data='increase'),
    ]
    keyboard.row(*buttons)
    keyboard.add(types.InlineKeyboardButton(_("Выбрать воду"), callback_data='select_water'))

    await callback_query.message.edit_caption(caption, reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'select_water', state=Order.ChoiseQuality)
async def handle_select_water_callback(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    water_selected = water_quantity[user_id]   
    data = await state.get_data()
    offer: Offer = data.get("offer")
    offer.quantity = water_selected
    currency = 10000 * water_selected
    offer.price = currency

    # Здесь вы можете добавить логику для выбора определенной воды
    await callback_query.message.edit_caption(_("Выбрано {water_selected} штук воды <b> {offer_product} </b>".format(water_selected=water_selected, offer_product=offer.product)))
    await callback_query.message.answer(_("Отправьте новую гео-локацию,либо пропустите шаг"), reply_markup=await address_send_offer())
    await Order.LocationChoise.set()
    await state.update_data(offer=offer)

@dp.message_handler(content_types=[ContentType.LOCATION, ContentType.TEXT],state=Order.LocationChoise)
async def location_send(message: types.Message, state: FSMContext):

    if message.content_type == ContentType.LOCATION:
        location = message.location
        data = await state.get_data()
        offer: Offer = data.get("offer")
        offer.location = location 
    elif message.content_type == ContentType.TEXT:
        location = message.text
        data = await state.get_data()
        offer: Offer = data.get("offer")
        offer.location = location 
    await message.answer(_(f"Выберите тип оплаты:"), reply_markup=await payments_type())
    await Order.ChoisePayments.set()
    await state.update_data(offer=offer)

PAYMENTS_TOKEN = '398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065'

@dp.message_handler(state=Order.ChoisePayments, text="💳 Click UP")
async def location_send(message: types.Message, state: FSMContext):
    data = await state.get_data()
    offer: Offer = data.get("offer")
    price = offer.price
    offer.payment = "💳 Click UP"
    PRICE = types.LabeledPrice(label=f"Вода {offer.product}, {offer.quantity} штук", amount=price*100)

    if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, _("Оплатите платеж,для дальнейшего заказа!"), reply_markup=await back_keyboard())

    await bot.send_invoice(message.chat.id,
    title="TozaSuv / ClickUP",
    description=f"Вода {offer.product}, {offer.quantity} штук",
    provider_token=PAYMENTS_TOKEN,
    currency="uzs",
    photo_url="https://www.tozasuv.uz/img/tiles-item-3.jpg",
    is_flexible=False,
    prices=[PRICE],
    start_parameter="one-month-subscription",
    payload="test-invoce-payload")
    await Order.Invoise.set()
    await state.update_data(offer=offer)


@dp.pre_checkout_query_handler(lambda query: True, state=Order.Invoise)
async def pre_checkout(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
    await Order.Successful.set()

# Succesful payment

@dp.message_handler(state=Order.Successful, content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message, state: FSMContext):
    data = await state.get_data()
    offer: Offer = data.get("offer")
    offer.status = "Оплачен"
    payment_info = message.successful_payment.to_python()
    await bot.send_message(message.chat.id, _("Оплата прошла успешно 💸, напишите коментарии к заказу либо пропустите этот шаг"), reply_markup=await select_keyboard())
    
    await Order.Commentary.set()


@dp.message_handler(state=Order.ChoisePayments)
async def location_send(message: types.Message, state: FSMContext):
    payments_type = message.text
    data = await state.get_data()
    offer: Offer = data.get("offer")
    offer.payment = payments_type 
    await message.answer(_(f"Напишите комментарии к заказу либо пропустите этот шаг"), reply_markup=await select_keyboard())
    await Order.Commentary.set()
    await state.update_data(offer=offer)

# Словарь для отслеживания состояния кнопок
button_states = {}

@dp.callback_query_handler(lambda c: c.data in ['confirm_order', 'waiting_order', 'cancel_order'])
async def handle_button_click(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    button_data = callback_query.data

    # Обновляем состояния кнопок
    button_states[user_id] = button_data

    # Создаем клавиатуру с обновленным состоянием кнопок
    markup = await offer_confirm_keyboard(user_id)

    # Редактируем сообщение с новой клавиатурой
    await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=markup)

async def offer_confirm_keyboard(user_id) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=3)

    # Проверяем состояние каждой кнопки и устанавливаем галочку только на выбранной
    confirm_text = "Доставлен"
    wait_text = "Ожидание"
    cancel_text = "Отменить"
    
    if button_states.get(user_id) == "confirm_order":
        confirm_text += " ✅"
    elif button_states.get(user_id) == "waiting_order":
        wait_text += " ✅"
    elif button_states.get(user_id) == "cancel_order":
        cancel_text += " ❌"

    btn1 = InlineKeyboardButton(text=confirm_text, callback_data="confirm_order")
    btn2 = InlineKeyboardButton(text=wait_text, callback_data="waiting_order")
    btn3 = InlineKeyboardButton(text=cancel_text, callback_data="cancel_order")

    markup.add(btn1, btn2, btn3)
    return markup


@dp.message_handler(state=Order.Commentary)
async def location_send(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    current_datetime = datetime.datetime.now()    
    commentary = message.text
    data = await state.get_data()
    offer: Offer = data.get("offer")
    offer.commentary = commentary 
    offer.username = message.from_user.username
    offer.telegram_id = message.from_user.id
    offer.date = current_datetime

    user_data = await get_data(message.from_user.id)
    user_phone = user_data[1]
    # await bot.send_message(chat_id, "TEST", reply_markup=await offer_confirm_keyboard(user_id))

    if offer.location == "Пропустить ➡️":
        user_location = user_data[2]
        location_data_json_str = user_location[0]  # Извлекаем строку из кортежа
        parsed_location = json.loads(location_data_json_str)
        latitude = parsed_location["latitude"]
        longitude = parsed_location["longitude"]
    else:
        user_location = offer.location
        location_data_json_str = user_location[0]  # Извлекаем строку из кортежа
        parsed_location = json.loads(location_data_json_str)
        latitude = parsed_location["latitude"]
        longitude = parsed_location["longitude"]
    try:
        await bot.send_location(chat_id, latitude=latitude, longitude=longitude)

        await bot.send_message(chat_id, "Новый заказ! 💸\n"
        f"Номер телефона: {user_phone} \n"
        f"Дата и время: {offer.date} \n"
        f"Продукт: {offer.product} \n"
        f"Количество: {offer.quantity} \n"
        f"Цена: {offer.price} \n"
        f"Типа оплаты: {offer.payment}\n"
        f"Никнем телеграм: @{offer.username} \n"
        f"Комментарии: {offer.commentary} \n", reply_markup=await offer_confirm_keyboard(user_id)
        )
        offer.save()
    except Exception as e:
        # Обработка ошибок при сохранении в базе данных, если необходимо
        await message.answer(f"Произошла ошибка при сохранении заказа: {str(e)}")
    else:
        await message.answer(_("Ваш заказ приняли, ожидайте"), reply_markup=await main_keyboard())

    finally:
        await state.reset_state()



