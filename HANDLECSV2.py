from csv import writer

with open("cats,csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "color"])
    csv_writer.writerow(["ktty", "black"])
    csv_writer.writerow(["frankie", 'brown'])