# open a file
# specify mode
# close mode
# open():
# r - read
# w - write
# rb - read binary
# wb - write binary
# a - append
# r+ - read and write
# w+ - write and read
# a+ - append and read
# binary files - any image , mp3 , mp4, docx, png
# text files will only contain characters that should be human readable
# seek - takes the pointer to passed position
# tell - tells us about the postion of the pointer or cursor
# read methods retunrs a string
file = open('textfile.txt', 'r')
print(file)
data = file.read() #pass the number of characters you want to read . pass -1 to read all characters from the file .. if not passed
print(file.tell())
print(data)                        #by default it takes all characters.
file.seek(0)
print(file.tell())
file.close()































