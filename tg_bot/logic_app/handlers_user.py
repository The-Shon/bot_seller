from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from .keyboards import get_kb_start_menu, get_kb_catalog, get_kb_order_categories, get_kb_product_categories

user_router = Router()

@user_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text=f"Hello, {message.from_user.full_name}!", reply_markup=get_kb_catalog())


@user_router.message()
async def echo_handler(message: Message) -> None:
    try:
        print(message.text)
        await message.send_copy(chat_id=message.chat.id)

    except TypeError:
        await message.answer("Nice try!")