for i in range(5):
    for k in range(i):
        print(' ', end = ' ')
    for j in range(5,i, -1):
        print(j, end = ' ')
    print()


for i in range(1,5):
    for k in range(i):
        print(' ', end = ' ')
    for j in range(1,7-i):
        print(j, end = ' ')
    print()
    
print(22/7)