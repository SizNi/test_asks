def is_int(x):
    return isinstance(x, int)

def each2d(test, matrix):
    return all(all(elem_1) for elem_1 in ((test(elem) for elem in one_list) for one_list in matrix))


def some2d(test, matrix):
    return any(any(elem_1) for elem_1 in ((test(elem) for elem in one_list) for one_list in matrix))


def sum2d(test, matrix):
    return sum((sum((elem for elem in one_list if test(elem))) for one_list in matrix))



a = [[1, 'T'], [9, 10]]
#each2d(is_int, a)
#some2d(is_int, a)
sum2d(is_int, a)
