def make_song(item = 'soda', count = 99):
    for i in range(count,-1,-1):
        if i == 0:
            yield "No more {}".format(item)
        elif i == 1:
            yield "Only {} bottle of {}".format(i, item)
        else:
            yield "{} bottles of {} on the wall".format(i, item)

song = make_song(3, 'Christy')

print(next(song))
print(next(song))
print(next(song))
print(next(song))




    