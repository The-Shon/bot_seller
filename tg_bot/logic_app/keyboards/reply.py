from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# start_menu -----------------------------------------------------
start_menu_kb1 = KeyboardButton(text='🛍 Каталог')
start_menu_kb2 = KeyboardButton(text='🚀 Сделать заказ')
start_menu_kb3 = KeyboardButton(text='🛎 Обратная связь')
start_menu_kb4 = KeyboardButton(text='🌐 Соц.сети')
start_menu_kb5 = KeyboardButton(text='💭 FAQ')
start_menu_kb6 = KeyboardButton(text='🗣️ Отзывы')
start_menu_kb7 = KeyboardButton(text='📦 Отследить заказ')


# catalog --------------------------------------------------------
catalog_kb1 = KeyboardButton(text='🔥 Original')
catalog_kb2 = KeyboardButton(text='⚡ Luxury Copy')



# order_categories -----------------------------------------------
order_categories_kb2 = KeyboardButton(text='✅ В наличии')
order_categories_kb1 = KeyboardButton(text='📬 На заказ')


# product_categories ---------------------------------------------
product_categories_kb1 = KeyboardButton(text='👟 Кросовки')
product_categories_kb2 = KeyboardButton(text='🩳 Одежда')
product_categories_kb3 = KeyboardButton(text='🧢 Аксессуары')


# Back / Cancel ---------------------------------------------------
back_kb = KeyboardButton(text='⬅️ Назад')
cancel_kb = KeyboardButton(text='↪️ Отмена')


#------------------------------------------------------------------
def get_kb_start_menu() -> ReplyKeyboardMarkup:
    kb = [
        [ start_menu_kb1, start_menu_kb2 ],
        [ start_menu_kb3 ],
        [ start_menu_kb4, start_menu_kb5, start_menu_kb6 ],
        [ start_menu_kb7],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def get_kb_catalog() -> ReplyKeyboardMarkup:
    kb = [
        [ catalog_kb1 ],
        [ catalog_kb2 ],
        [ back_kb ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def get_kb_order_categories() -> ReplyKeyboardMarkup:
    kb = [
        [ order_categories_kb1 ],
        [ order_categories_kb2 ],
        [ back_kb ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def get_kb_product_categories() -> ReplyKeyboardMarkup:
    kb = [
        [ product_categories_kb1 ],
        [ product_categories_kb2 ],
        [ product_categories_kb3 ],
        [ back_kb ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard