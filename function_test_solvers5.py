# BEGIN (write your solution here)
import copy
coll = [1, 2, 3, 4]
def fill(coll, value, begin = 0, end = None):
    if end == None:
        end = len(coll)
    elif end > len(coll):
        end = len(coll)
    while begin < end:
        coll[begin] = value
        begin += 1
    print(coll)
    return coll
fill(coll, '*', 0, 10)
# END
