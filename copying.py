def copy(fname,nfname):
    with open(fname) as oldfile:
        data = oldfile.read()
    with open(nfname, "w") as newfile:
        newfile.write(data)

copy('story.txt', 'story_copy.txt')