def sumInRange(nums, queries):
    new_list = []
    for i in queries:
        new_list.append(sum(nums[i[0]:i[1]+1]))
    return sum(new_list) % (10**9 + 7)




nums = [-4, -18, -22, -14, -33, -47, -29, -35, -50, -19]
queries = [[2,9],  [5,6], [1,2],  [2,2],  [4,5]]


print(sumInRange(nums,queries))