from aiogram.fsm.state import State, StatesGroup

class StateForm(StatesGroup):
    START_MENU = State()
    CATALOG = State()
    ORIGINAL_ORDER = State()
    COPY_ORDER = State()
    