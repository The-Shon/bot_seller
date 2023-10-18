def get_text_comm_info_main():
    return '''Связь/Инфо:

🛎 Обратная связь - напишите ваще мнение о нас

🌐 Соц.сети - следите за нами на других платформах

💭 FAQ - часто задаваемые вопросы

🗣️ Отзывы - посмотрите честные отзывы от наших покупателей'''


def get_text_state_data(state_data: dict) ->str:
    return f'''От пользователя - @{state_data['user_name']}
Тип сообщения - {state_data['type']}

Сообщение:

{state_data['content']} '''