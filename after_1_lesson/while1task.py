question_answer = {
        'Как дела?': 'Хорошо',
        'Что делаешь': 'Программирую',
        'Что программируешь': 'Тебя'
        }


def ask_user():
    users_answer = 0
    while 'Хорошо' != users_answer:
        users_answer = input('Как дела?\n')

    while True:
        user_say = input('Задайте вопрос:\n')
        if user_say in question_answer:
            print(question_answer[user_say])
        else:
            print('Введите другой вопрос')


ask_user()