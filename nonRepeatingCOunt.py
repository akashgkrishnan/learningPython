def firstNotRepeatingCharacter(s):
    for c in s:
        print(f"s.index  of {c} ={s.index(c)} s.rindex of {c} ={s.rindex(c)}")
        if s.index(c) == s.rindex(c):
            return c
    return '_'
        
s = "cdohzvvslmvchrcuydjxaoub"

print(firstNotRepeatingCharacter(s))