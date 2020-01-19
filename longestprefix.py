def longestDigitsPrefix(inputString):
    if inputString[0].isalpha():
        return ""
    ans = []
    for i in inputString:
        if i.isnumeric():
            ans.append(i)
        else:
            break
    return ''.join(ans)

print(longestDigitsPrefix('123aa1'))
