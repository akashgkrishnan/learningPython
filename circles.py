def circleOfNumbers(n, firstNumber):
    sum = int(n/2) + firstNumber
    if sum == n:
        return 0
    elif sum < n:
        return sum
    else:
        return sum -n

circleOfNumbers(12,10)