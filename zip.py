def interleave(string1, string2):
    ans = []
    z = list(zip(string1,string2))
    for i in z:
        ans.append(''.join(i))
    return ''.join(ans)


#   return ''.join(''.join(x) for x in (zip(str1,str2)))

print(interleave('hi','ha'))