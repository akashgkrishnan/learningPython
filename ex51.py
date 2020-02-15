import os
path = os.getcwd()
names = os.listdir(path) # returns a list of all files and directories in the specified path
#print(names)
#names = os.listdir(os.getcwd()

filecount = 0
dircount = 0

for n in names:
    if os.path.isfile(os.path.join(path,n)):
        filecount += 1
    elif os.path.isdir(os.path.join(path,n)):
        dircount += 1

print(f"File Count : {filecount} Dir name: {dircount}")