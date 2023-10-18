from aiogram import Router
from aiogram.types import Message
from aiogram import Bot


user_router_other = Router()

@user_router_other.message()
async def echo_handler(message: Message, bot: Bot) -> None:
    try:
        print(message.text)
        await message.answer(text=str(message.from_user.id))
        await message.send_copy(chat_id=message.chat.id)

    except TypeError:
        await message.answer("Nice try!")