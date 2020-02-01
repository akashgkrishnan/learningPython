def find_greater_numbers(nums):
    l = len(nums)
    count = 0
    for i in range(l):
        for j in range(i,l):
            if nums[i] < nums[j]:
                count += 1
    return count





print(find_greater_numbers([6,1,2,7]))