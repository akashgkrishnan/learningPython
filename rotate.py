def rotateImage(a):

    a.reverse()
    print(f"a = {a}")
    for i in range(len(a)):
        for j in range(i):
            a[i][j],a[j][i] = a[j][i],a[i][j]

    return a
    






a = [[1, 2, 3], [4, 5, 6],  [7, 8, 9]]
print(f"answer:{rotateImage(a)}")