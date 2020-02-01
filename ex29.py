
def is_odd_string(words):
    return sum(ord(letter)-96 for letter in words) % 2 == 1

print(is_odd_string('veryfunny'))

