'''

exception handling in function

a function either returns  actual value of return stmt or exception to the calling code

we may handle exception in 2 ways:
in function itself
in calling code

exp:

def show(): # in function itself
    try:
        stmt
    exception:
        stmt


#in calling code itself

def show():
    stmt

try:
    show()
except()
    stmt


    is it possible to execute statement of a function after return statement>?
    ans yes
    we may write finally , and finaly is always executed even after try contains returns statement


    def show():
        try:
            return 0
        finaly:
            return 1
    print(show()) --> this would always print 1 no matter what is returned from the try

'''