def matmult(a, b):
    zip_b = list(zip(*b))
    print(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]

###
def matmult_1(a, b):
    zip_b = list(zip(*b))
    result_1 = []
    result_2 = []
    result_3 = []
    result_4 = []
    for row_a in a:
        for col_b in zip_b:
            #print(list(zip(row_a, col_b)))
            for elem_a, elem_b in zip(row_a, col_b):   
                result_1.append(elem_a * elem_b)
                print(result_1)
            result_2.append(result_1)
            result_1.clear
        print(result_2)
        return
        result_3.append(result_2)
        result_2.clear
    result_4.append(result_3)
    result_3.clear
    #print(result_4)
            

    
###  


A = [
  [2, 5],
  [6, 7],
  [1, 8],
]
B = [[1, 2, 1],
  [0, 1, 0],
]
zip_b = list(zip(*B))
#print(zip_b)
matmult_1(A, B)  # [[2, 9, 2], [6, 19, 6], [1, 10, 1]]