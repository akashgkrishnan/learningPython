def fixMessage(message):
    return adjust(message)

def adjust(a):
    a = list(a)
    for i in range(len(a)):
        if i == 0:
            a[i] = a[0].upper()
        else:
            a[i] = a[i].lower()
    
    return ''.join(a)

print(fixMessage("you'll NEVER believe what that 'FrIeNd' of mine did!!1"))