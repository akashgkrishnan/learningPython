def reverseInParentheses(inputString):
    #inputString = "foo(bar)baz"
    i = 0
    inputString_list = list(inputString)
    new_str = []
    rev_str = []
    while i < len(inputString_list):
        if inputString_list[i] == '(':
            i += 1
            j = i
            while inputString_list[j] != ')':
                rev_str.append(inputString_list[j])
                j += 1

            i = j + 1
            rev_str.reverse()
            rev_str = "".join(rev_str)
            new_str.extend(rev_str)
            rev_str = []
        else:
            new_str.append(inputString_list[i])
            i += 1
    new_str = "".join(new_str)
    return new_str

inputString = "foo(bar(baz))blim"
print(reverseInParentheses(inputString))



