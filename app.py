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

USER = {"first_name":"Akash",
"age" :12, "fathers_name": "Gopala Krishnan",
"mother_name": "Thankamony g krishnan"
}
print("_"*20)
print(USER["first_name"])




