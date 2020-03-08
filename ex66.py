'''

how to generate exception explicitely:

raise
assert

both keywords are used to generate exception based on the need of the application

eg: we may want to generate exception if program receive -ve age from user

syntax of raise:

 raise ExceptionName

or raise ExceptionName( 'message' )



assert keyword


it always generate assertion error
we need not write if stmt and we can directly write condition with assert

syntax: 

assert condition

or assert condition, 'msg'


condition is true -> do nothing
condition if false-> generate assertion error

assert statement can be ignored in runtime by using the following command
python -O filenam.py when run will omit the assrtions while run time

'''