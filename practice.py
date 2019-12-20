class human:
    no_of_humans = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        no_of_humans += 1 

    def __repr__(self):
        return f"My name is {self.name}"

    def total_humans():
        return no_of_humans
