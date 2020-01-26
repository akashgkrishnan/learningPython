def bishopAndPawn(bishop, pawn):
    if bishop[0] == pawn[0] or bishop[1] == pawn[1]:
        return False
    elif abs((ord(bishop[0])-96) - (ord(pawn[0])-96)) == abs(int(bishop[1])- int(pawn[1])):
        return True
    return False


print(bishopAndPawn('a1','c3'))