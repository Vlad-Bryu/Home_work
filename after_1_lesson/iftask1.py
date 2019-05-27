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
        else:
            print('Вы пенсионер')
    else:
        print('Введите корректный возраст')


age = int(input('Введите возраст целым числом: '))
activity_person(age)
