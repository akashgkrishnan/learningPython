def arithmeticExpression(a, b, c):
    ops = ['+','-','*','/']
    for i in range(4):
        if ops[i] == '+':
            if a + b == c:
                return True
        elif ops[i] == '-':
            if a - b == c:
                return True
        elif ops[i] == '*':
            if a *b ==c:
                return True
        else:
            if (a/b) == float(c):
                return True
            else:
                return False