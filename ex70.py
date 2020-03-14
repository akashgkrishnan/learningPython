import re
s = "india is my country: "

m = re.search("my", s)


if m:
	print(m.start(), m.span(), m.end(), m.group())
else:
	print("none")


'''
it finds patterns at any location and returns the first occurence

'''