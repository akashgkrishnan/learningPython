l = [10,20,30,40,80,20,20]
print(l)
for i in l:
    print(i)

l.append(50)
print(l)

l.insert(1,60)
print(l)

del l[0]
print(l)

e = l.pop(0)
print(l)
print(e)

l.remove(20)
print(l)

l.clear()
print(l)