from aiogram.dispatcher.filters.state import State, StatesGroup


class RegData(StatesGroup):
    Language = State()
    Phone = State()
    Location = State()

