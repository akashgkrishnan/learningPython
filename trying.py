def reverseInParentheses(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


inputString = "foo(bar(baz))blim"
print(reverseInParentheses(inputString))
