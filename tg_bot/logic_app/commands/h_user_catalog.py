from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram import F
from aiogram.fsm.context import FSMContext


# my imports --------------------------------
from .stateforms import CatalogStateForm, EnumsCatalog ,EnumsCategory
from .keyboards import reply_menu_catalog as kb
from ...settings_app import text_menu_catalog as text

from .h_user_start import cmd_start
# -------------------------------------------

user_router_catalog = Router()

# ----------------------------------------------------------------------------------------
@user_router_catalog.message(F.text.contains('Каталог'))
async def cmd_catalog(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_order_text(), reply_markup=kb.get_kb_order_categories())
    await state.set_state(CatalogStateForm.CATALOG)


# ----------------------------------------------------------------------------------------
# @user_router_catalog.message(F.text == '🔥 Original', CatalogStateForm.CATALOG)
# async def cmd_original_order(message: Message, state=FSMContext) -> None:
#     await message.answer(text=text.get_order_text(type_order='Original'), reply_markup=kb.get_kb_order_categories())
#     await state.set_state(CatalogStateForm.ORDER)
#     # TODO нужно допилить передачу данных о type_order


# @user_router_catalog.message(F.text == '⚡ Luxury Copy', CatalogStateForm.CATALOG)
# async def cmd_copy_order(message: Message, state=FSMContext) -> None:
#     await message.answer(text=text.get_order_text(type_order='Luxury Copy'), reply_markup=kb.get_kb_order_categories())
#     await state.set_state(CatalogStateForm.ORDER)
#     # TODO нужно допилить передачу данных о type_order


# ----------------------------------------------------------------------------------------
@user_router_catalog.message(F.text.contains('В наличии'), CatalogStateForm.CATALOG)
async def cmd_categories_in_stock(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_categories_text(), reply_markup=kb.get_kb_product_categories())
    await state.set_state(CatalogStateForm.CATEGORIES)
    await state.update_data(catalog=EnumsCatalog.in_stock)
    # TODO нужно допилить передачу данных о type_categories


@user_router_catalog.message(F.text.contains('На заказ'), CatalogStateForm.CATALOG)
async def cmd_categories_to_order(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_categories_text(), reply_markup=kb.get_kb_product_categories())
    await state.set_state(CatalogStateForm.CATEGORIES)
    await state.update_data(catalog=EnumsCatalog.to_order)


# ----------------------------------------------------------------------------------------
@user_router_catalog.message(F.text.contains('Кроссовки'), CatalogStateForm.CATEGORIES)
async def cmd_sneakers(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_description_categories_text(type_categories='Кросовки'), reply_markup=kb.get_kb_product_categories())
    await state.update_data(categories=EnumsCategory.sneakers)
    state_data = await state.get_data()

    await message.answer(text=str(state_data), reply_markup=kb.get_kb_product_categories())
    # await state.set_state(MainStateForm.PRODUCT)


@user_router_catalog.message(F.text.contains('Одежда'), CatalogStateForm.CATEGORIES)
async def cmd_clothes(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_description_categories_text(type_categories='Одежда'), reply_markup=kb.get_kb_product_categories())
    await state.update_data(categories=EnumsCategory.clothes)
    state_data = await state.get_data()

    await message.answer(text=str(state_data), reply_markup=kb.get_kb_product_categories())
    # await state.set_state(MainStateForm.PRODUCT)


@user_router_catalog.message(F.text.contains('Аксессуары'), CatalogStateForm.CATEGORIES)
async def cmd_accessories(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_description_categories_text(type_categories='Аксессуары'), reply_markup=kb.get_kb_product_categories())
    await state.update_data(categories=EnumsCategory.accessories)
    state_data = await state.get_data()

    await message.answer(text=str(state_data), reply_markup=kb.get_kb_product_categories())
    # await state.set_state(MainStateForm.PRODUCT)


# ----------------------------------------------------------------------------------------
@user_router_catalog.message(F.text.contains('Назад'), StateFilter(CatalogStateForm))
async def cmd_back(message: Message, state=FSMContext) -> None:
    state_form = await state.get_state()

    if state_form == CatalogStateForm.CATALOG:
        await cmd_start(message, state)
    elif state_form == CatalogStateForm.CATEGORIES:
        await cmd_catalog(message, state)