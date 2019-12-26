def capitalizeVowelsRegExp(input):
    input = [char.upper() if char in 'aeiou' else char for char in input]
    return ''.join(input)

print(capitalizeVowelsRegExp("There are 12 points"))