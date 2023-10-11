from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.context import FSMContext


# my imports --------------------------------
from .keyboards import reply_start_menu as kb
from ...settings_app import text_start as text
# -------------------------------------------

user_router_start = Router()

# ----------------------------------------------------------------------------------------
@user_router_start.message(CommandStart())
async def cmd_start(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_start_menu_text(), reply_markup=kb.get_kb_start_menu())
    await state.clear()
    

@user_router_start.message(F.text == '↪️ Отмена')
async def cmd_back(message: Message, state=FSMContext) -> None:
    await cmd_start(message, state)