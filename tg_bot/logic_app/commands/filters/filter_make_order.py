from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message


# class FilterMakeOrderNameModel(BaseFilter):
#     def __init__(self, model_type: str):
#         self.model_type = model_type

#     async def __call__(self, message: Message) -> bool:
#         if isinstance(self.chat_type, str):
#             return message.chat.type == self.chat_type
#         else:
#             return message.chat.type in self.chat_type

# class FilterMakeOrderUserSize(BaseFilter):
#     def __init__(self, size: str)