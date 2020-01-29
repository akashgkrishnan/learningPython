def find_factors(num):
    return [i for i in range(1,num+1) if num %i == 0]



print(find_factors(412146))