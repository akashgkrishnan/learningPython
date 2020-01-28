def intersection(l1, l2):
    return list(set(l1).intersection(set(l2)))

def intersection2(list1, list2):
    return [val for val in set(list1) & set(list2)]

def intersection3(l1, l2):
    return [val for val in l1 if val in l2]
    


print(intersection([1,2,3], [2,3,4]))