def sum_even_value(*args):
    return sum(x for x in args if x % 2 == 0 )

print(sum_even_value(1,3,5))