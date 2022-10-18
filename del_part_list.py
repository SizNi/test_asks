def odds_from_odds(list_list):  # функциональное решение задачи
    if list_list != [] and list_list != [[]]:
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


def keep_odds_from_odds(list_list):  # процедурное решение для удаления элементов
    i = 1  # два счетчика нужно для компенсации уменьшения длины списка после удаления элемента
    prev_i = 0
    while prev_i < len(list_list):
        print(prev_i, len(list_list))
        if list_list != [] and list_list != [[]]:
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
    print(list_list)



#a = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [0, 7, 8], [True, 2, 'aaaaa', 8]]
a = [[1, 2, 3, 4, 5], ['c', 'a', 't'], ['d', 'o', 'g'], [100, 200, 300, 400], [True, False], [], [],]
#print(a[::2][::2])
#odds_from_odds(a)


def delete_elem(list_list):
    new_list = list_list[::2]
    return new_list

def odds_from_odds2(list_list):
    print(list(map(delete_elem, list_list[::2])))
    return(list(map(delete_elem, list_list[::2])))


keep_odds_from_odds(a)



