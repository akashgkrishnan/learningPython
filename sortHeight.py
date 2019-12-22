def sortByHeight(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] != -1:
                if a[i] < a[j]:
                    a[i],a[j] = a[j], a[i]
    return a



a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))