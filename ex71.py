'''
findall()

it returns a list of all the matched objects or patterns

metacharacters

[] -> range of characters
* -> zero or more occurence
+ -> one or more occurence
? zero or one occurence
{}exact occurence

() grouping of chars
. -> any char
|
$ _> end character

'''
import re

s = "india is my country: "

m = re.findall("my", s)

flag = False

for i in m:
	print(i.span(),'....' , i.group())
	flag = True
if not flag:
	print("none")