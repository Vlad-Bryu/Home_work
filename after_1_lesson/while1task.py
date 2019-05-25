question_answer = {
        'Как дела?': 'Хорошо',
        'Что делаешь': 'Программирую',
        'Что программируешь': 'Тебя'
        }


def ask_user():
    x = 'Хорошо'
    y = 0
    while x != y:
        print('Как дела?')
        y = input()

    while True:
        user_say = input('Задайте вопрос: ')
        if user_say in question_answer:
            print(question_answer[user_say])
        else:
            print('Введите другой вопрос')


ask_user()