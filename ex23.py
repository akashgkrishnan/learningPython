def find_the_duplicate(nums):
    ans = set()
    for n in nums:
        if n in ans:
            return n
        else:
            ans.add(n)
    return None


print(find_the_duplicate([6,1,9,5,3,4,9]))
    