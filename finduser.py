from csv import DictReader
def find_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        i = 0
        for row in csv_reader:
            if row['First Name'] == first_name and row['Last Name'] == last_name:
                return i+1
            i += 1
        return f"{first_name} {last_name} not found"




print(find_user('Colt','Steele'))