string = 'Word hello Who are you'
def invert_case(string):
    result = ''
    for char in string:
        result += char.swapcase()
    return result
