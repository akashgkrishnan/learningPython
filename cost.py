def fancyRide(l, fares):
    cost = []
    for i in range(len(fares)):
        if l * fares[i] <= 20:
            cost.append(l* fares[i])
    len_cost = len(cost)
    if len_cost == 1:
        return "UberX"
    elif len_cost ==2:
        return "UberXL"
    elif len_cost ==3:
        return "UberPlus"
    elif len_cost ==4:
        return "UberBlack"
    else:
        return "UberSUV"


        
    

print(fancyRide(20,[0.3, 0.5, 0.7, 1, 1.3]))