coll  = [2, 7, 3, 2, 4]
value =  'a'
index =  -10
length = len(coll)
if index < 0:
    if index < -length:
        index = 0
    else:
        index += length
print(coll.index(value, index))