from csv import writer, DictReader

def add_user(first_name,last_name):
    with open("users.csv" , "a") as file:       
        csv_writer = writer(file)
        csv_writer.writerow([first_name,last_name])

def all_user(file_name):
    print("All user function to the resque")
    with open(file_name) as file:
        csv_reader = DictReader(file)
        for f in csv_reader:
            print(f['First Name'], f['Last Name'])


#inp = int(input("How much names you want to store: ?"))
#for i in range(inp):
 #   first_name = input(f"Enter First name of {i+1}th user: ")
 #   last_name = input(f"Enter last name of {i+1}th user: ")
 #   print()
 #   add_user(first_name,last_name)


all_user('users.csv')
