def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    return inputArray

def extractEachKth_1(inputArray, k):
    return [i for (n,i) in enumerate(inputArray) if (n+1) % k != 0]