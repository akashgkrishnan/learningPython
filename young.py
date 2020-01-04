def willYou(young, beautiful, loved):
    if loved:
        if young and beautiful:
            return False
        else:
            return True
    else:
        if young and beautiful:
            return True
        else:
            return False
    



print(willYou(True,False, True))