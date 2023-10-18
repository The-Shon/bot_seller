from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

comm_info_menu_kb1 = KeyboardButton(text='🛎 Обратная связь')
comm_info_menu_kb2 = KeyboardButton(text='🌐 Соц.сети')
comm_info_menu_kb3 = KeyboardButton(text='💭 FAQ')
comm_info_menu_kb4 = KeyboardButton(text='🗣️ Отзывы')

feedback_kb1 = KeyboardButton(text='❓ Задайть вопрос менеджеру')
feedback_kb2 = KeyboardButton(text='📋 Оставить отзыв')

send_review_kb = KeyboardButton(text='⚡ Отправить сообщения')
cancel_kb = KeyboardButton(text='↪️ Отмена')

back_kb = KeyboardButton(text='⬅️ Назад')


def get_kb_comm_info():
    kb = [
        [ comm_info_menu_kb1,],
        [ comm_info_menu_kb2,  comm_info_menu_kb3, comm_info_menu_kb4],
        [ back_kb ],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_kb_feedback():
    kb = [
        [ feedback_kb1 ],
        [ feedback_kb2 ],
        [ back_kb ],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_kb_back():
    kb = [
        [ back_kb ],
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_kb_send_review():
    kb = [
        [ send_review_kb ],
        [ cancel_kb ]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)