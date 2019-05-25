def get_sum():
    num_one = input()
    num_two = input()
    try:
        sum_number = int(num_one) + int(num_two)
        print(sum_number)
    except ValueError:
        print('Кек. Введите другой тип данных')


get_sum()







