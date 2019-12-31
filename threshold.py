def ratingThreshold(threshold, ratings):
    count = []
    for i,v in enumerate(ratings):
        if sum(v)/len(v) < threshold:
            count += 1
    return count

ratingThreshold()