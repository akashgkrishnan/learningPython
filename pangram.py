def isPangram(sentence):
    found = []
    result = True
    for i in range(26):
        found.append(False)
    for i in range(len(sentence)):
        code = ord(sentence[i].lower())
        if ord('A') <= code and code <= ord('Z'):
            code += ord('A') - ord('a')
        if ord('a') <= code and code <= ord('z'):
            found[code - ord('a')] = True

    for i in range(26):
        if not found[i]:
            result = False

    return result

sentence = "The quick brown fox jumps over the lazy dog."
print(isPangram(sentence))