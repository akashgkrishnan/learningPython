def list_manipulation(nums, command, location , val = 0):
    if command == "remove" and location == "end":
        return nums.pop()
    elif command == "remove" and location == "beginning":
        return nums.pop(0)
    elif command == "add" and location == "beginning":
        nums.insert(0, val)
        return nums
    elif command == "add" and location == "end":
        nums.append(val)
        return nums

print(list_manipulation([1,2,3], "remove", "beginning"))
