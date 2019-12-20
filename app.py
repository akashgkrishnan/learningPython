from practice import Human
from random import choice

def getUserInput():
    name = input("enter name:")
    age = int(input("enter age: "))
    gender = input("Enter gender M/F: ")
    return name,age,gender 

nam,ag,gend = getUserInput()
new_human = Human(nam,ag,gend)

print(f"The total number of active users we have is: {Human.no_of_humans}")

data = ['1','2',3, 'akash g krishnan']

new_human.print_the_Data(data)



