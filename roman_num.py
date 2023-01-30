NUMERALS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


# BEGIN (write your solution here)
def to_roman(num):
    result = ''
    roman_num = list(NUMERALS.keys())
    roman_znach = list(NUMERALS.values())
    i = 0
    while i < len(roman_znach):
        if num < roman_znach[i]:
            i += 1
        else:
            num = num - roman_znach[i]
            result = result + roman_num[i]
    return result


def to_arabic(str):
    result = 0
    roman_num = list(NUMERALS.keys())
    i = 0
    while i < len(str):
        if str[i] not in roman_num:
            return False
        elif len(str) - i >= 2 and str[i] + str[i + 1] in roman_num:
            result += NUMERALS[str[i] + str[i + 1]]
            i+=2
        else:
            result += NUMERALS[str[i]]
            i += 1
    if str != to_roman(result):
        return False
    else:
        return result
# END
to_arabic('IIII')
