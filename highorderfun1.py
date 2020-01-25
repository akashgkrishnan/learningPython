'''
A function is said to be high order function if it takes a function as argument or returns a function
from the return statement

in python lib, there are some HOF
    map()
    filter()
    reduce()
'''

m = map(len, ['akash', 'akhila', 'christy'])
print(list(m))

m = map(max, ['akash', 'akhila', 'christy'])
print(list(m))

m = map(str.upper, ['akash', 'akhila', 'christy'])
print(list(m))
