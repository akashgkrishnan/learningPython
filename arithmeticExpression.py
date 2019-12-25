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
            print(a/b)
            print(float(c))
            if (a/b) == float(c):

                return True






a=8
b=2
c=4
print(arithmeticExpression(a, b, c))