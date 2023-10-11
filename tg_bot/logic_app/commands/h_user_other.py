from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.context import FSMContext

user_router_other = Router()

@user_router_other.message()
async def echo_handler(message: Message) -> None:
    try:
        print(message.text)
        await message.send_copy(chat_id=message.chat.id)

    except TypeError:
        await message.answer("Nice try!")