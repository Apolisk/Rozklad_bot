from aiogram.dispatcher.filters.state import State, StatesGroup

class user_choose(StatesGroup):
    first_station = State()
    second_station = State()