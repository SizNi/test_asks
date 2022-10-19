# мое решение
def number_of_unique_letters(str_word):  # подсчет количества уникальных букв в слове или фразе (без пробелов)
    return len({char: pos for pos, char in enumerate(str_word.lower())
    if char.isalpha()
    })


# решение преподавателя
def number_of_unique_letters(text):
    return len({char.lower() for char in text if char.isalpha()})