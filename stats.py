def statistics(file_name):
    res ={}
    with open(file_name) as file:
        data = file.read()
        file.seek(0)
        lines = file.readlines()

        res['lines'] = len(lines)
        res['words'] = len(data.split())
        res['characters'] = len(data)
    return res
    

print(statistics('story.txt'))