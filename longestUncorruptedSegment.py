def longestUncorruptedSegment(sourceArray, destinationArray):
    index = 0
    count = 0
    start = 0
    for i in zip(sourceArray,destinationArray):
        if i[0] != i[1] and index < len(sourceArray):
            count = 0
            start = index + 2
        else:
            count += 1
        index += 1
    if count-1 == len(sourceArray) or start == len(sourceArray) +1:
        return [0,0]
    else:
        return(count, start-1)


####not complete







sourceArray = [99919628, 77504204, 18846830, 86785029, 86230362, 96953294, 53208680, 95327090, 68996760, 26366538, 90490275, 62583792, 87514087, 96921389, 21309822]
destinationArray = [99919628, 77503204, 18546830, 86785029, 86230362, 96953264, 53208680, 95327090, 68996760, 26366538, 90420275, 62583792, 87514087, 39692139, 21303822]
print(longestUncorruptedSegment(sourceArray, destinationArray))

