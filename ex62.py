L = [10, 20, 30, 40, 50]

try:
    INDEX = int(input("Enter a number[0-3]: "))
    print(L[INDEX])
except IndexError:
    print("invalid index, using -1 as default")
    INDEX = -1
    print(L[INDEX])
except ValueError:
    print("Invalid value")
print("bye")


'''
Try block 
it contains logically related statements whose execution may generate exception

after try block we must define either except or finally block

except block 
it is the handler of exception and executed only if an exception is generated from its try block

we may define one more block for a try

excepty blocks

it is a handler of exception 

try:
    stmt
except error1:
    stmt

try:
    stmt
except (error1, error2):
    stmt


try:
    stmt
except error1:
    stmt
except error2:
    stmt

we can also use parent exceptin block to handle all the exceptions  except stopiteration and keyboard interrupt


try:
    stmt
except:
    stmt

we maya lso use alia name in except block

try:
    stmt 
except eror name as e:
    stmt


order of execution


try:
    stmt

except specific:
    stms
except exception  -> parent
    stmt

except:
    stmt -> default

    




'''

