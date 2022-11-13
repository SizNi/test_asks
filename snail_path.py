from itertools import chain

# мое решене (что-то кривое пипец, надо будет поправить)
def snail_path(lst):
    if lst == []:
        return []
    if len(lst) == 1:
        return lst[0]
    if len(lst[0]) == 1:
        print(list(chain(*lst)))
        return list(chain(*lst))
    len_x = len(lst[0])
    len_y = len(lst)
    summ_len = len_x * len_y
    x = 0
    y = 0
    dx = 0
    dy = 0
    summ_list = []
    i = 0
    while i < len_x + len_y:
        for dx in range(x, len_x):
            summ_list.append(lst[dy][dx])
        y += 1
        for dy in range(y, len_y):
            summ_list.append(lst[dy][dx])
        len_x -= 1
        for dx in reversed(range(x, len_x)):
            summ_list.append(lst[dy][dx])
        len_y -= 1
        for dy in reversed(range(y, len_y)):
            summ_list.append(lst[dy][x])
        x += 1
        i += 2
    summ_list = summ_list[:summ_len]
    print(summ_list)
    return summ_list

# решение преподавателя


def rotate(matrix):
    """
    Rotate the matrix counter-clockwise.

    >>> rotate([[1]])
    [(1,)]
    >>> rotate([[1, 2, 3]])
    [(3,), (2,), (1,)]
    >>> rotate([[1, 2], [3, 4]])
    [(2, 4), (1, 3)]
    """
    return list(reversed(list(zip(*matrix))))


def snail_path(matrix):
    path = []

    def trace(submatrix):
        if not submatrix:
            return
        path.extend(submatrix[0])
        trace(rotate(submatrix[1:]))
    trace(matrix)
    return path

# решение другого студента

def snail_path_1(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1]
        print(out)
        print(array)
    return out

            
snail_path_1([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ])