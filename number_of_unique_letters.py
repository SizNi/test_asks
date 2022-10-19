#def number_of_unique_letters(str_word):
    #char in enumerate(str_word)
str_word = ' '
print({len(char): pos for pos, char in enumerate(str_word.lower()) if char.isalpha()==True})