import itertools
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

# решение учителя:

def stringify_1(value, replacer=' ', spaces_count=1):
    print
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):  # если не словарь - возвращаем строчное значение value
            return str(current_value)

        deep_indent_size = depth + spaces_count  # отсчет количества отступов
        deep_indent = replacer * deep_indent_size  # умножаем количество отступов на значение отступа - отступ следующего этапа
        current_indent = replacer * depth  # текущий отступ (в начале = 0, тк depth = 0)
        lines = []
        for key, val in current_value.items():  # для ключа и значения в value
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])  # добавляет открывающие и закрывающие скобки
        return '\n'.join(result)
    print(iter_(value, 0))
    return iter_(value, 0)

value1 = {
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
value = {
    "common": {
      "setting1": "Value 1",
      "setting2": 200,
      "setting3": 'true',
      "setting6": {
        "key": "value",
        "doge": {
          "wow": ""
        }
      }
    },
    "group1": {
      "baz": "bas",
      "foo": "bar",
      "nest": {
        "key": "value"
      }
    },
    "group2": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  }
value3 = {'  common': {'+ follow': False, '  setting1': 'Value 1', '- setting2': 200, '- setting3': True, '+ setting3': None, '+ setting4': 'blah blah', '+ setting5': {'+ key5': 'value5'}, '  setting6': {'  doge': {'- wow': '', '+ wow': 'so much'}, '  key': 'value', '+ ops': 'vops'}}, '  group1': {'- baz': 'bas', '+ baz': 'bars', '  foo': 'bar', '- nest': {'- key': 'value'}, '+ nest': 'str'}, '- group2': {'- abc': 12345, '- deep': {'- id': 45}}, '+ group3': {'+ deep': {'+ id': {'+ number': 45}}, '+ fee': 100500}}
# value = {'123': '12', 'affaf': '1dslmg'}
stringify_1(value3, '|~|', 1)