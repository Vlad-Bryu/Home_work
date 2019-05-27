def get_sum(num_one, num_two):
    try:
        sum_number = int(num_one) + int(num_two)
        print(sum_number)
    except ValueError:
        print('Кек. Введите другой тип данных')


get_sum(3, 5)







