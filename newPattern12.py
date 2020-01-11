n = int(input("Enter: "))
for i in range(n):
    print(" "*i, end = ' ')
    for j in range(n-i):
        print(chr(65 + j), end = ' ')
    print()
    