def isIPv4Address(inputString):
    count = 0
    inputString = inputString.split(".")
    if len(inputString) == 4:
        for i in range(len(inputString)):#len(inputString) == 4:
            if inputString[i].isnumeric(): 
                if int(inputString[i]) >= 256 or inputString[i] == '' or inputString[i].isalpha():
                    return False
                else:
                    count += 1
            else:
                return False    
    else:
        return False

    if count == 4:
        return True


print(isIPv4Address("172.16.254.1"))