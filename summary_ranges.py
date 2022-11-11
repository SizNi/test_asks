# мое решение
def summary_ranges(lst):
    if len(lst) < 2:
        return []
    start = 0
    end = 1
    result = {}
    result_list = []
    while end < len(lst):
        if lst[end-1] == lst[end]-1:
            result[lst[start]] = lst[end]
            end += 1
        else:
            start = end
            end += 1
    i = 0
    keys_list = list(result.keys())
    print(keys_list)
    values_list = list(result.values())
    print(values_list)
    while i < len(result):
        result_list.append(f'{keys_list[i]}->{values_list[i]}')
        i += 1
    print(result_list)
    return result_list

# решение преподавателя

def summary_ranges(numbers):
    if not numbers:
        return []

    ranges = []
    current_sequence = [numbers[0]]
    sequences = [current_sequence]

    for x, y in zip(numbers, numbers[1:]):
        if (y - x) == 1:
            current_sequence.append(y)
        else:
            current_sequence = [y]
            sequences.append(current_sequence)

    # здесь [0, 1, 2, 7, 5, 6] уже преобразован
    # в [[0, 1, 2], [7], [5, 6]]

    for sequence in sequences:
        if len(sequence) > 1:
            first, last = sequence[0], sequence[-1]
            ranges.append(f'{first}->{last}')

    return ranges

lst = [0, 1, 2, 7, 5, 6]
summary_ranges(lst)