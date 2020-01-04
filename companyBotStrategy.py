def companyBotStrategy(trainingData):
    tot = 0
    count = 0
    for i in range(len(trainingData)):
        if trainingData[i][1] == 1:
            count += 1
            data += trainingData[i][0]

    if count:
        return data/count
    else:
        return 0.0
    
