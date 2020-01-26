def amendTheSentence(s):
    ans = list(s)
    i = 0
    while i < len(ans):
        if ans[i].isupper():
            if i == 0:
                ans[i] = ans[i].lower()
            else:
                ans[i] = ans[i].lower()
                ans.insert(i, " ")
        i += 1   
         

    return "".join(ans)


            


    

print(amendTheSentence("YqRKKvLGYLwEFXcJiyYWLqjBvHjeqE"))
        


