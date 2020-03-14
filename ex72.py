import re

l = ['paa', 'pan', 'pattern', 'prince', 'parents', 'print','pin', 'p5n', 'page3423', '123123ppasr31', 'penpkn']

for str in l:
	itr = re.finditer('p.n', str)
	for m in itr:
		print(m.group(), '....', str)

print('*'*20)

for str in l:
	itr = re.finditer('p[aeiou]n', str) #starts with p and ends with e and contains a single vowel in between
	for m in itr:
		print(m.group(), '....', str)


print('*'*20)

for str in l:
	itr = re.finditer('p[a-z]n', str) #starts with p and ends with e and contains a single alphabet character
	for m in itr:
		print(m.group(), '....', str)


print('*'*20)

for str in l:
	itr = re.finditer('p[a-z]*n', str) #starts with p and ends with e and contains a single alphabet character
	for m in itr:
		print(m.group(), '....', str)


print('*'*20)

for str in l:
	itr = re.finditer('p[a-z]{1,5}n', str) #starts with p and ends with e and contains a 1 to 5 number of alphabbets
	for m in itr:
		print(m.group(), '....', str)