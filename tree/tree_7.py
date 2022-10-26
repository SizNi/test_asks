from hexlet.fs import flatten, get_children, get_name, is_file
import os.path


# мое решение с комментариями (надо вернуть пусть для файлов, содержащих find_str)
def find_files_by_name(tree, find_str):
    ancestry = '/'  # чтоб начиналось с директории
    name = get_name(tree)
    children = get_children(tree)
    # если файл и в его имени есть наша часть
    if is_file(tree) and find_str in name:
        ancestry = os.path.join(ancestry, name)  # добавляем адрес
        print(ancestry)
        return ancestry  # возвращаем путь

    # внутреняя функция, нужна для передачи агрегатора ancestry, в который пишется путь
    def find(tree, find_str, ancestry):
        name = get_name(tree)
        ancestry = os.path.join(ancestry, name)
        # если файл и в его имени есть наша часть
        if is_file(tree) and find_str in name:
            return ancestry  # возвращаем путь
        children = get_children(tree)  # получаем детей
        ways = list(map(
            lambda child: find(child, find_str, ancestry),
            children,
            ))  # входим в рекурсию
        return flatten(ways)  # возвращаем размер всего что ниже
    ways = list(map(
        lambda child: find(child, find_str, ancestry),  # lambda нужна для вызова внутри нее функции с аргументами
        children,
        ))
    print(f'{flatten(ways)} in main')  # flatten - раскрывает все вложенные списки
    return flatten(ways)

# решение преподавателя:
def find_files_by_name(tree, substr):
    def walk(node, ancestry):
        name = get_name(node)
        new_ancestry = os.path.join(ancestry, name)
        if is_file(node):
            return [] if name.find(substr) < 0 else new_ancestry  # тут сократил условия
        children = get_children(node)
        paths = map(lambda child: walk(child, new_ancestry), children)  # тут не передавал substr
        return flatten(paths)
    return walk(tree, '')

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
tree2 = mkdir('firest', [
    mkfile('nginx.conf'),
    mkfile('coco.co'),
])
tree3 = mkfile('nginx.conf')
        
find_files_by_name(tree, 'co')
