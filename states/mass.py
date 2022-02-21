from aiogram.dispatcher.filters.state import StatesGroup, State


class MassSend(StatesGroup):
    text = State()