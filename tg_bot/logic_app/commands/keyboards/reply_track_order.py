from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

sdek_kb = KeyboardButton(text='🚛 Открыть CDEK', web_app=WebAppInfo(url='https://www.cdek.ru/ru/tracking/'))
back_kb = KeyboardButton(text='⬅️ Назад') 

def det_kb_track_order():
    kb = [
        [ sdek_kb ],
        [ back_kb ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard
