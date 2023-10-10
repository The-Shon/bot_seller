from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.context import FSMContext


# my imports --------------------------------
from .stateforms import MainStateForm

from .keyboards import (get_kb_start_menu, 
                        get_kb_catalog, 
                        get_kb_order_categories,
                        get_kb_product_categories)

from ..settings_app import (get_start_menu_text,
                            get_catalog_text,
                            get_order_text,
                            get_categories_text,
                            get_description_categories_text)
# -------------------------------------------


user_router = Router()

# ----------------------------------------------------------------------------------------
@user_router.message(CommandStart())
async def cmd_start(message: Message, state=FSMContext) -> None:
    await message.answer(text=get_start_menu_text(), reply_markup=get_kb_start_menu())
    await state.set_state(MainStateForm.START_MENU)


# ----------------------------------------------------------------------------------------
@user_router.message(F.text == '🛍 Каталог', MainStateForm.START_MENU)
async def cmd_catalog(message: Message, state=FSMContext) -> None:
    await message.answer(text=get_catalog_text(), reply_markup=get_kb_catalog())
    await state.set_state(MainStateForm.CATALOG)


# ----------------------------------------------------------------------------------------
@user_router.message(F.text == '🔥 Original', MainStateForm.CATALOG)
async def cmd_original_order(message: Message, state=FSMContext) -> None:
    await message.answer(text=get_order_text(type_order='Original'), reply_markup=get_kb_order_categories())
    await state.set_state(MainStateForm.ORDER)
    # TODO нужно допилить передачу данных о type_order


@user_router.message(F.text == '⚡ Luxury Copy', MainStateForm.CATALOG)
async def cmd_copy_order(message: Message, state=FSMContext) -> None:
    await message.answer(text=get_order_text(type_order='Luxury Copy'), reply_markup=get_kb_order_categories())
    await state.set_state(MainStateForm.ORDER)
    # TODO нужно допилить передачу данных о type_order


# ----------------------------------------------------------------------------------------
@user_router.message(F.text == '✅ В наличии', MainStateForm.ORDER)
async def cmd_categories_in_stock(message: Message, state=FSMContext) -> None:
    await message.answer(text=get_categories_text(), reply_markup=get_kb_product_categories())
    await state.set_state(MainStateForm.CATEGORIES)
    # TODO нужно допилить передачу данных о type_categories


@user_router.message(F.text == '📬 На заказ', MainStateForm.ORDER)
async def cmd_categories_to_order(message: Message, state=FSMContext) -> None:
    await message.answer(text=get_categories_text(), reply_markup=get_kb_product_categories())
    await state.set_state(MainStateForm.CATEGORIES)
    # TODO нужно допилить передачу данных о type_categories


# ----------------------------------------------------------------------------------------
@user_router.message(F.text == '👟 Кросовки', MainStateForm.CATEGORIES)
async def cmd_sneakers(message: Message, state=FSMContext) -> None:
    await message.answer(text=get_description_categories_text(type_categories='Кросовки'), reply_markup=get_kb_product_categories())
    # TODO нужно допилить передачу данных о type_categories


@user_router.message(F.text == '🩳 Одежда', MainStateForm.CATEGORIES)
async def cmd_clothes(message: Message, state=FSMContext) -> None:
    await message.answer(text=get_description_categories_text(type_categories='Одежда'), reply_markup=get_kb_product_categories())
    # TODO нужно допилить передачу данных о type_categories


@user_router.message(F.text == '🧢 Аксессуары', MainStateForm.CATEGORIES)
async def cmd_accessories(message: Message, state=FSMContext) -> None:
    await message.answer(text=get_description_categories_text(type_categories='Аксессуары'), reply_markup=get_kb_product_categories())
    # TODO нужно допилить передачу данных о type_categories


# ----------------------------------------------------------------------------------------
@user_router.message(F.text == '⬅️ Назад')
async def cmd_back(message: Message, state=FSMContext) -> None:
    state_form = await state.get_state()

    if state_form == MainStateForm.CATALOG:
        await cmd_start(message, state)
    elif state_form == MainStateForm.ORDER:
        await cmd_catalog(message, state)
    else:
        await cmd_original_order(message, state)
    # TODO сделать нормальных возврат по функциям
 


@user_router.message()
async def echo_handler(message: Message) -> None:
    try:
        print(message.text)
        await message.send_copy(chat_id=message.chat.id)

    except TypeError:
        await message.answer("Nice try!")