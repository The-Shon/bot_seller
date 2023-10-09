from .handlers import routers

from aiogram import Dispatcher

def get_dispatcher():
    dp = Dispatcher()
    for router in routers:
        dp.include_router(router)
    return dp

