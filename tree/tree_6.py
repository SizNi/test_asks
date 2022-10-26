from hexlet.fs import get_children, get_meta, get_name, is_file
from hexlet.fs import mkdir, mkfile


# BEGIN (write your solution here)
def calculate_entry_size(tree):  # функция, считающая размер фалов
    if is_file(tree):  # если файл - верни размер
        meta = get_meta(tree)  # получаем мета-данные
        return meta['size']  # возвращаем данные по размеру
    children = get_children(tree)  # получаем детей
    sizes = list(map(calculate_entry_size, children))  # входим в рекурсию
    return sum(sizes)  # возвращаем размер всего что ниже


def du(tree):  # основная функция
    children = get_children(tree)  # получаем детей
    result = list(map(
        lambda child: (get_name(child), calculate_entry_size(child)),
        children,
    ))
    result.sort(key=lambda entry: entry[1], reverse=True)  # сортируем по ключу entre[1] в обратном порядке
    print(result)
    return result

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
du(tree)