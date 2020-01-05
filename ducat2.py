print("------continue------")
for i in range(5):
    print("apple")
    if i < 3:
        continue
    print("mango")

print("------break-----")

for i in range(5):
    print("apple")
    if i > 3:
        break
    print("mango")