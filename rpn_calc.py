import operator

# мое решение
def rpn_calc(lst):
    collection = ['+', '-', '*', '/']
    i = 0
    while i < len(lst):
        if lst[i] in collection:
            new_i = eval(f'{lst[i-2]}{lst[i]}{lst[i-1]}')
            lst.insert(i+1, new_i)
            del lst[i-2:i+1]
            i = 0
        else:
            i += 1
    return round(new_i)


# решение преподавателя
get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}.get


def rpn_calc(rpn):
    stack = []
    for elem in rpn:
        op = get_operator(elem)
        if op is not None:
            x = stack.pop()
            y = stack.pop()
            elem = op(y, x)
        stack.append(elem)
    return stack[0]
rpn_calc([1, 2, '+', 4, '*', 3, '/'])
