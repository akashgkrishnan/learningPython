def arrayMaximalAdjacentDifference(inputArray):
    min_no = -1000
    for i in range(len(inputArray)-1):
        diff = max(inputArray[i],inputArray[i+1]) - min(inputArray[i],inputArray[i+1])
        if diff > min_no:
            min_no = diff
        
    return min_no
            

inputArray= [2, 4, 1, 0]
print(arrayMaximalAdjacentDifference(inputArray))