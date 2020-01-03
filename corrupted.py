def longestUncorruptedSegment(sourceArray, destinationArray):
    num = []
    for i in range(len(sourceArray)):
        if sourceArray[i] != destinationArray[i]:
            num.append(i)
    min = - 10
    if len(num) == 0:
        return [0,0]
    elif len(num) == 1:
        return [len(sourceArray) - num[0], num[0] + 1]
    else:
        for i in range(len(num)-1):
            if num[i+1]-num[i] > min:
                min = num[i+1] - num[i]
 