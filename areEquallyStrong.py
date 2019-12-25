def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if min(yourLeft,yourRight) == min(friendsLeft,friendsRight) and max(yourLeft,yourRight) == max(friendsLeft,friendsRight):
        return True
    else:
        return False


