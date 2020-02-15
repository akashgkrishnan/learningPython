'''
file.readline() read a single line as string 
file.readlines() read number of lines as string and stores in a list

'''

file = open('textfile.txt' , 'r')
print(file.readline())
file.seek(0)
print(file.readlines())
