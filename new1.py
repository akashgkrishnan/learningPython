def adjacentElementsProduct(inputArray):
    max = -100
    for num in range(len(inputArray)-1):
        if num < len(inputArray):
            prod = inputArray[num] * inputArray[num +1]
            if prod > max:
                max = prod              
                
    return max

print(adjacentElementsProduct([-23, 4, -3, 8, -12]))
                
            
                  
    

