from aiogram import Bot

# my imports -----
from .logging_app import logging_bot
from .settings_app import settings
from .logic_app import get_dispatcher
# ----------------

async def start_bot():

    logging_bot

    dp = get_dispatcher()
    bot = Bot(token=settings.bots.bot_token)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()