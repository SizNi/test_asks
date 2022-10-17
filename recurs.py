def length(num_list, len_list = 0):  # принимает список и возращает его длинну
    if num_list == []:  # проверка на пустой список
        return len_list
    else:
        del num_list[0]  # удаляем первый член списка
        len_list += 1  # прибавляем к счетчику 1
        return length(num_list, len_list)


length([1, 2, 3])


def reverse_range(begin, end, memory = []):  # получает начало и конец, то что между ними надо выдать списком и перевернуть
    if begin <= end:
        memory.append(end)
        end -= 1
        return reverse_range(begin, end, memory)
    else:
        memory_ret = memory.copy()
        memory.clear()
        return memory_ret


reverse_range(1, 10)


def filter_positive(num_list, new_num_list = [], i = 0):
    if i < len(num_list):
        if num_list[i] > 0:
            new_num_list.append(num_list[i])
            i += 1
            return filter_positive(num_list, new_num_list, i)
        else:
            i += 1
            return filter_positive(num_list, new_num_list, i)
    else:
        new2_num_list = new_num_list.copy()
        new_num_list.clear()
        return new2_num_list
        
    
filter_positive([1, -2, 3])
        
            




