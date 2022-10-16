def invert_case(text): #меняет регистр на противоположный в полученной фразе
    i = 0
    new_text = ''
    while i < len(text):
        if text[i] == text[i].upper():
           new_text = f'{new_text}{text[i].lower()}'
           i += 1
        else:
            new_text = f'{new_text}{text[i].upper()}'
            i += 1
    return new_text 
