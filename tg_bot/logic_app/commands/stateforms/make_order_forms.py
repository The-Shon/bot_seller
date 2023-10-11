from aiogram.fsm.state import State, StatesGroup

class MakeOrderStateForm(StatesGroup):

    ENTER_MODEL_NAME = State()
    ENTER_USER_SIZE = State()
    ENTER_USER_FULL_NAME = State()
    ENTER_USER_PHONE_NUMBER = State()
    ENTER_USER_ADDRESS = State()
