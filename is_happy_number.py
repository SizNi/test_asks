def sum_of_square_digits(number): # вычисляет сумму квадратов цифр числа
    return sum(int(x) ** 2 for x in str(number))


def is_happy_number(number): # ищет счастливое число, которое за 10 итераций пришло к 1
    i = 0
    result = number
    print(number)
    while i < 10:
        if result != 1:
            result = sum_of_square_digits(result)
            i += 1
        else:
            return True
    return False
