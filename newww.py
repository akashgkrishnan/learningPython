def leastFactorial(n):
    m=1
    count=0
    while m < n:
        count += 1
        m *= count
    return m