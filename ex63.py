'''
else block is only executed only when the try block is executed without any exception


try:
    stmt
except:
    stmt
else:
    stmt

stmt



finaly block 

'''
try:
    print(1)
except:
    print(2)
else:
    print(3)
finally:
    print(4)
print(5)


try:
    print(1)
    print(1/0)
except:
    print(2)
else:
    print(3)
finally:
    print(4)
print(5)


try:
    print(1)
    print(1/0)
except IndexError:
    print(2)
else:
    print(3)
finally:
    print(4)
print(5)


'''
finally block

this block is always executed no matter , there is an exception or not handled or not 

it means interpreter always gives the chance for finally block to execute its statement before program  termination 

finaly block may also generate exception 

generally , we use finaly block to free the resource like file, socket database

'''