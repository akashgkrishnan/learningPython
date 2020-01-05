def firstDigit(inputString):
    for i in list(inputString):
        if i.isnumeric():
            return i 




print(firstDigit("a a_933"))