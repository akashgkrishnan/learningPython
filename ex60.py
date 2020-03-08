#2 types of error in python syntax and exception error
# error occured while machine code execution of byte code is called as exception error
# if any error related to logic or env then it is an exception
# logical or environmental
# FileNotFoundError
'''
exception
it is an unwanted condition that can occur in the program duriing compiled code execution
due to logical or env related error

it can terminate the program abnormally

commmonly used exceptions

IndexError
TypeError
ValueError
KeyError
ZeroDivisionError
FileNotFoundError
NameError



Exception handling is done to handle exceptions so that we can avoid abnormal program tremination

Following keywords are used in python for the purpose of handling exceptions


TRY
except
finally
raise
assert

'''




L = [10, 20, 30, 40, 50]

try:
    INDEX = int(input("Enter a number[0-3]: "))
    print(L[INDEX])
except (IndexError, ValueError):
    print("invalid index, using -1 as default")
    INDEX = -1
    print(L[INDEX])
print("bye")
