class Human:
    no_of_humans = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Human.no_of_humans += 1 

    def __repr__(self):
        return f"My name is {self.name}"
    
    def total_humans(self):
        return Human.no_of_humans

    def print_the_Data(self,user_raw_data):
        for index, value in enumerate(user_raw_data):
            print(f"{value} is stored at {index+1}")


