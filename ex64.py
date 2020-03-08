try:
    print(1)
    try:
        print(1/0)
    finally:
        print(2)
    print(3)
except:
    print(4)

print(5)