def reorderingOfProducts(boundaries, y):
    boundaries.insert(0, -float('inf'))
    l = 0
    r = len(boundaries) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if y > mid:
            l = mid
        else:
            r = mid
    return l


boundaries= [0, 10, 50, 100, 120]
y= 45
print(reorderingOfProducts(boundaries,y))

