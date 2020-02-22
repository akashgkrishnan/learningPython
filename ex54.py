import os

path = input("Enter path: ")
file_list = os.listdir(path)
fileCount = 0
dirCount = 0

for n in file_list:
    path = os.path.abspath(n)
    print(path)
    if os.path.isfile(path):
        fileCount += 1
    elif os.path.isdir(path):
        dirCount += 1
        file_list.extend(os.listdir(path))

print(f"File Count: {fileCount}")
print(f"Directory count: {dirCount}")


