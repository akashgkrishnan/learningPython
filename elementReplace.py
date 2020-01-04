'''
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
        
    return inputArray
    '''

def arrayReplace(i, e, s):
    return [x if x!=e else s for x in i]

print(arrayReplace([1,2,1],1,3))