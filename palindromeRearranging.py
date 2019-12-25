def palindromeRearranging(inputString):
    count = 0
    str_set = set(inputString)
    str_set = list(str_set)
    for i in range(len(str_set)):
        if inputString.count(str_set[i])%2 == 0:
            count
        else:
            count += 1

    if count <= 1:
        return True
    else:
        return False

        
inputString = 'aabb'   
print(palindromeRearranging(inputString))