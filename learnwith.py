with open('akash.txt') as file:
    data = file.readline()
    data2 = file.read()
    print(file.closed)

print(data)
print(data2)
print(file.closed)



    