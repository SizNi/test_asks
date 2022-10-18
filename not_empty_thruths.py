def non_empty_truths(list_of_lists):  # решение преподавателя
    print([truths for truths in 
    [[elem for elem in one_list if elem] 
    for one_list in list_of_lists] 
    if truths
    ])
    
a = [[0, 1, 2], [], [], [False, True, 42], [[[]]]]
non_empty_truths(a)

# расшифровка решения преподавателя:
# 1. самый вложенный список [elem for elem in one_list if elem]
res_1 = []
for elem in one_list:  # перебор элементов во вложенных списках
    if elem == True:  # определение типа элемента
            res_1.append(elem)  # если это не false элементы - добавление их в список
# 2. второй по вложенности список [...for one_list in list_of_lists]
for one_list in list_of_list: # перебор вложенных списков в оригинальном списке и отправка one_list на уровень 1
# 3. внешний список [truths for truths in ... if truths]
res_3 = []
for truths in res_1:  # для элементов truths в списке res_1
    if truths == True:  # если элементы соответсвуют True
        res_3.append(res_1) # добавь элемент в результирующий список
        return res_3


    




