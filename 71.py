import re

s = "india is my country: "

m = re.finditer("my", s)

flag = False

for i in m:
	print(i.span(),'....' , i.group())
	flag = True
if not flag:
	print("none")