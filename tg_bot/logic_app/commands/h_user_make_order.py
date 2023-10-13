from aiogram import Router
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram.filters import CommandStart
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.types import Location

# my imports --------------------------------
from .stateforms import MakeOrderStateForm
from .keyboards import reply_make_order as kb
from ...settings_app import text_menu_make_order as text
from ...settings_app import settings
from .utils import regular_expressions as re

from .h_user_start import cmd_start
# -------------------------------------------

user_router_make_order = Router()

# ----------------------------------------------------------------------------------------
@user_router_make_order.message(F.text == '🚀 Сделать заказ')
async def cmd_enter_model_name(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_text_order_main())
    await message.answer(text=text.get_text_order_model_name(), reply_markup=kb.get_kb_order_main())
    await state.set_state(MakeOrderStateForm.ENTER_MODEL_NAME)
    await state.update_data(user_name=message.from_user.username)


@user_router_make_order.message(MakeOrderStateForm.ENTER_MODEL_NAME)
async def cmd_enter_size(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_text_order_size(), reply_markup=kb.get_kb_order_main())
    await state.set_state(MakeOrderStateForm.ENTER_USER_SIZE)
    await state.update_data(model_name=message.text)


@user_router_make_order.message(MakeOrderStateForm.ENTER_USER_SIZE)
async def cmd_enter_user_name(message: Message, state=FSMContext) -> None:
    try:
        size = int(message.text)
        if (30 < size and size < 50):
            await message.answer(text=text.get_text_order_user_name(), reply_markup=kb.get_kb_order_main())
            await state.set_state(MakeOrderStateForm.ENTER_USER_FULL_NAME)
            await state.update_data(user_size=message.text)
        else:
            await message.answer(text=text.get_text_unreal_size(), reply_markup=kb.get_kb_order_main())
    except:
        await message.answer(text=text.get_text_incorrect_size(), reply_markup=kb.get_kb_order_main())      


@user_router_make_order.message(MakeOrderStateForm.ENTER_USER_FULL_NAME)
async def cmd_enter_phone_number(message: Message, state=FSMContext) -> None:
    if re.is_full_name(message.text):
        await message.answer(text=text.get_text_order_phone(), reply_markup=kb.get_kb_order_get_number())
        await state.set_state(MakeOrderStateForm.ENTER_USER_PHONE_NUMBER)
        await state.update_data(full_name=message.text)
    else:
        await message.answer(text=text.get_text_incorrect_name(), reply_markup=kb.get_kb_order_get_number())  


@user_router_make_order.message(MakeOrderStateForm.ENTER_USER_PHONE_NUMBER, F.content_type == ContentType.CONTACT)
async def cmd_enter_address(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_text_order_address(), reply_markup=kb.get_kb_order_get_location())
    await state.set_state(MakeOrderStateForm.ENTER_USER_ADDRESS)
    await state.update_data(phone_number=message.contact.phone_number)


@user_router_make_order.message(MakeOrderStateForm.ENTER_USER_PHONE_NUMBER)
async def cmd_enter_address(message: Message, state=FSMContext) -> None:
    if re.is_phone_number(message.text):
        await message.answer(text=text.get_text_order_address(), reply_markup=kb.get_kb_order_get_location())
        await state.set_state(MakeOrderStateForm.ENTER_USER_ADDRESS)
        await state.update_data(phone_number=message.text)
    else:
        await message.answer(text=text.get_text_incorrect_phone(), reply_markup=kb.get_kb_order_get_number())


@user_router_make_order.message(MakeOrderStateForm.ENTER_USER_ADDRESS, F.content_type == ContentType.LOCATION)
async def cmd_order_finish(message: Message, bot: Bot, state=FSMContext) -> None:
    await state.update_data(address=message.location)
    state_data = await state.get_data()

    await bot.send_message(chat_id=settings.bots.manager_id, text=text.get_order(state_data=state_data))
    await bot.send_location(chat_id=settings.bots.manager_id, latitude=message.location.latitude, longitude=message.location.longitude)
    await message.answer(text='Ваши данные успешно отправлены', reply_markup=kb.get_kb_order_main())
    await cmd_start(message, state)


@user_router_make_order.message(MakeOrderStateForm.ENTER_USER_ADDRESS)
async def cmd_order_finish(message: Message, bot: Bot, state=FSMContext,) -> None:
    await state.update_data(address=message.text)
    state_data = await state.get_data()

    await bot.send_message(chat_id=settings.bots.manager_id, text=text.get_order(state_data=state_data))
    await message.answer(text='Ваши данные успешно отправлены', reply_markup=kb.get_kb_order_main())
    await cmd_start(message, state)