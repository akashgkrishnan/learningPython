def isLucky(n):
    sum1 = 0
    sum2 = 0
    n = str(n)
    
    for i in range(0,int(len(n)/2)):
                   sum1 += int(n[i])
                   
    for i in range(int(len(n)/2),len(n)):
                   sum2 += int(n[i])
                   
    if sum1 == sum2:
        return True
    else:
        return False


print(isLucky(1230))