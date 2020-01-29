def remove_every_other(collections):
    new_lis = []
    for i in range(0,len(collections),2):
        new_lis.append(collections[i])
    return new_lis



print(remove_every_other([5,1,2,4,1]))


'''

    def remove_every_other(lst):
        return [val for i,val in enumerate(lst) if i % 2 == 0]


        '''