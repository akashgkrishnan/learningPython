def sum_pairs(nums, val):
    for i in range(len(nums)-1):
        if nums[i] + nums[i+1] == val:
            return [nums[i], nums[i+1]]
    return []




print(sum_pairs([11,20,4,2,1,5], 100))