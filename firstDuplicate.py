def firstDuplicate(a):
    unique = set()
    print(f" set is :{unique}")
    for num in a:
        if num in unique:
            return num
        unique.add(num)
    return -1

firstDuplicate([2, 4, 3, 5, 1])