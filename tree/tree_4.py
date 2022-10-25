import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# мое решение (задача - рекурсивно обойти дерево и все названия файлов привести к нижнему регистру):
def downcase_file_names(tree):
    name = get_name(tree)
    meta = copy.deepcopy(get_meta(tree))
    if is_file(tree):
        name = name.lower()
        return mkfile(name, meta)
    children = get_children(tree)
    new_children = list(map(lambda child: downcase_file_names(child), children))
    new_tree = mkdir(name, new_children, meta)
    return new_tree


# решение преподавателя:

def downcase_file_names(node):
    new_meta = copy.deepcopy(get_meta(node))
    name = get_name(node)
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    children = get_children(node)
    new_children = map(downcase_file_names, children)
    return mkdir(name, list(new_children), new_meta)

