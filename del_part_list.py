def odds_from_odds(list_list):  # процедурное решение № 1 через создание нового списка
    new_list = []
    i = 0
    while i < len(list_list):
        i_i = 0
        small_new_list = []
        while i_i < len(list_list[i]):
            small_new_list.append(list_list[i][i_i])
            i_i += 2
        new_list.append(small_new_list)
        i += 2
    print(new_list)


def keep_odds_from_odds(list_list):  # процедурное решение № 2 с изменение списка на месте
    i = 1  # два счетчика нужно для компенсации уменьшения длины списка после удаления элемента
    prev_i = 0
    while prev_i < len(list_list):
        print(prev_i, len(list_list))
        if i == prev_i:  # тут удаляется элемент внешнего списка если он нечетный
            del list_list[i]
            i += 1
        else:  # тут происходит работа с четными вложенными списками
            i_i = 1  # два счетчика нужно для компенсации уменьшения длины списка после удаления элемента
            prev_i_i = 0
            while i_i < len(list_list[prev_i]):
                if i_i == prev_i_i:  # удаление четного элемента списка
                    del list_list[prev_i][i_i]
                    i_i += 1
                else:
                    prev_i_i += 1
            prev_i = i




#a = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [0, 7, 8], [True, 2, 'aaaaa', 8]]
#a = [[1, 2, 3, 4, 5], ['c', 'a', 't'], ['d', 'o', 'g'], [100, 200, 300, 400], [True, False], [], [],]
a = [[]]
#print(a[::2][::2])
#odds_from_odds(a)


def delete_elem(list_list):
    new_list = list_list[::2]
    return new_list

def odds_from_odds2(list_list):  # функциональное решение № 1
    print(list(map(delete_elem, list_list[::2])))
    return(list(map(delete_elem, list_list[::2])))


keep_odds_from_odds(a)

# два решения преподавателя
# BEGIN
def odds(source):
    is_odd_position = lambda pair: pair[0] % 2 == 0  # noqa: E731
    get_value = lambda pair: pair[1]  # noqa: E731
    return list(map(
        get_value,
        (filter(is_odd_position, enumerate(source)))
    ))


def odds_from_odds(list_of_lists):
    return list(map(odds, odds(list_of_lists)))

# Альтернативное решение с помощью itemgetter
# https://docs.python.org/3/library/operator.html#operator.itemgetter
#
# odds = itemgetter(slice(None, None, 2))
#
# def odds_from_odds(list_of_lists):
#     return list(map(odds, odds(list_of_lists)))


def keep_odd(some_list):
    index = 0
    for i in range(len(some_list)):
        if i % 2 == 1:
            some_list.pop(index)
        else:
            index += 1


def keep_odds_from_odds(list_of_lists):
    keep_odd(list_of_lists)
    for one_list in list_of_lists:
        keep_odd(one_list)
# END



