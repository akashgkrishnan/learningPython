l =[]
for i in range(5):
    sal = int(input("enter salary: "))
    l.append(sal)

print(l)
l.sort(reverse=True)
print(l[0:3:1])
