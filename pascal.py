# мое решение (делал через создание всего треугольника Паскаля)


def pascal(n):
    if n == 1:
        return {1: [1]}
    p = pascal(n - 1)
    p[n] = list(map(sum, zip([0] + p[n - 1], p[n - 1] + [0])))
    return p

def triangle(n):
    if n < 0:
        return []
    elif n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        a = n + 1
        result = pascal(a)
        return result[a]


# Решение преподавателя


# Определяем функцию для вычисления факториала
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


# делал без построения всего треугольника, использовал формулу биноминального коэффициента


def triangle(row_number):
    numbers_count = row_number + 1
    line = []
    calculated = fact(row_number)
    for i in range(numbers_count):
        # Для вычисления числа заданной строки используем формулу
        # расчёта биноминальных коэффициентов С(n, k) = n! / (k! * (n - k)!)
        line.append(calculated / (fact(i) * fact(row_number - i)))
    return line


# что-то близкое к моему решению, но мне кажется слишком сложным
def triangle(row):
    line = [1]
    for i in range(row):
        line.append(line[i] * ((row - i) / (i + 1)))
    return line


from operator import add


def triangle(row_number):
    row = [1]
    for _ in range(row_number):
        row = list(map([x,y,z]
            add,         x y z 0
            row + [0],   + + + +
            [0] + row,   0 x y z
        ))
    return row
# END   

triangle(4)