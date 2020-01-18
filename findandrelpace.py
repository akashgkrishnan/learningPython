def find_and_replace(file_name, old_name, new_name):
    with open(file_name, "r+") as file:
        data = file.read() 
        file.seek(0)   
        file.write(data.replace(old_name, new_name))
        

find_and_replace('story.txt', 'AKASH', 'Christy') 