# Modules  moduls is an independent part of a program which is used along with other files 
# The file which the interpreter will first run in a big software is called as script and the rest of the files are 
# called modules
# defintitions and classes and statements . variables these are what is contained in a python file
# module is a python file that may contain def and stmts
# Advantages of modules -> easy maintainence of application     -> reusability of code      -> reduce development time
# by developing parallely its modules
# How to use modules    -> use import key word 
# import module_name 
# module.name (for using)
# interpreter provides a special name __name__ to each python file 
# value of this variable is __main__ if this python file is executed as script and the value of __name__ is same as module
# name if the python file is executed as module
# from module_name import function_name
# from module import func1 as a, func2 as b
# a() b()
# from module _name import * - > loads every def in the module

from arith import add as a, mul as b

print(a(5,6))
print(b(30,30))

