def truncate(phrase, num):
    length = num - 3
    if length < 0:
        return "Truncation must be at least 3 characters."
    elif num > len(phrase):
        return phrase
    else:
        return phrase[:length] + '...'

print(truncate("Problem solving is the best!", 10))