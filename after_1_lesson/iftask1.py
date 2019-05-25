print('введите возраст')
age = float(input())


def activity_person(age):
    if 3 <= age < 100:
        if age < 7:
            print('Вы в детском саде')
        elif age < 18:
            print('Вы учитесь в школе')
        elif age < 23:
            print('Вы учитесь в универе')
        elif age < 65:
            print('Вы работаете')
        elif age < 100:
            print('Вы пенсионер')
    else:
        print('Введите корректный возраст')


activity_person(age)
