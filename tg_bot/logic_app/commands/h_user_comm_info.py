from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram import F
from aiogram.fsm.context import FSMContext

# my imports --------------------------------
from .stateforms import CommInfoStateForm
from .keyboards import reply_comm_info as kb
from ...settings_app import text_comm_info as text
from ...settings_app import settings

from .h_user_start import cmd_menu
# -------------------------------------------

user_router_comm_info = Router()

@user_router_comm_info.message(F.text.in_((['📌 Связь/Инфо','Связь/Инфо','Инфо', 'Связь', '📌'])))
async def cmd_menu_comm_info(message: Message, state=FSMContext) -> None:
    await message.answer(text=text.get_text_comm_info_main(), reply_markup=kb.get_kb_comm_info())
    await state.set_state(CommInfoStateForm.MENU)


# ------------------------------------------------------------------------------------
@user_router_comm_info.message(F.text.contains('FAQ'), CommInfoStateForm.MENU)
async def cmd_faq(message: Message, state=FSMContext) -> None:
    await message.answer(text='FAQ')

# TODO вывод статьи про часто задаваемые вопросы

# ------------------------------------------------------------------------------------
@user_router_comm_info.message(F.text.contains('Соц.сети'), CommInfoStateForm.MENU)
async def cmd_faq(message: Message, state=FSMContext) -> None:
    await message.answer(text='Соц.сети')
    # await state.set_state(CommInfoStateForm.FEEDBACK)

    # TODO сделать состояния для меню и тексты для сообщений в папке настроек

# ------------------------------------------------------------------------------------
@user_router_comm_info.message(F.text.contains('Отзывы'), CommInfoStateForm.MENU)
async def cmd_faq(message: Message, state=FSMContext) -> None:
    await message.answer(text='Отзывы')
    # await state.set_state(CommInfoStateForm.FEEDBACK)

    # TODO сделать состояния для меню и тексты для сообщений в папке настроек

# ------------------------------------------------------------------------------------
@user_router_comm_info.message(F.text.contains('Обратная связь'), CommInfoStateForm.MENU)
async def cmd_feedback_and_review(message: Message, state=FSMContext) -> None:
    await message.answer(text='Обратрная связь', reply_markup=kb.get_kb_feedback())
    await state.set_data({})
    await state.set_state(CommInfoStateForm.FEEDBACK)

@user_router_comm_info.message(F.text.contains('Оставить отзыв'), CommInfoStateForm.FEEDBACK)
async def cmd_review(message: Message, state=FSMContext) -> None:
    await message.answer(text='Напишите свой отзыв:\n'
'Вы можете отправить несколько сообщений боту, прикрепить фото, голосовые сообщения и все что посчитаете нужным', reply_markup=kb.get_kb_send_review())
    
    await state.set_state(CommInfoStateForm.GET_REVIEW)
    await state.update_data(type='Отзыв')


@user_router_comm_info.message(F.text.contains('Отмена'), CommInfoStateForm.GET_REVIEW)
async def cmd_get_cancel(message: Message, state=FSMContext) -> None:
    await cmd_feedback_and_review(message, state)


@user_router_comm_info.message(F.text.contains('Отправить сообщения'), CommInfoStateForm.GET_REVIEW)
async def cmd_get_cancel(message: Message, state=FSMContext) -> None:
    await state.set_state(CommInfoStateForm.SEND_REVIEW)
    await cmd_send_review(message, state)


@user_router_comm_info.message(CommInfoStateForm.GET_REVIEW)
async def cmd_get_review(message: Message, state=FSMContext) -> None:
    state_data = await state.get_data()
    if not ('messages' in state_data):
        await state.update_data(messages=[])
    state_data = await state.get_data()

    copy_message = { 
        'from_chat_id' : message.chat.id, 
        'message_id': message.message_id,
        'message_thread_id' : message.message_thread_id
    }

    mes = state_data['messages'].append(copy_message)
    state.update_data(messages=mes)

    if settings.bots.number_messages_review == (len(state_data['messages'])):
        await state.set_state(CommInfoStateForm.SEND_REVIEW)
        await cmd_send_review(message, state)


@user_router_comm_info.message(CommInfoStateForm.SEND_REVIEW)
async def cmd_send_review(message: Message, state=FSMContext) -> None:
    await message.answer(text='Cпасибо за ваш отзыв')
    state_data = await state.get_data()

    for mes in state_data['messages']:
        await message.bot.forward_message(chat_id=settings.bots.manager_id, 
                                        from_chat_id=mes['from_chat_id'], 
                                        message_id=mes['message_id'],
                                        message_thread_id=mes['message_thread_id'],)
        
    await state.set_state(CommInfoStateForm.FEEDBACK)
    await cmd_feedback_and_review(message, state)


@user_router_comm_info.message(F.text.contains('Задайть вопрос менеджеру'), CommInfoStateForm.FEEDBACK)
async def cmd_question(message: Message, state=FSMContext) -> None:
    await message.answer(text='Напишите свой вопрос', reply_markup=kb.get_kb_back())
    await state.set_state(CommInfoStateForm.GET_QUESTION)
    await state.update_data(type='Вопрос')
    await state.update_data(user_name=message.from_user.username)


@user_router_comm_info.message(CommInfoStateForm.GET_QUESTION)
async def cmd_get_question(message: Message, state=FSMContext) -> None:
    await message.answer(text='Спасибо за ваш вопрос')
    await state.update_data(content=message.text)
    state_data = await state.get_data()

    await message.bot.send_message(chat_id=settings.bots.manager_id, text=text.get_text_state_data(state_data))

    await state.set_state(CommInfoStateForm.FEEDBACK)
    await cmd_feedback_and_review(message, state)
    # TODO сделать отправку фото менеджеру

# ------------------------------------------------------------------------------------
@user_router_comm_info.message(F.text.contains('Назад'), CommInfoStateForm.MENU)
async def cmd_back(message: Message, state=FSMContext) -> None:
    await cmd_menu(message, state)

@user_router_comm_info.message(F.text.contains('Назад'), CommInfoStateForm.FEEDBACK)
async def cmd_back(message: Message, state=FSMContext) -> None:
    await cmd_menu_comm_info(message, state)

@user_router_comm_info.message(F.text.contains('Назад'), CommInfoStateForm.GET_QUESTION)
async def cmd_back(message: Message, state=FSMContext) -> None:
    await cmd_feedback_and_review(message, state)

@user_router_comm_info.message(F.text.contains('Назад'), CommInfoStateForm.GET_REVIEW)
async def cmd_back(message: Message, state=FSMContext) -> None:
    await cmd_feedback_and_review(message, state)