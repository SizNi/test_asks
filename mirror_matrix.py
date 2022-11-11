import math

# мое решение
def mirror_matrix(mirror):
    if mirror == []:
        return []
    for elem in mirror:
        if len(elem) < 2:
            return None
        half_len = math.floor(len(elem) / 2)
        i = 1
        while i <= half_len:
            elem[-i] = elem[i-1]
            i += 1
    return mirror

# решение преподавателя

def mirror_matrix(matrix):
    if matrix:
        half_len = len(matrix[0]) // 2
        for line in matrix:
            line[half_len:] = line[-half_len - 1::-1]

l = [
    [42],
    [41],
]
 
mirror_matrix(l)