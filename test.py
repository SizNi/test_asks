def is_int(x):
    return isinstance(x, int)

def each2d(test, matrix):
    b = [elem_1 for elem_1 in [[test(elem) for elem in one_list] for one_list in matrix]]
    #print(all(all(elem_1) for elem_1 in ((test(elem) for elem in one_list) for one_list in matrix)))
    print(b)


def some2d(test, matrix):
    print(any(any(elem_1) for elem_1 in ((test(elem) for elem in one_list) for one_list in matrix)))


def sum2d(test, matrix):
    b = sum([sum([elem for elem in one_list if test(elem)]) for one_list in matrix])
    #print(sum(elem for elem in (elem_1 for elem_1 in (one_list for one_list in matrix)))
    print(b)


a = [[1, 'T'], [9, 10]]
#each2d(is_int, a)
#some2d(is_int, a)
sum2d(is_int, a)
