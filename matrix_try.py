def matrixElementsSum(matrix):
    for index,value in enumerate(matrix):
        print (index,value)
    sum = 0

    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])):
            if i == 0:
                sum += matrix[i][j]
            else:
                if matrix[i-1][i-1] ==0:
                    sum
                else:
                    sum += matrix[i][j]
    return sum


print(matrixElementsSum([[0,1,1,2],  [0,5,0,0],  [2,0,3,3]]))