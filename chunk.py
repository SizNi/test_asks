from itertools import islice

# Мое решение
def chunked(number, seq):
    start_number = 0
    end_number = number
    seq_result = []
    while end_number <= len(seq):
        seq_part = islice(seq, start_number, end_number)
        start_number += number
        end_number += number
        seq_result.append(format(seq_part, seq))
    if end_number != len(seq) and start_number != len(seq):
        seq_result.append(format(seq[start_number:], seq))
    return seq_result

        
def format(seq_part, seq):
    if isinstance(seq, str):
        return (''.join(seq_part))
    if isinstance(seq, tuple):
        return tuple(seq_part)
    if isinstance(seq, list):
        return list(seq_part)

# Решение преподавателя
def chunked(size, source):
    result = []
    index = 0
    while index < len(source):
        result.append(source[index:index + size])
        index += size
    return result     


value = (['a', 'b', 'c', 'd'])
chunked(2, value)
