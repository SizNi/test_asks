from hexlet.fs import get_children, get_name, is_file


# мое решение. Надо в дереве найти все скрытые файлы (начинающиеся на точку)
def get_hidden_files_count(tree):
    name = get_name(tree)
    if is_file(tree) and name.startswith('.'):
        return 1
    elif is_file(tree) and not name.startswith('.'):
        return 0
    children = get_children(tree)
    result = list(map(get_hidden_files_count, children))
    return sum(result)


# решение преподавателя:
def get_hidden_files_count(node):
    name = get_name(node)
    if is_file(node):
        return name.startswith('.')  # у преподавателя по другому реализована проверка на начальный знак,
    children = get_children(node)  # он объединил две моих проверки в одну
    hidden_files_count = list(map(get_hidden_files_count, children))
    return sum(hidden_files_count)
