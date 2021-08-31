from aiogram.dispatcher.filters.state import StatesGroup, State


class Tests(StatesGroup):
    Stop = State()
    Back = State()