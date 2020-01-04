def longestUncorruptedSegment(sourceArray, destinationArray):
    if len(sourceArray) == 0 and sourceArray[0] == destinationArray[0]:
        return [0,0]