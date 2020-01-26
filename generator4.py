def get_multiples(num  = 1, count = 10):
    for i in range(1,count+1):
        yield i * num
    

events = get_multiples(2, 3)
print(next(events))
print(next(events))
print(next(events))

