# мое решение
def transposed(matrix):
    trans_matrix = [
        [0 for j in range(len(matrix))] for i in range(len(matrix[0]))
    ]
    for i in range(len(matrix)):
        print(i)
        for j in range(len(matrix[i])):
            trans_matrix[j][i] = matrix[i][j]
    return(trans_matrix)

# решение преподавателя


def transposed(matrix):
    result = []
    for column in zip(*matrix):
        result.append(list(column))
    return result

transposed([[]])