def copy(file_name,new_file_name):
    with open(file_name) as oldfile:
        data = oldfile.read()
    
    data = data[::-1]



    with open(new_file_name, "w") as newfile:
        newfile.write(data)

copy('story.txt', 'story_copy_reverse.txt')