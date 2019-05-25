question_answer = {
        'Как дела?': 'Хорошо',
        'Что делаешь': 'Программирую',
        'Что программируешь': 'Тебя'
        }


def ask_user():
    while True:
        try:
            print('Как дела?')
            y = input()
        except KeyboardInterrupt:
            print('Пока!')
            break



ask_user()
