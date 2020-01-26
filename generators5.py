def get_unlimited_multiples(num = 1):
    n = 1
    while True:
        yield n * num
        n += 1

new = get_unlimited_multiples(5)

print(next(new))
print(next(new))
print(next(new))
print(next(new))
print(next(new))