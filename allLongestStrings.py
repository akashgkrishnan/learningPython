def allLongestStrings(inputArray):
    length = len(inputArray)
    biggest_String = 0
    new_list = []
    for i in range(length):
        if len(inputArray[i]) > biggest_String:
            biggest_String = len(inputArray[i])
        
    for i in range(length):
        if len(inputArray[i]) == biggest_String:
            new_list.append(inputArray[i])

    return new_list   



inputArray = ["aba",  "aa",  "ad",  "vcd", "aba"]
print(allLongestStrings(inputArray))