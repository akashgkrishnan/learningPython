
def multiply_even_numbers(collection):
    prod = 1
    for i in collection:
        if i%2 == 0:
            prod *= i
    
    return prod


print(multiply_even_numbers([1,2,3,4,5,6]))