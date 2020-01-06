def sumOfTwo(a, b, v):
    if not a or not b:
        return False
    
    
    b = set(b)
    
    for x in a:
        if v-x in b:
            return True
        
    return False

        

