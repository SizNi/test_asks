# Мое решение (найти длину отрезков, с учетом их пересечения)
def sum_of_intervals(lst):
    summ_len = 0
    lst_set = set()
    dif_list = []
    i = 0
    for elem in lst:
        elem_set = set(range(elem[0], elem[1]+1))
        if len(elem_set) < 2 and len(lst) < 2:
            elem_set.clear()
            i -= 1
        lst_set.update(elem_set)
    lst_list = list(lst_set)
    n = 1
    while n < len(lst_list):
        dif_list.append(lst_list[n] - lst_list[n-1])
        n += 1
    if all([x == 1 for x in dif_list]):
        i += 1
    else:
        i += 2
    summ_len = len(lst_set) - i
    print(summ_len)
    return summ_len

# решение преподавателя


def sum_of_intervals(intervals):
    values = []
    for start, end in intervals:
        for i in range(start, end):
            if i not in values:
                values.append(i)
    print(len(values))
    return len(values)
         


lst = [[2,7], [6, 6]]
sum_of_intervals(lst)