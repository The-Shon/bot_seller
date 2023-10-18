from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram import F



# my imports --------------------------------
from .stateforms import TrackOrderForm
from .keyboards import reply_track_order as kb
from ...settings_app import text_track_order as text
from ...settings_app import settings


from .h_user_start import cmd_menu
# -------------------------------------------

user_router_track_order = Router()


@user_router_track_order.message(F.text.contains('Отследить заказ'))
async def cmd_track_order(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_text_track_order(), reply_markup=kb.det_kb_track_order())
    await state.set_state(TrackOrderForm.TRACK)


@user_router_track_order.message(F.text.contains('Назад'), StateFilter(TrackOrderForm))
async def cmd_back(message: Message, state=FSMContext) -> None:
    await cmd_menu(message, state)
