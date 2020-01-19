def si():
    p = int(input("Enter Principle: "))
    r = int(input("Enter rate: "))
    t = int(input("Enter tenure: "))
    return f"SI: {p*r*t/100}"
print(si())