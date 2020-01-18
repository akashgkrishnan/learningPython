with open("created_from_python.txt", "w") as file:
    file.write("my name is akash \n")
    file.write("i am a beginner in python \n" )
    file.write("i am learnign file handling \n")
    print(file.closed)
print(file.closed)

with open("created_from_python.txt") as file:
    print(file.read())
    file.seek(10)
    print(file.read())

with open("created_from_python.txt", "a") as file:
    file.write("\nmy name is akash  3 \n")
    file.write("i am a beginner in python 3 \n" )
    file.write("i am learnign file handling 3 \n")
    print(file.closed)
print("\n"*100)
with open("created_from_python.txt") as file:
    print(file.read())
    file.seek(10)
    print(file.read())

