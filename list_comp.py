l = [] 
for i in range(3):
    for j in range(3):
        l.append(i*j)
print(l)

l = [i*j for i in range(3) for j in range(3)]
print(l)

