def encrypt(word):
    b = [word[x:x+2][::-1] for x in range(0, len(word), 2)]
    result = ''.join(b)
    print(result)
    return result