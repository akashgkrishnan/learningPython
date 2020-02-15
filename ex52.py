import os 
import shutil

os.remove('msg.txt') # removes files from the given path
os.rmdir('test') #removes file from the given path but will only delete if the folder is empty

shutil.rmtree('directory_name') # removes all the files and folder inside the folder unlike remove which can only delete from a given empty folder
os.rename('file_new_name', 'old_file_name')