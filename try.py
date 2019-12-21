def almostIncreasingSequence(sequence):
    initial_length = len(sequence)-1
    length = len(sequence)-1
    count = 0
    i = 0
    while i < length:
        if sequence[i] >= sequence[i+1]:
            if i == 0:
                sequence.pop(0)
                count +=1
                length = len(sequence)-1
                i =0
            elif sequence[i] == sequence[i+1]:
                sequence.pop(i+1)
                length = len(sequence)-1
                i -= 1
                count += 1
            elif sequence[i] > sequence[i+1]:
                sequence.pop(i)
                length = len(sequence)-1
                i -= 1
                count +=1
        else:
            i += 1
    length = len(sequence)-1
    if count == 1:
        if initial_length - length == 1:
            return True
        else:
            return False
    elif count > 1:
        if initial_length - length > 1:
            return False
    else:
        return True


