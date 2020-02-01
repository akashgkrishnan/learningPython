def marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime):
    if successfulSubmissionTime == 1:
        return maxScore
    elif successfulSubmissionTime < 1:
        return 0
    else:
        newScore = maxScore
        newScore =maxScore -( (submissions-1)*10 + ((maxScore / 2) * (1 / marathonLength))*successfulSubmissionTime)

        if newScore > maxScore/2:
            return newScore
        return int(maxScore/2)
    


#adding some comments to understand commit and branching and branches in git



marathonLength = 100
maxScore = 400
submissions = 4
successfulSubmissionTime = -1

print(marathonTaskScore(marathonLength,maxScore, submissions, successfulSubmissionTime))