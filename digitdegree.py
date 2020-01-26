def digitDegree(n):
    d=0
    while n>=10:
        n=sum([int(i) for i in str(n)])
        d+=1
    return d


print(digitDegree(9839))