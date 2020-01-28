def is_even(val):
    return val%2 ==0
    


def partition(lis, fn):
    truthy = []
    falsey = []
    for value in lis:
        if fn(value):
            truthy.append(value)
        else:
            falsey.append(value)
    return [truthy, falsey]


print(partition([1,2,3,4], is_even))

