def two_oldest_ages(ages):
    return [sorted(ages)[-2], sorted(ages)[-1]]


print(two_oldest_ages( [1, 2, 10, 8] ))