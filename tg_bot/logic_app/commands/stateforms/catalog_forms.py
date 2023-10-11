from aiogram.fsm.state import State, StatesGroup

class CatalogStateForm(StatesGroup):
    
    CATALOG = State()
    # ORDER = State()
    CATEGORIES = State()