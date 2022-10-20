def my_map(f, xs):  # упрощенная версия map
    for item in xs:
        yield f(item)


def my_filter(f, xs):  # упрощенная версия filter
    for item in xs:
        if f(item):
            yield item


def replicate_each(n, xs):  # увеличивает количество каждого элемента итерируемого xs в n раз
    for elem in xs:
        i = n
        while i > 0:
            yield elem
            i -= 1

    