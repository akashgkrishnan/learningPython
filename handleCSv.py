from csv import reader, DictReader
with open('fighters.csv') as file:
    csv_reader = reader(file)
    next(file)
    for row in csv_reader:
        print(f" {row[0]} is from {row[1]}")

print("_"*40)

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(f"{row['Name']} is from {row['Country']}")