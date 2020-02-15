src = input("Enter source file: ")
des = input("Enter destination")
with open(src,'r')  as file:
    data = file.read()
    

with open(des, 'w') as file:
    file.write(data)

print("done")