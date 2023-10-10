from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from .handlers_user import user_router

routers = (user_router,)

def get_dispatcher():
    dp = Dispatcher(storage=MemoryStorage())
    for router in routers:
        dp.include_router(router)
    return dp