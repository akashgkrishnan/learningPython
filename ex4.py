def multiple_letter_count(word):
     return {letter : word.count(letter) for letter in word}


def multiple_letter_count2(string):
    return {letter: string.count(letter) for letter in string}


print(multiple_letter_count("akash"))
