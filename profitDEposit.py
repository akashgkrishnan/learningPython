def depositProfit(deposit, rate, threshold):
    count = 0
    while deposit< threshold:
        deposit  += (rate/100)*deposit
        count +=1
    return count
    