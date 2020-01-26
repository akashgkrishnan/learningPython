i = 10  # here i is not callable 
print(i)

def add():
    return "this is add: "

i = add
print(i()) # here i is pointing to add and made callable
'''
A variable is callable if it points to functions def in memory
'''