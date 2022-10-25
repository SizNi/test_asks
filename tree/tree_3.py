import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile

# BEGIN
def compress_images(tree):  # получаем директорию
    children = get_children(tree)  # получаем каталог объектов в директории

    def reduce_image_size(node):  # почему то получает объект из children
        name = get_name(node)  # получаем имя объекта
        if not is_file(node) or not name.endswith('.jpg'):  # если объект не файл и не заканчивается на .jpg - не трогаем его
            return node
        meta = get_meta(node)  # иначе - получаем метаданные
        new_meta = copy.deepcopy(meta)  # делаем их глубокую копию
        new_meta['size'] //= 2  # new_meta[] = new_meta[]/2
        return mkfile(name, new_meta)  # возвращаем файл со старым именем и новой метой

    new_children = map(reduce_image_size, children) # используем map для применения функции на каждый объект списка чилдрен
    new_meta = copy.deepcopy(get_meta(tree))  # делаем глубокую копию меты директории
    return mkdir(get_name(tree), list(new_children), new_meta)  # возвращаем созданием директории имя, вложенные объекты списком и новую мету
# не забывать, что всегда работаем через создание новых объектов (пробовал с изменением меты на месте, почему-то тесты не проходит)
