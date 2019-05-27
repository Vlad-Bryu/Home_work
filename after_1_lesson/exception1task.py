question_answer = {
        'Как дела?': 'Хорошо',
        'Что делаешь': 'Программирую',
        'Что программируешь': 'Тебя'
        }


def ask_user():
        try:
            users_answer = 0
            while 'Хорошо' != users_answer:
                users_answer = input('Как дела? ')

            while True:
                user_say = input('Задайте вопрос: ')
                if user_say in question_answer:
                    print(question_answer[user_say])
                else:
                    print('Введите другой вопрос')
        except KeyboardInterrupt:
            print('Пока!')


ask_user()
