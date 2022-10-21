def is_happy_ticket(number):
    if len(number) % 2 == 0:
        number_list = [int(elem) for elem in number]
        param = round(len(number)/2)
        print(param)
        print(sum(number_list[:param]))
        print(sum(number_list[param:]))
        if sum(number_list[:param - 1]) == sum(number_list[param:]):
            print(True)
        else:
            print(False)
    else:
        print(False)

is_happy_ticket('12344321')
