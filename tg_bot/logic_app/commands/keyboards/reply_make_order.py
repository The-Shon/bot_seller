from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_kb = KeyboardButton(text='↪️ Отмена')
number_kb = KeyboardButton(text='📱 Отправить номер телефона', request_contact=True)
location_kb = KeyboardButton(text='🌏 Отправить геолокацию', request_location=True)

def get_kb_order_main() -> ReplyKeyboardMarkup:
    kb = [
        [ cancel_kb],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

def get_kb_order_get_number() -> ReplyKeyboardMarkup:
    kb = [
        [ number_kb],
        [ cancel_kb],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

def get_kb_order_get_location() -> ReplyKeyboardMarkup:
    kb = [
        [ location_kb],
        [ cancel_kb],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard