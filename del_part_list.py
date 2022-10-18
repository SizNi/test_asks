def keep_odds_from_odds(list_list):  # процедурное решение для удаления элементов
    i = 1  # два счетчика нужно для компенсации уменьшения длины списка после удаления элемента
    prev_i = 0
    while prev_i < len(list_list):
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



a = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [0, 7, 8], [1, 3, 5, 6, 9]]
keep_odds_from_odds(a)
