from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_kb = KeyboardButton(text='↪️ Отмена')

def get_kb_order_main() -> ReplyKeyboardMarkup:
    kb = [
        [ cancel_kb],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard