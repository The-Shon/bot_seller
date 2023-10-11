from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from .commands import (user_router_start,
                       user_router_catalog,
                       user_router_make_order)

routers = (user_router_start, user_router_catalog, user_router_make_order,)

def get_dispatcher():
    dp = Dispatcher(storage=MemoryStorage())
    for router in routers:
        dp.include_router(router)
    return dp