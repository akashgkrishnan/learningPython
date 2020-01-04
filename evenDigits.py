def evenDigitsOnly(n):
    n = str(n)
    for i in n:
        if int(i)%2 !=0:
            return False
    else:
        return True



''' alternatively it can be done using the following code in thhe following way

def evenDigitsOnly(n):
    return all([int(i)%2==0 for i in str(n)])

'''
        

print(evenDigitsOnly(24612))