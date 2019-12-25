def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value2 + value1
    elif value2 > value1 and weight2 <= maxW:
        return value2
    elif value1 > value2 and weight1 <= maxW:
        return value1
    
    elif min(weight1,weight2) > maxW:
        return 0
    else: 
        return value1
    


value1= 3
weight1= 4
value2= 5
weight2= 3
maxW= 3
 
print(knapsackLight(value1, weight1, value2, weight2, maxW))