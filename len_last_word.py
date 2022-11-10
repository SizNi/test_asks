# мое решение
import re
def length_of_last_word(phrase):
    phrase = phrase.strip()
    words_list = re.split(' |\n|\t', phrase)
    print(words_list)
    return len(words_list[-1])

# решение преподавателя


def length_of_last_word(string):
    words = string.split()  # не знал, что сплит по умолчанию делит по всем возможным разделителям
    if not words:
        return 0
    last_word = words[-1]
    return len(last_word)

length_of_last_word('man\nin\nBlack     ')