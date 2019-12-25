def arrayChange(inputArray):
    count = 0
    i = 0
    for i in range(len(inputArray)-1):
        if inputArray[i]>inputArray[i+1]:
            count += inputArray[i]-inputArray[i+1] + 1
            inputArray[i+1] = inputArray[i] + 1 
            i -= 1
        elif inputArray[i] == inputArray[i+1]:
            inputArray[i+1] += 1
            count += 1
            
        else:
            inputArray[i]
    return count

inputArray = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
print(arrayChange(inputArray))

