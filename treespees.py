def growingPlant(upSpeed, downSpeed, desiredHeight):
    days = 0
    height = 0
    while height < desiredHeight:
        height += upSpeed
        days += 1
        if height >= desiredHeight:
            return days
        else:
            height -= downSpeed
        
        
'''
def growingPlant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight <= upSpeed:
        return 1
    return math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed) + 1)
    '''        


        
print(growingPlant(100,10,910))