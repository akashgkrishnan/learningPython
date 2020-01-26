def yes_or_no():
    l = ('yes', 'no')
    i = 0
    while True:
        if i == 1:
            yield l[i]
            i = 0
        else:
            yield l[i]
            i += 1

gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))