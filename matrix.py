def matrixElementsSum(matrix):
    sum = 0
    row = len(matrix)
    column = len(matrix[0])
    
    for r in range(row):
        for v in range(column):
            if r == 0:
                sum += matrix[0][v]
                if matrix[0][v] == 0:
                    for k in range(row):
                        matrix[k][v] = 0
            else:
                if v == 0:
                    if matrix[r-1][0] == 0:
                        sum
                    else:
                        sum += matrix[r][0]
                else:
                    if matrix[r-1][v] == 0:
                        sum

                    else:
                        sum += matrix[r][v]                          
        
    return sum

print(matrixElementsSum([[1,0,3], 
 [0,2,1], 
 [1,2,0]]))