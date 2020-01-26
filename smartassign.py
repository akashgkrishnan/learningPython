def smartAssigning(names, statuses, projects, tasks):
    if len == 1 and not statuses[0]:
        return names[0]
    else:
        i = 0
        while i < len(names):
            if not statuses[i] and tasks[i] == min(tasks) and len(set(tasks)) != 1:
                    return names[i]
                    
            if len(set(tasks)) == 1 and min(projects) == projects[i]:
                return names[i]
                
                
            elif statuses[i]:
                statuses.pop(i)
                tasks.pop(i)
                projects.pop(i)
                names.pop(i)
                i = 0
                continue
            i += 1



names =["John","Martin"]
statuses= [False, False]
projects= [1,2]
tasks= [6, 6]
print(smartAssigning(names, statuses, projects, tasks))