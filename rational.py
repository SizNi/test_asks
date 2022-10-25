from math import gcd


# BEGIN (write your solution here)
def make(num, denom):
    gcd_all = int(gcd(num, denom))
    num = int(num/gcd_all)
    denom = int(denom/gcd_all)
    print({'num': num, 'denom': denom})
    return {
        'num': num,
        'denom': denom
    }


def get_numer(make):
    print(make['num'])
    return make['num']


def get_denom(make):
    print(make['denom'])
    return make['denom']

def add(num1, num2):
    num1_1 = get_numer(num1)
    denom1_1 = get_denom(num1)
    num2_2 = get_numer(num2)
    denom2_2 = get_denom(num2)
    num_all = (denom2_2 * num1_1) + (denom1_1 * num2_2)
    denom_all = (denom1_1 * denom2_2)
    gcd_num_denom = int(gcd(num_all, denom_all))
    num_all = int(num_all/gcd_num_denom)
    denom_all = int(denom_all/gcd_num_denom)
    print(f'{num_all}/{denom_all}')
    return {
        'num': num_all,
        'denom': denom_all
    }

        


def sub(num1, num2):
    num1_1 = get_numer(num1)
    denom1_1 = get_denom(num1)
    num2_2 = get_numer(num2)
    denom2_2 = get_denom(num2)
    num_all = (denom2_2 * num1_1) - (denom1_1 * num2_2)
    denom_all = (denom1_1 * denom2_2)
    gcd_num_denom = gcd(num_all, denom_all)
    num_all = int(num_all/gcd_num_denom)
    denom_all = int(denom_all/gcd_num_denom)
    print(f'{num_all}/{denom_all}')
    return {
        'num': num_all,
        'denom': denom_all
    }

# END


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"


object1 = make(4, 12)
object2 = make(9, 12)
get_numer(object1)
get_denom(object2)
add(object1, object2)
sub(object1, object2)