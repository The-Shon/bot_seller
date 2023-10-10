from aiogram.fsm.state import State, StatesGroup

class MainStateForm(StatesGroup):
    START_MENU = State()
    CATALOG = State()
    ORDER = State()
    CATEGORIES = State()
    