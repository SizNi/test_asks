from collections import Counter
import copy


# Мое решение
def visualize(coins, bar_char='₽'):
    big_bar_char = bar_char
    coins_count = dict(Counter(coins))
    keys_list = list(coins_count.keys())
    keys_list.sort()
    summ_list = []
    summ_list_all = []
    i = 0
    raws = []
    small_raws = []
    result = ''
    big_result = ''
    for elem in keys_list:
        summ_list.append(f'{elem}')
        summ_list.append('%')
        summ_list.append(f'{big_bar_char * coins_count[elem]}')
        summ_list.append(f'{coins_count[elem]}')
        obj = copy.deepcopy(summ_list)
        summ_list_all.append(obj)
        summ_list.clear()
    for i in range(4):
        raws.append(add_raws(summ_list_all, i))
    small_raws = make_matrix(raws)  # создаем матрицу
    small_raws = rotate_matrix(small_raws)  # переворачиваем ее
    for elem in small_raws:
        result = 'o'
        for deep_elem in elem:
            if deep_elem is not None and deep_elem.isdigit() == True and len(deep_elem) == 1:
                result += f' {deep_elem} '  
            elif deep_elem == bar_char:
                result += f' {deep_elem * 2}'
            elif deep_elem == None:
                result += '   '
            elif deep_elem == '%':
                a = '-'
                result = f' {a * (len(small_raws[0])* 3 - 1)}'
            else:
                result += f' {deep_elem}'
        result += 'ko'
        result = result.strip()
        result = result.replace("o ","")
        result = result.replace("ko","")
        big_result += f'{result}\n'
        result = ''
    big_result = big_result[:-1]
    return big_result
        

def add_raws(lst, i):
    small_raws = []
    for elem in lst:
        small_raws.append(elem[i])
    return small_raws


def make_matrix(raws):  # добавляет цифру в конец и None
    i = 0
    index = raws[2]
    value = raws[3]
    new_lst = []
    max_len = 0
    new_lst_2 = []
    summ_lst = []
    while i < len(index):
        new_lst.append(list(index[i] + value[i]))
        i += 1
    for elem in new_lst:
        if len(elem) > max_len:
            max_len = len(elem)
    for elem in new_lst:  # доделываем матрицу с индексам и значениями
        while len(elem) < max_len:
            elem.append(None)
    n = 0
    while n < len(raws[0]):  # присоединяем две нижних строчки
        new_lst_2.append(raws[0][n])
        new_lst_2.append(raws[1][n])
        new_lst_2.extend(new_lst[n])
        obj = copy.deepcopy(new_lst_2)
        summ_lst.append(obj)
        new_lst_2.clear()
        n += 1
    return summ_lst


def rotate_matrix(matrix):
    new_lst = []
    summ_lst = []
    i = len(matrix[0]) - 1
    while i >= 0:
        for elem in matrix:
            new_lst.append(elem[i])
        obj = copy.deepcopy(new_lst)
        summ_lst.append(obj)
        new_lst.clear()
        i -= 1
    return summ_lst

# решение преподавателя


def visualize(coins, bar_char='₽'):
    counts = Counter(coins)
    nominals = sorted(counts.keys())
    highest_stack = max(counts.values())

    rows = []
    delimiter = ''

    for level in range(highest_stack, -1, -1):
        row = ''
        for _, bar in sorted(counts.items()):
            if bar > level:
                row += f'{bar_char * 2} '
            elif bar == level and bar != 0:
                row += f'{bar:<2d} '
                delimiter += '---'
            else:
                row += '   '
        rows.append(row[:-1])

    rows.append(delimiter[:-1])
    row = ''
    for nominal in nominals:
        row += f'{nominal:<2d} '
    rows.append(row[:-1])

    return '\n'.join(rows)

coins = (
    1, 20, 2, 5, 20,
    3, 5, 2, 10, 2,
    20, 2, 20, 1, 2,
    1, 1, 2, 10, 20, 3,
)
visualize(coins)
