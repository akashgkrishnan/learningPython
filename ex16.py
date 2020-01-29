
def vowel_count(word):
    word = word.lower()
    return {letter : word.count(letter) for letter in word if letter in 'aeiou'}




print(vowel_count('Elie'))
    