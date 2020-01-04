def variableName(name):
    for i in range(len(name)):
        if name[0].isnumeric():
            return False
        elif name[i].isalnum() or name[i] == '_':
            continue
        else:
            return False
    else:
        return True


'''' 
which can alternately be done by the underspecified way:

def variableName(name):
    return name.isidentifier()
'''

print(variableName("a-bc"))


