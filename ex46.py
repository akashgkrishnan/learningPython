file = open('msg.txt', 'w+')
print(file.tell())
file.write("ducat india")
print(file.read())
file.seek(0)
print(file.read())
file.close()

"""
with statement is used for automatically closing a resource


with resource as alias:
    set of statements
    opening a DB
    opening a file 
    opening and closing socket 
    etc are the type of resources which can be opened and closed using the with statemnets

advantages are that we dont need to close or flush a resource it will be done automatically
As soon as the with block is completed the resource gets automatically closed
"""