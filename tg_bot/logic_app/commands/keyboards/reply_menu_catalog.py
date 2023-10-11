from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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