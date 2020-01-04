def chessBoardCellColor(cell1, cell2):
    cell1 = list(cell1)
    cell2 = list(cell2)
    #converting letter to number using the ord() -64 for caps and ord()-96 for small 
    cell1[0], cell2[0] = ord(cell1[0])-64, ord(cell2[0])- 64  
    cell1[1], cell2[1]  = int(cell1[1]), int(cell2[1])
    # to check the diagonals
    if cell1[0] == cell1[1] and cell2[0] == cell2[1]:
        return True
    #to check the same columns
    elif cell1[1] == cell2[1]:
        if cell2[0] % 2 == 0 and cell1[0] % 2 == 0:
            return True
        elif cell2[0] % 2 == 1 and cell1[0] % 2 == 1:
            return True
    # to check the same rows
    elif cell1[0] == cell2[0]:
        if cell1[1] % 2 == 0 and cell2[1] % 2 == 0:
            return True
        elif cell1[1] % 2 == 1 and cell2[1] % 2 == 1:
            return True

    elif cell1[0] % 2 == 1 and cell2[0] % 2 == 1:
        if cell1[1] == cell2[1]:
            return True
        if cell1[1] % 2 == 0 and cell2[1] % 2 == 0:
            return True
        elif cell1[1] % 2 == 1 and cell2[1] %2 == 1:
            return True
    
    elif (max(cell1[0],cell2[0]) - min(cell1[0],cell2[0])) % 2 == 1:
        if cell1[1] % 2 == 1 and cell2[1] % 2 == 0:
            return True
        elif cell1[1] % 2 == 0 and cell2[1] %2 == 1:
            return True
    elif (max(cell1[0],cell2[0]) - min(cell1[0],cell2[0])) % 2 == 0:
        if cell1[1] % 2 == 0 and cell2[1] % 2 == 0:
            return True
        elif cell1[1] % 2 == 1 and cell2[1] %2 == 1:
            return True
    
    return False
        
print(chessBoardCellColor('A1','C5')) 