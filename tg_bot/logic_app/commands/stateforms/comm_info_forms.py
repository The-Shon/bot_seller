from aiogram.fsm.state import State, StatesGroup

class CommInfoStateForm(StatesGroup):
    
    MENU = State()
    # FAQ = State()
    FEEDBACK = State()
    GET_QUESTION = State()
    GET_REVIEW = State()
    SEND_REVIEW = State()