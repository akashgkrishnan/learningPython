L = [10, 20, 30, 40, 50]

try:
    INDEX = int(input("Enter a number[0-3]: "))
    print(L[INDEX])
except Exception as e:
    print(e)
    print("invalid index, using -1 as default")
    INDEX = -1
    print(L[INDEX])
print("bye")



'''
stopiteration and keyboardinterupt are not the child of General Exception 
default except can handle all the exceptions including the stopiteration of general exception
'''


