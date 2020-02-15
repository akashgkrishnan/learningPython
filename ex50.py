import os
print(os.getcwd())
print(os.path.exists('msg.txt'))
print(os.path.isdir('msg.txt'))
print(os.path.isfile('msg.txt'))
names = os.listdir(os.getcwd())
for name in names:
    print(name)