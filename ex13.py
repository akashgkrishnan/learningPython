def list_check(collection):
    for val in collection:
        if type(val) != list:
            return False
    return True


print(list_check([[],[1],[2,3]]))



'''
    def list_check(vals):
        return all(type(l) == list for l in vals)
'''