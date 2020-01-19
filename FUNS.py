def show(x,y): #non default argument 
    print("x ", x)
    print("y ", y)

show(10,20) #positional argument 

show(x = 'x', y = 'k') # keyword argument
#show(x =20, y = 30, z = 40)
# positonal arguments should be before keyword argument
show(10, y = 20) 
