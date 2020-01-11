n = int(input("enter: "))
print() 
for i in range(n):
    print(' '*(n-i-1) + (str(i+1) + ' ')*(i+1))