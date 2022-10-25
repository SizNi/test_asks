import itertools

# Мое решение
def remove_first_level(tree):
    new_tree = []
    if tree != []:
        for elem in tree:
            if isinstance(elem, list):
                for elem_low in elem:
                    new_tree.append(elem_low)
        return new_tree
    else:
        return []


# Решение преподавателя
def remove_first_level(tree):
    children = filter(lambda item: isinstance(item, list), tree)
    return list(itertools.chain(*children))


remove_first_level([1, [2, 3], 4, [[5,6], 7]])