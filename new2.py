def makeArrayConsecutive2(statues):
    count = 0
    statues.sort()
    print(statues)
    for i in range(len(statues)-1):
        print (f"{i}th iteration {statues[i]}")
        if statues[i+1]-statues[i] >=1:
            count += (statues[i+1]-statues[i])-1

    return count
    


print(makeArrayConsecutive2([6, 3]))
        
            
    
                
    


