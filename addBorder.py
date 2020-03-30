def addBorder(picture):
    for i in range(len(picture)):
        picture[i] = list(picture[i])
        picture[i].insert(0,"*")
        picture[i].append("*")
        picture[i] = "".join(picture[i])
        
    len_val = len(picture[0])
    picture.insert(0,"*"*(len_val))
    picture.append("*"*(len_val))
    print("hi")

    return picture

    
    


picture = ["abc","ded"]
print(addBorder(picture))
    

