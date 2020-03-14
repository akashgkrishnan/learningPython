''''
finding a pattern inside a string
the logic of finding a pattern is done using the regular expression
applications 
finding substrings or patters in a string
and replacing
The pattern used to pull out the substring based on a pattern is called as pattern
regular expression is itself a stiring
form matchin
form validations
word matching
text clening

python provides the re module
\
> match : used to find a pattern in the zero position of a string
it returns match object if it finds a match in the zero pos of a string
it returns none if it does not find a pattern in the begining
by default it finds pattern in a case sensitive manner
m.group() returns pattern matched string and notthe actual string
m.start() returns start pos of the mathced pattern 
m.end() returns end pos of the match patterns
m. span()
> search
> findall
> finditer
> sub

'''


import re

s = "india is muy country"
pater = input("enter a patern to search: ")
m = re.match(pater, s)

if m:
	print(m.start(), m.span(), m.end(), m.group())
else:
	print("none")