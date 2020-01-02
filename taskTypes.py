def tasksTypes(deadlines, day):
    ans = [0,0,0]
    deadlines.sort()
    for i in deadlines:
        if i <= day:
            ans[0] +=1
        elif i > day and i <= day + 7:
            ans[1] += 1
        else:
            ans[2] += 1
 
    return ans



print(tasksTypes([1, 2, 4, 2, 10, 3, 1, 4, 5, 4, 9, 8],1))