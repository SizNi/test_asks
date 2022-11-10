def hamming_weight(number):
    number_b = bin(number)
    print(number_b)
    print(type(number_b))
    print(number_b.count('1'))

hamming_weight(1000)