from practice import human
from random import choice

def getUserInput():
    name = input("enter name:")
    age = int(input("enter age: "))
    gender = input("Enter gender M/F: ")
    return name,age,gender 

nam,ag,gend = getUserInput()
new_human = human(nam,ag,gend)

print(new_human.total_human())
