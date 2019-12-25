def avoidObstacles(inputArray):
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1  



inputArray = [5, 3, 6, 7, 9]
print(avoidObstacles(inputArray))
