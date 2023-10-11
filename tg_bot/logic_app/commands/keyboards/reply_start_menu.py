from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# start_menu -----------------------------------------------------
start_menu_kb1 = KeyboardButton(text='🛍 Каталог')
start_menu_kb2 = KeyboardButton(text='🚀 Сделать заказ')
start_menu_kb3 = KeyboardButton(text='🛎 Обратная связь')
start_menu_kb4 = KeyboardButton(text='🌐 Соц.сети')
start_menu_kb5 = KeyboardButton(text='💭 FAQ')
start_menu_kb6 = KeyboardButton(text='🗣️ Отзывы')
start_menu_kb7 = KeyboardButton(text='📦 Отследить заказ')

def get_kb_start_menu() -> ReplyKeyboardMarkup:
    kb = [
        [ start_menu_kb1, start_menu_kb2 ],
        [ start_menu_kb3 ],
        [ start_menu_kb4, start_menu_kb5, start_menu_kb6 ],
        [ start_menu_kb7],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard