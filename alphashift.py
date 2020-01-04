def alphabeticShift(inputString):
    ans = list(inputString)
    return ''.join([chr(ord(i)+1) if ord(i) < 122 else 'a' for i in ans])

        

    

print(alphabeticShift('abc'))
print(ord('z'))