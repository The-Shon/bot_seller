from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.context import FSMContext


# my imports --------------------------------
from .stateforms import MakeOrderStateForm
from .keyboards import reply_make_order as kb
from ...settings_app import menu_make_order as text

from .h_user_start import cmd_start
# -------------------------------------------

user_router_make_order = Router()

# ----------------------------------------------------------------------------------------
@user_router_make_order.message(F.text == '🚀 Сделать заказ')
async def cmd_enter_model_name(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_order_main_text())
    await message.answer(text=text.get_order_model_name_text(), reply_markup=kb.get_kb_order_main())
    await state.set_state(MakeOrderStateForm.ENTER_MODEL_NAME)


@user_router_make_order.message(MakeOrderStateForm.ENTER_MODEL_NAME)
async def cmd_enter_size(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_order_size_text(), reply_markup=kb.get_kb_order_main())
    await state.set_state(MakeOrderStateForm.ENTER_USER_SIZE)


@user_router_make_order.message(MakeOrderStateForm.ENTER_USER_SIZE)
async def cmd_enter_user_name(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_order_user_name_text(), reply_markup=kb.get_kb_order_main())
    await state.set_state(MakeOrderStateForm.ENTER_USER_FULL_NAME)


@user_router_make_order.message(MakeOrderStateForm.ENTER_USER_FULL_NAME)
async def cmd_enter_address(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_order_address_text(), reply_markup=kb.get_kb_order_main())
    await state.set_state(MakeOrderStateForm.ENTER_USER_ADDRESS)


@user_router_make_order.message(MakeOrderStateForm.ENTER_USER_ADDRESS)
async def cmd_order_finish(message: Message, state=FSMContext) -> None:
    await message.answer(text='все отлично', reply_markup=kb.get_kb_order_main())
    # await state.set_state(MakeOrderStateForm.ENTER_USER_ADDRESS)

# TODO сделать кнопку отмены + доп фильты на вводимые данные

# ----------------------------------------------------------------------------------------
# @user_router_catalog.message(F.text == '⬅️ Назад')
# async def cmd_back(message: Message, state=FSMContext) -> None:
#     state_form = await state.get_state()

#     if state_form == CatalogStateForm.CATALOG:
#         await cmd_start(message, state)
#     elif state_form == CatalogStateForm.ORDER:
#         await cmd_catalog(message, state)
#     elif state_form == CatalogStateForm.CATEGORIES:
#         await cmd_original_order(message, state)
#     else:
#         await cmd_categories_in_stock(message, state)
#     # TODO сделать нормальных возврат по функциям