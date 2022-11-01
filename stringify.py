def stringify(value, replacer=' ', space_count=1):
    if type(value) != dict:  # проверяем, словарь или нет
        return str(value)
    lines = ['{']  # открывающая скобка в начале итоговой сроки
    space = space_count  # начальное значение пробела, на него будем увеличивать отступ уровней
    lines = (_stringify(value, lines, replacer, space_count, space))
    lines.append('}')
    summ_str = ('\n'.join(lines))
    print(summ_str)
    return summ_str


def _stringify(value, lines, replacer, space_count, space):
    keys_dict = []
    kov = '{'  # почему-то не в двойных кавычках скобка не проходит, линтер ругается, убрал ее в переменную
    replacer_new = replacer * space_count  # задаем отступ как отступ*коэф
    keys_dict = value.keys()  # записываем ключи в список
    for elem in keys_dict:  # для каждого ключа в списке
        if type(value[elem]) == dict:  # если значение ключа - словарь
            lines.append(f'{replacer_new}{elem}: {kov}')  # вставляем ключ с открытой скобкой и увеличиваем отступ
            _stringify(value[elem], lines, replacer, space_count + space, space)  # вызываем рекурсию
            lines.append(replacer_new + '}')  # добавляем закрывающую скобку по старому реплейсеру (не из рекурсии)
        else:  # если значение -  не словарь
            lines.append(f'{replacer_new}{elem}: {value[elem]}')  # вставляем пробел, ключ, двоеточие и значение
    return lines
# END

value = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}
stringify(value, '|-', 2)