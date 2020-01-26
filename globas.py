x = 10
print(x)
if True:
    x = 20

def show():
    global x
    print(x)
    x += 20
show()
print(x)



def show1():
    x = 10
    def disp():
        nonlocal x
        x = 20
    disp()
    print(x)

show1()