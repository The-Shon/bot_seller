from aiogram import Bot, Dispatcher, Router, types

from aiogram.filters import CommandStart
from aiogram.types import Message
# from aiogram.utils.markdown import hbold
# from aiogram.enums import ParseMode


# my imports -----
from .logging_app.logging_main import logging_bot
from .settings_app.settings_main import settings
from .dispatcher import get_dispatcher
# ----------------


async def start_bot():

    logging_bot()

    dp = get_dispatcher()
    bot = Bot(token=settings.bots.bot_token)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()