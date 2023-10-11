from aiogram.fsm.state import State, StatesGroup
import enum

class MakeOrderStateForm(StatesGroup):

    ENTER_MODEL_NAME = State()
    ENTER_USER_SIZE = State()
    ENTER_USER_FULL_NAME = State()
    ENTER_USER_PHONE_NUMBER = State()
    ENTER_USER_ADDRESS = State()


class EnumsCatalog(enum.Enum):
    in_stock = 1
    to_order = 2


class EnumsCategory(enum.Enum):
    sneakers = 1
    clothes = 2
    accessories = 3
