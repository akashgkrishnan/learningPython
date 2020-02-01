
def sum_up_diagonals(nums):
    sum = 0
    l = len(nums)
    for i in range(l):
        sum += nums[i][i] + nums[i][l-i-1]
    

    return sum


list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]
print(sum_up_diagonals(list3))

    